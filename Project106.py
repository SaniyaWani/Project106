import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
   Rollno=[]
   PD =[]
   with open(data_path) as csv_file:
       csv_reader = csv.DictReader(csv_file)
       for row in csv_reader:
           Rollno.append(float(row["Roll No"]))
           PD.append(float(row["Days Present"]))           

   return {"x": Rollno, "y":PD }       

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print ("correlation" , correlation[0,1])

def setup():
    data_path = "Project106.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup() 