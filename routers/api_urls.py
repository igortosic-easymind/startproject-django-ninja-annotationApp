# routers/api.py
from ninja import NinjaAPI
from users.api import user_router
from projects.api import project_router
from shapes.api import shape_router

api = NinjaAPI()

api.add_router("/auth/", user_router, tags=["Users API"])
api.add_router("/projects/", project_router, tags=["Projects API"])
api.add_router("/shapes/", shape_router, tags=["Shapes API"])
