from django.urls import path
from .views import index, by_rubric, detail, go_home, BbCreateView

urlpatterns = [
    path('', index, name='index'),
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('detail/<int:bb_id>/', detail, name='detail'),
    path('go/', go_home, name='go_home'),
    path('add/', BbCreateView.as_view(), name='add'),
]
