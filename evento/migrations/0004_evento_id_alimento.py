# Generated by Django 2.2.2 on 2019-09-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_auto_20190927_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='id_alimento',
            field=models.ManyToManyField(to='evento.Alimento'),
        ),
    ]