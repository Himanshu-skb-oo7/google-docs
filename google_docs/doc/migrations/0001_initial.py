# Generated by Django 3.2 on 2023-07-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
    ]