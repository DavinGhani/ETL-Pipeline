# ETL Pipeline for Product Data

This project automates the process of extracting, transforming, and loading (ETL) product data from a fashion website. The pipeline scrapes product information, processes it, and stores it in a structured format for further analysis or use.

## Project Overview

The project consists of an **ETL (Extract, Transform, Load)** pipeline that:
1. **Extracts** product data from a website using web scraping.
2. **Transforms** the data into a clean, usable format.
3. **Loads** the transformed data into a CSV file or a PostgreSQL database.

### Key Components

- **`extract.py`**: Contains functions for extracting product data from the website using BeautifulSoup.
- **`transform.py`**: Processes the extracted data by cleaning it, converting prices to IDR, and applying necessary transformations.
- **`load.py`**: Saves the cleaned data to a CSV file or a PostgreSQL database.
- **`main.py`**: Orchestrates the entire ETL pipeline, calling the functions from `extract.py`, `transform.py`, and `load.py` in sequence.

### Directory Structure

```plaintext
ETL-Pipeline
├── test
│   ├── test_extract.py       # Unit tests for the extract functions
│   ├── test_load.py          # Unit tests for the load functions
│   └── test_transform.py     # Unit tests for the transform functions
├── utils
│   ├── extract.py            # Contains the extraction functions
│   ├── load.py               # Contains functions for saving data (to CSV/PostgreSQL)
│   └── transform.py          # Contains data transformation functions
├── README.md                 # Project overview and setup instructions
├── main.py                   # Main script to run the ETL pipeline
├── products.csv              # CSV file where transformed data is stored
├── requirements.txt          # List of dependencies required for the project
└── submission.txt            # Any notes or additional documentation
```
## Setup Instructions

Follow these steps to set up and run the ETL pipeline.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/DavinGhani/ETL-Pipeline
cd project-name
```

### 2. Install Dependencies
```
# Create a virtual environment (if you don't have one already)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt
```
### 3. Run The ETL
```
python main.py
```

### 4. Testing the ETL Components
```
python -m unittest discover test/
coverage run -m unittest discover test/
coverage report
```
