# FastAPI Python Project

Welcome to the **FastAPI Python Project**! This repository demonstrates a scalable, high-performance web application built using [FastAPI](https://fastapi.tiangolo.com/), Python's modern, fast (high-performance) web framework.

---

## 🚀 Features

- **High Performance**: Built with Python's FastAPI for blazing-fast response times.
- **Asynchronous Programming**: Leverages Python's async capabilities for improved efficiency.
- **Scalable**: Modular structure for scalability and maintainability.
- **OpenAPI Documentation**: Automatically generated interactive API docs with Swagger UI.
- **Type-Safe**: Built-in support for type hints to catch errors early.
- **Ready for Deployment**: Configured to work seamlessly with tools like Docker and Kubernetes.

---

## 🛠️ Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.8+ installed
- [pip](https://pip.pypa.io/en/stable/) for package management
- [mysql server](https://www.mysql.com/) for database
- [Docker](https://www.docker.com/) for containerization

---

### Installation

1. Clone the repository:

```
git clone https://github.com/rushi2828/fastapi-python-project.git
cd fastapi-python-project
```
## Running the Application locally
1. Check server status
```
$ service mysql status
```

2. Start the development server  
```
$ service mysql start 
```

3. Run the commad
```
$ uvicorn app.main:app --reload
```

4. Create item using postman at [POST] http://127.0.0.1:8000/items
```
{
    "name": "first",
    "description": "This is first description"
}
```

5. Visit the item in your local browser at http://127.0.0.1:8000/items/1

6. Stop mysql service
```
$ service mysql stop
```

## Running the Application with Docker Compose

1. Build Docker Image
```
docker build -t <username>/fastapi-app:latest .
docker push <username>/fastapi-app:latest
```

2. Build and Run the Project (Linux/Windows)
```
docker-compose down
docker-compose up --build
```
3. Access Swagger API
```
http://localhost:8000/docs
```
![image](https://github.com/user-attachments/assets/17ae6dd5-7099-4413-8281-9db57f683eae)

### Troubleshooting

1. Stop running containers:
```
docker-compose down
```
2. Rebuild and run:
```
docker-compose up --build
```
### To Stop Containers
```
docker-compose down
```
# FastAPI + MySQL Kubernetes Deployment
## 📄 Apply Kubernetes Manifests
- Secret
```
kubectl apply -f k8s/mysql-secret.yaml
```
- ConfigMaps
```
kubectl apply -f k8s/mysql-configmap.yaml
```
- Persistent Volume
```
kubectl apply -f k8s/mysql-pvc.yaml
```
- Deploy MySQL deployment+service
```
kubectl apply -f k8s/mysql-deployment.yaml
```
- Deploy Fastapi deployment and expose service
```
kubectl apply -f k8s/fastapi-deployment.yaml
```
### 🔍 Verify Deployments
- List running pods:
```
kubectl get pods
```
### 🔥 Port Forwarding
```
kubectl port-forward svc/fastapi-service 8000:8000
```
### ✅ Test API
- Open your browser and visit:
```
Swagger Docs: http://localhost:8000/docs
```
![image](https://github.com/user-attachments/assets/2663162f-56d6-4cbf-a59f-6829d4075ccb)

