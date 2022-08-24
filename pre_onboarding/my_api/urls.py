from django.urls import include, path
from rest_framework import routers
from my_api.views import PersonViewSet, JobPostingViewSet, ApplicationViewSet, CompanyInfoViewSet, CompanyInfoListViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'jobpostings', JobPostingViewSet)
router.register(r'companyInfo', CompanyInfoListViewSet)
router.register(r'application', ApplicationViewSet)

urlpatterns = [
   path('', include(router.urls)),
]