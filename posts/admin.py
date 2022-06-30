from operator import rshift
from django.contrib import admin
from .models import vilae, aparteman, zamin ,vilae_images,zamin_images,aparteman_images
# Register your models here.
# admin.site.register(Post)

class BookInline(admin.TabularInline):
    model = vilae_images

@admin.register(vilae)
class only_identity_match_change(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    #list_display=("name","price")
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(nevisande=request.user)
    list_display = ('titr','nevisande','id','sanad','vise','active')
    # list_editable = ('active',)
    list_filter = ('vise','active')
    search_fields = ('id','titr','locations')
    ordering = ('upload_time',)
    
    



class BookInline(admin.TabularInline):
    model = aparteman_images

@admin.register(aparteman)
class only_identity_match_change(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    #list_display=("name","price")
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(nevisande=request.user)
    list_display = ('titr','nevisande','id','sanad','vise','active')
    # list_editable = ('active',)
    list_filter = ('vise','active')
    search_fields = ('id','titr','locations')
    ordering = ('upload_time',)



class BookInline(admin.TabularInline):
    model = zamin_images

@admin.register(zamin)
class only_identity_match_change(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    #list_display=("name","price")
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(nevisande=request.user)
