"""
    Visualizing diets over the course of time
"""
from functools import reduce
import random
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Attach our dataframe to our app
DF_PATH = '/Users/samuelfolledo/Library/Mobile Documents/com~apple~CloudDocs/Desktop/MakeSchool/Term3-2/DS2.3 - Data Science in Production/HW 1 - Chartist and Flask/all_stocks_5yr.csv'
app.df = pd.read_csv(DF_PATH, skiprows=1)
app.df.columns = ["date", "open", "high", "low", "close", "volume", "Name"]

class Stock():
    def __init__(self, name, hex_color):
        self.name = name
        self.hex_color = hex_color

# MARK: - Home
@app.route("/", methods=["GET"])
def get_root():
    """
        Root route that returns the index page
    """
    stocks_list = ['AAL', 'AAPL', 'AAP', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'ADS', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALLE', 'ALL', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMGN', 'AMG', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'APTV', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'A', 'BAC', 'BAX', 'BA', 'BBT', 'BBY', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'CAG', 'CAH', 'CAT', 'CA', 'CBG', 'CBOE', 'CBS', 'CB', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CFG', 'CF', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CINF', 'CI', 'CLX', 'CL', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'C', 'DAL', 'DE', 'DFS', 'DGX', 'DG', 'DHI', 'DHR', 'DISCA', 'DISCK', 'DISH', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'D', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ESRX', 'ESS', 'ES', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'FAST', 'FBHS', 'FB', 'FCX', 'FDX', 'FE', 'FFIV', 'FISV', 'FIS', 'FITB', 'FLIR', 'FLR', 'FLS', 'FL', 'FMC', 'FOXA', 'FOX', 'FRT', 'FTI', 'FTV', 'F', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOGL', 'GOOG', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX', 'HON', 'HPE', 'HPQ', 'HP', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IPG', 'IP', 'IQV', 'IRM', 'IR', 'ISRG', 'ITW', 'IT', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KORS', 'KO', 'KR', 'KSS', 'KSU', 'K', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LYB', 'L', 'MAA', 'MAC', 'MAR', 'MAS', 'MAT', 'MA', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MON', 'MOS', 'MO', 'MPC', 'MRK', 'MRO', 'MSFT', 'MSI', 'MS', 'MTB', 'MTD', 'MU', 'MYL', 'M', 'NAVI', 'NBL', 'NCLH', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'NWS', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'O', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PGR', 'PG', 'PHM', 'PH', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PXD', 'PX', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'REGN', 'REG', 'RE', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPGI', 'SPG', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWKS', 'SWK', 'SYF', 'SYK', 'SYMC', 'SYY', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TPR', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'T', 'UAA', 'UAL', 'UA', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'V', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WMB', 'WMT', 'WM', 'WRK', 'WU', 'WYNN', 'WYN', 'WY', 'XEC', 'XEL', 'XLNX', 'XL', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    stocks = []
    for stock_name in stocks_list:
        # generate random hex color each stock
        hex_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        # append Stock
        stock = Stock(stock_name, hex_color)
        stocks.append(stock)
    return render_template("index.html", stocks=stocks), 200


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

    print("Query results\nWANTED STOCKS=", wanted_stocks,"\nYEARS=",ls_year)
    stocks_list = app.df["Name"].unique() #list of unique stocks in Name column
    # print("All stocks:", stocks_list)
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
