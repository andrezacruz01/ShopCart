from django.conf.urls import url
from shopcart import views
from shopcart.views import RegisterCreditcardView

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^cart/$', RegisterCreditcardView.as_view(), name='cart'),
    ]
