from django.test import TestCase

from apps.core.models import CoreModel
from apps.applications.models import Company, JobPosition, ApplicationStatus, JobApplication


class CoreModelTests(TestCase):
    
    def setUp(self):
        # Create test data
        self.company = Company.objects.create(name='Test Company')
        self.job_position = JobPosition.objects.create(
            title='Test Position',
            description='Test Description',
            company=self.company,
            date_posted='2024-01-01'
        )
        self.status = ApplicationStatus.objects.create(status='Applied')
        self.application = JobApplication.objects.create(
            job_position=self.job_position,
            status=self.status,
            resume='path/to/resume.pdf'
        )

    def test_all(self):
        companies = Company.all()
        self.assertIn(self.company, companies)

    def test_first(self):
        first_job_position = JobPosition.first()
        self.assertEqual(first_job_position, self.job_position)

    def test_last(self):
        last_application = JobApplication.last()
        self.assertEqual(last_application, self.application)

    def test_exists(self):
        exists = JobApplication.exists(job_position=self.job_position)
        self.assertTrue(exists)

    def test_not_exists(self):
        exists = JobApplication.exists(job_position=self.job_position, status=None)
        self.assertFalse(exists)
