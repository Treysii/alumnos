# Generated by Django 2.1.3 on 2018-11-04 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0005_auto_20181103_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
