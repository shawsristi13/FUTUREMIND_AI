# 🧠 FUTUREMIND AI

### Learn Smarter • Plan Better • Grow Faster

FUTUREMIND AI is an AI-powered Study & Career Assistant designed to help students learn concepts, test their knowledge, plan their careers, identify skill gaps, and prepare for interviews.

It combines modern AI technology with a simple and interactive web interface built using Streamlit.

---

## 🌟 Features

### 📚 AI Study Tutor
- Ask any academic question.
- Receive simple and easy-to-understand AI explanations.
- Helps students learn complex concepts faster.

---

### 📝 Smart Quiz Generator
- Generate AI-powered quizzes on any topic.
- Choose difficulty level:
  - Easy
  - Medium
  - Hard
- Select number of questions.
- Answer questions interactively.
- Get:
  - Correct answers
  - Explanations
  - Final score
  - Performance feedback

---

### 🚀 Career Roadmap Generator
- Enter your dream career.
- Select your current education or experience level.
- Receive a personalized step-by-step roadmap.

---

### 📊 Skill Gap Analyzer
- Compare your current skills with your desired career.
- Discover missing skills.
- Receive a personalized learning plan.

---

### 🎤 AI Mock Interview
- Generate realistic interview questions.
- Choose your experience level.
- Improve confidence and interview preparation.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Streamlit | Interactive web application |
| AI API | Intelligent response generation |
| OpenRouter API | AI model access |
| Python Dotenv | Secure API key management |
| Requests | API communication |

---

## 📂 Project Structure

```
FUTUREMIND_AI/
│
├── app.py                    # Main Streamlit application
│
├── modules/
│   ├── quiz.py               # Quiz generation module
│   ├── career.py             # Career roadmap module
│   ├── skill_gap.py          # Skill analysis module
│   └── interview.py          # Mock interview module
│
├── utils/
│   └── gemini_api.py         # AI API integration
│
├── .env                      # API keys (not uploaded)
├── .gitignore                # Git ignored files
├── requirements.txt          # Project dependencies
│
└── README.md                 # Project documentation
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/FUTUREMIND_AI.git
```

### 2. Enter the Project Folder

```bash
cd FUTUREMIND_AI
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows**

```powershell
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Create `.env` File

Create a `.env` file in the root folder:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🔒 Security

API keys are stored in a `.env` file and are excluded from GitHub using `.gitignore`.

Never upload your private API keys to public repositories.

---

## 🎨 User Interface

FUTUREMIND AI provides:
- Modern dashboard design
- Dark mode support
- Interactive sidebar navigation
- Professional loading animations
- User-friendly feedback messages

---

## 🚀 Future Improvements

Planned upgrades for FUTUREMIND AI:

- 💬 Chat-style AI Study Tutor
- 📄 PDF export for reports and quizzes
- 📈 Student progress dashboard
- 👤 User authentication system
- ☁️ Cloud database integration
- 🌐 Public web deployment

---

## 📸 Screenshots

Screenshots of the application will be added here.

Example:

```
assets/
├── home_page.png
├── quiz_module.png
└── career_roadmap.png
```

---

## 👩‍💻 Author

**Sristi Shaw**

AI Developer | Student | Technology Enthusiast

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

### 🧠 FUTUREMIND AI

**Learn Smarter • Plan Better • Grow Faster**