# Generated by Django 5.1.7 on 2025-03-24 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_notifications', '0006_note_delete_notification'),
        ('users', '0003_alter_user_options_remove_instructor_signup_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_notes', to='users.instructor'),
        ),
        migrations.AlterField(
            model_name='note',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='st_notifications.student'),
        ),
    ]
