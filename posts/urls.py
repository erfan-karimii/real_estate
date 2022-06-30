from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('listview/aparteman/', views.list_view_aparteman, name='listview-aparteman'),
    path('listview/zamin/', views.list_view_zamin, name='listview-zamin'),
    path('listview/vila/', views.list_view_vila, name='listview-vila'),
    path('aparteman/detail/<int:product_id>', views.detail_view_aparteman,name='detailview-aparteman'),
    path('vila/detail/<int:product_id>', views.detail_view_vila,name='detailview-vila'),
    path('zamin/detail/<int:products_id>', views.detail_view_zamin,name='detailview-zamin'),
    path('melk/<wh>',views.footer_listview,name="footer_view")
]
