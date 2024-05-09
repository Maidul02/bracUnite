from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='HOME'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('about/', views.about, name='ABOUT'),
    path('portfolio/<int:user_id>', views.portfolio, name='portfolio'),
    path('study/', views.study, name='STUDY'),
    path('contact/', views.contact, name='CONTACT ME'),
    path('login/', views.Handle_login, name='Log In'),
    path('signup/', views.Handle_signup, name='Sign Up'),
    path('logout/', views.Handle_logout, name='Log Out'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    path('student/', views.student, name='Student'),
    path('alumni/', views.alumni, name='Alumni'),
    path('faculty/', views.faculty, name='Faculty'),
    path('edit/', views.profile_update, name='profile_update'),
    path('cv/<int:user_id>', views.cv, name='cv'),
    path('ride/', views.ride, name='ride'),
    path('send_notification/<int:recipient_id>/', views.send_notification, name='send_notification'),
    path('notification/', views.see_notification, name='notification'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)