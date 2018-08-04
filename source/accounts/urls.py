from django.urls import path

from .views import (LogInView, SignUpView, LogOutView, CreateNewPublicationView, PublicationsListView)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),    
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('publications/createNewPublication/', CreateNewPublicationView.as_view(), name='createNewPublication')
]
