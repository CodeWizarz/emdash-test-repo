# Quick Start Guide

## Setup (One-time)
```bash
pip install -r requirements.txt
```

## Running the System

### Method 1: API Manager (Recommended)
```bash
python3 api_manager.py
```
Commands available:
- `start` - Start API server
- `stop` - Stop API server  
- `status` - Check status
- `quit` - Exit

### Method 2: Direct Server
```bash
python3 api_server.py
```

## Using the Web UI

1. Start the API server (using either method)
2. Open `index.html` in your browser
3. Click buttons to control the API

## Quick Test
```bash
# Terminal 1: Start server
python3 api_manager.py
> start

# Terminal 2: Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/api/status

# Web UI: Open index.html in browser
# Should show green "API Running" indicator
```

## Running Tests
```bash
python3 test_api.py
```

## What Was Built

✅ **Flask REST API** - Health, status, and stop endpoints  
✅ **API Manager** - Process control with CLI  
✅ **Web UI** - Modern control panel with real-time status  
✅ **Unit Tests** - Automated validation  
✅ **Documentation** - Complete setup and usage guide

**Ready for MVP orchestration validation!**
