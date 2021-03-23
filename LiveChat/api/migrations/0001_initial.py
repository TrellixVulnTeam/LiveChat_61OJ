# Generated by Django 3.1.7 on 2021-03-23 13:00

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('user_bio', models.CharField(blank=True, default='', max_length=300, verbose_name='User Bio')),
                ('user_icon', models.ImageField(default='default_user.png', upload_to=api.models.user_icon_path, verbose_name='User icon')),
                ('is_hosting', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_chat', models.IntegerField()),
                ('num_chat', models.IntegerField(default=1)),
                ('chat_code', models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True)),
                ('open_chat', models.BooleanField(default=True)),
                ('live_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modded_at', models.DateTimeField(auto_now_add=True)),
                ('mod_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mod_for', to=settings.AUTH_USER_MODEL)),
                ('my_mods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_mods', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('mod_for', 'my_mods')},
            },
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_at', models.DateTimeField(auto_now_add=True)),
                ('user_followers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Followers', to=settings.AUTH_USER_MODEL)),
                ('user_following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_following', 'user_followers')},
            },
        ),
        migrations.CreateModel(
            name='UserBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_at', models.DateTimeField(auto_now_add=True)),
                ('block_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ban_user', to=settings.AUTH_USER_MODEL)),
                ('blocked_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ban_from', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('block_user', 'blocked_from')},
            },
        ),
    ]
