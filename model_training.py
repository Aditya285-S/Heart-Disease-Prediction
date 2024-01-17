import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

heart_data = pd.read_csv('heart.csv')


heart_data['Sex']=heart_data['Sex'].map({'M':0 , 'F':1})
heart_data['ChestPainType']=heart_data['ChestPainType'].map({'ATA':0 , 'NAP':1 , 'ASY':2 , 'TA':3})
heart_data['RestingECG']=heart_data['RestingECG'].map({'Normal':0 , 'ST':1 , 'LVH':2})
heart_data['ExerciseAngina']=heart_data['ExerciseAngina'].map({'N':0 , 'Y':1})
heart_data['ST_Slope']=heart_data['ST_Slope'].map({'Up':0 , 'Flat':1 , 'Down':2})


X = heart_data.drop(columns='HeartDisease', axis=1)
Y = heart_data['HeartDisease']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)


model = RandomForestClassifier()
model.fit(X_train, Y_train)


train_predictions = model.predict(X_train)
training_accuracy = accuracy_score(train_predictions, Y_train)
print('Accuracy on Training data:', training_accuracy * 100, '%')


test_predictions = model.predict(X_test)
test_accuracy = accuracy_score(test_predictions, Y_test)
print('Accuracy on Test data:', test_accuracy * 100, '%')


joblib.dump(model, 'heart_disease_model')

RFC_model = joblib.load('heart_disease_model')
