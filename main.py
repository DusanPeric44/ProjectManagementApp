from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

#HTTP metode: GET, POST, PUT, DELETE

@app.post('/developers/')
def create_developer(developer: Developer):
    # dodavali u bazu
    return {
        "message": "Developer created successfully",
        "developer": developer
    }

@app.post('/projects/')
def create_project(project: Project):
    # dodavali u bazu
    return {
        "message": "Project created successfully",
        "project": project
    }

@app.get('/projects/')
def get_projects():
    # poziv na bazu za dohvatanje svih projekata

    sample_project = Project(
        title="Sample Project",
        description="...",
        languages=["Python", "JavaScript"],
        lead_developer=Developer(name="John Doe", experience=5)
    )

    return {
        "projects": [sample_project]
    }