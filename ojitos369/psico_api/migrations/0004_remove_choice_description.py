# Generated by Django 4.0.2 on 2022-02-12 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psico_api', '0003_rename_description_question_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='description',
        ),
    ]