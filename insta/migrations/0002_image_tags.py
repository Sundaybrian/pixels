# Generated by Django 2.2.4 on 2019-08-31 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='insta.tags'),
        ),
    ]