# Generated by Django 5.1.6 on 2025-02-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]
