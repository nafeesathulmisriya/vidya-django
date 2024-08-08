# Generated by Django 5.0.7 on 2024-08-06 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_specialisation', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctor')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.department')),
            ],
        ),
    ]
