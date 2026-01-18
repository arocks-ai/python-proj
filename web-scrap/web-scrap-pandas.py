import requests
import pandas as pd
import numpy as np


'''
    pip install requests lxml  pandas numpy

    Tasks
    1.Use Webscraping to extract required information from a website.
    2.Use Pandas to load and process the tabular data as a dataframe.
    3.Use Numpy to manipulate the information contatined in the dataframe.
    4.Load the updated dataframe to CSV file.
'''


#  1.Use Webscraping to extract required information from a website.

# URL - Countries by GDP (nominal)
url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Add browser-like headers (IMPORTANT)
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#
# Fetch Table for coutries by GDP (Millions of USD) numbers
#
response = requests.get(url, headers=headers)
response.raise_for_status()  # will raise error if request fails

tables = pd.read_html(response.text)
#tables = pd.read_html(url)
df = tables[2]



#
# 2. Print top 10 countries by thier GDP, list Country name and GDP value in Millions
#

# Replace the column headers with column numbers, like 0,1,2,3 etc..
# df.shape[1] gives number of columns
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df.loc[1:,[0,2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.loc[1:10,[0,2]]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ["Country", "GDP (Million USD)"]
#print(df)


#
# 3.Convert GDP value from Millions to Billions (updated column name also)
#


# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'}, inplace=True)
print(df)


# 4. Load the updated dataframe to CSV file.
# index=False to avoid writing row index numbers to the CSV file.
df.to_csv("./largest_economies.csv", index=False)