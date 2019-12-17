import pandas as pd
import time
df = pd.read_csv('/Volumes/GoogleDrive/My Drive/Researcher_KyotoU/walkInKyotoGPS_201809-201902/DataOutput/DataOutput/android_1810.csv')
d=[]
for i in range(len(df)):
    temp = df['pos'][i][1:-1].split(',')
    d.append([temp[0],temp[1]])
d_df = pd.DataFrame(d, columns = ['latitude' , 'longitude'])
result = pd.concat([df, d_df], axis=1, sort=False)
result = result.drop(columns=['Unnamed: 0','aid','cd3','cd4','cd5','cd6','cd7','cd8','cd9','cd10'])

result.to_csv('/Volumes/GoogleDrive/My Drive/Researcher_KyotoU/walkInKyotoGPS_201809-201902/DataOutput/DataOutput/byDay/kyotoData/dataPlot_1810.csv', index = None, header=True)
print("complete")
