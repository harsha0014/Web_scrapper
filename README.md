# 🕷️ AI Web Scraper with Streamlit & Ollama

This is a Streamlit-based web application that allows users to scrape content from any website and interactively query the page data using an AI language model powered by Ollama.

## 🚀 Features

- 🧠 **AI Parsing**: Describe what you want, and let the model extract it for you.
- 🔍 **Web Scraping**: Retrieve HTML content from any publicly accessible URL.
- 🧼 **Content Cleaning**: Automatically removes scripts, styles, and unnecessary whitespace.
- 📄 **DOM Viewer**: Expandable viewer to inspect the scraped page content.
- ✂️ **Chunking**: Breaks down large page data into manageable pieces for better parsing.

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – UI Framework
- [Selenium (optional)](https://selenium.dev/) – (Not fully used, placeholder for advanced scraping)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing
- [Ollama](https://ollama.com/) – Local LLM inference
- [LangChain](https://www.langchain.com/) – Prompt templating and model chaining
- [Python 3.8+](https://www.python.org/) – Backend logic



## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
