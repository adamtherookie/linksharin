# Generated by Django 4.1.2 on 2022-12-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_page_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='colorscheme',
            field=models.CharField(default='default', max_length=1000),
        ),
    ]
