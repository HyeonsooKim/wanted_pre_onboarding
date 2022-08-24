from rest_framework import serializers
from my_api.models import Person, JobPosting, Application, CompanyInfo

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
   class Meta:
       model = JobPosting
       fields = '__all__'

class CompanyInfoSerializer(serializers.ModelSerializer):
   jobpostings = JobPostingSerializer(read_only=True, many=True)
   class Meta:
       model = CompanyInfo
       fields = ('company_id', 'name', 'nation', 'location', 'jobpostings')

class ApplicationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Application
       fields = '__all__'