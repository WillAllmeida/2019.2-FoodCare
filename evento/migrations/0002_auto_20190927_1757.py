# Generated by Django 2.2.2 on 2019-09-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('un_medida', models.CharField(max_length=60)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='evento',
            name='endereco',
        ),
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
