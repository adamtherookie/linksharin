# Generated by Django 4.1.2 on 2022-12-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_page_effect'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
