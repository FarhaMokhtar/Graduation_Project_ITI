# Generated by Django 5.1.7 on 2025-03-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_notifications', '0004_alter_notification_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredefinedNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
