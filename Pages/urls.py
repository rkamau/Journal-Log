"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name="Log"

urlpatterns = [

    path("topic/", views.topic_view, name = "topic-page"),
    path("topic/entries/<int:id>/", views.entries_view, name = "contents-page"),
    path("new_topic/", views.addtopicview, name= "add-topic"),
    path("new_entry/", views.navigatetopicview, name = "nav-topic"),
    path("newentry/<int:topic_id>/", views.addentryview, name = "add-entry"),
    path("edit_entry/<int:entry_id>/", views.editentryview, name="edit-entry")
]
