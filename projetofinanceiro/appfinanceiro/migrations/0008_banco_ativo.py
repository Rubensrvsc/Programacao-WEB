# Generated by Django 2.1.3 on 2018-12-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfinanceiro', '0007_auto_20181211_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='banco',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
