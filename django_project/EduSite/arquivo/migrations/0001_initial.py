# Generated by Django 2.1.7 on 2019-02-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('upload_data', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clientes_foto')),
            ],
        ),
    ]
