from django.urls import path, include
from .apiviews import test_auth, transformer_list

urlpatterns = [
    path('test-auth/', test_auth, name='test_user'),
    path('transformers/', transformer_list, name='transformers_list'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(r'^', include('django.contrib.auth.urls')),
]