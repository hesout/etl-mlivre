# ETL-mlivre

## Setup
### Python version (pyenv)
```bash
# Python 3.12.5
pyenv local 3.12.5
```

### Virtual environment (venv)
```bash
# Creating environment
python3 -m venv .venv

# Activating environment
source .venv/bin/activate
```

### Python packages
```bash
# Scraping data
pip install scrapy
```

## Extract
### Web-scraping
```bash
# Running web-scraper and saving data to jsonl file.
# /etl-mlivre/src/

scrapy crawl mercadolivre -o ../data/data-mlivre.jsonl
```