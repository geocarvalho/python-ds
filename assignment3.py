import pandas as pd
import numpy as np

def ans_one():
    """
    After instructions to merge all data, This function should return a DataFrame with 20 columns and 15 entries.
    """

    #Starting with energy data, exclude the header and footer
    energy = pd.read_excel("./data/Energy_Indicators.xls", skiprows=18, skip_footer=38, header=None)
    # Exclude the two first columns
    energy.drop([0, 1], axis=1, inplace=True)
    # Make your header
    energy_col = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = energy_col
    # Treat your missing values
    energy.replace("...", np.NaN, inplace=True)
    # Convert "Energy Supply" to gigajoules
    energy["Energy Supply"] = energy["Energy Supply"].apply(lambda x: x*1000000)
    # Replace the numbers in countries names
    energy["Country"] = energy["Country"].replace(to_replace=["0","1","2","3","4","5","6","7","8","9"], value="", regex=True)
    # Cleaning data
    energy["Country"].replace(to_replace={
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Republic of Korea": "South Korea",
    "China, Hong Kong Special Administrative Region": "Hong Kong"
    }, inplace=True)
    # Cleaning strings with "()"
    energy["Country"] = energy["Country"][energy["Country"].notnull()].apply(
    lambda x: x.split(" (")[0] if x.endswith(")") else x)

    # Now, GDP data, skip the header
    GDP = pd.read_csv("./data-bank/world_bank.csv", skiprows=4)
    # Cleaning data
    GDP["Country Name"].replace(to_replace={
    "Korea, Rep.": "South Korea",
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"
    }, inplace=True)
    # Using the last 10 years of data
    GDP_use = pd.concat([GDP.ix[:, 0], GDP.ix[:, -12:-2]], axis=1)
    # Change the column name for the merge
    GDP_use.rename(columns={"Country Name": "Country"}, inplace=True)

    # Finally, ScimEn data
    ScimEn = pd.read_excel("./data/scimagojr-3.xlsx")
    # Using just the 15 first countries
    ScimEn_use = ScimEn.ix[:14,:]

    # Merging data
    df_use = ScimEn_use.merge(energy, how="inner", on="Country").merge(GDP_use, how="inner", on="Country").set_index("Country")
    # Organize your data
    df_use = df_use[df_use["Rank"].notnull()]
    df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "H index"]] = df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "H index"]].astype(int)
    df_use[["Energy Supply", "Energy Supply per Capita", "% Renewable"]] = df_use[["Energy Supply", "Energy Supply per Capita", "% Renewable"]].astype(float)
    return df_use

def ans_two():
    """
    The previous question joined three datasets then reduced this to just the top 15 entries.
    When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
    This function should return a single number.
    """

    #Starting with energy data, exclude the header and footer
    energy = pd.read_excel("./data/Energy_Indicators.xls", skiprows=18, skip_footer=38, header=None)
    # Exclude the two first columns
    energy.drop([0, 1], axis=1, inplace=True)
    # Make your header
    energy_col = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = energy_col
    # Treat your missing values
    energy.replace("...", np.NaN, inplace=True)
    # Convert "Energy Supply" to gigajoules
    energy["Energy Supply"] = energy["Energy Supply"].apply(lambda x: x*1000000)
    # Replace the numbers presente in the strings
    energy["Country"] = energy["Country"].replace(to_replace=["0","1","2","3","4","5","6","7","8","9"], value="", regex=True)
    # Cleaning data
    energy["Country"].replace(to_replace={
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Republic of Korea": "South Korea",
    "China, Hong Kong Special Administrative Region": "Hong Kong"
    }, inplace=True)
    # Cleaning strings with "()"
    energy["Country"] = energy["Country"][energy["Country"].notnull()].apply(
    lambda x: x.split(" (")[0] if x.endswith(")") else x)

    # Now, GDP data, skip the header
    GDP = pd.read_csv("./data-bank/world_bank.csv", skiprows=4)
    # Cleaning data
    GDP["Country Name"].replace(to_replace={
    "Korea, Rep.": "South Korea",
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"
    }, inplace=True)
    # Change the column name for the merge
    GDP.rename(columns={"Country Name": "Country"}, inplace=True)

    # Finally, ScimEn data
    ScimEn = pd.read_excel("./data/scimagojr-3.xlsx")
    # Using just the 15 first countries

    # Merging data to take the intersection (inner)
    df_i = pd.merge(pd.merge(energy, GDP, on="Country"), ScimEn, on="Country")
    # Merging data to take the union (outer)
    df_u = pd.merge(pd.merge(energy, GDP, on="Country", how="outer"), ScimEn, on="Country", how="outer")
    return df_u.shape[0] - df_i.shape[0]

def ans_three():
    """
    This function should return a Series named avgGDP with 15 countries and their average GDP
    sorted in descending order.
    """
    Top15 = ans_one()
    avgGDP = Top15.ix[:,-10:].mean(axis=1).sort_values(ascending=False)
    return avgGDP

def ans_four():
    """
    By how much had the GDP changed over the 10 year span for the country with the
    6th largest average GDP?
    """
    Top15 = ans_one()
    avgGDP = Top15.ix[:,-10:].mean(axis=1).sort_values(ascending=False)
    country = avgGDP.reset_index(level=0)["Country"][5]
    avgGDP = Top15.ix[:,-10:].var(axis=1).sort_values(ascending=False)
    return avgGDP.ix[country, 0]
    # not done

def ans_five():
    """
    What is the mean energy supply per capita?
    """
    Top15 = ans_one()
    return Top15["Energy Supply per Capita"].mean()

def ans_six():
    """
    What country has the maximum % Renewable and what is the percentage?
    """
    Top15 = ans_one()
    sr = tuple(Top15[Top15["% Renewable"] == Top15["% Renewable"].max()]["% Renewable"].iloc[0])
    return sr

def main():
    data = ans_six()
    print(data)

if __name__ == "__main__":
    main()
