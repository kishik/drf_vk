# Generated by Django 4.2.1 on 2023-05-09 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('from_id', models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_id', models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
