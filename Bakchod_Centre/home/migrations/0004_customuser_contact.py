# Generated by Django 2.1.5 on 2019-01-27 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190127_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.IntegerField(default=0),
        ),
    ]