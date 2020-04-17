# Generated by Django 3.0.2 on 2020-04-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synergy', '0010_auto_20200417_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
