# Generated by Django 2.1.5 on 2019-05-17 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='PostID',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]