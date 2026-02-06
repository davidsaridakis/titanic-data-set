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
- `README.md`

**Note:** Raw data is not included in repo intentionally. 

## Workflow Overview

### 1. Data Exploration (`exploration.ipynb`)

- Load the raw dataset  
- Inspect structure and missing values  
- Generate summary statistics  
- Visualize survival patterns

---

### 2. Data Preprocessing (`src/preprocessing.py`)

- Handle missing values  
- Encode categorical variables (e.g., one-hot encoding for `Embarked`)  
- Separate target variable (`Survived`) for training  
- Return feature matrix `X` and target vector `y`

---

### 3. Modeling

The following models were implemented and evaluated:

- Logistic Regression  
- Random Forest  
- Gradient Boosting  

Each model:
- Uses a stratified train/validation split  
- Is trained on preprocessed features  
- Outputs validation accuracy  
- Optionally inspects feature importance

---

### 4. Prediction

- Load Kaggle test dataset  
- Apply the same preprocessing pipeline  
- Generate predictions  
- Save submission file in `submissions/`


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