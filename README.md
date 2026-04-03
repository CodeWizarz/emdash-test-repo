# Acme AI - The #1 AI Note-Taking App

🚀 **Goal**: Build to $1M MRR

## Overview
Acme AI is an intelligent note-taking application that leverages AI to help users capture, organize, and extract insights from their notes effortlessly.

## Key Features
- 📝 **Rich Text Editor**: Markdown and WYSIWYG support with code highlighting
- 🤖 **AI-Powered**: Auto-summarization, smart tagging, and intelligent search
- 🔍 **Semantic Search**: Find notes by meaning, not just keywords
- 🏷️ **Smart Organization**: AI-generated tags and categories
- 💡 **Insights**: Get actionable insights from your notes
- 🔐 **Secure**: JWT authentication with OAuth support
- ⚡ **Fast**: Real-time sync and instant search

## Tech Stack
- **Frontend**: Next.js 14, React 18, TailwindCSS, TypeScript
- **Backend**: Python FastAPI, SQLAlchemy, PostgreSQL
- **AI**: OpenAI GPT-4, Vector embeddings
- **Deployment**: Docker, Vercel, Railway

## Quick Start
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Project Structure
```
acme-ai/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── api/      # API routes
│   │   ├── models/   # Database models
│   │   ├── services/ # Business logic
│   │   └── core/     # Config, auth, AI
│   └── requirements.txt
├── frontend/         # Next.js frontend
│   ├── src/
│   │   ├── app/      # App routes
│   │   ├── components/ # React components
│   │   └── lib/      # Utils, API client
│   └── package.json
└── docker-compose.yml
```

## Development Roadmap
- [x] Project setup
- [ ] Backend API with CRUD operations
- [ ] AI integration (summarization, tagging)
- [ ] Frontend UI and note editor
- [ ] Search and indexing
- [ ] Authentication system
- [ ] Deployment and scaling
