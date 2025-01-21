from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .models import Company, JobPosition, ApplicationStatus, JobApplication
from .serializers import CompanySerializer, JobPositionSerializer, ApplicationStatusSerializer, JobApplicationSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


class ApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer
    permission_classes = [IsAuthenticated]


class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = [IsAuthenticated]


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        job_position = JobPosition.objects.get(id=request.data['job_position'])
        job_description = job_position.job_description

        if job_description:
            resume_text = request.data.get('resume', '')
            cover_letter_text = request.data.get('cover_letter', '')
            response_data = serializer.data
        else:
            response_data = serializer.data

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)