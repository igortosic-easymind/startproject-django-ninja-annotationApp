from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_projects"
    )
    collaborators = models.ManyToManyField(
        User, through="ProjectCollaborator", related_name="collaborated_projects"
    )
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class ProjectCollaborator(models.Model):
    ROLE_CHOICES = [
        ("VIEWER", "Viewer"),
        ("EDITOR", "Editor"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="VIEWER")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["project", "user"]
