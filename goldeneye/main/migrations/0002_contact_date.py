# Generated by Django 5.0 on 2023-12-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
