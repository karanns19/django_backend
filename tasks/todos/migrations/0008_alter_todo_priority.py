# Generated by Django 4.2 on 2024-03-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.TextField(),
        ),
    ]
