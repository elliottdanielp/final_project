# Import Database Dependencies
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import psycopg2
from config import user, password, hostname, port, db

# Import Data Preprocessing Dependencies
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Establish connection to database
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{db}')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Inspect Database to get columns from dataset
inspector = inspect(engine)
column_info = inspector.get_columns("titanic_dataset")
titanic_columns = []
for column in column_info:
    titanic_columns.append(column["name"].title())

# Query titanic dataset
titanic = engine.execute("SELECT * FROM titanic_dataset").fetchall()
# Create dataframe
titanic_df = pd.DataFrame(titanic, columns=titanic_columns)

# Change Age and Fare to floating types
titanic_df["Age"] = titanic_df["Age"].astype("float64")
titanic_df["Fare"] = titanic_df["Fare"].astype("float64")

# Drop Passenger ID and Name Columns
titanic_df.drop(["Passengerid", "Name", "Ticket"], axis=1, inplace=True)

# Fill null values for Embarked, Fare, and Cabin
titanic_df["Embarked"].fillna("S", inplace=True)
titanic_df["Fare"].fillna(0, inplace=True)
titanic_df["Cabin"].fillna("U", inplace=True)
titanic_df.interpolate(method="linear", inplace=True)

# Create two functions to engineer new rows from Cabin
# Pass cabin information and return the deck
def get_deck(cabin):
    # Return First Character of Cabin 
    return cabin[0]

# Pass cabin information and return which side of boat cabin is located
def get_location(cabin):
    # Create string list of integers 0 through 9
    nums = str(list(range(0,10)))
    # If last character of Cabin is not a number, return neither
    if cabin[-1] not in nums:
        return "Neither"
    else:
        # Convert string number into integer to perform math on
        end_num = int(cabin[-1])
        # Even number ending cabins are Port(Left) side and odd are Starboard(Right) side
        if end_num%2 == 0:
            return "Port"
        else:
            return "Starboard"

# Engineer two new columns from Cabin. Deck and Cabin_Location.
titanic_df["Deck"] = titanic_df["Cabin"].apply(get_deck)
titanic_df["Cabin_Location"] = titanic_df["Cabin"].apply(get_location)

# Drop cabin as Deck and Cabin_Location give same information
titanic_df.drop(["Cabin"], axis=1, inplace=True)

# Use OneHotEncoder to transform non-numeric columns into numeric
# Reset titanic dataframe index to match with encode merge
titanic_df.reset_index(drop=True, inplace=True)

# Generate categorical variable list
titanic_cat = titanic_df.dtypes[titanic_df.dtypes == "object"].index.tolist()

# Create OneHotEncoder Instance
enc = OneHotEncoder(sparse=False)
# Fit and transform OneHotEncoder using categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(titanic_df[titanic_cat]))
# Add the encoded variable names to dataframe
encode_df.columns = enc.get_feature_names_out(titanic_cat)

# Merge encoded features and drop originals
merged_titanic_df = titanic_df.merge(encode_df, left_index=True, right_index=True).drop(labels=titanic_cat, axis=1)

# Export to csv for ML model
merged_titanic_df.to_csv("Data/DataPreprocessing.csv",index=False)