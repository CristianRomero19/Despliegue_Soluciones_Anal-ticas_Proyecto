import pandas as pd
import numpy as np

import mlflow
import mlflow.sklearn

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./Data/Human_Resources.csv")
X=data.drop('Attrition', axis=1)
Y = data['Attrition'].map({'Yes': 1, 'No': 0})

categoricas=[]
for i in X.columns:
    if X[i].dtype == "object":
        categoricas.append(i)

le = LabelEncoder()

for i in categoricas:
    X[i]=le.fit_transform(X[i])
X=X.astype('int64')

for i in X.columns:
    X[i] = MinMaxScaler().fit_transform(X[[i]])
    #print(i)

FEATURES = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
       'Education', 'EducationField', 'EmployeeCount', 'EmployeeNumber',
       'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement',
       'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus',
       'MonthlyRate', 'NumCompaniesWorked', 'Over18',
       'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany'      
    ]

X_new = X[FEATURES]

x_train, x_test, y_train, y_test=train_test_split(X_new, Y, test_size = 0.25, random_state = 42)

experiment = mlflow.set_experiment("Modelo_Random_Forest")

with mlflow.start_run(experiment_id=experiment.experiment_id):

    n_estimators = 850
    max_depth = 19
    random_state = 1200

    forest = RandomForestClassifier(n_estimators=n_estimators, max_depth = max_depth, random_state = random_state)
    forest.fit(x_train,y_train)
    y_pred = forest.predict(x_test)

    mlflow.log_param("num_trees", n_estimators)
    mlflow.log_param("maxdepth", max_depth)
    mlflow.log_param("random_state", random_state)

    mlflow.sklearn.log_model(forest, "random-forest-model")

    test_acc = metrics.accuracy_score(y_test, y_pred)
    roc = metrics.roc_auc_score(y_test, y_pred)
    f1 = metrics.f1_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)

    mlflow.log_metric("Accuracy", test_acc)
    mlflow.log_metric("ROC", roc)
    mlflow.log_metric("F1-Score", f1)
    mlflow.log_metric("Precision", precision)
    mlflow.log_metric("Recall", recall)

    print(f'Accuracy Score {str(experiment.name)}', test_acc)
    print(f'Precision {str(experiment.name)}', precision)
    print(f'Recall {str(experiment.name)}', recall)
    print(f'F1-Score {str(experiment.name)}', f1)
    print(f'ROC Score {str(experiment.name)}', roc)


experiment2 = mlflow.set_experiment("Modelo_Naive_Bayes")

with mlflow.start_run(experiment_id=experiment2.experiment_id):

    clfNB = GaussianNB()
    clfNB.fit(x_train,y_train)
    y_pred = clfNB.predict(x_test)

    mlflow.sklearn.log_model(clfNB, "naive-bayes-model")

    test_acc = metrics.accuracy_score(y_test, y_pred)
    roc = metrics.roc_auc_score(y_test, y_pred)
    f1 = metrics.f1_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)

    mlflow.log_metric("Accuracy", test_acc)
    mlflow.log_metric("ROC", roc)
    mlflow.log_metric("F1-Score", f1)
    mlflow.log_metric("Precision", precision)
    mlflow.log_metric("Recall", recall)

    print(f'Accuracy Score {str(experiment2.name)}', test_acc)
    print(f'Precision {str(experiment2.name)}', precision)
    print(f'Recall {str(experiment2.name)}', recall)
    print(f'F1-Score {str(experiment2.name)}', f1)
    print(f'ROC Score {str(experiment2.name)}', roc)


