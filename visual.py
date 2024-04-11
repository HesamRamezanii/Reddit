import praw
import datetime
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
#import sctap



conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()


main_query = """CREATE TABLE IF NOT EXISTS Reddit (INdex int , Subreddit text, Sitle text ,
 Id text , Author text , Score int , Name text , Comments_number , Subscribers , Time text)"""


query1 ="""SELECT subreddit, title, author, score,
  CASE
    WHEN score BETWEEN 15000 AND 20000 THEN 'Perfect'
    WHEN score BETWEEN 10000 AND 15000 THEN 'Good'
    WHEN score BETWEEN 5000 AND 10000 THEN 'Not Bad'
    WHEN score BETWEEN 1000 AND 5000 THEN 'Bad'
    ELSE 'Out of the Way'
  END AS "interest"
FROM "Reddit"
WHERE score > (SELECT AVG(score) AS AverageScore FROM "Reddit")
ORDER BY score;"""


query2 = """SELECT author, title, time,
  CASE
    WHEN strftime('%H', datetime(time)) BETWEEN '00' AND '08' THEN 'morning'
    WHEN strftime('%H', datetime(time)) BETWEEN '08' AND '16' THEN 'afternoon'
    WHEN strftime('%H', datetime(time)) BETWEEN '16' AND '24' THEN 'night'
    ELSE NULL
  END as "GoldenTime"
FROM "Reddit";"""


status = [0 , 0 , 0 , 0 , 0]
status1 = [0 , 0 , 0]

def CreateAndConvert():
    cursor.execute(main_query)
    conn.commit()

    #sctap.df.to_sql("Reddit" , conn , if_exists="replace" , index=False)


def read():
    cursor.execute('SELECT * FROM "Reddit";')
    for row in cursor.fetchall():
        print(row)
    

def Extract(Query):
    cursor.execute(Query)
    for row in cursor.fetchall():
        print(row)
        print("-----------------------------------")



def Score_Status():
    cursor.execute(query1)
    for row in cursor.fetchall():
        if row[4] == "Out of the Way":
            status[0] = status[0] + 1
        elif row[4] == "Bad":
            status[1] = status[1] + 1
        elif row[4] == "Not Bad":
            status[2] = status[2] + 1
        elif row[4] == "Good":
            status[3] = status[3] + 1
        elif row[4] == "Perfect":
            status[4] = status[4] + 1
        
    print(status)
        

def ScorePlot():
    left = [1 , 2 , 3 , 4 , 5]
    height = status
    label = ["Under 1000" , "1000\nTo 5000" , "5000\nTo 10000" , "10000\nTo 15000" , "15000\nT0 20000"]
    
    plt.bar(left, height, tick_label = label,   
        width = 0.8, color = ['red', 'gold', 'orange' ,'green' ,'cyan'])

    plt.xlabel('Status') 
    plt.ylabel('Number')
    plt.title('ScoresNumber')

    plt.show()


def PostTime():
    cursor.execute(query2)
    for row in cursor.fetchall():
        if row[3] == "morning":
            status1[0] = status1[0] + 1
        elif row[3] == "afternoon":
            status1[1] = status1[1] + 1
        elif row[3] == "night":
            status1[2] = status1[2] + 1
    print(status1)


def TimePlot():
    left = [1 , 2 , 3]
    height = status1
    label = ["Morning" , "Afternoon" , "Night"]
    
    plt.bar(left, height, tick_label = label,   
        width = 0.8, color = ['cyan' , 'orange' , 'black'])

    plt.xlabel('Time of Day') 
    plt.ylabel('Number')
    plt.title('Time')

    plt.show()

read()
PostTime()
TimePlot()