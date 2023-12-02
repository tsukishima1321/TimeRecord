# Generated by Django 3.2 on 2023-12-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='timecount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('classroom', models.CharField(max_length=10)),
                ('writer', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=10)),
            ],
        ),
    ]