# Generated by Django 4.0 on 2022-01-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_titre_ticket_title_userfollows_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollows',
            name='follows',
        ),
    ]
