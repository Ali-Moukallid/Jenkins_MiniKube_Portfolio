from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CollaborationRequest(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    COUNTRY_CHOICES = [
        ('LEB', 'Lebanon'),
        ('CYP', 'Cyprus'),
        ('JOR', 'Jordan'),
        ('EGY', 'Egypt'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES)
    available_online = models.BooleanField(default=False)
    project_name = models.CharField(max_length=200)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.project_name}" 