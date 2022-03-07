# Generated by Django 4.0.1 on 2022-03-07 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0005_rename_subtitulo_post_cualidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='imagenblog'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='imagenblog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
