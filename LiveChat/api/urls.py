from django.urls import path

# , CreateUserView
from .views import UserProfileView, GetPublicUserProfile, CheckUserEmailExists
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserProfileView.as_view()),
    path('user/<str:userPage>', GetPublicUserProfile),

    # userEmail will come in the form test@email instead of test@email.com
    path('email/<str:userEmail>', CheckUserEmailExists),

    # path('create-user/', CreateUserView.as_view()),
    # this view requires an authToken when adding 'obtain_auth_token'
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]
