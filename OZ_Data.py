
import pandas as pd
import datetime
import pyasx
from datetime import datetime
import pandas_datareader as web
import pyasx.data.companies
import pyasx.data.securities
from pandas.io.json import json_normalize
import json

start = datetime(2015, 1 , 1)

end  = datetime(2019, 2 ,13)


#function to get stock data for a ticker from morningstar API, this is general
def get_stock_data(ticker):
    try:
        df = web.DataReader('%s' % (ticker), 'morningstar', start, end)
    except ValueError:
        print('Ticker Symbol %s is not available!' % (ticker))

#for commodities we are going to query quandl
def get_commodity_data(ticker):
    try:
        data = quandle.get()
        print(data)
    except:
        None


#function to get selected macroeconomic indicators from the World bank Wesbote
def get_macro_data(indicator, country):
    try:
        data = wb.search()
        hir_df = wb.download()
    except ValueError:
        print("Indicator")

#ASX data
def get_ASX_company_data(ticker):
    try:
        json_response = pyasx.data.companies.get_company_info(ticker)
        df = pd.read_json(json_response)
        print(df)
    except:
        None

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def get_ASX_security_data(ticker):
    json_response = pyasx.data.securities.get_security_info(ticker)
    print(json_response)
    jdata = json.dumps(json_response, default = myconverter)
    df = pd.read_json(jdata)
    print(df)
    return df



def get_ASX_listed_security():
    try:
        json_response = pyasx.data.securities.get_listed_securities()
        print(json_response)
        json_response = json.dumps(json_response)
        df_security_information = pd.read_json(json_response, orient='columns')
        print(df_security_information)
        return df_security_information
    except ValueError:
        print("unable to gain list of all securities on ASX")

#this function sorts and splits the list of securities into all the different types of securties, returns a series for each security clas
def security_list_classifier():
    df_ASX_listed_companies = get_ASX_listed_security()
    print(df_ASX_listed_companies)
    df_ASX_listed_companies.sort_values(by='type')
    print(df_ASX_listed_companies)


#we want to make some of the columns the index i think



def get_ASX_listed_companies():
    results = pyasx.data.companies.get_listed_companies()
    results = json.dumps(results)
    df_ASX_listed_companies = pd.read_json(results, orient = 'columns')
    return df_ASX_listed_companies

class ASX(object):

    def __init__(self):
        self.companies = ASX.companies()
        self.industry = ASX.industry(input)
        self.industry_list = ASX.industry_list()
    def companies():
        try:
            df = get_ASX_listed_companies()
            companies = list(df['ticker'])
            print(companies)
            return companies
        except ValueError:
            print('error')

    def industry_list():
        try:
            df = get_ASX_listed_companies()
            industries = df['gics_industry'].unique().tolist()
            return industries
        except ValueError:
            print('error')

    def industry():
        i = 0
        industry_list = ASX.industry_list()
        for i in industry_list:
            if i < len(industry_list)
            df = get_ASX_listed_companies()
            industry = df.loc[df['gics_industry'] == '%s' % (i)]
            print(industry)
            i += 1
            return industry






#this function describes ...

def get_ASX_listed_companies_alternative():
    results = pyasx.data.companies.get_listed_companies()
    results = json.dumps(results)
    df = pd.io.json.json_normalize(results)
    print(df)
    return df




if __name__ == '__main__':
    ASX.industry()