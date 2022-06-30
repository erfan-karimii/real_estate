# Generated by Django 4.0.4 on 2022-06-10 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_informations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='aparteman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titr', models.CharField(max_length=150, verbose_name='تیتر')),
                ('status_buy', models.CharField(choices=[('برای خرید', 'برای خرید'), ('برای رهن و اجاره', 'برای رهن و اجاره')], default='برای خرید', max_length=50, verbose_name='برای خرید/رهن و اجاره')),
                ('gheymat', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('gheymat_rahn', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت رهن')),
                ('gheymat_ejare', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت اجاره')),
                ('locations', models.TextField(verbose_name='ادرس اپارتمان')),
                ('sanad', models.CharField(choices=[('شش دانگ', 'شش دانگ'), ('مشاع', 'مشاع'), ('اصلاحات ارضی', 'اصلاحات ارضی')], default='شش دانگ', max_length=32, verbose_name='نوع سند')),
                ('andaze', models.PositiveSmallIntegerField(verbose_name='اندازه')),
                ('tabage', models.CharField(max_length=2, verbose_name='طبقه')),
                ('tedad_tabaghe', models.PositiveSmallIntegerField(verbose_name='تعداد طبقه')),
                ('tedad_vahed_tabaghe', models.PositiveSmallIntegerField(verbose_name='تعداد واحد در هر طبقه')),
                ('tedad_otagh', models.CharField(max_length=2, verbose_name='تعداد اتاق')),
                ('tedad_dastshoe', models.PositiveSmallIntegerField(verbose_name='تعداد سرویس بهداشتی')),
                ('sal_sakht', models.PositiveSmallIntegerField(verbose_name='چند سال ساخت')),
                ('ghabel_moaveze', models.BooleanField(default=False, verbose_name='قابل معاوضه؟')),
                ('tozihat_karbar', models.TextField(verbose_name='توضیحات کاربر')),
                ('tozihat_khososy', models.TextField(blank=True, null=True, verbose_name='توضیحات خصوصی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('map_1', models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')),
                ('upload_time', models.DateField(default=django.utils.timezone.now, verbose_name='زمان ثبت')),
                ('vise', models.BooleanField(default=False, verbose_name='ویژه؟')),
                ('active', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('moshakhasat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_informations.admininformation', verbose_name='مشخصات نویسنده')),
                ('nevisande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'اپارتمان',
                'verbose_name_plural': 'اپارتمان ها',
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='vilae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titr', models.CharField(max_length=300, verbose_name='تیتر')),
                ('status_buy', models.CharField(choices=[('برای خرید', 'برای خرید'), ('برای اجاره', 'برای رهن و اجاره')], default='برای خرید', max_length=50, verbose_name='برای خرید/رهن و اجاره')),
                ('gheymat', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('gheymat_rahn', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت رهن')),
                ('gheymat_ejare', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت اجاره')),
                ('locations', models.TextField(verbose_name='ادرس ویلا')),
                ('sanad', models.CharField(choices=[('شش دانگ', 'شش دانگ'), ('مشاع', 'مشاع'), ('اصلاخات ارضی', 'اصلاحات ارضی')], default='شش دانگ', max_length=32, verbose_name='نوع سند')),
                ('andaze_zamin', models.PositiveSmallIntegerField(verbose_name='اندازه زمین')),
                ('andaze_bana', models.PositiveSmallIntegerField(verbose_name='اندازه بنا')),
                ('tedad_otagh', models.PositiveSmallIntegerField(verbose_name='تعداد اتاق')),
                ('tedad_dastshoe', models.PositiveSmallIntegerField(verbose_name='تعداد سرویس بهداشتی')),
                ('sal_sakht', models.CharField(max_length=2, verbose_name='چند سال ساخت')),
                ('ghabel_moaveze', models.BooleanField(default=False, verbose_name='قابل معاوضه؟')),
                ('tozihat_karbar', models.TextField(verbose_name='توضیحات کاربر')),
                ('tozihat_khososy', models.TextField(blank=True, null=True, verbose_name='توضیحات خصوصی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('map_1', models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')),
                ('upload_time', models.DateField(default=django.utils.timezone.now, verbose_name='زمان ثبت')),
                ('vise', models.BooleanField(default=False, verbose_name='ویژه؟')),
                ('active', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('moshakhasat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_informations.admininformation', verbose_name='مشخصات نویسنده')),
                ('nevisande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'ویلا',
                'verbose_name_plural': 'ویلاها',
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='zamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titr', models.CharField(max_length=150, verbose_name='تیتر')),
                ('gheymat', models.PositiveIntegerField(verbose_name='قیمت')),
                ('andaze', models.PositiveSmallIntegerField(verbose_name='اندازه')),
                ('noe_zamin', models.CharField(choices=[('تفریحی توریستی', 'تفریحی توریستی'), ('باغ', 'باغ'), ('مسکونی', 'مسکونی')], default='مسکونی', max_length=30)),
                ('locations', models.TextField(verbose_name='ادرس زمین')),
                ('sanad', models.CharField(choices=[('شش دانگ', 'شش دانگ'), ('مشاع', 'مشاع'), ('اصلاحات ارضی', 'اصلاحات ارضی')], default='شش دانگ', max_length=32, verbose_name='نوع سند')),
                ('ghabel_moaveze', models.BooleanField(default=False, verbose_name='قابل معاوضه؟')),
                ('tozihat_karbar', models.TextField(verbose_name='توضیحات کاربر')),
                ('tozihat_khososy', models.TextField(blank=True, null=True, verbose_name='توضیحات خصوصی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('map_1', models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')),
                ('upload_time', models.DateField(default=django.utils.timezone.now, verbose_name='زمان ثبت')),
                ('vise', models.BooleanField(default=False, verbose_name='ویژه؟')),
                ('active', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('moshakhasat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_informations.admininformation', verbose_name='مشخصات نویسنده')),
                ('nevisande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'زمین',
                'verbose_name_plural': 'زمین ها',
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='zamin_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='', verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.zamin')),
            ],
            options={
                'verbose_name': 'عکس زمین',
                'verbose_name_plural': 'عکس های زمین',
            },
        ),
        migrations.CreateModel(
            name='vilae_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='', verbose_name='عکس های بیشتر')),
                ('vila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.vilae')),
            ],
            options={
                'verbose_name': 'عکس ویلا',
                'verbose_name_plural': 'عکس های ویلا',
            },
        ),
        migrations.CreateModel(
            name='aparteman_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='', verbose_name='عکس های بیشتر')),
                ('aparteman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.aparteman')),
            ],
            options={
                'verbose_name': 'عکس اپارتمان',
                'verbose_name_plural': 'عکس های اپارتمان',
            },
        ),
    ]