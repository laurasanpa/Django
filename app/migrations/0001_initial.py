# Generated by Django 3.1.4 on 2020-12-30 20:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('titulo', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=100)),
                ('imdb', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('fecha_publi', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libro')),
            ],
        ),
    ]
