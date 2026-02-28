# DAG Workflow Builder – Backend

This backend service powers the DAG Workflow Builder application. It is built using FastAPI and is responsible for managing workflow logic, validating graph structure, and ensuring that all workflows follow Directed Acyclic Graph (DAG) principles.

The system allows users to create workflow nodes, connect nodes using edges, validate the graph structure, detect cycles, and return structured responses to the frontend. Before any workflow is accepted, the backend verifies that the graph remains acyclic and logically consistent.

## Tech Stack
Python 3.x, FastAPI, Uvicorn, Pydantic

## Local Setup

Clone the repository:
git clone https://github.com/your-username/dag-workflow-builder_backend.git  
cd dag-workflow-builder_backend  

Install dependencies:
pip install -r requirements.txt  

Run the server:
uvicorn main:app --reload  

The server will run at:
http://127.0.0.1:8000  

API documentation (Swagger UI):
https://dag-workflow-builder-backend-2.onrender.com/docs 

## Deployment (Render)

Build Command:
pip install -r requirements.txt  

Start Command:
uvicorn main:app --host 0.0.0.0 --port 10000  

## Core Workflow Logic

1. User creates nodes  
2. User connects nodes via edges  
3. Backend validates the graph  
4. Cycle detection ensures DAG compliance  
5. Valid workflow data is returned to frontend  

## Environment Variables
No environment variables are currently required. If database or secret keys are added in future, they should be configured via the deployment platform.

##

This project was developed as part of a technical assessment.
