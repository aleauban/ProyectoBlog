# Generated by Django 4.0.1 on 2022-03-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=250)),
                ('autor', models.EmailField(max_length=254)),
                ('fecha', models.DateField(null=True)),
                ('imagen', models.ImageField(upload_to='imagenblog')),
            ],
        ),
    ]
