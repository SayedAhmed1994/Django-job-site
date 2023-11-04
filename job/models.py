#first step in project is creating models

from django.db import models
#for more details search for django models field in documentation.
# Create your models here.
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):                         #equal table in database
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)       #equal column in database
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name    