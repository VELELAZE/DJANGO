# Generated by Django 5.1.2 on 2024-11-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=30)),
                ('Sname', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')], default='inactive', max_length=15)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
