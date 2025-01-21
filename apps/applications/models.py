from django.db import models

from apps.core.models import CoreModel

class Company(CoreModel):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class JobPosition(CoreModel):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='job_positions', on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_posted = models.DateField()
    application_deadline = models.DateField(blank=True, null=True)
    description = models.TextField()
    keywords = models.JSONField(default=list)

    def __str__(self):
        return f'{self.title} at {self.company.name}'

class ApplicationStatus(CoreModel):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class JobApplication(CoreModel):
    job_position = models.ForeignKey(JobPosition, related_name='applications', on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(ApplicationStatus, related_name='applications', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover-letters/')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Applied for {self.job_position.title}'
