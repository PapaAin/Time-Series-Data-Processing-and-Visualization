#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def commute():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df = df.dropna(axis=0,how='all').dropna(axis=1,how='all')
 
    days = pd.Series({"ma":1,"ti":2,"ke":3,"to":4,"pe":5,"la":6,"su":7})
    month =pd.Series({"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,"syys":9,"loka":10,"marras":11,"joulu":12})
 
    dr = df["Päivämäärä"].str.split(expand=True)
    dr.columns = ["Weekday","Day","Month","Year","Hour"]
 
    dr["Weekday"] = dr["Weekday"].map(days)
    dr["Month"] = dr["Month"].map(month)
    df2 = dr["Hour"].str.split(":",expand=True)
    dr["Hour"] = df2.loc[:,0]
 
    dr = dr.astype({"Weekday":int,"Day":int,"Month":int,"Year":int,"Hour":int})
    df = df.drop(columns=["Päivämäärä"])
    df = pd.concat([dr,df],axis=1)

    df["Date"] = pd.to_datetime(df[["Year","Month","Day","Hour"]])
    df = df.drop(columns=["Year","Month","Day","Hour"])
    df = df.set_index("Date")
    df = df["2017-08-01 00:00:00":"2017-08-31 23:00:00"]

    ds = df.groupby(["Weekday"]).sum()
    return ds
    
def main():
    df = commute()
    plt.plot(df)
    plt.show()

if __name__ == "__main__":
    main()
