# Generated by Django 3.1 on 2021-01-19 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakerapp', '0002_feedbackdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackdata',
            name='data',
        ),
    ]
