#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request 
import joblib


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


scaler = joblib.load('scaler.bin')
scaler


# In[4]:


app = Flask(__name__)


# In[5]:


@app.route("/")
def home():
    return render_template('home.html')


# In[6]:


@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        drug_selected = request.form['drug']
        drug = -1.0
        if drug_selected == "D-penicillamine":
            drug = 0.0
        elif drug_selected == "Placebo":
            drug = 1.0
        age = float(request.form['age']) #range: (26.0,78.0)
        gender = request.form['sex']
        sex = -1.0
        if gender == 'Female':
            sex = 0.0
        elif gender == 'Male':
            sex = 1.0
        ascites_selected = request.form['ascites']
        ascites = -1.0
        if ascites_selected == 'No':
            ascites = 0.0
        elif ascites_selected == 'Yes':
            ascites = 1.0
        hepa_selected = request.form['hepatomegaly']
        hepatomegaly = -1.0
        if hepa_selected == 'No':
            hepatomegaly = 0.0
        elif hepa_selected == 'Yes':
            hepatomegaly = 1.0
        spider_selected = request.form['spiders']
        spider = -1.0
        if spider_selected == 'No':
            spider = 0.0
        elif spider_selected == 'Yes':
            spider = 1.0
        edema_selected = request.form['edema']
        edema = -1.0
        if edema_selected == 'No edema and no diuretic therapy for edema':
            edema = 0.0
        elif edema_selected == 'Edema present without diuretics, or edema resolved by diuretics':
            edema = -1.0
        elif edema_selected == 'Edema despite diuretic therapy':
            edema = 1.0
        bilirubin = float(request.form['bilirubin']) #range: (0.30,7.30)
        cholesterol = float(request.form['cholesterol']) #range: (160.875,459.875)
        albumin = float(request.form['albumin']) #range: (2.45,4.56)
        copper = float(request.form['copper']) #range: (4.0,175.0)
        alk_phos = float(request.form['alk_phos']) #range: (289.0,2745.0)
        sgot = float(request.form['sgot']) #range: (26.35,202.88)
        tryglycerides = float(request.form['tryglycerides']) #range: (45.875,176.875)
        platelets = float(request.form['platelets']) #range: (62.0,503.75)
        prothrombin = float(request.form['prothrombin']) #range: (9.0,12.75)
        
        X_test = scaler.transform([[
                drug,
                age,
                sex,
                ascites,
                hepatomegaly,
                spider,
                edema,
                bilirubin,
                cholesterol,
                albumin,
                copper,
                alk_phos,
                sgot,
                tryglycerides,
                platelets,
                prothrombin
        ]])
#         print(X_test)
        predictions = model.predict(X_test)
        output = predictions[0]
#         print(output)
        if output == 1:
            return render_template('home.html',prediction_text="The person with the given details has a normal liver.")
        elif output == 2:
            return render_template('home.html',prediction_text="The person with the given details has a fatty liver.")
        elif output == 3:
            return render_template('home.html',prediction_text="The person with the given details is suffering from Liver Fibrosis.")
        elif output == 4:
            return render_template('home.html',prediction_text="The person with the given details is suffering from Liver Cirrhosis.")


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

