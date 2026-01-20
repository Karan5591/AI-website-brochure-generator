### AI Website Brochure Generator

- An AI-powered application that automatically generates a company brochure by analyzing a company’s website.
- The tool scrapes relevant web pages, filters useful links using LLM reasoning, and synthesizes a concise, well-structured Markdown brochure.
- A Gradio web interface is provided for easy interaction.

#### Features

- Scrapes company websites to extract content
- Uses LLMs to identify relevant pages (About, Products, Careers, etc.)
- Generates a clean Markdown brochure
- Streams LLM responses in real time
- Interactive Gradio UI (enter company name & URL)
- Environment-safe API key handling using .env

#### Tech Stack

- Python
- OpenAI GPT models
- Web scraping (requests, BeautifulSoup)
- Prompt engineering
- Streaming responses
- Gradio (UI)
- Jupyter Notebook (experimentation)

#### Project Structure
AI-Website-Brochure-Generator/
│
├── scraper.py                 # Core scraping & brochure logic
├── Company_Broucher.ipynb     # Development & experimentation
├── README.md                  # Project documentation
├── .gitignore
├── .env                       # API keys (not committed)
└── .venv/                     # Virtual environment (not committed)

#### Gradio Interface
- The Gradio UI allows users to:
- Enter a Company Name
- Enter a Company Website URL
- Generate a brochure directly in the browser

#### Example input:
- Company Name: huggingFace
- Company URL: https://huggingface.com

#### Current Status

- Website scraping
- LLM-based link selection
- Brochure generation
- Gradio UI integration