# doc/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DocConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope["url_route"]["kwargs"]["id"]
        self.room_group_name = "doc_%s" % self.doc_id
        print(self.room_group_name+" "+self.doc_id+" "+self.channel_name)
    
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print("DISCONNECTED")

    # Receive content from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json["content"]

        print(text_data_json)
        # Send content to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "doc_content", "content": content}
        )

    # Receive content from room group
    async def doc_content(self, event):
        content = event["content"]

        # Send content to WebSocket
        await self.send(text_data=json.dumps({"content": content}))