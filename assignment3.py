import pandas as pd
import numpy as np

def main():
    energy = pd.read_excel("./data/Energy_Indicators.xls", header=None)
    energy.drop([0, 1], axis=1, inplace=True)
    energy_col = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = energy_col
    energy["Energy Supply"][energy["Energy Supply"] == "Petajoules"] = 1000000
    #energy[energy["Country"] == "..."] = np.NaN
    energy.replace("...", np.NaN, inplace=True)
    energy["Country"].replace(to_replace={
    "Iran (Islamic Republic of)": "Iran",
    "Micronesia (Federated States of)": "Micronesia",
    "Sint Maarten (Dutch part)": "Sint Maarten",
    "Falkland Islands (Malvinas)": "Malvinas",
    "Bolivia (Plurinational State of)": "Bolivia",
    "Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"
    }, inplace=True)

    GPI = pd.read_csv("./data-bank/world_bank.csv", skiprows=5, header=None)
    GPI[0].replace(to_replace={
    "Korea, Rep.": "South Korea",
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"
    })

    ScimEn = pd.read_excel("./data/scimagojr-3.xlsx")
    print(ScimEn.head())
    #print(energy["Country"].to_string()) to see the entire series

if __name__ == "__main__":
    main()
