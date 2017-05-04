import pandas as pd
import numpy as np

def main():
    #Starting with energy data
    energy = pd.read_excel("./data/Energy_Indicators.xls", skiprows=18, skip_footer=38, header=None)
    energy.drop([0, 1], axis=1, inplace=True)
    energy_col = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.columns = energy_col
    energy.replace("...", np.NaN, inplace=True)
    energy["Energy Supply"] = energy["Energy Supply"].apply(lambda x: x*1000000)
    energy["Country"].replace(to_replace={
    "China2": "China",
    "United States of America20": "United States",
    "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
    "Japan10": "Japan",
    "France6": "France",
    "Italy9": "Italy",
    "Spain16": "Spain",
    "Australia1": "Australia",
    "Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"
    }, inplace=True)
    energy["Country"] = energy["Country"][energy["Country"].notnull()].apply(
    lambda x: x.split(" (")[0] if x.endswith(")") else x)
    #energy["Country"].apply(lambda x: print(x) if x.startswith("B") else x)
    #print("\n\n")
    #print("Energy\n", energy.head(5))

    # Now, GDP data
    GDP = pd.read_csv("./data-bank/world_bank.csv", skiprows=4)
    GDP["Country Name"].replace(to_replace={
    "Korea, Rep.": "South Korea",
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"
    }, inplace=True)
    GDP_use = pd.concat([GDP.ix[:, 0], GDP.ix[:, -12:-2]], axis=1)
    GDP_use.rename(columns={"Country Name": "Country"}, inplace=True)
    #GDP_use["Country"].apply(lambda x: print(x) if x.startswith("B") else x)
    #print("GDP\n", GDP_use["Country"].tail(5))

    # Finally, ScimEn data
    ScimEn = pd.read_excel("./data/scimagojr-3.xlsx")
    ScimEn_use = ScimEn.ix[:14,:]
    #print(ScimEn_use["Country"])
    #print("ScimEn size: ", ScimEn_use.shape)
    #print("Scimen\n", ScimEn["Country"].tail(5))

    df_use = ScimEn_use.merge(energy, how="inner", on="Country").merge(GDP_use, how="inner", on="Country").set_index("Country")
    df_use = df_use[df_use["Rank"].notnull()]
    df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "H index"]] = df_use[["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "H index"]].astype(int)
    df_use[["Energy Supply", "Energy Supply per Capita", "% Renewable"]] = df_use[["Energy Supply", "Energy Supply per Capita", "% Renewable"]].astype(float)
    print(df_use)

if __name__ == "__main__":
    main()
