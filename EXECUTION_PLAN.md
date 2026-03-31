# Acme AI Labs - Orchestration API Control

## Overview
Complete implementation of an API server with start/stop control functionality for the Acme AI Labs orchestration system MVP.

## Files Created

### Backend Components
1. **api_server.py** - Flask-based REST API server
   - Health check endpoint: `GET /health`
   - Status endpoint: `GET /api/status`
   - Stop endpoint: `POST /api/stop`

2. **api_manager.py** - Python API manager for server control
   - Start/stop API server programmatically
   - Check server status
   - CLI interface for manual control

### Frontend Component
3. **index.html** - Web UI control panel
   - Visual status indicator (running/stopped)
   - Start/Stop buttons
   - Auto-refresh status every 5 seconds
   - Modern, responsive design

### Dependencies
4. **requirements.txt** - Python dependencies
   - Flask 3.0.0
   - Requests 2.31.0

## Usage

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Option 1: Using API Manager (Recommended)
```bash
python api_manager.py
```
Then use commands:
- `start` - Start the API server
- `stop` - Stop the API server
- `status` - Check server status
- `quit` - Exit manager

### Option 2: Direct Server Start
```bash
python api_server.py
```

### Access Web UI
1. Start the API server using either method above
2. Open `index.html` in a web browser
3. Use the buttons to control the API server

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check - returns server status |
| GET | `/api/status` | Detailed system status and version |
| POST | `/api/stop` | Signal server shutdown |

## Features Implemented

✅ **Backend API Server**
- RESTful API with Flask
- Health monitoring
- Graceful shutdown support
- Configurable port (default: 5000)

✅ **API Manager**
- Programmatic start/stop control
- Process management
- Status checking
- Interactive CLI

✅ **Frontend UI**
- Real-time status indicator
- Start/Stop controls
- Auto-refresh functionality
- Professional, modern design
- Responsive layout

## Architecture

```
┌─────────────┐
│  index.html │  (Browser UI)
│  (Frontend) │
└──────┬──────┘
       │ HTTP Requests
       ▼
┌─────────────┐
│ api_server  │  (Flask Server)
│   :5000     │
└──────┬──────┘
       │ Managed by
       ▼
┌─────────────┐
│ api_manager │  (Process Control)
│   (Python)  │
└─────────────┘
```

## Testing

### Manual Test
1. Start API: `python api_manager.py` → `start`
2. Check status: Open browser to check connectivity
3. View UI: Open `index.html` - should show "API Running"
4. Stop API: Click "Stop API" button in UI
5. Verify: Status should change to "API Stopped"

### Health Check
```bash
curl http://localhost:5000/health
# Expected: {"status":"running","message":"API server is healthy"}
```

### Status Check
```bash
curl http://localhost:5000/api/status
# Expected: {"status":"active","service":"Acme AI Labs Orchestration","version":"0.1.0"}
```

## Production Considerations

For production deployment:
1. Remove `debug=True` from api_server.py
2. Use a production WSGI server (gunicorn, uwsgi)
3. Add authentication/authorization
4. Implement proper logging
5. Add error handling and monitoring
6. Use environment variables for configuration
7. Containerize with Docker

## Validation Checklist

- [x] API server starts successfully
- [x] Health endpoint responds correctly
- [x] Status endpoint returns system info
- [x] Stop endpoint triggers shutdown
- [x] API manager can start server
- [x] API manager can stop server
- [x] API manager reports status correctly
- [x] Web UI displays current status
- [x] Web UI can trigger stop command
- [x] Auto-refresh updates status
- [x] Dependencies documented
- [x] Usage instructions provided
