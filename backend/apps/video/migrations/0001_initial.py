# Generated by Django 4.0.2 on 2022-02-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(max_length=255, verbose_name='동영상 URL')),
                ('title', models.CharField(max_length=255, verbose_name='동영상 제목')),
            ],
            options={
                'verbose_name_plural': '동영상',
                'db_table': 'video',
            },
        ),
    ]