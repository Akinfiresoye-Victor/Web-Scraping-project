# Web Scraping Project

Scrapes book information (title, price, stock, etc.) from [Books to Scrape](https://books.toscrape.com/) by category with pagination support.

---

## 📋 What It Does

- Fetches all categories from the site  
- For each category, scrapes multiple pages (pagination) to collect book details  
- Extracts data such as title, price, availability, and possibly rating  
- Saves results in a structured format 

---

## 🧰 Requirements

- Python 3.x  
- Libraries (as listed in `requirements.txt`), e.g. `requests`, `beautifulsoup4`, etc.

---

## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/Akinfiresoye-Victor/Web-Scraping-project.git
   cd Web-Scraping-project
2. Set environment
   * python -m venv env
   * pip install -r requirements.txt
3. Run
    python book_scrape.py
