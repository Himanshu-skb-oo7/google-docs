# Generated by Django 3.2 on 2023-08-09 19:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doc', '0008_alter_doc_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='shared_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='shared_docs', to=settings.AUTH_USER_MODEL),
        ),
    ]
