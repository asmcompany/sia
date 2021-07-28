
from django.contrib import admin
from django.urls import path, include

# static config
from django.conf.urls.static import static
from VEGAN import settings

# dummy view
from django.shortcuts import render
def home(r):
    return render(r, 'base/base.html', {})


urlpatterns = [
    # django admin urls
    path('admin/', admin.site.urls),

    # render partial urls
    path('partial/', include('VEGAN_PARTIAL.urls')),

    # main apps urls
    path('', home, name='home_page'),
    path('shop/', include('VEGAN_API.VEGAN_API_PRODUCT.urls')),
    path('comment/', include('VEGAN_API.VEGAN_API_COMMENT.urls')),
    path('cart/', include('VEGAN_API.VEGAN_API_CART.urls')),
    path('account/', include('VEGAN_API.VEGAN_API_ACCOUNT.urls')),
    path('search/', include('VEGAN_API.VEGAN_API_SEARCH.urls')),
    path('checkout/', include('VEGAN_API.VEGAN_API_CHECKOUT.urls')),
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
