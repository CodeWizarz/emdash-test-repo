# emdash-test-repo
Test repo for SpecFlow + Emdash execution validation

## Hello Service

Minimal FastAPI service with a hello endpoint.

### Setup

```bash
pip install -r requirements.txt
```

### Run

```bash
uvicorn hello:app --reload
```

### Test

```bash
pytest test_hello.py -v
```

### Endpoint

- `GET /hello` - Returns `{"message": "hello"}`
