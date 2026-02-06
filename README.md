# Titanic Data Analysis & Modeling

An demonstration of a machine learning workfloe on the Titanic dataset from Kaggle. Includes data exploration, preprocessing, model building, evaluation, predictions and model comparisons.

The focus is on **clean organized code**, **reproducible results**, 

## Project Structure

- `data/raw/` → Raw CSV files downloaded from Kaggle (not tracked in Git)   
- `notebooks/` → Jupyter notebooks  
  - `exploration.ipynb` 
   - `model_random_forest.ipynb` → Random Forest  
  - `model_logistic_regression.ipynb` → Logistic Regression  
  - `model_gradient_boosting.ipynb` → Gradient Boosting  
- `src/` → Python scripts  
  - `preprocessing.py` → Functions for cleaning and preparing data  
- `.gitignore`  
- `requirements.txt`  
- `README.md

**Note:** Raw data is not included in repo intentionally. 

## Dependencies
- pandas
- scikit-learn
- seaborn
```bash
pip install -r requirements.txt
```
- See `requirements.txt` for exact versions.

## Instalation
1. Clone the repository:

```bash
git clone https://github.com/davidsaridakis/titanic-data-set.git
cd titanic-data-set
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```