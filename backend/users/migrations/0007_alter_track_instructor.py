# Generated by Django 5.1.7 on 2025-03-27 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_track_instructors_track_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='users.instructor'),
        ),
    ]
