# ⚡ Task Manager Dashboard

<div align="center">

![Task Manager Banner](https://img.shields.io/badge/Full--Stack-Spring%20Boot%20%2B%20Django-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**A beautiful, interactive full-stack task management application with animated UI and AI-powered suggestions**

[Live Demo](https://springboot-django-full-stack-2.onrender.com) · [Report Bug](https://github.com/regalleo/springboot_django_full_stack/issues) · [Request Feature](https://github.com/regalleo/springboot_django_full_stack/issues)

</div>

---

## 🌟 Features

### 🎨 **Stunning Visual Experience**
- **Animated Network Background** - Dynamic particle connections that respond to mouse movement
- **Staircase Visualization** - Watch your character climb stairs as you complete tasks
- **Glassmorphism Design** - Modern UI with backdrop blur effects
- **Smooth Animations** - Celebrate task completion with animated characters

### 🚀 **Core Functionality**
- ✅ Create, Read, Update, and Delete tasks
- 🎯 Priority management (Low, Medium, High)
- 📊 Task status tracking (Todo, Done)
- 🖼️ Dynamic task images powered by Pixabay API
- 💬 AI-powered suggestion chatbot using Hugging Face

### 🎭 **Interactive Elements**
- 🧍 Animated characters that sleep on incomplete tasks
- 🎉 Celebration animations when tasks are completed
- 💬 Speech bubbles with motivational messages
- 🏆 Success platform for completed tasks

---

## 🛠️ Tech Stack

### **Backend**
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat&logo=springboot&logoColor=white)
![Java](https://img.shields.io/badge/Java%2017-ED8B00?style=flat&logo=openjdk&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat&logo=apachemaven&logoColor=white)

- **Spring Boot** - RESTful API backend
- **Java 17** - Core programming language
- **REST API** - Clean endpoint architecture

### **Frontend**
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

- **Django** - Frontend framework
- **Vanilla JavaScript** - Interactive animations
- **Bootstrap 5** - Responsive design
- **Canvas API** - Network background animation
- **Axios** - HTTP client

### **AI Integration**
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)

- **Hugging Face API** - AI-powered suggestion chatbot
- **Pixabay API** - Dynamic task image generation

### **Deployment**
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

- **Render.com** - Cloud hosting platform
- **Docker** - Containerization
- **WhiteNoise** - Static file serving

---

## 📸 Screenshots

<div align="center">

### 🏠 Main Dashboard
![Dashboard](https://via.placeholder.com/800x400/0a0a0f/BB86FC?text=Task+Manager+Dashboard)

### 🎯 Task Management
![Tasks](https://via.placeholder.com/800x400/0a0a0f/03DAC6?text=Interactive+Task+Cards)

### 💬 AI Chatbot
![Chatbot](https://via.placeholder.com/800x400/0a0a0f/BB86FC?text=AI+Suggestion+Chatbot)

</div>

---

## 🚀 Getting Started

### Prerequisites

- **Java 17+**
- **Python 3.11+**
- **Maven** (for backend)
- **pip** (for frontend)

### Installation

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/regalleo/springboot_django_full_stack.git
cd springboot_django_full_stack
```

#### 2️⃣ Setup Backend (Spring Boot)
```bash
cd taskmanager

# Build the project
./mvnw clean install

# Run the application
./mvnw spring-boot:run
```
Backend will run on `http://localhost:8080`

#### 3️⃣ Setup Frontend (Django)
```bash
cd ../task_frontend

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "HUGGINGFACE_API_KEY=your_api_key_here" > .env
echo "HF_MODEL=gpt2" >> .env
echo "BACKEND_API_URL=http://localhost:8080" >> .env

# Collect static files
python manage.py collectstatic --noinput

# Run the server
python manage.py runserver
```
Frontend will run on `http://localhost:8000`

---

## 🌐 Live Deployment

### **Production URLs**
- 🎨 **Frontend**: [https://springboot-django-full-stack-2.onrender.com](https://springboot-django-full-stack-2.onrender.com)
- 🔧 **Backend API**: [https://todo-backend-8l4s.onrender.com](https://todo-backend-8l4s.onrender.com)

### **API Endpoints**
```bash
GET    /api/tasks          # Get all tasks
POST   /api/tasks          # Create new task
PUT    /api/tasks/{id}     # Update task
DELETE /api/tasks/{id}     # Delete task
```

---

## 🎯 Usage

### Creating a Task
1. Enter task title and description
2. Select priority level
3. Click "Add Task"
4. Watch your character appear on a new stair!

### Completing Tasks
1. Click "Toggle Status" on any task
2. Watch the character celebrate 🎉
3. See them reach the SUCCESS platform 🏆

### AI Suggestions
1. Click the chat icon (💬) in bottom-right
2. Type your question or request
3. Get AI-powered suggestions instantly!

---

## 🎨 Customization

### Change Color Theme
Edit `task_list.html` CSS variables:
```css
:root {
    --primary-color: #BB86FC;
    --secondary-color: #03DAC6;
    --background: #0a0a0f;
}
```

### Configure AI Model
Edit `.env` file:
```env
HF_MODEL=gpt2  # Change to any Hugging Face model
HUGGINGFACE_API_KEY=your_key_here
```

---

## 📁 Project Structure

```
springboot_django_full_stack/
├── taskmanager/                 # Spring Boot Backend
│   ├── src/
│   │   └── main/
│   │       ├── java/           # Java source files
│   │       └── resources/      # Configuration files
│   ├── pom.xml                 # Maven dependencies
│   └── Dockerfile              # Docker configuration
│
├── task_frontend/              # Django Frontend
│   ├── static/
│   │   └── images/            # Static assets
│   ├── templates/
│   │   └── tasks/             # HTML templates
│   ├── tasks/                 # Django app
│   ├── manage.py              # Django CLI
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables
│
└── README.md                   # You are here!
```

---

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐛 Known Issues

- Tasks are stored in memory (no persistent database)
- Avatar image requires static file collection on deployment
- AI chatbot requires valid Hugging Face API key

---

## 📝 Future Enhancements

- [ ] Add user authentication
- [ ] Implement persistent database (PostgreSQL)
- [ ] Add task categories and tags
- [ ] Export tasks to CSV/PDF
- [ ] Mobile app version
- [ ] Real-time collaboration
- [ ] Task reminders and notifications
- [ ] Dark/Light theme toggle

---

## 👨‍💻 Developer

<div align="center">

**Raj Shekhar Singh**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/raj-shekhar-singh-aa16ab245)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/regalleo)

</div>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Spring Boot](https://spring.io/projects/spring-boot) - Backend framework
- [Django](https://www.djangoproject.com/) - Frontend framework
- [Bootstrap](https://getbootstrap.com/) - UI components
- [Pixabay](https://pixabay.com/) - Image API
- [Hugging Face](https://huggingface.co/) - AI models
- [Render](https://render.com/) - Deployment platform
- [Animate.css](https://animate.style/) - Animation library
- [Font Awesome](https://fontawesome.com/) - Icons

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

**Made with ❤️ and lots of ☕**

</div>
