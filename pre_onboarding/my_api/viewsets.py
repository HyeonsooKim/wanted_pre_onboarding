from django.urls import path
from .views import *

# jobpostings 목록 보여주기
jobpostings_list = JobPostingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# jobpostings detail 보여주기 + 수정 + 삭제
jobpostings_detail = JobPostingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('jobpostings/', jobpostings_list),
    path('jobpostings/<int:pk>/', jobpostings_detail),
]