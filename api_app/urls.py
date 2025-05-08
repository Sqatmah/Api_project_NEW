from django.urls import path
from . import views

urlpatterns = [
    path('fbv/',views.user_form_fbv, name ='form_fbv'),
    path('cbv/',views.UserFormCBV.as_view(), name='form_cbv'),
    path('generic/', views.UserFormGenericView.as_view(), name='form_generic'),
]