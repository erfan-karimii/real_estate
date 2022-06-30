# Generated by Django 4.0.4 on 2022-06-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(max_length=250, verbose_name='نام خوانوادگی')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='تلفن اول')),
                ('phone_2', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='تلفن دوم')),
                ('semat', models.CharField(default='مشاور فروش', max_length=100, verbose_name='سمت')),
                ('tozih', models.TextField(blank=True, null=True, verbose_name='توضیح نقش')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'مشاور',
                'verbose_name_plural': 'اطلاعات کارکنان',
            },
        ),
    ]
