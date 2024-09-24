
from django.urls import path
from . import views

urlpatterns = [
    # 고객 목록 페이지로 연결되는 URL 설정
    path('', views.customer_list, name='customer'),
    path('new', views.predict_churn, name='new_churn'),
    path('<str:customer_id>/', views.customer_detail, name='customer_detail'),
]

