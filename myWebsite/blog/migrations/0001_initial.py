# Generated by Django 4.1.3 on 2022-11-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Lengkap', models.CharField(max_length=20)),
                ('Tanggal_Lahir', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=30)),
                ('alamat', models.TextField()),
            ],
        ),
    ]