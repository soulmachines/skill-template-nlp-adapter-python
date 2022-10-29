from fastapi import FastAPI
from .views import skill

def create_app():
  app = FastAPI(
    title="Skill Hooks",
    version="0.0.0",
    description="Your description goes here",
  )

  # Add routes
  app.include_router(router=skill.router)

  return app