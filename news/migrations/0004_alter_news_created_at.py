# Generated by Django 4.2.3 on 2023-12-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_user_name_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(),
        ),
    ]