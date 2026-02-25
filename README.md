# 🤖𝑨𝑰-𝑪𝒉𝒂𝒕𝒃𝒐𝒕𝒔 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕𝒔  – 𝑨𝑰-𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝑴𝒖𝒍𝒕𝒊-𝑭𝒆𝒂𝒕𝒖𝒓𝒆 𝑵𝑳𝑷 𝑨𝒑𝒑𝒍𝒊𝒄𝒂𝒕𝒊𝒐𝒏


<p align="center">
  <img src="https://drive.google.com/file/d/1aSmksFLnllIOVuW1aD1LTW1boiS5AYj-/view?usp=sharing" 
       alt=" 𝑨𝑰-𝑪𝒉𝒂𝒕𝒃𝒐𝒕𝒔 Banner Image" width="98%" height="97%">
</p>


An end-to-end **LLM-powered NLP web application** built using **Streamlit + Google Gemini API**, providing multiple Natural Language Processing services in one unified platform.

## 𝐓𝐡𝐢𝐬 𝐩𝐫𝐨𝐣𝐞𝐜𝐭 𝐝𝐞𝐦𝐨𝐧𝐬𝐭𝐫𝐚𝐭𝐞𝐬 𝐩𝐫𝐚𝐜𝐭𝐢𝐜𝐚𝐥 𝐢𝐦𝐩𝐥𝐞𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧 𝐨𝐟:

- Large Language Model (LLM) integration
- Secure API handling
- Multi-feature NLP pipeline design
- Session-based authentication
- Interactive web UI deployment

---

## ✨ 𝑲𝒆𝒚 𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔

### 🧠 Core NLP Services

- Sentiment Analysis
- Language Translation
- Language Detection
- Text Summarization
- PDF Upload & Document Summarization

### 📚 AI Study Assistant

- Concept Explanation
- Topic Summarization
- Practice Question Generation
- 7-Day Study Plan Generator

---

## 🏗️ 𝙎𝙮𝙨𝙩𝙚𝙢 𝘼𝙧𝙘𝙝𝙞𝙩𝙚𝙘𝙩𝙪𝙧𝙚

The application follows a modular and production-style structure:

- `NLPModel` class for centralized model configuration
- Secure API key management using `.env`
- Streamlit session-based authentication
- Feature-based LLM prompting strategy
- Controlled token input for large document handling
- Structured UI with sidebar-based navigation

---

## 🛠️ 𝙏𝙚𝙘𝙝 𝙎𝙩𝙖𝙘𝙠

| Layer                              | Technology                           |
| ---------------------------------- | ------------------------------------ |
| **Programming Language**     | Python 3.11+                         |
| **Frontend/UI Layer**        | Streamlit                            |
| **LLM Engine**               | Google Gemini (`gemini-2.5-flash`) |
| **LLM SDK**                  | `google-generativeai`              |
| **Document Parsing**         | PyPDF2                               |
| **Configuration Management** | python-dotenv                        |
| **State Management**         | Streamlit Session State              |
| **Architecture Pattern**     | Modular Class-Based Design           |
| **Security Practice**        | Environment-based API Key Handling   |

## **Concepts Applied**

- OOP Concepts
- LLM Integration
- NLP Task Automation
- File Handling & Text Extraction
- Session State Management
- Secure Environment Configuration

---

## 🔐 Authentication System

The application includes:

- User Registration
- Login System
- Session Persistence
- Logout functionality

> ⚠️ Note: This is a session-based demo authentication system (not production database-backed).

---

## 📂 Project Structure


𝑨𝑰-𝑪𝒉𝒂𝒕𝒃𝒐𝒕𝒔 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕𝒔/

│

├── app.py

├── .env

├── requirements.txt

└── README.md


## 🚀 𝙃𝙤𝙬 𝙩𝙤 𝙍𝙪𝙣 𝙩𝙝𝙚 𝘼𝙥𝙥𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣

### 1️⃣ Clone the Repository

```
git clone https://github.com/KzRaihan/AI-Chatbots-and-Virtual-Assistants.git
cd 𝑨𝑰-𝑪𝒉𝒂𝒕𝒃𝒐𝒕𝒔 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕𝒔
```

### 2️⃣ Create a Virtual Environment

```
conda create -n AiChartbot python=3.11 -y
```

### 3️⃣ Activate the Environment

```
conda activate AiChartbot
```

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory and Set Gemini API Key (Windows)

```

setx GEMINI_API_KEY "your_api_key_here"
```

⚠️ API keys are **never hardcoded** for security reasons.

### 5️⃣ Run the Application

```
streamlit run app.py
```

---

## 📈 𝙋𝙧𝙤𝙙𝙪𝙘𝙩𝙞𝙤𝙣 𝘾𝙤𝙣𝙨𝙞𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣𝙨 𝙄𝙢𝙥𝙡𝙚𝙢𝙚𝙣𝙩𝙚𝙙

- ✔ Modular model class design
- ✔ Environment-based API key configuration
- ✔ Controlled PDF text input size (`[:8000]`)
- ✔ Error handling using `try-except`
- ✔ Streamlit session state management
- ✔ User-friendly UI with structured sections

---

## 🧠 𝙇𝙚𝙖𝙧𝙣𝙞𝙣𝙜 & 𝙀𝙣𝙜𝙞𝙣𝙚𝙚𝙧𝙞𝙣𝙜 𝙁𝙤𝙘𝙪𝙨

This project demonstrates:

- Designing multi-service NLP systems
- Integrating real-world LLM APIs
- Handling document-based AI workflows
- Applying prompt engineering principles
- Building interactive AI dashboards

---

## 🚀 𝙁𝙪𝙩𝙪𝙧𝙚 𝙄𝙢𝙥𝙧𝙤𝙫𝙚𝙢𝙚𝙣𝙩𝙨

- Database-backed authentication (PostgreSQL / Firebase)
- Role-based access control
- Deployment on Streamlit Cloud / Render
- Conversation history memory
- Token usage monitoring
- Response streaming

---

## 📊 𝙄𝙙𝙚𝙖𝙡 𝙐𝙨𝙚 𝘾𝙖𝙨𝙚𝙨

- AI Study Companion
- Educational NLP Tool
- LLM Experimentation Platform
- Academic Research Assistant

## 👨‍💻 𝘼𝙪𝙩𝙝𝙤𝙧

**Md Kamruzzaman Raihan**
Data Scientist | Machine Learning Engineer | Generative AI Enthusiast

📫 Contact: kamruzzamanraihan00@gmail.com

---

## ⭐ 𝙒𝙝𝙮 𝙏𝙝𝙞𝙨 𝙋𝙧𝙤𝙟𝙚𝙘𝙩 𝙈𝙖𝙩𝙩𝙚𝙧𝙨

This project reflects the ability to:

- Build production-style AI systems
- Integrate LLMs into real applications
- Design scalable NLP workflows
- Combine UI + AI + secure configuration
- Deliver real-world usable AI tools

---

# 🏁𝙁𝙞𝙣𝙖𝙡 𝙉𝙤𝙩𝙚

This is not just an NLP demo —
it is a **multi-functional AI platform built with scalable architecture principles.**

If you found this useful, feel free to ⭐ the repository.
