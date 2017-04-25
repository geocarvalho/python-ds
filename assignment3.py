import pandas as pd
import numpy as np

def main():
    #Starting with energy data
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
    # Now, GDP data
    GDP = pd.read_csv("./data-bank/world_bank.csv", skiprows=4)
    GDP["Country Name"].replace(to_replace={
    "Korea, Rep.": "South Korea",
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"
    })
    GDP_use = pd.concat([GDP.ix[:, 0], GDP.ix[:, -12:-2]], axis=1)
    GDP_use.rename(columns={"Country Name": "Country"}, inplace=True)
    # Finally, ScimEn data
    ScimEn = pd.read_excel("./data/scimagojr-3.xlsx")
    ScimEn_use = ScimEn.ix[:14,:]
    print("ScimEn size: ", ScimEn_use.shape)
    df_use = ScimEn_use.merge(energy, how="outer", on="Country").merge(GDP_use, how="outer", on="Country").set_index("Country")
    df_use = df_use[df_use["Rank"].notnull()]
        df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", \
            "H index"]] = df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "H index"]].astype(int)
    df_use[["Energy Supply", "Energy Supply per Capita", \
            "% Renewable"]] = df_use[["Energy Supply", "Energy Supply per Capita", "% Renewable"]].astype(float)
    return df_use["Energy Supply"]

if __name__ == "__main__":
    main()
