# Generated by Django 2.2.3 on 2020-01-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200114_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='page_views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
