
from django.urls import path
from . import views

urlpatterns = [
    # 고객 목록 페이지로 연결되는 URL 설정
    path('', views.index, name='EDA'),
]

