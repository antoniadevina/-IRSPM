# Generated by Django 3.1.7 on 2021-03-14 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AGRApi', '0008_auto_20210310_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='accomplishment',
        ),
    ]
