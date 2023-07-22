# Generated by Django 3.2 on 2023-07-22 17:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_alter_doc_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
