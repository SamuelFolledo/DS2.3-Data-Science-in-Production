"""
    Visualizing diets over the course of time
"""
from functools import reduce

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Attach our dataframe to our app
app.df = pd.read_csv("all_stocks_5yr.csv", skiprows=1)
# app.df.columns = ["date", "close", "Name"]


@app.route("/", methods=["GET"])
def get_root():
    """
        Root route that returns the index page
    """
    return render_template("index.html"), 200


@app.route("/time_series", methods=["GET"])
def get_time_series_data():
    """
        Return the necessary data to create a time series
    """
    # Grab the requested years and columns from the query arguments
    ls_year = [int(year) for year in request.args.getlist("n")]
    ls_col = request.args.getlist("m")

    df_columns = ["date", "close", "Name"]

    # Generate a list of all the months we need to get
    all_years = [str(year) for year in range(min(ls_year), max(ls_year) + 1)]

    # Grab all of the wanted dates by filtering for the ones we want
    wanted_months = reduce(
        lambda a, b: a | b, (app.df["date"].str.contains(year) for year in all_years)
    )

    #get wanted days

    print("LS COL:", ls_col)
    # Create a new dataframe from the one that
    # df_new = app.df[wanted_months][["date"] + ls_col]
    df_new = app.df[wanted_months][["date"] + ["close"]]

    print("NEW DF with + ", df_new.to_json())

    # Convert all string dates into datetime objects and then sort them
    df_new["date"] = pd.to_datetime(df_new["date"])
    df_new = df_new.sort_values(by=["date"])

    df_new = df_new[df_columns] #select right columns

    #now select the right rows
    df_new = df_new[df_columns["Name"] == "AAPL"]
    print("New DF:", df_new)
    # Return the dataframe as json
    return df_new.to_json(), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)
