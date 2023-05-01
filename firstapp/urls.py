from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login_view,name="login"),
    path('accountverify/<str:id>',views.account_verify_view,name='accountverify'),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('settingprofile/',views.setting_profile,name="setting_profile"),
    path('changepassword/',views.change_password,name="change_password"),
    path('adduser/',views.adduser,name="adduser"),
    path('allusers/',views.allusers,name="allusers"),
    path('edituser/<int:id>/',views.edituser,name="edituser"),
    path('deleteuser/<int:id>/',views.deleteuser,name="deleteuser"),
    path('profile/',views.profile,name="profile"),
]


