# Generated by Django 4.1.3 on 2023-04-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_play_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_list_add',
            name='Name_Play_list',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
