# Generated by Django 5.0.6 on 2024-05-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]