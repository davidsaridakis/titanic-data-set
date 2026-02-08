# Titanic Data Analysis & Modeling

An demonstration of a machine learning workflow on the Titanic dataset from Kaggle. Includes data exploration, preprocessing, model building, evaluation, model comparisons and predictions.

My focus was on clean organized code, reproducible results, and a logical workflow.  

---

## Project Overview

This project demonstrates a structured machine learning workflow:

1. **Data Exploration**  
   - Initial look at the training data  
   - Missing value checks and summary statistics  
   - Visualizations of gender_submission survival rates 

2. **Data Preprocessing** `src/preprocessing.py`
   - Cleaning raw data  
   - Handling missing values  
   - Encoding categorical variables 
   - Basic feature engineering 
   - Separate target variable (`Survived`) for training
   - Implemented in `src/preprocessing.py` for reusability

3. **Model Comparison**  
   - Models included: Logistic Regression, Random Forest, Gradient Boosting; coming from `src/models.py` for efficiency and reusability
   - Scaling features when required
   - Train/validation split to evaluate models  
   - Accuracy comparison visualized in `notebooks/model_comparison.ipynb`  
   - Logistic Regression with scaling identified as the best performer

4. **Final Model & Submission**  
   - Best model retrained on the full training dataset  
   - Predictions generated for the test set  
   - Submission CSV saved to `data/submissions/` with versioned filenames  
   - Implemented in `notebooks/final_model.ipynb`

---

## Project Structure
- `data/`
  - `raw/` → Raw CSV files downloaded from Kaggle (not tracked in Git)  
  - `submissions/` → Versioned submission CSVs
- `notebooks/` → Jupyter notebooks  
  - `exploration.ipynb` → Initial data exploration
   - `model_comparison.ipynb`  
  - `final_model.ipynb` → Train and test most accurate model on full dataset and generate submission CSV   
- `src/` → Python scripts  
  - `preprocessing.py` → Functions for cleaning and preparing data
  - `models.py` → Return a dictionary of models to be used in model comparison
- `.gitignore`  
- `requirements.txt`  
- `README.md`

**Note:** Raw data is not included in repo intentionally. 

## Dependencies
- pandas
- scikit-learn
- seaborn
- matplotlib
```bash
pip install -r requirements.txt
```
- See `requirements.txt` for exact versions.

## How to use
1. **Clone the repository**
```bash
git clone https://github.com/davidsaridakis/titanic-data-set.git
cd titanic-data-set
```

2. **Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  
# or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run notebooks in order**
`notebooks/exploration.ipynb` → Explore and clean data
`notebooks/model_comparison.ipynb` → Train and compare models
`notebooks/final_model.ipynb` → Train best model on full dataset and generate submission