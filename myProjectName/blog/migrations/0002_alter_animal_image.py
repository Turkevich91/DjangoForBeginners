# Generated by Django 4.1.7 on 2023-11-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(upload_to='static/animals/'),
        ),
    ]
