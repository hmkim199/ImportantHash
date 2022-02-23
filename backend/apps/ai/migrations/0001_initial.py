# Generated by Django 4.0.2 on 2022-02-23 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TimeField(verbose_name='타임스탬프')),
                ('keyword', models.CharField(max_length=255, verbose_name='시간대 키워드')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyword_video_id', to='video.video', verbose_name='동영상 id')),
            ],
            options={
                'verbose_name_plural': '키워드',
                'db_table': 'keyword',
            },
        ),
        migrations.CreateModel(
            name='Importance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TimeField(verbose_name='타임스탬프')),
                ('score', models.FloatField(verbose_name='시간에 대한 중요도 점수')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='importance_video_id', to='video.video', verbose_name='동영상 id')),
            ],
            options={
                'verbose_name_plural': '중요도',
                'db_table': 'importance',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, verbose_name='단어')),
                ('count', models.IntegerField(default=0, verbose_name='단어 빈도 수')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequency_video_id', to='video.video', verbose_name='동영상 id')),
            ],
            options={
                'verbose_name_plural': '단어 빈도 수',
                'db_table': 'frequency',
            },
        ),
    ]
