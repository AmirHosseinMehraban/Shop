# Generated by Django 4.2.4 on 2023-12-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='scategory', to='home.category'),
        ),
    ]
