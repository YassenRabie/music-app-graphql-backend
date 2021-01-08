# Generated by Django 3.1.5 on 2021-01-08 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('publish_date', models.DateField(verbose_name='release date')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
                ('artist_birthday', models.DateField(verbose_name='birthday')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('song_playtime', models.CharField(max_length=50)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artist'),
        ),
    ]
