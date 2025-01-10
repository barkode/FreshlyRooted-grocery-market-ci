from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('profile/', include('profile.urls', namespace='profile')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500
