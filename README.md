# Python Web Scraper with BeautifulSoup & Pandas

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12%2B-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-darkblue.svg)](https://pandas.pydata.org/)

A robust web scraping pipeline that extracts online news metrics (titles, canonical links, publication dates, and view counts) and converts unstructured HTML into structured **Pandas DataFrames**.

---

## 🚀 Key Features

* **DOM Parsing**: Uses `BeautifulSoup` with `lxml` parser for efficient HTML traversal.
* **Safe Attribute Extraction**: Prevents `AttributeError` exceptions when handling missing HTML tags.
* **User-Agent Spoofing**: Custom HTTP headers to ensure request reliability and bypass basic anti-scraping filters.
* **Pandas Data Structuring**: Converts extracted dictionaries into tabular `DataFrame` structures for export (CSV/Excel).

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Scraping Framework**: BeautifulSoup4, Requests
* **Parser Engine**: lxml
* **Data Processing**: Pandas

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/python-news-scraper-pandas.git
cd python-news-scraper-pandas

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the scraper
python main.py

---

**Author**: QA Automation Engineer & Python Developer
