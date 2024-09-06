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

# Transforming data
pip install pandas

# Visualizing data
pip intall streamlit
```

## Extract
### Web-scraping
```bash
# Running web-scraper and saving data to jsonl file.
# /etl-mlivre/src/

scrapy crawl mercadolivre -o ../data/data-mlivre.jsonl
```

## Transform
### Data handling
```bash
# Cleaning data and saving it to a SQLite database.
# /etl-mlivre/src/

python3 transform/main.py
```

## Visualize
### Dashboard
```bash
# Visualizing data in a web page.
# /etl-mlivre/src/

streamlit run dashboard/app.py
```