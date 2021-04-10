from django.urls import path

from .views import HomeRendr, MakePostView

urlpatterns = [
    path('', HomeRendr.as_view(), name='home'),
    path('post/', MakePostView.as_view(), name='add_post')
]
