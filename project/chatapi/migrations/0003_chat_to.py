# Generated by Django 4.1.3 on 2023-01-05 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapi', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatapi.person'),
            preserve_default=False,
        ),
    ]
