# Generated by Django 5.1.1 on 2024-10-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Survey', '0003_complain_invoice_image_complain_invoice_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='category',
            field=models.CharField(choices=[('None', 'None'), ('Foreign Material', 'Foreign Material'), ('Personal Hygiene', 'Personal Hygiene'), ('Food Quality', 'Food Quality'), ('Others', 'Others')], default='Others', max_length=20),
        ),
    ]
