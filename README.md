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
## Running the Application
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
$ uvicorn main:app --reload
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


