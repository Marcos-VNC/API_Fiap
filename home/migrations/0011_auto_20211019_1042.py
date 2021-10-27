# Generated by Django 3.2.7 on 2021-10-19 13:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211019_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.turma'),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataFinal',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 10, 42, 36, 52236), null=True),
        ),
        migrations.AlterField(
            model_name='fiap',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 10, 42, 36, 52236)),
        ),
        migrations.AlterField(
            model_name='observacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 10, 42, 36, 54235)),
        ),
    ]