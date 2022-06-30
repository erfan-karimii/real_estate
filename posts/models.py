from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from admin_informations.models import AdminInformation
from django.utils import timezone


class vilae(models.Model):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای اجاره', 'برای اجاره'),
    )
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاخات ارضی', 'اصلاحات ارضی'),
    )

    titr = models.CharField(max_length=300, verbose_name="تیتر")
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="نویسنده")
    moshakhasat = models.ForeignKey(
        AdminInformation, on_delete=models.CASCADE, verbose_name="مشخصات نویسنده")
    status_buy = models.CharField(
        max_length=50, choices=STATUS_BUY, default='برای خرید', verbose_name="برای خرید/رهن و اجاره")
    gheymat = models.BigIntegerField(
        default=0, verbose_name="قیمت")
    gheymat_rahn = models.PositiveIntegerField(
       default=0, verbose_name="قیمت رهن")
    gheymat_ejare = models.PositiveIntegerField(
        default=0, verbose_name="قیمت اجاره")
    locations = models.TextField(verbose_name="ادرس ویلا")
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name="نوع سند")
    andaze_zamin = models.PositiveSmallIntegerField(verbose_name="اندازه زمین")
    andaze_bana = models.PositiveSmallIntegerField(verbose_name="اندازه بنا")
    tedad_otagh = models.PositiveSmallIntegerField(
        verbose_name="تعداد اتاق")
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name="تعداد سرویس بهداشتی")
    sal_sakht = models.CharField(
        max_length=2, verbose_name="چند سال ساخت")
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name="قابل معاوضه؟")
    tozihat_karbar = models.TextField(verbose_name="توضیحات کاربر")
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name="توضیحات خصوصی")
    map_1 = models.TextField(blank=True, null=True, verbose_name="نقشه گوگل")
    image = models.ImageField(verbose_name="عکس اصلی")
    upload_time = models.DateField(
        default=timezone.now, verbose_name="زمان ثبت")
    vise = models.BooleanField(default=False, verbose_name="ویژه؟")
    active = models.BooleanField(default=True, verbose_name="نمایش؟")

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'ویلا'
        verbose_name_plural = 'ویلاها'

    def __str__(self):
        return self.titr


class vilae_images(models.Model):
    vila = models.ForeignKey(vilae, on_delete=models.CASCADE)
    images = models.ImageField(verbose_name="عکس های بیشتر")

    def __str__(self):
        return self.vila.titr

    class Meta:
        verbose_name = 'عکس ویلا'
        verbose_name_plural = 'عکس های ویلا'


class aparteman(models.Model):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای رهن و اجاره', 'برای رهن و اجاره'),
    )
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )

    titr = models.CharField(max_length=150, verbose_name='تیتر')
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='نویسنده')
    moshakhasat = models.ForeignKey(
        AdminInformation, on_delete=models.CASCADE, verbose_name='مشخصات نویسنده')
    status_buy = models.CharField(
        max_length=50, choices=STATUS_BUY, default='برای خرید', verbose_name='برای خرید/رهن و اجاره')
    gheymat = models.PositiveIntegerField(
        default=0, verbose_name='قیمت')
    gheymat_rahn = models.PositiveIntegerField(
        default=0, verbose_name='قیمت رهن')
    gheymat_ejare = models.PositiveIntegerField(
        default=0, verbose_name='قیمت اجاره')
    locations = models.TextField(verbose_name='ادرس اپارتمان')
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name='نوع سند')
    andaze = models.PositiveSmallIntegerField(verbose_name='متراژ')
    tabage = models.CharField(max_length=2, verbose_name='طبقه')
    tedad_tabaghe = models.PositiveSmallIntegerField(verbose_name='تعداد طبقه')
    tedad_vahed_tabaghe = models.PositiveSmallIntegerField(
        verbose_name='تعداد واحد در هر طبقه')
    tedad_otagh = models.CharField(max_length=2, verbose_name='تعداد اتاق')
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name='تعداد سرویس بهداشتی')
    sal_sakht = models.PositiveSmallIntegerField(verbose_name='چند سال ساخت')
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name='قابل معاوضه؟')
    tozihat_karbar = models.TextField(verbose_name='توضیحات کاربر')
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name='توضیحات خصوصی')
    map_1 = models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')
    image = models.ImageField(verbose_name='عکس اصلی')
    upload_time = models.DateField(
        default=timezone.now, verbose_name='زمان ثبت')
    vise = models.BooleanField(default=False, verbose_name='ویژه؟')
    active = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')

    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'اپارتمان'
        verbose_name_plural = 'اپارتمان ها'


class aparteman_images(models.Model):
    aparteman = models.ForeignKey(aparteman, on_delete=models.CASCADE)
    images = models.ImageField(verbose_name="عکس های بیشتر")

    def __str__(self):
        return self.aparteman.titr

    class Meta:
        verbose_name = 'عکس اپارتمان'
        verbose_name_plural = 'عکس های اپارتمان'


class zamin(models.Model):
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )
    ZAMIN_CHOICES = (
        ('تفریحی توریستی', 'تفریحی توریستی'),
        ('باغ', 'باغ'),
        ('مسکونی', 'مسکونی'),
    )
    titr = models.CharField(max_length=150, verbose_name='تیتر')
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='نویسنده')
    moshakhasat = models.ForeignKey(
        AdminInformation, on_delete=models.CASCADE, verbose_name='مشخصات نویسنده')
    gheymat = models.PositiveIntegerField(verbose_name='قیمت')
    andaze = models.PositiveSmallIntegerField(verbose_name=' اندازه')
    noe_zamin = models.CharField(
        max_length=30, choices=ZAMIN_CHOICES, default='مسکونی',verbose_name='نوع زمین')
    locations = models.TextField(verbose_name='ادرس زمین')
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name='نوع سند')
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name='قابل معاوضه؟')
    tozihat_karbar = models.TextField(verbose_name='توضیحات کاربر')
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name='توضیحات خصوصی')
    map_1 = models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')
    image = models.ImageField(verbose_name='عکس اصلی')
    upload_time = models.DateField(
        default=timezone.now, verbose_name='زمان ثبت')
    vise = models.BooleanField(default=False, verbose_name='ویژه؟')
    active = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')

    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'زمین'
        verbose_name_plural = 'زمین ها'


class zamin_images(models.Model):
    product = models.ForeignKey(zamin, on_delete=models.CASCADE)
    images = models.ImageField(verbose_name="عکس")

    def __str__(self):
        return self.product.titr

    class Meta:
        verbose_name = 'عکس زمین'
        verbose_name_plural = 'عکس های زمین'
