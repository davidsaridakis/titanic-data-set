# The purpose of this file is to do a universal data 
# clean to prepare data for the different models in 
# project.
# 
# Fill missing data
# Encode sex
# Drop cabin
# Create 'family size'.
import pandas as pd 

def clean_data(df, is_train=True):
    """
    Perform universal preprocessing for Titanic dataset.

    Parameters
    ----------
    df: pandas.DataFrame
        Raw Titanic dataframe (train or test)
    is_train: bool
        Whether the dataframe is training data (contains 'Survived' column)

    Returns
    --------
    X : pandas.DataFrame
        Cleaned feature matrix
    y : pandas.Series or None
        Target variable if training data, else None
    """
    
    data = df.copy()

    # --- Target ---
    y = None
    if is_train:
        y = data['Survived']
        data = data.drop(columns=['Survived'])
    
    # --- Drop high noise / unused columns ---
    data = data.drop(columns=['Cabin', 'Ticket', 'Name'])

    # --- Handle missing values ---
    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())

    # --- Feature Engineering ---
    data['Family Size'] = data['SibSp'] + data['Parch'] + 1

    # --- Encode Categoricals ---
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

    return data, y