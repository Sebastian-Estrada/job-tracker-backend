from django.test import TestCase

from apps.applications.models import Company, JobPosition, ApplicationStatus, JobApplication


class CompanyModelTests(TestCase):
    
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', website='http://test.com', address='123 Test St')

    def test_company_str(self):
        self.assertEqual(str(self.company), 'Test Company')

class JobPositionModelTests(TestCase):
    
    def setUp(self):
        self.company = Company.objects.create(name='Test Company')
        self.job_position = JobPosition.objects.create(
            title='Test Position',
            description='Test Description',
            company=self.company,
            date_posted='2024-01-01'
        )

    def test_job_position_str(self):
        self.assertEqual(str(self.job_position), 'Test Position at Test Company')

class ApplicationStatusModelTests(TestCase):
    
    def setUp(self):
        self.status = ApplicationStatus.objects.create(status='Applied')

    def test_application_status_str(self):
        self.assertEqual(str(self.status), 'Applied')

class JobApplicationModelTests(TestCase):
    
    def setUp(self):
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

    def test_job_application_str(self):
        self.assertEqual(str(self.application), 'Applied for Test Position')

    def test_job_application_data(self):
        self.assertEqual(self.application.job_position, self.job_position)
        self.assertEqual(self.application.status, self.status)
        self.assertEqual(self.application.resume, 'path/to/resume.pdf')
