# Generated by Django 4.2.20 on 2025-04-03 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='families',
            options={'verbose_name': 'Family', 'verbose_name_plural': 'Families'},
        ),
        migrations.AlterModelOptions(
            name='itemsdetails',
            options={'verbose_name': 'Item Detail', 'verbose_name_plural': 'Item Details'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
