# Generated by Django 5.1 on 2024-08-26 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_litfic_litfiction_remove_memoir_memoir_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='comment',
        ),
    ]
