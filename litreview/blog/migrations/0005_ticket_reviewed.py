# Generated by Django 4.0 on 2022-01-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_userfollows_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
