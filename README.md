[Go to Back to Home Page](https://ukthanki.github.io/)

# MIT Data Engineering Professional Certification

## Transit Data Application Project
[Go to Repo](https://github.com/ukthanki/MIT_Transit_Data_Application)

<p align="center">
    <img width="100%" src="https://github.com/ukthanki/MIT_Transit_Data_Application_Project/assets/42117481/a2e27cb7-dc4d-4f2e-82cc-fdbcff125596">
</p>

Up to this point in the course, we had learned the following topics:
1. NumPy
2. Pandas
3. SQL
4. Linear Regression
5. ETL Fundamentals
6. Flask
7. Java
8. CDC Fundamentals
9. Docker
10. Maven

In this project, we used the various skills we have learned to build a transit application that shows the position of buses along Route 1 for the Massachusetts Bay Transportation Authority (MBTA). The project was presented to us in a way that a majority of the base code was already provided to us and we had to fill in various sections with code.

You can learn more about the MBTA [here](https://www.mbta.com/).

This project was split up into two main parts. The first part involved setting up the infrastructure, completing the code, and collecting 12 hours of transit data. This was followed by analyzing the data in a Jupyter Notebook.

We began the project by creating a Docker network for all of our containers. The first container we made was a MySQL server that would store data returned by the MBTA API. We also made a MongoDB container for CDC. As we followed the steps in the procedure provided to us, we opened the web application on localhost:3000 and saw our functioning transit application, as shown in Figure 1 below:

| ![download](https://github.com/ukthanki/MIT_Transit_Data_Application_Project/assets/42117481/aea78afa-991c-4210-bb8d-fea7adbe2f51)| 
|:--:| 
| **Figure 1.** Transit Application Landing Page. |

At this point, we created a Debezium container and let the server.py file run for approximately 12 hours to collect enough data for analysis.

Once sufficient data was collected, we pivoted to the Jupyter Notebook to conduct analysis. We used the pymysql library and the following code to read the data from the MySQL database and store it in a Pandas Data Frame:

```python
import os
import pymysql
import pandas as pd
from datetime import datetime

host = '127.0.0.1'
port = '3306'
user = 'root'
password = 'MyNewPass'
database = 'MBTAdb'

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db=database,
    charset='utf8mb4')

df = pd.read_sql_query("SELECT * FROM mbta_buses",
    conn)

df.tail(10)

```

The Data Frame produced the output shown below in Figure 2:

| ![download](https://github.com/ukthanki/MIT_Transit_Data_Application_Project/assets/42117481/cb9d6ec5-5671-40a2-9670-1b0d0d5b7fea)| 
|:--:| 
| **Figure 2.** Data Frame output of the collected transit data. |

Once our data was loaded into a Data Frame, we could answer questions such as 1) What is the average time it takes for certain buses to complete Route 1? and 2) What is an estimate of the speed of a bus from current_stop_sequence = 1 to the last current_stop_sequence?

The answer to the first question is shown in a bar chart below in Figure 3:

| ![download](https://github.com/ukthanki/MIT_Transit_Data_Application_Project/assets/42117481/6702d4ac-3f0f-448e-b865-b5a5c0f5bb81)| 
|:--:| 
| **Figure 3.** Average time to complete Route 1. |

Furthermore, we answered the second question with an estimate of 4.15 mph using the following code:

```python
from haversine import haversine, Unit

def getEstimatedSpeed(df, bus_id):    
    test = timings(df, bus_id)

    first = getMinStopNumber(df, bus_id)
    last = getMaxStopNumber(df, bus_id)

    fsindexlist = getIndices(test, first)
    lsindexlist = getIndices(test, last)
    
    start_end_df = test.loc[combinedIndexList(fsindexlist,lsindexlist)]
    
    first_stop_latlon = (start_end_df.iloc[0]['latitude'], start_end_df.iloc[0]['longitude'])
    last_stop_latlon = (start_end_df.iloc[1]['latitude'], start_end_df.iloc[0]['longitude'])
    
    distance = haversine(first_stop_latlon, last_stop_latlon, unit='mi')
    time = avgTimeInMin(getTripTimes(df, bus_id))
    return round(distance/(time/60),2)

print(f'The estimated speed for Bus y1895 to complete Route 1 is {getEstimatedSpeed(df, "y1895")} mph.')

```

This project was interesting because it leveraged APIs and Docker containers, and also allowed us to create a visually pleasing web application. This project was also realistic in nature and allowed us to analyze real-world data and gain insights from it.

**You can view the full Project in the various files in the Repository.**
