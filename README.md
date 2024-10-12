# Next.js & Flask Submission Form App

This is a full-stack application built with Next.js (Frontend) and Flask (Backend). The project includes a submission form that collects user details and stores them in a database. The app is containerized using Docker for easy setup and deployment.

## Features

- Responsive form using Next.js
- Backend API using Flask with SQLAlchemy. Database using MySQL
- Data submission using Axios
- Modal feedback on form submission
- Dark mode toggle
- Dockerized setup for seamless deployment

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## Project Structure
. ├── backend │ ├── app.py # Flask backend │ ├── models.py # SQLAlchemy models │ ├── Dockerfile ├── frontend │ ├── pages │ │ └── index.js # Next.js frontend │ ├── public │ ├── Dockerfile ├── docker-compose.yml # Docker compose for orchestration └── README.md 

# Project instructions
## Installation
### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Setup Environment Variables

```makefile
FLASK_APP = server
FLASK_DEBUG = True
JWT_SECRET = 5b3b7a106b81e92a6a6e6c36d2c7d6316a7eb13e42a26ca7b24a7502f660466f5f4da9e10e938c33ff8b92bd3e1e6383922e525715450cf80c2330a19c353ded3502d432d578003df30b11dcbd66b6973248d4b35b7748eaa65a3e4dda718954d2d37661755eb2297641f1271d8a6919dd0480d0dd1f64a0f6d88381c195513f

DB_HOST = 127.0.0.1:3306
DB_DATABASE = profile
DB_USERNAME = root
DB_PASSWORD = 
DATABASE_URL = mysql+pymysql://root@localhost:3306/profile?charset=utf8mb4
```

### 3. Docker Setup
Build and Run with Docker. Run the following command in the root directory (where docker-compose.yml is located):
```bash
docker-compose up --build
```

### 4. Access the Application
* The frontend (Next.js) will be available at: http://localhost:3000
* The backend (Flask API) will be available at: http://localhost:5000

# Docker Configuration
## Dockerfile (Frontend)
```dockerfile
# frontend/Dockerfile

FROM node:16-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
```

## Dockerfile (Backend)
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## Docker Compose
```yaml
version: '3'
services:
  frontend:
    build: ./client
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:5000
  backend:
    build: ./server
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    volumes:
      - ./server:/app

```
### Key Sections:
1. **Prerequisites**: Lists Docker and Docker Compose.
2. **Installation**: Step-by-step instructions for cloning the repo, setting environment variables, and launching the app with Docker.
3. **Dockerfile and Docker Compose**: Explains how the app is containerized.
4. **Running the App**: Instructions to access the frontend and backend.
5. **Troubleshooting**: Common issues you might encounter.
