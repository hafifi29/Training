# Generated by Django 4.1.7 on 2023-03-28 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='nominee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.nominee_user'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.user_model'),
        ),
    ]