# Generated by Django 5.0.8 on 2024-08-08 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_option', models.CharField(choices=[('A', 'Option_a'), ('B', 'Option_b'), ('C', 'Option_c'), ('D', 'Option_d')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BolimTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testchek.bolim')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testchek.test')),
            ],
        ),
        migrations.AddField(
            model_name='bolim',
            name='tests',
            field=models.ManyToManyField(through='testchek.BolimTest', to='testchek.test'),
        ),
        migrations.AddConstraint(
            model_name='bolimtest',
            constraint=models.UniqueConstraint(fields=('bolim', 'test'), name='unique_bolim_test'),
        ),
    ]
