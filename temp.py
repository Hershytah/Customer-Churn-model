# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

df_1 = pd.read_csv("C:/Users/harsh/Downloads/first git/Customer_Churn.csv")


q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    print(new_df__dummies.tail(1))

    
    '''
     Call  Failure
     Complains
     Tenure
     Charge  Amount
     Seconds of Use
     Frequency of use
     Frequency_SMS
     Distinct Called Numbers
     Age Group
     Tariff Plan
     Status
     Age
     Customer Value
     
    '''
    

    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    
    
    model = pickle.load(open("model.sav", "rb"))
   
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
            inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13]]
    
    new_df = pd.DataFrame(data, columns = ['Call  Failure', 'Complains', 'Tenure', 'Charge  Amount',
            'Seconds of Use', 'Frequency of use', 'Frequency_SMS',
            'Distinct Called Numbers', 'Age Group', 'Tariff Plan', 'Status', 'Age',
            'Customer Value'])
    
    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    
    # Group the tenure in bins of 12 months
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    df_2['Subscription length group'] = pd.cut(df_1['Subscription  Length'], range(1, 80, 12), right=False, labels=labels)
    
    # Group the Age in bins of 12 months
    labels = ["{0} - {1}".format(i, i + 9) for i in range(15, 55, 10)]
    df_2['Age_group'] = pd.cut(df_1['Age'], range(15, 60, 10), right=False, labels=labels)
    
    # convert status as 1 for active and 0 for non active
    # convert Tariff plan as 1 for pa y as you go and 0 for contractual
    df_2['Status'] = df_1['Status'].map({1: 1, 2: 0})
    df_2['Tariff Plan'] = df_1['Tariff Plan'].map({1: 1, 2: 0})

    #drop column customerID and tenure
    df_2.drop(columns= ['Age', 'Subscription  Length', 'Age Group','Frequency of use', 'Distinct Called Numbers'], axis=1, inplace=True)   
   
    new_df__dummies = pd.get_dummies(df_2[['Call  Failure', 'Complains', 'Tenure', 'Charge  Amount',
            'Seconds of Use', 'Frequency of use', 'Frequency_SMS',
            'Distinct Called Numbers', 'Age Group', 'Tariff Plan', 'Status', 'Age',
            'Customer Value']])
   
    print(new_df__dummies.columns)

    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, 
                           query1 = request.form['query1'], 
                           query2 = request.form['query2'],
                           query3 = request.form['query3'],
                           query4 = request.form['query4'],
                           query5 = request.form['query5'], 
                           query6 = request.form['query6'], 
                           query7 = request.form['query7'], 
                           query8 = request.form['query8'], 
                           query9 = request.form['query9'], 
                           query10 = request.form['query10'], 
                           query11 = request.form['query11'], 
                           query12 = request.form['query12'], 
                           query13 = request.form['query13'] 
                           )
    
if __name__ == "__main__":
    app.run(debug=True)
