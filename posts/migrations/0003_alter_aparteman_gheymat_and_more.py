# Generated by Django 4.0.4 on 2022-06-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_aparteman_andaze_alter_vilae_gheymat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparteman',
            name='gheymat',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='aparteman',
            name='gheymat_ejare',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت اجاره'),
        ),
        migrations.AlterField(
            model_name='aparteman',
            name='gheymat_rahn',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت رهن'),
        ),
        migrations.AlterField(
            model_name='vilae',
            name='gheymat',
            field=models.BigIntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='vilae',
            name='gheymat_ejare',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت اجاره'),
        ),
        migrations.AlterField(
            model_name='vilae',
            name='gheymat_rahn',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت رهن'),
        ),
        migrations.AlterField(
            model_name='vilae',
            name='status_buy',
            field=models.CharField(choices=[('برای خرید', 'برای خرید'), ('برای اجاره', 'برای اجاره')], default='برای خرید', max_length=50, verbose_name='برای خرید/رهن و اجاره'),
        ),
    ]