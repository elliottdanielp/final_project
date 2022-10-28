# Technologies Used
## Data Cleaning and Analysis
Panda DataFrame will be used to clean the data and perform an exploratory analysis. Pandas allows data engineers to provide descriptive statiscs that summarize central tendency, dispersion and the overall shape of datasets distribution and values.  It allows analysis for numeric and object series and data frames of mixed types to output data for critical decision making.  

Further analysis will be completed using other Python segments as well. 
   

## Database Storage
PgAdmin is the database we intend to use for hosting, and we will integrate with to display the data.

### Our Main structure will be:

- CREATE TABLE IF NOT EXISTS public.titanic_main
- (
    - passegerID integer NOT NULL,
    - survived integer,
    - pclass integer,
    - name text,
    - sex text,
    - age numeric,
    - sibsp integer,
    - parch integer,
    - ticket text,
    - cabin text,
    - embarked text,
    - fare numeric,
    - CONSTRAINT titanic_main_pkey PRIMARY KEY (passegerID)
- )

Example data:

- PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Cabin,Embarked,Fare
- 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,,S,7.25
- 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,C85,C,71.2833
- 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,,S,7.925
- 4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,C123,S,53.1
- 5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,,S,8.05
- 6,0,3,"Moran, Mr. James",male,,0,0,330877,,Q,8.4583
- 7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,E46,S,51.8625
- 8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,,S,21.075
- 9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,,S,11.1333
- 10,1,2,"Nasser, Mrs. Nicholas (Adele Achem)",female,14,1,0,237736,,C,30.0708



## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is setup to be a Logistic Regression Classifier 

- Our main source file will be as such in the main branch:
    /final_project/MachineLearningModel.ipynb

## Dashboard
In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will be hosted on Tableau.
