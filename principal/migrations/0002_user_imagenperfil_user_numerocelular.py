# Generated by Django 5.1.1 on 2024-10-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imagenPerfil',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='user',
            name='numeroCelular',
            field=models.CharField(default='00000000', max_length=15),
        ),
    ]
