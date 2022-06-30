from searchform.forms import SearchFormZamin
from django.http import Http404
from django.shortcuts import render
from .models import vilae, aparteman, zamin, vilae_images, zamin_images, aparteman_images
from django.core.paginator import Paginator
from django.db.models import Q

# Filter Active emal mikonim


def list_view_aparteman(request):
    if request.GET and not request.GET.get('page'):
        # if request.GET and request.GET != 'page':
        status_buy = request.GET.get('status_buy')
        # sanad = request.GET.get('sanad')
        # ghabel_moaveze = request.GET.get('ghabel_moaveze')
        # locations = request.GET.get('locations')
        # tedad_otagh = request.GET.get('tedad_otagh')
        # tabage = request.GET.get('tabage')
        # sal_sakht=request.GET.get('sal_sakht')
        min_gheymat = request.GET.get('min_gheymat',0)
        max_gheymat = request.GET.get('max_gheymat')
        

        posts = aparteman.objects.filter(active=True,
        status_buy=status_buy
                    ).filter(
                    Q(gheymat__gte=min_gheymat) |
        Q(gheymat__lte=max_gheymat))
    else:
        apartemans = aparteman.objects.all().order_by('-upload_time')

        paginator = Paginator(apartemans, 4)

        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

    context = {
        "activebar": "aparteman",

        'posts': posts,
        'min_gheymat':0,
       
   

    }
    return render(request, 'aparteman.html', context)


def list_view_zamin(request):
    zamins = zamin.objects.filter(active = True).order_by('-upload_time')
    paginator = Paginator(zamins, 4)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        "activebar": "zamin",
        'zamin': zamin.objects.all(),
        'posts': posts,
    }
    return render(request, 'zamin.html', context)


def list_view_vila(request):

    if request.GET and not request.GET.get('page'):

        status_buy = request.GET.get('status_buy')
        # sanad = request.GET.get('sanad')
        # ghabel_moaveze = request.GET.get('ghabel_moaveze')
        # locations = request.GET.get('locations')
        # tedad_otagh = request.GET.get('tedad_otagh', 0)
        min_gheymat = request.GET.get('min_gheymat')
        max_gheymat = request.GET.get('max_gheymat')
        
        posts = vilae.objects.filter(active=True,
        status_buy=status_buy
                    ).filter(
                    Q(gheymat__gte=min_gheymat) |
        Q(gheymat__lte=max_gheymat))
        context = {
        "activebar": "vila",
        'vilaes': vilae.objects.filter(active=True),
        # 'tedad_otagh':tedad_otagh,
        'posts': posts,
        'min_gheymat':0,
    }

   
    else:
        posts = vilae.objects.filter(active=True).order_by('-upload_time')

        paginator = Paginator(posts, 2)

        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

        context = {
            "activebar": "vila",
            'vilaes': vilae.objects.filter(active=True),
            'posts': posts,
            'min_gheymat':0,
        }

    return render(request, 'vila.html', context)


def detail_view_aparteman(request, product_id):
    context = {
        'post': aparteman.objects.get(id=product_id),
        'image_posts': aparteman_images.objects.filter(aparteman_id=product_id),
    }
    return render(request, 'aparteman-detail.html', context)


def detail_view_vila(request, product_id):
    context = {
        'post': vilae.objects.get(id=product_id),
        'image_posts': vilae_images.objects.filter(vila_id=product_id),
    }
    return render(request, 'vila-detail.html', context)


def detail_view_zamin(request, products_id):
    context = {
        'post': zamin.objects.get(id=products_id),
        'image_posts': zamin_images.objects.filter(product_id=products_id),
    }
    return render(request, 'zamin-detail.html', context)


def footer_listview(request, wh):
    context = {}
    if wh == "vila_kharid":
        context = {"post": vilae.objects.filter(status_buy='برای خرید').order_by(
            '-upload_time'), 'title': 'vila_baraye_kharid', }
    elif wh == "vila_rahn":
        context = {"post": vilae.objects.filter(status_buy='برای اجاره').order_by(
            '-upload_time'), 'title': 'vila_braye_rahn_ejare', }
    elif wh == "vila_vise":
        context = {"post": vilae.objects.filter(vise=True).order_by(
            '-upload_time'), 'title': 'vila_vise', }
    elif wh == "aparteman_kharid":
        context = {"post": aparteman.objects.filter(status_buy='برای خرید').order_by(
            '-upload_time'), 'title': 'aparteman_baraye_kharid', }
    elif wh == "aparteman_rahn":
        context = {"post": aparteman.objects.filter(status_buy='برای رهن و اجاره').order_by(
            '-upload_time'), 'title': 'aparteman_braye_rahn_ejare', }
    elif wh == "aparteman_vise":
        context = {"post": aparteman.objects.filter(vise=True).order_by(
            '-upload_time'), 'title': 'aparteman_vise', }
    elif wh == "zamin_maskoni":
        context = {"post": zamin.objects.filter(noe_zamin='مسکونی').order_by(
            '-upload_time'), 'title': 'zamin_maskoni', }
    elif wh == "zamin_bag":
        context = {"post": zamin.objects.filter(noe_zamin='باغ').order_by(
            '-upload_time'), 'title': 'zamin_bag', }
    elif wh == "zamin_tafrihi":
        context = {"post": zamin.objects.filter(noe_zamin='تفریحی توریستی').order_by(
            '-upload_time'), 'title': 'zamin_tafrihi', }
    elif context == {}:
        raise Http404
    return render(request, 'footer_view.html', context)

