# Generated by Django 4.2.11 on 2024-06-04 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0006_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.AutoField(default=uuid.UUID('7dfc3755-61f8-41b7-a134-dfeb89b31f6f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
