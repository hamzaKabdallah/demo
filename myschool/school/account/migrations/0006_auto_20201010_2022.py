# Generated by Django 3.0.5 on 2020-10-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201008_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachernotes',
            name='note',
            field=models.TextField(),
        ),
    ]