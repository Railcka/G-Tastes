# Generated by Django 5.0.6 on 2024-06-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_grade_recipes_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutritionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cookingFullTime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cookingTime',
            field=models.IntegerField(),
        ),
    ]
