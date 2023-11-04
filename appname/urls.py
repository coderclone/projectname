from django.urls import path
from . import views

urlpatterns = [
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
    path('encrypt-form/', views.encrypt_form_view, name='encrypt-form'),
    path('decrypt-form/', views.decrypt_form_view, name='decrypt-form'),
    path('api/encrypt/', views.EncryptAPIView.as_view(), name='encrypt-api'),
    path('api/decrypt/', views.DecryptAPIView.as_view(), name='decrypt-api'),

]
