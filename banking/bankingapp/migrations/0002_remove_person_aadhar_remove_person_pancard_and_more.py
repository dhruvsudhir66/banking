# Generated by Django 4.0.6 on 2022-09-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='aadhar',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pancard',
        ),
        migrations.AddField(
            model_name='person',
            name='creditcard',
            field=models.BooleanField(default=False, verbose_name='Credit Card'),
        ),
        migrations.AddField(
            model_name='person',
            name='debitcard',
            field=models.BooleanField(default=False, verbose_name='Debit Card'),
        ),
        migrations.AddField(
            model_name='person',
            name='passbook',
            field=models.BooleanField(default=False, verbose_name='Passbook'),
        ),
    ]
