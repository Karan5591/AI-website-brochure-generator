## AI Website Brochure Generator

### Overview

AI Website Brochure Generator is an AI-powered Python application that automatically creates a professional company brochure by analyzing content from a company’s website.

#### The application:

- Scrapes relevant pages from a company website
- Uses an LLM to identify important sections (About, Careers, etc.)
- Generates a concise, marketing-ready brochure in Markdown
- Supports streaming output via a Gradio web interface

### Why This Project Was Refactored

- This project was initially developed as a Jupyter Notebook for rapid experimentation and prompt iteration.
- To make it production-ready and suitable for job applications, it was refactored into a modular Python project with:
- Clear separation of concerns
- Reusable modules
- A clean execution entry point
- UI isolated from business logic
- This refactor demonstrates real-world software engineering practices, not just experimentation.

### Architecture & Design

The project follows a layered architecture to avoid tight coupling and circular dependencies.

UI (Gradio)
   ↓
Brochure Generator (Business Logic)
   ↓
LLM Service (OpenAI API)
   ↓
Config / Prompts

*Design Principles Used*

- Single Responsibility Principle
- One-directional dependencies
- Separation of UI, logic, and infrastructure
- Streaming-safe LLM integration


### Tech Stack

- Python 3.10+
- OpenAI API
- Gradio (Web UI)
- BeautifulSoup / Requests (Web scraping)
- dotenv (Environment management)


### Features

- Automatic website link discovery
- Relevant page selection using LLM reasoning
- AI-generated company brochure in Markdown
- Streaming responses for better UX
- Clean, modular, production-ready architecture

### Sample Use Case

**Input:**

Company Name: Hugging Face
Website: https://huggingface.co


**Output:**

- Company overview
- Products & customers
- Culture and careers
- Investor-friendly summary

### Key Learnings

- Refactoring notebooks into production-ready Python projects
- Avoiding circular imports through layered architecture
- Handling streaming responses safely
- Separating prompt engineering from business logic

### Future Improvements

- Multi-language brochure generation
- FastAPI backend support
- Dockerization
- Unit tests for LLM and scraping layers

