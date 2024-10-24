# Generated by Django 5.0.9 on 2024-10-24 14:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_estudante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='estudante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.estudante', validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]