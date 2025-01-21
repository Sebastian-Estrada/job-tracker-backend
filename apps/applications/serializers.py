from rest_framework import serializers

from .models import Company, JobPosition, ApplicationStatus, JobApplication

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = '__all__'



# class JobPositionSerializer(serializers.ModelSerializer):
#     keywords = serializers.SerializerMethodField()

#     class Meta:
#         model = JobPosition
#         fields = ['id', 'title', 'company', 'location', 'date_posted', 'application_deadline', 'description', 'keywords']
#         # Exclude 'keywords' from input data handling
#         extra_kwargs = {
#             'keywords': {'write_only': True}
#         }

#     def get_keywords(self, obj):
#         # Return the keywords as a list if they are available, or an empty list otherwise
#         return obj.keywords or []

#     def create(self, validated_data):
#         # Remove 'keywords' from validated_data to prevent it from being set during creation
#         validated_data.pop('keywords', None)
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         # Remove 'keywords' from validated_data to prevent it from being set during updates
#         validated_data.pop('keywords', None)
#         return super().update(instance, validated_data)

class JobPositionSerializer(serializers.ModelSerializer):
    # Define the 'keywords' field as a SerializerMethodField to manage visibility in GET requests
    keywords = serializers.SerializerMethodField()

    class Meta:
        model = JobPosition
        fields = ['id', 'title', 'company', 'location', 'date_posted', 'application_deadline', 'description', 'keywords']
        extra_kwargs = {
            'keywords': {'write_only': True}
        }

    def get_keywords(self, obj):
        # This method provides the 'keywords' field value when retrieving data
        return obj.keywords or []

    def create(self, validated_data):
        # Create JobPosition instance
        job_position = JobPosition.objects.create(**validated_data)
        job_position.save()
        return job_position

    def update(self, instance, validated_data):
        # Update JobPosition instance fields
        instance.title = validated_data.get('title', instance.title)
        instance.company = validated_data.get('company', instance.company)
        instance.location = validated_data.get('location', instance.location)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.application_deadline = validated_data.get('application_deadline', instance.application_deadline)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        instance.save()
        return instance

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'job_position', 'application_date', 'status', 'resume', 'cover_letter', 'notes']
