# Generated by Django 3.1.7 on 2021-05-18 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationSystem', '0002_auto_20210518_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymenthistory',
            old_name='captain',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='propertyowner',
            old_name='rider',
            new_name='propertyOwner',
        ),
        migrations.RenameField(
            model_name='renter',
            old_name='captain',
            new_name='renter',
        ),
    ]
