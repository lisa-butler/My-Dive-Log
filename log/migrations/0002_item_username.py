# Generated by Django 3.2.15 on 2022-09-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='username',
            field=models.CharField(default='myusername', max_length=50),
        ),
    ]
