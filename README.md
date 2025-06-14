# Onion Architecture Sample Project

This project demonstrates the implementation of Onion Architecture (Clean Architecture) using FastAPI in Python.

## Project Structure

```
onion1/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── user_router.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── interfaces.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── infrastructure/
│       ├── __init__.py
│       └── user_repository.py
├── tests/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_user_router.py
│   └── services/
│       ├── __init__.py
│       └── test_user_service.py
└── README.md
```

## Architecture Overview

The project follows the Onion Architecture pattern with the following layers:

1. **Domain Layer** (`app/domain/`)
   - Contains business models and repository interfaces
   - Independent of other layers
   - No external dependencies

2. **Service Layer** (`app/services/`)
   - Implements business logic
   - Depends on domain layer
   - Uses repository interfaces

3. **API Layer** (`app/api/`)
   - Handles HTTP requests and responses
   - Uses FastAPI for routing
   - Depends on service layer

4. **Infrastructure Layer** (`app/infrastructure/`)
   - Implements repository interfaces
   - Contains database and external service integrations
   - Depends on domain layer

## Testing

Tests are organized in a structure that mirrors the application:

- `tests/api/`: Tests for API endpoints
- `tests/services/`: Tests for service layer logic

To run tests:
```bash
# Run all tests
python -m pytest

# Run specific test directory
python -m pytest tests/api/
python -m pytest tests/services/

# Run specific test file
python -m pytest tests/api/test_user_router.py
python -m pytest tests/services/test_user_service.py
```

## Dependencies

- FastAPI: Web framework
- Pydantic: Data validation
- Pytest: Testing framework
- HTTPx: HTTP client for testing 