# Generated by Django 4.2.5 on 2023-12-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='reviews',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='publish_year',
            field=models.DateTimeField(),
        ),
    ]
