# Generated by Django 4.2.1 on 2023-05-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee_user',
            name='rec_letter',
            field=models.FileField(upload_to='rec_letters'),
        ),
    ]
