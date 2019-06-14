from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('accounts/login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add_skill/', views.CreateSkill.as_view(), name="add_skill"),
    path('skills_index/', views.SkillsIndex.as_view(), name="skills_index"),
]

