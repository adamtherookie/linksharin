# Generated by Django 4.1.2 on 2022-12-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_link_clicks_page_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='clicks',
        ),
    ]
