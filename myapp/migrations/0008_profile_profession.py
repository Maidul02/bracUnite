# Generated by Django 4.1.1 on 2023-08-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_profile_current_city_profile_research_interest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(default='N', max_length=200, null=True),
        ),
    ]