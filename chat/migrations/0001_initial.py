# Generated by Django 3.2 on 2022-12-11 02:10

import chat.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=2000, verbose_name='tag_text')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='uploads/')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('file', models.FileField(default=None, null=True, upload_to=chat.models.get_file_path)),
                ('downvoters', models.ManyToManyField(blank=True, null=True, related_name='downvoters', to=settings.AUTH_USER_MODEL)),
                ('message_tags', models.ManyToManyField(to='chat.Tag')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apiproduct', verbose_name='topic')),
                ('upvoters', models.ManyToManyField(blank=True, null=True, related_name='upvoters', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]