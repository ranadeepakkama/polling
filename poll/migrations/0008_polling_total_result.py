# Generated by Django 4.2 on 2023-06-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_alter_polling_choice_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='polling',
            name='total_result',
            field=models.IntegerField(default=0),
        ),
    ]