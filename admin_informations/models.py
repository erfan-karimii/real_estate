from django.db import models

# Create your models here.


class AdminInformation(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام")
    last_name = models.CharField(max_length=250,verbose_name="نام خوانوادگی")
    phone = models.CharField(max_length=11,unique=True,verbose_name="تلفن اول")
    phone_2 = models.CharField(max_length=11,null=True,blank=True, unique=True,verbose_name="تلفن دوم")
    semat = models.CharField(max_length=100,default='مشاور فروش',verbose_name="سمت")
    tozih = models.TextField(null=True,blank=True,verbose_name="توضیح نقش")
    image = models.ImageField(verbose_name="عکس")

    def __str__(self):
        return self.name+" "+self.last_name+" "+self.phone
    class Meta:
        verbose_name= 'مشاور'
        verbose_name_plural= 'اطلاعات کارکنان'
