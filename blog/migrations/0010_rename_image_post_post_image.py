# Generated by Django 4.2.9 on 2024-03-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
    ]