from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from projects.models import Project
from .models import Shape
from .schemas import ShapeCreate, ShapeUpdate, ShapeOut
from users.api import AuthBearer

shape_router = Router()


@shape_router.get("/{project_id}", response=List[ShapeOut], auth=AuthBearer())
def list_shapes(request, project_id: int):
    """List all shapes in a project"""
    project = get_object_or_404(Project, id=project_id)
    if not (
        project.is_public
        or project.owner == request.auth
        or project.collaborators.filter(id=request.auth.id).exists()
    ):
        return {"error": "Not authorized"}
    return Shape.objects.filter(project_id=project_id)


@shape_router.get("/{shape_id}", response=ShapeOut, auth=AuthBearer())
def get_shape(request, shape_id: int):
    """Get a specific shape"""
    shape = get_object_or_404(Shape, id=shape_id)
    project = shape.project
    if not (
        project.is_public
        or project.owner == request.auth
        or project.collaborators.filter(id=request.auth.id).exists()
    ):
        return {"error": "Not authorized"}
    return shape


@shape_router.post("/{project_id}", response=List[ShapeOut], auth=AuthBearer())
def create_shapes(request, project_id: int, payload: List[ShapeCreate]):
    """Create multiple shapes in a project"""
    project = get_object_or_404(Project, id=project_id)
    if not (
        project.owner == request.auth
        or project.collaborators.filter(
            id=request.auth.id, projectcollaborator__role="EDITOR"
        ).exists()
    ):
        return {"error": "Not authorized"}

    shapes = [
        Shape(
            project_id=project_id,
            created_by=request.auth,
            x=shape.x,
            y=shape.y,
            **shape.dict(exclude={"x", "y"}),
        )
        for shape in payload
    ]
    # Bulk create for better performance
    created_shapes = Shape.objects.bulk_create(shapes)
    return created_shapes


@shape_router.put("/{project_id}", response=List[ShapeOut], auth=AuthBearer())
def update_shapes(request, project_id: int, payload: List[ShapeUpdate]):
    """Update multiple shapes"""
    project = get_object_or_404(Project, id=project_id)
    if not (
        project.owner == request.auth
        or project.collaborators.filter(
            id=request.auth.id, projectcollaborator__role="EDITOR"
        ).exists()
    ):
        return {"error": "Not authorized"}

    updated_shapes = []
    for shape_data in payload:
        shape = get_object_or_404(Shape, id=shape_data.id, project_id=project_id)
        for key, value in shape_data.dict(exclude_unset=True).items():
            setattr(shape, key, value)
        shape.save()
        updated_shapes.append(shape)
    return updated_shapes


@shape_router.delete("/{project_id}/shapes", auth=AuthBearer())
def delete_shapes(request, project_id: int, shape_ids: List[int]):
    """Delete multiple shapes"""
    project = get_object_or_404(Project, id=project_id)
    if not (
        project.owner == request.auth
        or project.collaborators.filter(
            id=request.auth.id, projectcollaborator__role="EDITOR"
        ).exists()
    ):
        return {"error": "Not authorized"}

    Shape.objects.filter(id__in=shape_ids, project_id=project_id).delete()
    return {"success": True}
