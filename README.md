# Maternal_Health_Risk

## Summary

Pregnancy is a privileged time for medical follow-up. In rare cases, complications may arise for a variety of reasons, requiring rapid intervention.
By monitoring precise indicators, it is possible to categorize profiles and propose an emergency consultation. That's what this algorithm is all about: detecting profiles at risk and inviting them to an emergency consultation.

## Dataset

Data set is available in [Kaggle](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data)
and in [UC Irvin machin learning repository](https://archive.ics.uci.edu/dataset/863/maternal+health+risk)

Data has been collected from different hospitals, community clinics, maternal health cares through the IoT based risk monitoring system.

    Age: Age in years when a woman is pregnant.
    SystolicBP: Upper value of Blood Pressure in mmHg, another significant attribute during pregnancy.
    BS: Blood glucose levels is in terms of a molar concentration, mmol/L.
    BodyTemp: in F°
    HeartRate: A normal resting heart rate in beats per minute.
    
    Risk Level: Predicted Risk Intensity Level during pregnancy considering the previous attribute.

The DiastolicBP: Lower value of Blood Pressure in mmHg, another significant attribute during pregnancy was not keep for training the model due to hight correlation with SystolicBP.

## Approach

The data were explored and selected to best feed the model. Tests were carried out on various algorithms to select the most efficient, and the selected model was fine-tuned to improve its performance. These steps are presented in the attached notebook.
The final model was taken, trained and serialized in a python file called train.py
Then the model is deploied using Flask. The code is available in predict.py
Then this app is place in a docker container

## How-to

To use the app : install aned run Docker
                 build the image using "docker build -t Maternal_Health_Risk ."
                 run the container using "docker run Maternal_Health_Risk"
                 run a script predict_test.py containing patient variables value (exemple available)
