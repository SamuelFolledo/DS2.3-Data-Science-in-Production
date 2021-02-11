import pandas as pd
from functools import reduce


def read_stocks_csv():
    df = pd.read_csv (r'/Users/samuelfolledo/Library/Mobile Documents/com~apple~CloudDocs/Desktop/MakeSchool/Term3-2/DS2.3 - Data Science in Production/HW 1 - Chartist and Flask/all_stocks_5yr.csv')
    return df

df = read_stocks_csv()
stocks_list = df["Name"].unique() #list of unique stocks in Name column
wanted_stocks = ["AAL", "AAPL", "AMZN"]

ls_year = [2013, 2013]
all_years = [str(year) for year in range(min(ls_year), max(ls_year) + 1)] # get all years from the min and max range
# print(df.columns)

# Grab all of the wanted months by filtering for the ones we want
wanted_months = reduce(
    lambda a, b: a | b, (df["date"].str.contains(year) for year in all_years)
)

# Copy df and only get the wanted months
df_new = df[wanted_months]

# Get unwanted stocks
unwanted_stocks = []
for stock in stocks_list:
    if stock not in wanted_stocks:
        unwanted_stocks.append(stock)

# drop columns we dont need
df_new.drop(['open', 'high', 'low', 'volume'], axis=1, inplace=True)

# get the rows of stocks we want
first_stock_name = wanted_stocks[0]
filtered_df = df_new.loc[df_new['Name'] == first_stock_name]
filtered_df = filtered_df.rename(columns={'close': first_stock_name})
filtered_df.drop(['Name'], axis=1, inplace=True)

for i in range(1, len(wanted_stocks)):
    wanted_stock_name = wanted_stocks[i]
    wanted_stock_df = df_new.loc[df_new['Name'] == wanted_stock_name]
    wanted_stock_df = wanted_stock_df.rename(columns={'close': wanted_stock_name})
    wanted_stock_df.drop(['Name'], axis=1, inplace=True)
    # filtered_df = pd.concat([filtered_df, wanted_stock_df])
    filtered_df = pd.merge(filtered_df, wanted_stock_df, on='date')

print("DF NEW =\n", filtered_df)


# 1. Store each column as a list
# 2. use python's zip function to "zip" two columns you're interested in together into a dictionary
# 3. Loop through each item in the dictionary and append the year from the df