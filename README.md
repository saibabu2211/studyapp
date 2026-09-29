# 📚 Study Assistant

An AI-powered **Study Assistant** built with **Python, Streamlit, and Google Gemini API**. It helps students understand concepts, prepare for exams, practice interview questions, and learn technical topics through an interactive chat interface.

## ✨ Features

* 🤖 AI-powered answers using Google Gemini
* 💬 Interactive chat interface with Streamlit
* 🧠 Multiple learning personalities

  * Friendly
  * Teacher
  * Interview
  * Exam
* 📖 Simple explanations for difficult concepts
* 💡 Real-world examples
* 💻 Technical and coding explanations
* 🎯 Interview preparation
* 📝 Exam preparation
* 🗑️ Clear chat functionality
* 🔐 API key stored securely using `.env`

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini API**
* **Google GenAI SDK**
* **python-dotenv**

## 📁 Project Structure

```text
Study-Assistant/
│
├── app.py
├── prompts.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project

```bash
cd Study-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Gemini API key.

### ⚠️ Security

Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

## 💬 Example Questions

You can ask questions such as:

```text
Explain Python decorators with an example.

What is a DataFrame in PySpark?

Explain SQL joins.

What is machine learning?

Explain transformers in simple terms.

Give me interview questions for a Data Engineer.

Explain TCP vs UDP.
```

## 🧠 Assistant Modes

### Friendly

Provides simple explanations with examples.

### Teacher

Explains concepts step-by-step, starting from fundamentals.

### Interview

Focuses on technical interview preparation and commonly asked questions.

### Exam

Focuses on important concepts, definitions, formulas, and practice questions.

## 🔮 Future Improvements

* 📚 PDF/document question answering
* 📝 Automatic quiz generation
* 📊 Learning progress tracking
* 🧠 Personalized study plans
* 🔊 Voice-based interaction
* 📄 Notes generation
* 🔎 RAG-based document search
* 👤 User authentication
* ☁️ Cloud deployment

## 👨‍💻 Author

**Sai Babu**

Built as an AI-powered learning assistant using Python, Streamlit, and Google Gemini.

## 📄 License

This project is for educational and learning purposes.
