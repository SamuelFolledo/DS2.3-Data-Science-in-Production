"""
    Visualizing diets over the course of time
"""
from functools import reduce

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Attach our dataframe to our app
DF_PATH = '/Users/samuelfolledo/Library/Mobile Documents/com~apple~CloudDocs/Desktop/MakeSchool/Term3-2/DS2.3 - Data Science in Production/HW 1 - Chartist and Flask/all_stocks_5yr.csv'
app.df = pd.read_csv(DF_PATH, skiprows=1)
app.df.columns = ["date", "open", "high", "low", "close", "volume", "Name"]

@app.route("/", methods=["GET"])
def get_root():
    """
        Root route that returns the index page
    """
    return render_template("index.html"), 200


def format_df_for_chartist(df, stock_name):
    """
        Format df with columns of date, close, and by
        1. Getting (locating) df's rows with column "Name" == stock_name
        2. Renaming "close" column with stock_name
        3. Dropping Name column
    """
    filtered_df = df.loc[df['Name'] == stock_name] #1
    filtered_df = filtered_df.rename(columns={'close': stock_name}) #2
    filtered_df.drop(['Name'], axis=1, inplace=True) #3
    return filtered_df



@app.route("/time_series", methods=["GET"])
def get_time_series_data():
    """
        Return the necessary data to create a time series
    """
    # Grab the requested years and columns from the query arguments
    ls_year = [int(year) for year in request.args.getlist("n")]
    wanted_stocks = request.args.getlist("m")
    new_wanted_stocks = []
    for stock in wanted_stocks:
        new_wanted_stocks.append(stock.upper())
    wanted_stocks = new_wanted_stocks

    print("Query results\n", wanted_stocks,"\n\n",ls_year)
    stocks_list = app.df["Name"].unique() #list of unique stocks in Name column
    # wanted_stocks = ["AAL", "AAPL", "AMZN"]

    # ls_year = [2013, 2015]
    all_years = [str(year) for year in range(min(ls_year), max(ls_year) + 1)] # get all years from the min and max range
    # print(df.columns)

    # Grab all of the wanted months by filtering for the ones we want
    wanted_months = reduce(
        lambda a, b: a | b, (app.df["date"].str.contains(year) for year in all_years)
    )

    # Copy df and only get the wanted months
    df_new = app.df[wanted_months]

    # drop columns we dont need
    df_new.drop(['open', 'high', 'low', 'volume'], axis=1, inplace=True)

    # get the rows of stocks we want
    first_stock_name = wanted_stocks[0]
    # print("DF-NEW", df_new)

    # Make the first wanted stock the default value
    filtered_df = format_df_for_chartist(df_new, first_stock_name)

    # Loop through the rest of the wanted stocks and append it filtered_df
    for i in range(1, len(wanted_stocks)):
        stock_name = wanted_stocks[i]
        # get the df for the current stock
        wanted_stock_df = format_df_for_chartist(df_new, stock_name)
        # print("wanted stock df\n", wanted_stock_df)
        # merge df to filtered_df by their date values
        filtered_df = pd.merge(filtered_df, wanted_stock_df, on='date')

    print("Filtered Df=\n", filtered_df)

    # Return the dataframe as json
    return filtered_df.to_json(), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)
