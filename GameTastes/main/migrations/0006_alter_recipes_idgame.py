# Generated by Django 5.0.6 on 2024-06-05 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_nutritionals_alter_recipes_cookingfulltime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='idGame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.games'),
        ),
    ]
