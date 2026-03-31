# Execution Blueprint: API Control Button

## Task Overview
**Task**: Create a button to call the API and stop the API  
**Business Context**: MVP Orchestration Validation - Validate planner-builder-qa-improver flow  
**Company**: Acme AI Labs

## Current State Analysis
- Repository is a minimal test repo with only `hello.py` containing a basic function
- No existing web framework, API server, or UI components
- Clean working directory on branch `emdash/planner-create-a-bbutton-6fg`

## Architecture Decision

### Option A: Full-Stack Implementation (Recommended)
Build a complete minimal web application with:
- Flask/FastAPI backend with start/stop control endpoints
- Simple HTML/JS frontend with button interface
- API lifecycle management

### Option B: Minimal Script
Simple Python script with button simulation (CLI-based)

**Decision: Option A** - Aligns with "app UI" requirement in business context

## Implementation Blueprint

### Phase 1: Backend API Setup
**File**: `api_server.py`
- [ ] Flask web server with endpoints:
  - `GET /` - Serve UI
  - `POST /api/start` - Start API service
  - `POST /api/stop` - Stop API service (graceful shutdown)
  - `GET /api/status` - Check API status
- [ ] Server lifecycle management with threading/multiprocessing
- [ ] CORS support for local development
- [ ] Error handling and logging

**File**: `requirements.txt`
- [ ] Flask==3.0.0
- [ ] flask-cors==4.0.0

### Phase 2: Frontend UI
**File**: `static/index.html`
- [ ] Clean, responsive button interface
- [ ] Two buttons:
  - "Start API" (green) - triggers POST /api/start
  - "Stop API" (red) - triggers POST /api/stop
- [ ] Status indicator showing API state
- [ ] Error handling with user feedback
- [ ] Fetch API for async requests

**File**: `static/styles.css`
- [ ] Modern button styling
- [ ] Status indicators (colors, animations)
- [ ] Responsive layout

**File**: `static/script.js`
- [ ] Button event handlers
- [ ] API call functions with error handling
- [ ] Status polling mechanism
- [ ] UI state management

### Phase 3: API Lifecycle Manager
**File**: `api_manager.py`
- [ ] APIManager class for lifecycle control
- [ ] Start/stop methods with state tracking
- [ ] Thread-safe state management
- [ ] Process cleanup on shutdown

### Phase 4: Integration & Testing
**File**: `test_api_button.py`
- [ ] Unit tests for API endpoints
- [ ] Integration tests for start/stop flow
- [ ] UI interaction simulation

**File**: `README.md` (update)
- [ ] Add setup instructions
- [ ] Document API endpoints
- [ ] Usage guide for button interface

## Technical Specifications

### API Endpoints
```
POST /api/start
Response: {"status": "started", "message": "API service started"}

POST /api/stop
Response: {"status": "stopped", "message": "API service stopped"}

GET /api/status
Response: {"status": "running|stopped", "uptime": <seconds>}
```

### Button States
- **Idle**: Both buttons enabled, status shows "Stopped"
- **Running**: Start disabled, Stop enabled, status shows "Running"
- **Transitioning**: Both buttons disabled, status shows "Starting..." or "Stopping..."
- **Error**: Show error message, retry options

### Error Handling
- Network errors → user-friendly message
- API errors → specific error display
- Timeout handling → automatic retry option

## File Structure
```
.
├── api_server.py           # Main Flask app with routes
├── api_manager.py          # API lifecycle management
├── requirements.txt        # Python dependencies
├── static/
│   ├── index.html         # UI interface
│   ├── styles.css         # Styling
│   └── script.js          # Frontend logic
├── test_api_button.py     # Test suite
├── hello.py               # Existing (unchanged)
└── README.md              # Updated documentation
```

## Execution Steps

### Step 1: Backend Core (Builder Focus)
1. Create `api_manager.py` - State management class
2. Create `api_server.py` - Flask app with endpoints
3. Create `requirements.txt` - Dependencies

### Step 2: Frontend UI (Builder Focus)
1. Create `static/` directory
2. Create `index.html` - Button interface
3. Create `styles.css` - Visual styling
4. Create `script.js` - API interaction logic

### Step 3: Testing & Validation (QA Focus)
1. Create `test_api_button.py` - Test suite
2. Manual testing checklist:
   - [ ] Server starts successfully
   - [ ] UI loads correctly
   - [ ] Start button triggers API start
   - [ ] Stop button triggers API stop
   - [ ] Status updates correctly
   - [ ] Error states display properly
   - [ ] Can restart after stopping

### Step 4: Documentation (Improver Focus)
1. Update `README.md` with:
   - Setup instructions
   - API documentation
   - Usage guide
   - Architecture overview

## Success Criteria
- ✅ Button UI loads in browser at `http://localhost:5000`
- ✅ Start button successfully starts the API service
- ✅ Stop button successfully stops the API service
- ✅ Status indicator updates in real-time
- ✅ Error handling works for edge cases
- ✅ Tests pass for all endpoints
- ✅ Documentation is complete and clear

## Dependencies & Prerequisites
- Python 3.7+
- pip for package installation
- Modern web browser
- Network access to localhost

## Risk Mitigation
- **Risk**: Process management complexity
  - **Mitigation**: Use simple threading model, fallback to singleton pattern
- **Risk**: Port conflicts
  - **Mitigation**: Configurable port, check availability before start
- **Risk**: Browser CORS issues
  - **Mitigation**: Use flask-cors, serve from same origin

## Rollback Plan
- All changes are additive (no modifications to `hello.py`)
- Can safely delete new files to rollback
- No database or persistent state to manage

---

## Next Phase: Builder Implementation
**Builder Agent** should implement this blueprint following the file structure and specifications above.
