# projects/api.py
from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Project, ProjectCollaborator
from .schemas import ProjectCreate, ProjectUpdate, ProjectOut, CollaboratorSchema
from users.api import AuthBearer

project_router = Router()


@project_router.get("/", response=List[ProjectOut], auth=AuthBearer())
def list_projects(request):
    """List all projects user has access to (owned or collaborated)"""
    return Project.objects.filter(
        Q(owner=request.auth) | Q(collaborators=request.auth) | Q(is_public=True)
    ).distinct()


@project_router.post("/", response=ProjectOut, auth=AuthBearer())
def create_project(request, payload: ProjectCreate):
    """Create a new project"""
    project = Project.objects.create(owner=request.auth, **payload.dict())
    return project


@project_router.get("/{project_id}", response=ProjectOut, auth=AuthBearer())
def get_project(request, project_id: int):
    """Get project details"""
    project = get_object_or_404(Project, id=project_id)
    if not (
        project.is_public
        or project.owner == request.auth
        or project.collaborators.filter(id=request.auth.id).exists()
    ):
        return {"error": "Not authorized"}
    return project


@project_router.put("/{project_id}", response=ProjectOut, auth=AuthBearer())
def update_project(request, project_id: int, payload: ProjectUpdate):
    """Update project details"""
    project = get_object_or_404(Project, id=project_id, owner=request.auth)
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(project, key, value)
    project.save()
    return project


@project_router.delete("/{project_id}", auth=AuthBearer())
def delete_project(request, project_id: int):
    """Delete a project"""
    project = get_object_or_404(Project, id=project_id, owner=request.auth)
    project.delete()
    return {"success": True}


@project_router.post("/{project_id}/collaborators", auth=AuthBearer())
def add_collaborator(request, project_id: int, payload: CollaboratorSchema):
    """Add a collaborator to a project"""
    get_object_or_404(Project, id=project_id, owner=request.auth)
    ProjectCollaborator.objects.create(
        project_id=project_id, user_id=payload.user_id, role=payload.role
    )
    return {"success": True}


@project_router.delete("/{project_id}/collaborators/{user_id}", auth=AuthBearer())
def remove_collaborator(request, project_id: int, user_id: int):
    """Remove a collaborator from a project"""
    get_object_or_404(Project, id=project_id, owner=request.auth)
    ProjectCollaborator.objects.filter(project_id=project_id, user_id=user_id).delete()
    return {"success": True}
