from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#from .views import HomeRendr, MakePostView
from .views import MakePostView, printer

urlpatterns = [
    #path('', HomeRendr.as_view(), name='home'),
    path('post/', MakePostView.as_view(), name='add_post'),
    path('pred/', printer, name='print_pred')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
