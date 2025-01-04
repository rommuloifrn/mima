# Generated by Django 5.1.4 on 2025-01-04 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('bio', models.TextField()),
                ('data_de_nascimento', models.DateField()),
                ('foto', models.ImageField(upload_to=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Amizade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinatário', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to='core.amigo')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='de_quem_e_amigo', to='core.amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('Amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.amigo')),
            ],
        ),
    ]
