from django.urls import path
from . import views
from .views import logout_view

app_name = "tweetapp"

urlpatterns = [
    path("",views.listtweet,name="listtweet"),
    path("addtweet/",views.addtweet,name="addtweet"),
    path('logout/', logout_view, name='logout'),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet")
]