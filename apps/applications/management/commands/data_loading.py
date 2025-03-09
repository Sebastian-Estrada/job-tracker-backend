from django.core.management.base import BaseCommand
from applications.models import Company
from faker import Faker

class Command(BaseCommand):
    help = 'Loads the data of the companies into the database'

    def handle(self, *args, **options):
        fake = Faker()
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

        self.stdout.write(self.style.SUCCESS(f'Successfully created companies'))