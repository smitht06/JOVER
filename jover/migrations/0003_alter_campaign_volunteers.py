# Generated by Django 4.2.5 on 2023-10-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jover', '0002_campaign_materials_contactlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='volunteers',
            field=models.ManyToManyField(blank=True, related_name='campaign_volunteers', to='jover.person'),
        ),
    ]
