# Generated by Django 4.2.10 on 2024-03-26 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 26, 14, 43, 30, 137720, tzinfo=datetime.timezone.utc)),
        ),
    ]
