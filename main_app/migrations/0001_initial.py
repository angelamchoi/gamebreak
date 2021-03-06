# Generated by Django 3.1.7 on 2021-07-07 21:27

from django.db import migrations, models
import django.db.models.deletion


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
                ('date', models.CharField(max_length=100, verbose_name='version')),
                ('genre', models.CharField(choices=[('Adventure', 'Adventure'), ('Fighting', 'Fighting'), ('Indie', 'Indie'), ('Racing', 'Racing'), ('Sport', 'Sport'), ('Tactical', 'Tactical')], default='Adventure', max_length=20)),
                ('mode', models.CharField(choices=[('Multiplayer', 'Multiplayer'), ('Single Player', 'Single player'), ('Co-operative', 'Co-operative'), ('Battle Royale', 'Battle Royale')], default='Multiplayer', max_length=20)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Super Nintendo', 'Super Nintendo'), ('GameCube', 'GameCube'), ('Nintendo64', 'Nintendo64'), ('Gameboy', 'GameBoy'), ('Wii', 'Wii'), ('Nintendo Switch', 'Nintendo Switch')], default='Super Nintendo', max_length=20, verbose_name='gaming system')),
                ('date', models.IntegerField(verbose_name='version')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('key', models.CharField(default='Photo!', max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.system'),
        ),
    ]
