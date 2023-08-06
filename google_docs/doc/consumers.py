import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs

class DocConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope["url_route"]["kwargs"]["id"]
        self.room_group_name = "doc_%s" % self.doc_id
        query_string = self.scope.get("query_string", b"").decode("utf-8")
        parsed_query_string = parse_qs(query_string)
        self.user_id = parsed_query_string.get("user_id", [None])[0]  # Fetch the user_id from the query string

        print("SCOPE", self.user_id);
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print("DISCONNECTED")

    # Receive content from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        change = text_data_json["change"]
        version = text_data_json["version"]  # Get the version from the received data

        # Send change to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "doc_change", "change": change, "user_id": self.user_id, "version": version}
        )

    # Receive change from room group
    async def doc_change(self, event):
        change = event["change"]
        user_id = event.get("user_id")
        version = event.get("version")  # Get the version from the event data

        # Send change to WebSocket
        await self.send(text_data=json.dumps({"change": change, "user_id": user_id, "version": version}))
