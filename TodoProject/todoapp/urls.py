
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('cbndetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbndetail'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbnhome/',views.TaskListview.as_view(),name='cbnhome'),
    path('cbnupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbnupdate'),
    path('cbndelete/<int:pk>/',views.TaskUpdateview.as_view(),name='cbndelete'),
]