# ⚽ FootAi

**FootAi** is an AI-powered chat application specialized in football. Ask anything — about the World Cup, players, transfers, tactics… — and FootAi answers instantly using **Google Gemini**.

![stack](https://img.shields.io/badge/Stack-Vue%203%20%7C%20TypeScript%20%7C%20Tailwind%20%7C%20FastAPI%20%7C%20Python%20%7C%20Gemini-emerald)

---

## ✨ Features

- 💬 Modern chat interface ("night stadium" theme, glassmorphism)
- 🧠 Real-time AI answers via the Google Gemini API
- ⚡ Quick suggestions to kick off the conversation
- 🟢 "Bot is typing" indicator
- 🛡️ API key kept in `.env` (never committed)
- 🔄 CORS configured for local development

## 🏗️ Architecture

```
FootAi/
├── backend/                  # FastAPI API
│   ├── app/
│   │   ├── main.py           # FastAPI app + CORS + routing
│   │   ├── api/v1/chat.py    # POST /v1/chat endpoint
│   │   ├── services/
│   │   │   └── ai_service.py # Google Gemini call
│   │   ├── models/
│   │   │   └── ChatRequest.py# Request schema (Pydantic)
│   │   └── core/config.py    # Environment variable loading
│   └── requirement.txt
└── frontend/                 # Vue 3 + Vite SPA
    └── src/
        ├── main.ts           # Entry point
        ├── router/           # Vue Router
        ├── service/api.ts    # Axios client
        └── views/HomeView.vue# Chat interface
```

## 🛠️ Tech Stack

| Layer    | Technology                             |
| -------- | -------------------------------------- |
| Frontend | Vue 3, Vite, TypeScript, Tailwind CSS v4 |
| Backend  | FastAPI, Uvicorn, Pydantic             |
| AI       | Google Gemini (`gemini-3.5-flash`)     |
| HTTP     | Axios (front) / REST (back)            |

## 📋 Prerequisites

- **Node.js** `^22.18.0 || >=24.12.0`
- **Python** `>= 3.10`
- A **Google Gemini API key** ([AI Studio](https://aistudio.google.com/apikey))

## 🚀 Installation

### 1. Clone and set up the backend

```bash
cd backend

# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirement.txt

# Configure environment variables
cp .env.example .env            # then replace the key with yours
```

### 2. Install the frontend

```bash
cd frontend
npm install
```

## ▶️ Running the app

### Backend (port `8000`)

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

Interactive docs: http://127.0.0.1:8000/docs

### Frontend (port `5173`)

```bash
cd frontend
npm run dev
```

Open **http://localhost:5173** ⚽

## 🔐 Environment Variables

Copy `backend/.env.example` to `backend/.env`:

```env
GEMINI_API_KEY='your_gemini_api_key'
```

| Variable        | Description                  |
| --------------- | ---------------------------- |
| `GEMINI_API_KEY`| Google Gemini API key (required) |

> ⚠️ The `.env` file is git-ignored — never commit your keys.

## 🔌 API

### `POST /v1/chat`

Sends a message to the AI and returns its answer.

**Request:**

```json
{
  "message": "Who won the last World Cup?"
}
```

**Response:**

```json
{
  "message": "The last World Cup was won by Argentina in 2022..."
}
```

## 📝 Frontend scripts

| Command                | Description                          |
| ---------------------- | ------------------------------------ |
| `npm run dev`          | Development server                   |
| `npm run build`        | Type-check + production build        |
| `npm run type-check`   | TypeScript check (`vue-tsc`)         |
| `npm run preview`      | Preview the production build         |

---

<p align="center">Built with ⚽ and ☕</p>
