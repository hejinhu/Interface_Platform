# Generated by Django 3.1.4 on 2020-12-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interface',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=32, null=True)),
                ('type', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('body', models.CharField(max_length=300, null=True)),
                ('result', models.CharField(max_length=300, null=True)),
                ('res', models.CharField(max_length=10, null=True)),
                ('time', models.DateField(null=True)),
            ],
        ),
    ]
