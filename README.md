# emdash-test-repo
Test repo for SpecFlow + Emdash execution validation

## Hello API Service

Minimal FastAPI service with /hello endpoint.

### Installation
```bash
pip install -r requirements.txt
```

### Run Server
```bash
uvicorn hello:app --reload
```

Server runs on http://127.0.0.1:8000

### Test Endpoint
```bash
# Run tests
pytest test_hello.py -v

# Or test manually
curl http://127.0.0.1:8000/hello
```

Expected response: `{"message":"hello"}`
