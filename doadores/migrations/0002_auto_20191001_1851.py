# Generated by Django 2.2.5 on 2019-10-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doadores',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
