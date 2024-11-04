# EasyNotes Canvas - Backend

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Django Ninja](https://img.shields.io/badge/Django_Ninja-latest-orange.svg)](https://django-ninja.rest-framework.com/)

EasyNotes Canvas is a robust web-based application that enables users to create and edit visual notes on a digital canvas. The platform allows users to add various shapes, text elements, and collaborate in real-time, making it perfect for brainstorming, project planning, and visual organization.

## 🌟 Features

- **User Authentication & Authorization**
  - JWT-based authentication system
  - Role-based access control for projects
  - Secure password handling

- **Project Management**
  - Create and manage multiple canvas projects
  - Public/Private project settings
  - Collaborative editing capabilities
  - Project sharing and permissions management

- **Shape Management**
  - Support for multiple shape types (rectangle, circle, line, text)
  - Real-time shape manipulation
  - Layer ordering and z-index control
  - Custom styling options

- **Technical Features**
  - RESTful API using Django Ninja
  - PostgreSQL database integration
  - CORS support for frontend integration
  - Rate limiting middleware
  - Comprehensive API documentation

## 🚀 Live Demo

Try out the live demo of the application:
- **URL**: [Live Demo Link]
- **Demo Credentials**:
  ```
  Username: testuser
  Password: demo1234
  ```

> Note: The application is hosted on Render's free tier, which may cause initial cold starts. Please allow a few moments for the first load.

## 🛠️ Technology Stack

- **Backend Framework**: Django 4.2
- **API Framework**: Django Ninja
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Hosting**: Render
- **Additional Tools**:
  - `django-cors-headers` for CORS support
  - `whitenoise` for static file handling
  - `django-environ` for environment management
  - `psycopg2-binary` for PostgreSQL integration

## 🔧 Installation & Setup

### Prerequisites

- Python 3.x
- PostgreSQL (optional, can use SQLite for development)
- pip (Python package manager)
- virtualenv or pyenv

### Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/igortosic-easymind/startproject-django-ninja-annotationApp.git
   cd startproject-django-ninja-annotationApp
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## 📡 API Documentation

### Authentication Endpoints

```bash
POST /api/auth/login/
POST /api/auth/logout/
GET  /api/auth/me/
```

### Project Endpoints

```bash
GET    /api/projects/
POST   /api/projects/
GET    /api/projects/{id}/
PUT    /api/projects/{id}/
DELETE /api/projects/{id}/
```

### Shape Endpoints

```bash
GET    /api/shapes/{project_id}/
POST   /api/shapes/{project_id}/
PUT    /api/shapes/{project_id}/
DELETE /api/shapes/{project_id}/shapes/
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

For specific app tests:
```bash
python manage.py test projects
python manage.py test shapes
```

## 🔐 Security

- JWT token expiration
- CORS protection
- Rate limiting
- CSRF protection
- Secure password validation

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR adheres to:
- Proper documentation
- Test coverage
- Code style guidelines

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - *Initial work* - [YourGitHub](https://github.com/igortosic-easymind)

## 🙏 Acknowledgments

- Django community
- Django Ninja documentation
- Contributors and testers

## 📞 Support

For support, email me or open an issue in the repository.