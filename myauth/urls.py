from django.urls import path, include
from myauth import  views as om
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

"""
router = DefaultRouter()
router.register(r'apikeys', om.APIKeyViewSet, basename='apikey')
"""

urlpatterns = [
    # path('api/', include(router.urls)),
    
    # path("home", om.home, name="home"),
    # path("login_user", om.login_user_view, name="login_user_view"),
    # path("", om.user_view, name="user_view"),
    # path('apiview/', om.ClassBasedView.as_view()),
    # path('api-token-auth/', om.CustomAuthToken.as_view()),

    # # path("cash", om.protected_view, name="protected"),
    # path("services/", om.services, name="services"),
    # path("about/", om.about, name="about"),
    # path("faq/", om.faq, name="faq"),
    # path("portfolio/", om.portfolio, name="portfolio"),
    # path("our-team/", om.steam, name="team"),

    path('login/', om.login_view, name="login"),
    path('logout/', om.logout_view, name="logout"),
    path('register/', om.signup, name="register"),
    path('profile/', om.profile, name="profile"),
    path('form-success/', om.form_submitted, name="form_submitted"),
    path('verify_email_sent/', om.verify_email_sent, name="verify_email_sent"),
     
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    
    path('verify-user-existance/<uidb64>/<token>/', om.account_verification, name='account_verification'),

    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
    name='password_reset_confirm'),
    path('password_reset/', om.password_reset_request, name='password_reset'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
      name='password_reset_complete'),
]