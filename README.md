# final_project - Titanic_Passenger_Survival

## Communication Protocols

![team_communication_2](https://user-images.githubusercontent.com/106495422/198314850-c9e5acbf-42a1-47bc-92cf-9494c95e862d.png)


# Selected Topic

Titanic Passenger Survival...

Did the survival rate of the Titanic have anything to do with what class the passenger was in? Or was it the passengers age or maybe their sex that played a role in the survival rate? What if them having siblings or a spouse on board played a role?

The reason the group chose this question to answer is in April of 2012 the Titanic II was announced. The intended launch date was originally set to be 2016 but delayed to 2018 and push again until 2022. The project was resumed in November 2018 after a hiatus which began in 2015 cause by a financial dispute.

With the help of Kaggle the team was able to acquire multiple data sets, with information ranging from Passenger name's, sex, age all the way to if they had parents, siblings or a spouse on board. The data sets also include where the passenger embarked from with 3 options for the passengers - Southampton, Cherbourg and Queenstown.

Will the Titanic II ever set sail? Who knows, but if it does will the passengers face the same fate as the original?








# Machine Learning Model
## Overview
Can we create a machine learning model to predict which passengers will survive based on certain characteristics? To answer this question, we will target whether or not the passenger survived the shipwreck.

## Data Preprocessing
1. Our dataset has 12 columns with 891 separate data points.
2. Name and Passenger ID are variables are not needed in a Machine Learning Model, so they are dropped. 
3. After checking the number of unique values, I noticed 681 of the 891 values for ticket were unique, with no ticket occurring more than 7 times. Ticket is not a helpful feature for our machine learning model, so it is dropped.
4. Next, I looked at the null values in our dataset. 687 of the 891 values for cabin are null. This is around 77% of the dataset. Cabin would be a good predictor of survival as cabins closer to the impact could have a lower chance of survival. However, there are too many null values to use in our model, so it is dropped. 
5. I dropped all the rows with null values and rows that duplicates. The machine learning model cannot handle null values and we do not want to overfit our model with any duplicate rows. This left 8 columns and 674 data points. Our preprocessing removed 217 data points.
6. Lastly, the non-numeric values need to be converted into numeric values. To do so, I took all the non-numeric features and engineered “n” separate columns, where “n” is the number of unique values that exist in that column. The newly created columns will be either 0 or a 1. For example, the Sex column was originally “Male or Female”. It will turn into two new columns of Sex Male and Sex Female. If the original column had male as a result the Sex Male column will be 1 and the Sex Female column will be 0.
7. We finish our preprocessing with 11 columns and 674 rows.

## Features and Targets
Features:
-	Passenger Class
-	Passenger Sex
-	Passenger Age
-	Number of Siblings Aboard
-	Number of Parents Aboard
-	Price of Ticket
-	Port of Embarkation 
Target:
-	Survived or not

## Training and Testing Model
The data will be randomly split into a training and a testing set. 75% of the data will be randomly selected to be in the training set. The we will use this data to train or fit the machine learning model. The remaining 25% of the data will be used to test the validity of our model.

The training and testing datasets are then scaled to the unit variance of the training set. This reduces the impact of outliers and standardizes the values across columns so that one column isn’t weighted more due to its values being larger.

## Description of Model
