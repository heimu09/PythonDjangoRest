from django.urls import path
from auths.views import registr, auth, exit, edit_user_info


urlpatterns = [
    path('registr/', registr, name='registr'),
    path('login/', auth, name='auth'),
    path('logout/', exit, name='logout'),
    path('edit/', edit_user_info, name='edit')
]