from django.db import models


class CompanyInfo(models.Model):
	company_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, null=False)
	nation = models.CharField(max_length=20, null=False, default='한국')
	location = models.CharField(max_length=30, null=False)
	def __str__(self):
		return self.name

class JobPosting(models.Model):
	# jobposting_id = models.AutoField(primary_key=True)
	company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='jobpostings')
	position = models.CharField(max_length=100, null=False)
	reward = models.IntegerField(null=False)
	contents = models.CharField(max_length=1000, null=False)
	skill = models.CharField(max_length=50, null=False)

	def __str__(self):
		return self.company_id.name + '-' + self.position + f'({self.skill})'
       
class Person(models.Model):
	person_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, null=False)
	birth_year = models.CharField(max_length=10, null=False)
	skill = models.CharField(max_length=50, null=False)

	def __str__(self):
		return self.name

class Application(models.Model):
	company_name = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	def __str__(self):
		return self.company_name.id + '-' + self.person.person_id
