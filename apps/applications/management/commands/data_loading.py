from django.core.management.base import BaseCommand
from apps.applications.models import Company, JobPosition, ApplicationStatus, JobApplication
from faker import Faker

class Command(BaseCommand):
    help = 'Loads fake data for companies, job positions, application statuses, and job applications into the database'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate fake companies data
        companies_data = [
            {
                'name': fake.company(),
                'website': fake.url(),
                'address': fake.address()
            }
            for _ in range(20)
        ]

        if Company.objects.exists() is False:
            for company_data in companies_data:
                company, created = Company.objects.get_or_create(**company_data)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created company: {company.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Company already exists: {company.name}'))

        # Generate fake application statuses data
        statuses_data = ['Applied', 'Interviewing', 'Offer', 'Rejected', 'Hired']
        for status in statuses_data:
            status_obj, created = ApplicationStatus.objects.get_or_create(status=status)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created application status: {status_obj.status}'))
            else:
                self.stdout.write(self.style.WARNING(f'Application status already exists: {status_obj.status}'))

        # Generate fake job positions data
        job_positions_data = [
            {
                'title': fake.job(),
                'company': fake.random_element(companies_data),
                'location': fake.city(),
                'date_posted': fake.date_this_year(),
                'application_deadline': fake.date_this_year(),
                'description': fake.text(),
                'keywords': fake.words(nb=5)
            }
            for _ in range(20)
        ]

        for job_position_data in job_positions_data:
            company = Company.objects.get(name=job_position_data['company']['name'])
            job_position_data['company'] = company
            job_position, created = JobPosition.objects.get_or_create(**job_position_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created job position: {job_position.title} at {company.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Job position already exists: {job_position.title}'))

        # Generate fake job applications data
        job_applications_data = [
            {
                'job_position': fake.random_element(job_positions_data),
                'status': fake.random_element(statuses_data),
                'resume': fake.file_path(extension='pdf'),
                'cover_letter': fake.file_path(extension='pdf'),
                'notes': fake.text()
            }
            for _ in range(50)
        ]

        for job_application_data in job_applications_data:
            job_position = JobPosition.objects.get(title=job_application_data['job_position']['title'])
            status = ApplicationStatus.objects.get(status=job_application_data['status'])
            job_application_data['job_position'] = job_position
            job_application_data['status'] = status
            job_application, created = JobApplication.objects.get_or_create(**job_application_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created job application for {job_position.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Job application already exists for {job_position.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully created companies, job positions, application statuses, and job applications'))
