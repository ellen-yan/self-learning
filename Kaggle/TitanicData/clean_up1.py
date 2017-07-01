import numpy as np
import pandas as pd

def read_from_file(path):
    data_frame = pd.read_csv(path)
    return data_frame

def survived_pclass_sex_age_sibsp_parch_fare(df, to_drop):
    """Given titanic data, keeps only the columns of interest."""
    for e in to_drop:
        df.drop(e, axis=1, inplace=True) #inplace changes the df itself


def cleanup(df, list_of_headers):
    """Replaces NaN entries with the average of that column."""

    # Replaces NaN entries with the average of that column
    mu = df.mean(axis=0)
    for e in list_of_headers:
        df[e].replace(np.nan, mu[e], inplace=True)

    # drop any row with an NaN entry
    #df.dropna(axis=0, how='any', inplace=True)

def change_sex_to_int(df):
    mapping = {'male': 1, 'female': 0}
    df.replace({'Sex': mapping}, inplace=True)

def write_to_file(path, df):
    df.to_csv(path, index=False)



if __name__ == "__main__":
    path_to_csv = "/Users/ellenyan/Documents/SelfLearning/Kaggle/TitanicData/titanic_test.csv"
    path_to_new_csv = "/Users/ellenyan/Documents/SelfLearning/Kaggle/TitanicData/titanic_test_clean1.csv"
    titanic_df = read_from_file(path_to_csv)


    to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked']
    survived_pclass_sex_age_sibsp_parch_fare(titanic_df, to_drop)

    change_sex_to_int(titanic_df)

    headers = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    cleanup(titanic_df, headers)

    print titanic_df
    write_to_file(path_to_new_csv, titanic_df)
