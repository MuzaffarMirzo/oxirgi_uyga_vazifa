# Generated by Django 5.0.7 on 2024-07-16 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dars_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.darslar')),
            ],
        ),
        migrations.DeleteModel(
            name='Dars_baho',
        ),
    ]
