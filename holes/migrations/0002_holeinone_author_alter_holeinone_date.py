# Generated by Django 4.2.4 on 2023-08-07 12:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='holeinone',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='holeinone',
            name='date',
            field=models.DateField(),
        ),
    ]
