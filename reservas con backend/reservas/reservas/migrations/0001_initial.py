# Generated by Django 4.2.7 on 2023-11-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('numero_de_invitados', models.IntegerField()),
            ],
        ),
    ]
