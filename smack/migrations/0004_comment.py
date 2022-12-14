# Generated by Django 4.1.3 on 2022-11-27 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smack', '0003_smack_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('smack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='smack.smack')),
            ],
        ),
    ]
