# Generated by Django 4.1.3 on 2023-04-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_play_list_add_name_play_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_list_add',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
