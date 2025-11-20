# Study Buddy Services - Simple & Clean

This project demonstrates a **simple, minimal** service architecture with reusable utility functions.

## 🏗️ Project Structure

```
app/
├── services/
│   ├── service 1/          # General AI assistant 
│   │   ├── service1.py     # Main service logic
│   │   ├── service1_schema.py  # Request/response models
│   │   └── service1_route.py   # API endpoints
│   └── service 2/          # Simple fitness helper
│       ├── service2.py     # Main service logic  
│       ├── service2_schema.py  # Request/response models
│       └── service2_route.py   # API endpoints
└── utils/                  # Simple utility functions
    ├── __init__.py         # Package setup
    ├── common_utils.py     # All utility functions
    └── config_utils.py     # Configuration helpers
```

## 🚀 Services Overview

### Service 1 - General AI Assistant
- **Endpoint**: `POST /service1`  
- **What it does**: Answers any question you ask
- **Input**: `{\"example_field\": \"Your question here\"}`
- **Output**: Helpful AI response

### Service 2 - Simple Fitness Helper  
- **Endpoint**: `POST /service2`
- **What it does**: Gives fitness advice and workout suggestions
- **Input**: `{\"question\": \"I need a beginner workout\"}`
- **Output**: Friendly fitness guidance

## 🛠️ Simple Utility Functions

All utilities are **simple functions** - no classes needed!

### 1. Response Formatting
```python
# Success response
response = format_success_response(data, \"All good!\")

# Error response  
error = format_error_response(\"Something went wrong\", \"More details\")
```

### 2. Input Safety
```python
# Clean user input (removes bad stuff, limits length)
clean_text = sanitize_input(user_input)

# Check if prompt is too long
is_ok = validate_prompt_length(prompt, max_length=2000)
```

### 3. Logging Setup
```python
# Get a logger for your service
logger = setup_logger(\"MyService\")
logger.info(\"Everything is working!\")
logger.error(\"Oops, something broke\")
```

### 4. OpenAI Safety
```python
# Make sure OpenAI parameters are safe
safe_config = validate_openai_params(\"gpt-3.5-turbo\", 0.7, 1000)
# Returns: {\"model\": \"gpt-3.5-turbo\", \"temperature\": 0.7, \"max_tokens\": 1000}
```

## ✨ Why This is Great

### Super Simple
- **No complex classes** - just simple functions you import and use
- **Easy to understand** - each function does one thing well
- **Minimal code** - no unnecessary complexity

### Safe & Reliable  
- **Input sanitization** - prevents bad input from breaking things
- **Parameter validation** - ensures API calls are safe
- **Consistent logging** - see what's happening in your services
- **Error handling** - graceful failure when things go wrong

### Easy to Use
```python
# Just import what you need
from ...utils.common_utils import sanitize_input, setup_logger

# Use it right away
logger = setup_logger(\"MyService\")
clean_input = sanitize_input(user_question)
```

## 📖 Real Usage Example

Both services work the same way:

```python
# Set up logging (same for both services)
logger = setup_logger(\"Service1\")

# Clean user input (same function)  
clean_input = sanitize_input(user_text)

# Safe OpenAI call (same validation)
config = validate_openai_params(\"gpt-3.5-turbo\", 0.7, 1000)
```

## 🎯 Key Benefits

1. **Simple**: No classes, just functions
2. **Safe**: Input validation and sanitization built-in
3. **Consistent**: Same patterns everywhere
4. **Reusable**: Write once, use everywhere
5. **Minimal**: Only what you need, nothing extra

## 🔧 How to Add a New Service

1. Copy the structure from service 1 or 2
2. Import the utility functions you need
3. Write your service logic
4. Done! 

The utilities handle all the boring stuff (logging, validation, etc.) so you can focus on your service's unique functionality.

---

**This is a clean, simple architecture that's easy to understand, extend, and maintain!** 🎉