# Generated by Django 4.2 on 2023-06-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_polling_total_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='polling',
            name='user_count',
            field=models.IntegerField(default=0),
        ),
    ]