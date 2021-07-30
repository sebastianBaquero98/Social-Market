# Generated by Django 3.2.5 on 2021-07-30 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tag', '0001_initial'),
        ('Brand', '0001_initial'),
        ('Influencer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeSocial', models.CharField(choices=[('IG', 'Instagram'), ('TK', 'TikTok'), ('YT', 'YouTube')], max_length=150)),
                ('numSeguidores', models.IntegerField(default=0)),
                ('numPost', models.IntegerField(default=0)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Influencer.influencer')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Brand.brand')),
                ('tags', models.ManyToManyField(to='Tag.Tag')),
            ],
        ),
    ]