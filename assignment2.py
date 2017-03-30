import pandas as pd

def data_one():
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

    for col in df.columns:
        if col[:2]=='01':
            df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
        if col[:2]=='02':
            df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
        if col[:2]=='03':
            df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
        if col[:1]=='№':
            df.rename(columns={col:'#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\s\(') # split the index by '('

    df.index = names_ids.str[0] # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

    df = df.drop('Totals')
    return df

def ans_one(df):
    """
    Which country has won the most gold medals in summer games?
    """
    return df["Gold"].idxmax()

def ans_two(df):
    """
    Which country had the biggest difference between their summer and winter gold medal counts?
    """
    #df["Summer-Winter"] = df["Gold"] - df["Gold.1"]
    #return df["Summer-Winter"].idxmax()
    return df["Gold"].sub(df["Gold.1"], fill_value = 0).idxmax() # if I work with NaN

def ans_three(df):
    """
    Which country has the biggest difference between their summer gold medal counts and
    winter gold medal counts relative to their total gold medal count?
    Only include countries that have won at least 1 gold in both summer and winter!
    """
    df_copy = df.copy()
    df_copy = df_copy[(df_copy["Gold"]>0) & (df_copy["Gold.1"]>0)]
    df_copy["Sum-Win"] = df_copy["Gold"].sub(df_copy["Gold.1"], fill_value=0)
    df_copy["Total_gold"] = df_copy[["Gold", "Gold.1", "Gold.2"]].sum(axis=1)
    df_copy["Diff_3"] = df_copy["Sum-Win"]/df_copy["Total_gold"]
    return df_copy["Diff_3"].max()

def ans_four(df):
    """
    Write a function that creates a Series called "Points" which is a weighted
    value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2)
    for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return
    only the column (a Series object) which you created.
    """
    df_copy = df.copy()
    df_copy["Points"] = (df_copy["Gold.2"] * 3) + (df_copy["Silver.2"] * 2) + (df_copy["Bronze.2"])
    return df_copy["Points"]

def ans_five(census_df):
    """
    Which state has the most counties in it? (hint: consider the sumlevel key
    carefully! You'll need this for future questions too...)
    """
    census_copy = census_df.copy()
    census_copy = census_copy.set_index("STNAME")
    return census_copy["COUNTY"].idxmax()

def ans_six(census_df):
    """
    Only looking at the three most populous counties for each state, what are the
    three most populous states (in order of highest population to lowest population)?
    Use CENSUS2010POP.
    """
    return census_df

def main():
    df = data_one()
    #print(ans_four(df))
    census_df = pd.read_csv("census.csv")
    print(ans_five(census_df))


main()
