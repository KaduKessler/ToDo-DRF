from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>', views.TaskDetailed.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
