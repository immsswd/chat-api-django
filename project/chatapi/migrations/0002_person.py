# Generated by Django 4.1.3 on 2023-01-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
    ]