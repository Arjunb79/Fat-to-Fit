# Generated by Django 3.2.3 on 2021-07-15 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='gym_app.batch'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='gym_app.register'),
        ),
    ]
