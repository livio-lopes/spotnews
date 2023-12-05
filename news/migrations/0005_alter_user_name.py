# Generated by Django 4.2.3 on 2023-12-03 20:28

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_alter_news_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                max_length=200, validators=[news.models.validate_title]
            ),
        ),
    ]