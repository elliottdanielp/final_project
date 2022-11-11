# final_project - Titanic_Passenger_Survival

## Communication Protocols

![team_communication_2](https://user-images.githubusercontent.com/106495422/198314850-c9e5acbf-42a1-47bc-92cf-9494c95e862d.png)


# Selected Topic

Titanic Passenger Survival...

Did the survival rate of the Titanic have anything to do with what class the passenger was in? Or was it the passengers age or maybe their sex that played a role in the survival rate? What if them having siblings or a spouse on board played a role?

The reason the group chose this question to answer is in April of 2012 the Titanic II was announced. The intended launch date was originally set to be 2016 but delayed to 2018 and push again until 2022. The project was resumed in November 2018 after a hiatus which began in 2015 cause by a financial dispute.

With the help of Kaggle the team was able to acquire multiple data sets, with information ranging from Passenger name's, sex, age all the way to if they had parents, siblings or a spouse on board. The data sets also include where the passenger embarked from with 3 options for the passengers - Southampton, Cherbourg and Queenstown.

Will the Titanic II ever set sail? Who knows, but if it does will the passengers face the same fate as the original?

# Dashboard

Dashboard will consist of: 
- Showing the findings of the machine learning algorithm
- Graphic of survival rate by class 
- Graphic of survival rate by sex 
- Graphic of survival rate by age

The main tool used to create the dashboard will be Tableau. The Tableau dashboard will have an assortment of interactive charts. 
Tableau is a data visualization tool that helps create interactive graphs and charts in the form of dashboards and worksheets to gain insights into a data source.

By using Tableau public our viewers will be able to interact with our analysis by using the Passenger Lookup. With the passenger lookup a user can select a name from the drop down to view if they survived or not what class they are and their age along with other measures. The viewrs will also be able to sort the list by Male or Female. Also the list can be filtered by just class to show who survived or not from a selected class. Finaly the list can be filterd by all the survivers.   

[Tableau Dashboard](https://public.tableau.com/app/profile/dan5194/viz/Titanic_Dashboard_16674008648990/Titanic_Dashboard)

# Machine Learning Model
## Overview
Can we create a machine learning model to predict what types of passengers survived the crash? Moreover, which characteristics of a passenger lead them to be saved. To answer this question, we will feature the characteristics about the titanic passengers in the model and target if they survived or not.

## Data Preprocessing
1. Our dataset has 12 columns with 1309 separate data points. 11 columns containing passenger information and 1 column determining their survival. 0 equating to not surviving and 1 equating to survival.
2. Name and Passenger ID are variables are not needed in a Machine Learning Model, so they are dropped. 
3. After checking the number of unique values, I noticed 929 of the 1309 values for ticket were unique, with no ticket occurring more than 11 times. The ticket column refers to the unique ID ticket that was bought. This has no relation to if the passenger survived. Therefore, ticket is not a helpful feature for our machine learning model, so it is dropped.
4. Next, I looked at the null values in our dataset. Due to the small size of our dataset, we will attempt to keep as many rows as possible and fill in any null values. The two major columns for null values are age and cabin. All null values for the cabin column will be filled with "u" for unknown. All age values will be filled in taking the average value of the two ages they are next to in the dataset.
5. The cabin column now has 187 unique values. Known cabin values are in the form A 46, where A is the deck and 46 is the room. All odd numbered cabins are on the starboard(right) side and all even numbered cabins are on the port(left) side. I broke cabin into two separate rows. The first column is Deck, which contains values A through G, T, and Unknown. This consists of 9 unique values. The second column is Cabin_Location. This column contains values of starboard, port, or neither. We finish by dropping cabin row as the Deck and Cabin_Location columns represent the same values.
6. Now that the name, ID, and ticket number are dropped, 87 out of our 1309 rows have duplicate values. This is due to two different people sharing the exact same characteristics. Since the dataset is small and they are different passengers, I decided to leave them in the dataset for the model. Usually duplicate values overfit, but that is not a concern due to the dataset size.
7. Lastly, the non-numeric values need to be converted into numeric values. To do so, I took all the non-numeric features and engineered “n” separate columns, where “n” is the number of unique values that exist in that column. The newly created columns will be either 0 or a 1. For example, the Sex column was originally “Male or Female”. It will turn into two new columns of Sex Male and Sex Female. If the original column had male as a result the Sex Male column will be 1 and the Sex Female column will be 0.
8. We finish our preprocessing with 23 columns and 1309 rows.

## Features and Targets
Features:
-	Passenger Class
-	Passenger Sex
-	Passenger Age
-	Number of Siblings Aboard
-	Number of Parents Aboard
-	Price of Ticket
-	Port of Embarkation
-   Deck Location
-   Cabin Location

Target:
-	Survived the shipwreck

## Training and Testing Model
The data will be randomly split into a training and a testing set. 75% of the data will be randomly selected to be in the training set. The we will use this data to train or fit the machine learning model. The remaining 25% of the data will be used to test the validity of our model.

The training and testing datasets are then scaled to the unit variance of the training set. This reduces the impact of outliers and standardizes the values across columns so that one column isn’t weighted more due to its values being larger.

## Description of Model
### Overview
The model we are using is a Gradient Boosted Classifier model. The boosting element is it uses a large number of weak learning models that each learn from each other to create a stronger learning model. The gradient aspect is each model learns from the errors of the previous. 

We choose this because it is a classifier model that can be highly accurate and can be tuned to increase performance. 

### Pros and Cons
Benefits of the model:
- Classifier model that is able to predict both numerical and categorical values.
- Training off of weakness makes the model highly accurate
- Has several hyperparameters such as learning rate and estimators that can be adjusted to increase performance

Downsides of the model:
- The model will keep trying to minimize errors and can emphasize outliers too much and overfit easily
- Complex "black box" model that can be computationally intense

### Results
After adjusting the number of weak learners and rate at which the models learn to optimize performance, our model had an accuracy score of 86.28%. This means it correctly identified 86.28% of the test values into survived or died. This is solid, but still leaves room for improvement. These improvement areas are to use a random forest model to look at feature importance, perform dimensionality reduction, and switch from the gradient boosted classifier model.

[Google Slides](https://docs.google.com/presentation/d/1fPfQUhDatXaTUa1Yei5ws-fKyiqXjxEmRdNtDGr36yE/edit?usp=sharing)

