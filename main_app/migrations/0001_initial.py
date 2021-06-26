# Generated by Django 3.1.7 on 2021-06-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(verbose_name='release date')),
                ('genre', models.CharField(choices=[('A', 'Adventure'), ('F', 'Fighting'), ('I', 'Indie'), ('R', 'Racing'), ('S', 'Sport'), ('T', 'Tactical')], default='A', max_length=1)),
                ('mode', models.CharField(choices=[('M', 'Multiplayer'), ('S', 'Single player'), ('C', 'Co-operative'), ('B', 'Battle Royale')], default='M', max_length=1)),
            ],
        ),
    ]
