# Generated by Django 4.1.2 on 2022-11-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_delete_coremember'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]