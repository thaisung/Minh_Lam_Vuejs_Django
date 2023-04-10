# Generated by Django 4.1.3 on 2023-04-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_song_love'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='love',
            field=models.CharField(default='love', max_length=150),
        ),
        migrations.AddField(
            model_name='song_love',
            name='id_Song',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='mood',
            field=models.ManyToManyField(blank=True, null=True, related_name='songs', to='api.songmood'),
        ),
        migrations.AlterField(
            model_name='song',
            name='mp3_file',
            field=models.FileField(blank=True, null=True, upload_to='song_files'),
        ),
        migrations.AlterField(
            model_name='song',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='song_posters'),
        ),
        migrations.AlterField(
            model_name='song_love',
            name='duration',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='song_love',
            name='mp3_file',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='song_love',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='song_love',
            name='poster',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
