# Generated by Django 4.2.3 on 2023-09-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewLead',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('ticketno', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]