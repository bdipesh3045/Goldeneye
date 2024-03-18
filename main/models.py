from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class StudentsResgister(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course_name = models.CharField(max_length=255)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.course_name}"


class contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14, unique=True)
    comments = models.CharField(max_length=700)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.phone}"

    class Meta:
        ordering = ["-date"]


class Notification(models.Model):
    message = models.CharField(max_length=255)
    image = models.ImageField(upload_to="notification_images/", null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message}'"

    class Meta:
        ordering = ["-date"]


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.question}'"

    class Meta:
        ordering = ["-date"]


# Team Model
class TeamModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    facebook = models.CharField(max_length=255)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.post}"


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class ServiceDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to="service_images/", null=True, blank=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     filters = [
    #         models.Filter(fields=["title"]),
    #     ]
