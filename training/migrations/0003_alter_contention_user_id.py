# Generated by Django 4.1.7 on 2023-03-28 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_alter_vote_nominee_id_alter_vote_voter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contention',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.user_model'),
        ),
    ]
