# Generated by Django 5.0.9 on 2024-10-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_alter_estudante_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='data_nascimento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
