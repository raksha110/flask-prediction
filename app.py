from flask import Flask
from flask import Flask, request, make_response, jsonify
import pandas as pd
import requests
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import math
import numpy as np
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor

app = Flask(__name__)
df_final = pd.DataFrame()
@app.route("/", methods=['POST', 'GET'])
def hello():
	return "Hello, Welcome to agro basket prediction api!"


@app.route("/predictLinearModel", methods=['POST'])
def predictLinearModel():
	data = pd.read_csv("Final.csv")
	df=data[['Crop', 'State','District', 'Soil' ,'Season', 'SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']].copy()
	save_crop=df["Crop"].unique()
	crop_dict={}
	count=1
	for i in save_crop:
		crop_dict[count]=i
		count=count+1
	save_season=df["Season"].unique()
	season_dict={}
	count=1
	for i in save_season:
	  season_dict[i]=count
	  count=count+1

	save_soil=df["Soil"].unique()
	soil_dict={}
	count=1
	for i in save_soil:
	  soil_dict[i]=count
	  count=count+1
	save_SowingMonth={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
	for i,y in crop_dict.items():
	  df['Crop'] = df['Crop'].replace(y,i)
	for i,y in season_dict.items():
	  df['Season'] = df['Season'].replace([i],y)
	for i,y in save_SowingMonth.items():
	  df['SowingMonth'] = df['SowingMonth'].replace([i],y)
	for i,y in soil_dict.items():
	  df['Soil'] = df['Soil'].replace([i],y)

	df_final=df[['Crop', 'Soil' ,'Season', 'SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']].copy()
	soil = request.json['soil']
	season = request.json['season']
	month = request.json['month']
	mintemp = request.json['mintemp']
	maxtemp = request.json['maxtemp']
	soilPhMin = request.json['soilPhMin']
	soilPhMax = request.json['soilPhMax']
	minRainfall = request.json['minRainfall']
	maxRainfall = request.json['maxRainfall']
	
	soilS = str(soil_dict.get(soil))
	seasonS = str(season_dict.get(season))
	monthS = str(save_SowingMonth.get(month))
	if soilS == "None" or seasonS == "None" or monthS == "None":
		return "Error in passing data" + soilS + seasonS + monthS
	soilI = int(soilS)
	seasonI = int(seasonS)
	monthI = int(monthS)
	mintempI = int(mintemp)
	maxtempI = int(maxtemp)
	minsoilphI = float(soilPhMin)
	maxsoilphI = float(soilPhMax)
	minrainI = int(minRainfall)
	maxrainI = int(maxRainfall)
	y= df_final['Crop']
	X = df_final[['Season', 'Soil','SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']]
	model = linear_model.LinearRegression()
	model.fit(X, y)
	row = [soilI ,seasonI ,monthI ,mintempI,maxtempI,minsoilphI,maxsoilphI,minrainI ,maxrainI]
	yhat = model.predict([row])
	cp = str((crop_dict.get(round(yhat[0]))))
	return cp

@app.route("/predictKNeighborsRegressor", methods=['POST'])
def predictKNeighborsRegressor():
	data = pd.read_csv("Final.csv")
	df=data[['Crop', 'State','District', 'Soil' ,'Season', 'SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']].copy()
	save_crop=df["Crop"].unique()
	crop_dict={}
	count=1
	for i in save_crop:
		crop_dict[count]=i
		count=count+1
	save_season=df["Season"].unique()
	season_dict={}
	count=1
	for i in save_season:
	  season_dict[i]=count
	  count=count+1

	save_soil=df["Soil"].unique()
	soil_dict={}
	count=1
	for i in save_soil:
	  soil_dict[i]=count
	  count=count+1
	save_SowingMonth={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
	for i,y in crop_dict.items():
	  df['Crop'] = df['Crop'].replace(y,i)
	for i,y in season_dict.items():
	  df['Season'] = df['Season'].replace([i],y)
	for i,y in save_SowingMonth.items():
	  df['SowingMonth'] = df['SowingMonth'].replace([i],y)
	for i,y in soil_dict.items():
	  df['Soil'] = df['Soil'].replace([i],y)

	df_final=df[['Crop', 'Soil' ,'Season', 'SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']].copy()
	soil = request.json['soil']
	season = request.json['season']
	month = request.json['month']
	mintemp = request.json['mintemp']
	maxtemp = request.json['maxtemp']
	soilPhMin = request.json['soilPhMin']
	soilPhMax = request.json['soilPhMax']
	minRainfall = request.json['minRainfall']
	maxRainfall = request.json['maxRainfall']
	
	soilS = str(soil_dict.get(soil))
	seasonS = str(season_dict.get(season))
	monthS = str(save_SowingMonth.get(month))
	if soilS == "None" or seasonS == "None" or monthS == "None":
		return "Error in passing data" + soilS + seasonS + monthS
	soilI = int(soilS)
	seasonI = int(seasonS)
	monthI = int(monthS)
	mintempI = int(mintemp)
	maxtempI = int(maxtemp)
	minsoilphI = float(soilPhMin)
	maxsoilphI = float(soilPhMax)
	minrainI = int(minRainfall)
	maxrainI = int(maxRainfall)
	y= df_final['Crop']
	X = df_final[['Season', 'Soil','SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']]
	modelK = KNeighborsRegressor()
	modelK.fit(X, y)
	row = [soilI ,seasonI ,monthI ,mintempI,maxtempI,minsoilphI,maxsoilphI,minrainI ,maxrainI]
	yhat = modelK.predict([row])
	cp = str((crop_dict.get(round(yhat[0]))))
	return cp


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)