from django.db import models

class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def first(cls):
        return cls.objects.first()

    @classmethod
    def last(cls):
        return cls.objects.last()

    @classmethod
    def exists(cls, **kwargs):
        return cls.objects.filter(**kwargs).exists()
