#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Datos de entrada del modelo:
["fecha", "total_trafico", "tmed", "prec", "tmin", "tmax", "presMax", "presMin",
       "velmedia", "dir", "sol", "hrMedia", "hrMax", "hrMin", "trafico_aereo",
       "Temp_Hum", "VelViento_DirViento", "Temp_VelViento", "RadSolar_Temp",
       "Presion_Hum", "Prec_Hum", "RadSolar_Hum"]

    {"fecha": string,
    "total_trafico": float64, 
    "tmed": float64,
    "prec": float64, 
    "tmin": float64, 
    "tmax": float64, 
    "presMax": float64, 
    "presMin": float64,
    "velmedia": float64,
    "dir": float64, 
    "sol": float64, 
    "hrMedia": float64, 
    "hrMax": float64, 
    "hrMin": float64,
    "trafico_aereo": float64,
    "Temp_Hum": float64,
    "VelViento_DirViento": float64, 
    "Temp_VelViento": float64, 
    "RadSolar_Temp": float64,
    "Presion_Hum": float64, 
    "Prec_Hum": float64, 
    "RadSolar_Hum": float64
}



{ "fecha" : "2024-05-22",
  "total_trafico": 1865962.0,
 "tmed": 10.4,
 "prec": 0.0,
 "tmin": 6.7,
 "tmax": 14.0,
 "presMax": 959.4,
 "presMin": 953.8,
 "velmedia": 3.6,
 "dir": 23.0,
 "sol": 1.2,
 "hrMedia": 69.0,
 "hrMax": 82.0,
 "hrMin": 61.0,
 "trafico_aereo": 4457433.497948014,
 "AQI_calculated": 60.0,
 "Temp_Hum": 717.6,
 "VelViento_DirViento": 82.8,
 "Temp_VelViento": 239.2,
 "RadSolar_Temp": 12.48,
 "Presion_Hum": 78670.8,
 "Prec_Hum": 0.0,
 "RadSolar_Hum": 82.8
}


{fecha: "2024-08-01",
"total_trafico": 1223426.0,
 "tmed": 8.9,
 "prec": 0.0,
 "tmin": 2.2,
 "tmax": 15.6,
 "presMax": 959.9,
 "presMin": 957.1,
 "velmedia": 1.9,
 "dir": 99.0,
 "sol": 8.3,
 "hrMedia": 75.0,
 "hrMax": 98.0,
 "hrMin": 41.0,
 "trafico_aereo": 4445656.4400457945,
 "AQI_calculated": 101.0,
 "Temp_Hum": 667.5,
 "VelViento_DirViento": 188.1,
 "Temp_VelViento": 881.1,
 "RadSolar_Temp": 73.87,
 "Presion_Hum": 94070.2,
 "Prec_Hum": 0.0,
 "RadSolar_Hum": 622.5}
"""
from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load("modelo.pkl")

app = FastAPI()


def weekday_encoding(message):
    weekday_encoded = {"Dia_0": 0, "Dia_1": 0, "Dia_2": 0, "Dia_3": 0, "Dia_4": 0, "Dia_5" : 0, "Dia_6": 0}
    message["fecha"] = pd.to_datetime(message["fecha"]) 
    message["Dia_semana"] = message["fecha"].dayofweek 
    if message["Dia_semana"] == 0:
        weekday_encoded["Dia_0"] = 1
    elif message["Dia_semana"] == 1:
        weekday_encoded["Dia_1"] = 1
    elif message["Dia_semana"] == 2:
        weekday_encoded["Dia_2"] = 1
    elif message["Dia_semana"] == 3:
        weekday_encoded["Dia_3"] = 1
    elif message["Dia_semana"] == 4:
        weekday_encoded["Dia_4"] = 1   
    elif message["Dia_semana"] == 5:
        weekday_encoded["Dia_5"] = 1
    elif message["Dia_semana"] == 6:
        weekday_encoded["Dia_6"] = 1   
    del message["Dia_semana"]

    return message.update(weekday_encoded)


def month_encoding(message):
    month_encoded = {"Mes_1": 0, "Mes_2": 0, "Mes_3": 0, "Mes_4": 0, "Mes_5": 0, "Mes_6" : 0, "Mes_7": 0, "Mes_8": 0, "Mes_9": 0, "Mes_10": 0, "Mes_11":0 ,"Mes_10": 0, "Mes_11": 0, "Mes_12": 0}
    message["fecha"] = pd.to_datetime(message["fecha"]) 
    message["Mes"] = message["fecha"].month 
    if message["Mes"] == 1:
        month_encoded["Mes_1"] = 1
    elif message["Mes"] == 2:
        month_encoded["Mes_2"] = 1
    elif message["Mes"] == 3:
        month_encoded["Mes_3"] = 1
    elif message["Mes"] == 4:
        month_encoded["Mes_4"] = 1   
    elif message["Mes"] == 5:
        month_encoded["Mes_5"] = 1
    elif message["Mes"] == 6:
        month_encoded["Mes_6"] = 1
    elif message["Mes"] == 7:
        month_encoded["Mes_7"] = 1 
    elif message["Mes"] == 8:
        month_encoded["Mes_8"] = 1 
    elif message["Mes"] == 9:
        month_encoded["Mes_9"] = 1
    elif message["Mes"] == 10:
        month_encoded["Mes_10"] = 1
    elif message["Mes"] == 11:
        month_encoded["Mes_11"] = 1
    elif message["Mes"] == 12:
        month_encoded["Mes_12"] = 1 
    del message["Mes"]

    return message.update(month_encoded)

def season_encoding(message): 
    season_encoded = {"Estacion_1":0, "Estacion_2": 0, "Estacion_3": 0, "Estacion_4": 0}
    message["fecha"] = pd.to_datetime(message["fecha"]) 
    message["Estacion"] = message["fecha"].quarter 
    if message["Estacion"] == 1:
        season_encoded["Estacion_1"] == 1
    elif message ["Estacion"] == 2:
        season_encoded["Estacion_2"] == 1
    elif message ["Estacion"] == 3:
        season_encoded["Estacion_3"] == 1
    elif message ["Estacion"] == 4:
        season_encoded["Estacion_4"] == 1
    del message["Estacion"]

    return message.update(season_encoded)

 
def data_prep(message):
    weekday_encoding(message)
    month_encoding(message)
    season_encoding(message)
    del message["fecha"]
    return pd.DataFrame(message, index=[0])




def air_quality_prediction(message: dict):
    # Data Prep
    data = data_prep(message)
    label = model.predict(data)[0]
    return {"label": int(label)}

@app.get("/")
def main():
    return {"message": "Hola"}

@app.post("/air-quality-prediction/")
def predict_airq(message: dict):
    model_pred = air_quality_prediction(message)
    # return {"prediction": model_pred}
    return model_pred

