from django.urls import path, include
from main import views as v
urlpatterns = [

    path('', v.index, name='index'),
    path('daraja/stk_push',  v.stk_push_callback, name='stk_push'),
]
