# Generated by Django 4.2.20 on 2025-04-03 19:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_alter_families_options_alter_itemsdetails_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterField(
            model_name='families',
            name='members',
            field=models.ManyToManyField(related_name='families', to=settings.AUTH_USER_MODEL),
        ),
    ]
