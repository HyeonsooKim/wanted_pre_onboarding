from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from my_api.serializers import PersonSerializer, JobPostingSerializer, ApplicationSerializer, CompanyInfoSerializer
from my_api.models import Person, JobPosting, Application, CompanyInfo

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer

class CompanyInfoViewSet(viewsets.ModelViewSet):
   queryset = CompanyInfo.objects.all()
   serializer_class = CompanyInfoSerializer

class CompanyInfoListViewSet(viewsets.ModelViewSet):
   serializer_class = CompanyInfoSerializer
   queryset = CompanyInfo.objects.all()

class JobPostingViewSet(viewsets.ModelViewSet):
   queryset = JobPosting.objects.all()
   serializer_class = JobPostingSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
   queryset = Application.objects.all()
   serializer_class = ApplicationSerializer
