# Generated by Django 4.2 on 2023-06-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_alter_polling_choice_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polling',
            name='choice_count',
            field=models.IntegerField(default=0),
        ),
    ]
