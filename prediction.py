from sklearn.datasets import make_regression
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import math    
import pandas as pd 
import numpy as np
import sys
data = pd.read_csv("Final.csv")
#print(data) 
df=data[['Crop', 'State','District', 'Soil' ,'Season', 'SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']].copy()

save_crop=df["Crop"].unique()
crop_dict={}
count=1
for i in save_crop:
  crop_dict[count]=i
  count=count+1

#print(crop_dict)


#when hosted on cloudremovestate and district
save_state=df["State"].unique()
state_dict={}
count=1
for i in save_state:
  state_dict[i]=count
  count=count+1

#print(save_state)

save_dis=df["District"].unique()
dis_dict={}
count=1
for i in save_dis:
  dis_dict[i]=count
  count=count+1

#print(save_dis)

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

#print(save_season)

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

print(df_final)

for i,y in soil_dict.items():
  print(str(y) + " - " + i) 
soil = input("Enter the soil number : ")

for i,y in season_dict.items():
  print(str(y) + " - " + i) 
season = input("Enter the Season number : ")

for i,y in save_SowingMonth.items():
  print(str(y) + " - " + i) 
month = input("Enter the Sowing month number : ")

mintemp = input("Enter the min temp value : ")
maxtemp = input("Enter the max temp value : ")
minsoilph = input("Enter the min soil ph value: ")
maxsoilph = input("Enter the max soil ph value : ")
minrain = input("Enter the min rain value : ")
maxrain = input("Enter the max rain value : ")

soilI = int(soil)
seasonI = int(season)
monthI = int(month)
mintempI = int(mintemp)
maxtempI = int(maxtemp)
minsoilphI = float(minsoilph)
maxsoilphI = float(maxsoilph)
minrainI = int(minrain)
maxrainI = int(maxrain)

execute = False

if soilI >= 1 and soilI <= 12:
  if(seasonI >= 1 and seasonI <= 6):
    if(monthI >= 1 and monthI <= 12):
      if mintempI >= 19:
        if maxtempI <= 49:
          if minsoilphI >= 4.5:
            if maxsoilphI <= 8:
              if minrainI >= 250:
                if maxrainI <= 3000:
                  execute = True

# Preview the first 5 lines of the loaded data 
#print(data.shape)
 
if execute:
  y= df_final['Crop']
  X = df_final[['Season', 'Soil','SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']]
  print(X.shape)
  print(y.shape)
  # define model
  model = linear_model.LinearRegression()
  # fit model
  model.fit(X, y)
  # make a prediction
  row = [soilI ,seasonI ,monthI ,mintempI,maxtempI,minsoilphI,maxsoilphI,minrainI ,maxrainI]
  yhat = model.predict([row])
  # summarize prediction
  print(math.round(yhat))
  print(crop_dict.get(math.round(yhat)))
  print(model.score(X,y))
else:
  print("Problem in input format")

from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
# create datasets
if execute:
  y= df_final['Crop']
  X = df_final[['Season', 'Soil','SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']]
  # define model
  modelK = KNeighborsRegressor()
  # fit model
  modelK.fit(X, y)
  # make a prediction
  row = [soilI ,seasonI ,monthI ,mintempI,maxtempI,minsoilphI,maxsoilphI,minrainI ,maxrainI]
  yhat = modelK.predict([row])
  # summarize prediction
  print(yhat)
  print(math.round(yhat))
  print(crop_dict.get(math.round(yhat)))
  print(modelK.score(X,y))
else:
  print("Problem in input format")

# decision tree for multioutput regression
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
# create datasets
if execute:
  y= df_final['Crop']
  X = df_final[['Season', 'Soil','SowingMonth','MinTemp','MaxTemp','SoilPHMin','SoilPHMax','MinRainfall','MaxRainfall']]
  # define model
  modelD = DecisionTreeRegressor()
  # fit model
  modelD.fit(X, y)
  # make a prediction
  row = [soilI ,seasonI ,monthI ,mintempI,maxtempI,minsoilphI,maxsoilphI,minrainI ,maxrainI]
  yhat = modelD.predict([row])
  # summarize prediction
  print(yhat)
  print(math.round(yhat))
  print(crop_dict.get(math.round(yhat)))
  print(modelD.score(X,y))
else:
  print("Problem in input format")