from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Shape(models.Model):
    SHAPE_TYPES = [
        ("rectangle", "Rectangle"),
        ("circle", "Circle"),
        ("line", "Line"),
        ("text", "Text"),
    ]

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="shapes"
    )
    shape_type = models.CharField(max_length=20, choices=SHAPE_TYPES)
    x = models.FloatField()
    y = models.FloatField()
    properties = models.JSONField()  # For width, height, radius, etc.
    style = models.JSONField()  # For fill, stroke, padding, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_shapes"
    )
    order = models.IntegerField(default=0)  # For z-index/layering

    class Meta:
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"{self.shape_type} at ({self.x}, {self.y}) in {self.project.title}"
