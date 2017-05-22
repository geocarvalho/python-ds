import pandas as pd
import numpy as np

def class_two():
    """
    How do I read a tabular data file into pandas?
    """
    df1 = pd.read_table("./data/chipotle.tsv")
    user_cols = ["user_id", "age", "gender", "occupation", "zip_code"]
    df2 = pd.read_table("./data/movieusers.txt", sep="|", header=None, names=user_cols)
    return df2.head()
    # tip today
    # argumments: skiprows and skipfooter

def class_three():
    """
    How do I select a pandas Series from a DataFrame?
    """
    ufo = pd.read_csv("./data/ufo.csv")
    ufo["Location"] = ufo.City + ", " + ufo.State
    return ufo.Location.head()

def class_four():
    """
    Why do some pandas commands end with parentheses
    and other commands don't?
    """
    movies = pd.read_csv("./data/imdbratings.csv")
    # Describes stats from all numerical columns
    #return movies.describe()
    return movies.describe(include=["object"])
    # Return the number of rows x columns
    #return movies.shape
    # Type of data prensent in the dataframe (using an atribute)
    #return movies.dtypes

def class_five():
    """
    How do I rename columns in a pandas DataFrame?
    """
    ufo = pd.read_csv("./data/uforeports.csv")
    # columns in a list:
    #return ufo.columns
    # Rename specific columns
    ufo.rename(columns={
    'Colors Reported': 'Colors_Reported',
    'Shape Reported': 'Shape_Reported'
    }, inplace=True)
    # Rename all columns
    ufo_cols = ["city", "colors reported", "shape reported", "state", "time"]
    ufo.columns = ufo_cols
    # Rename columns in the import
    ufo = pd.read_csv("./data/uforeports.csv", names=ufo_cols, header=0)
    # Bonus tip: replace space with underscore
    ufo.columns = ufo.columns.str.replace(" ", "_")
    return ufo.head()

def class_six():
    """
    How do I remove columns from a pandas DataFrame?
    """
    ufo = pd.read_csv("./data/uforeports.csv")
    # Axis 1 indicate the column and axis 0 indicate a row
    # You can use a single string or a list of string to delete
    ufo.drop(['Colors Reported', 'State'], axis=1, inplace=True)
    # To drop a row you can use a string name or the row number in the index
    ufo.drop([0, 4], axis=0, inplace=True)
    return ufo.head()

def class_seven():
    """
    How do I sort a pandas DataFrame or a Series?
    """
    movies = pd.read_csv("./data/imdbratings.csv")
    # Sort just the serie:
    #movies["title"].sort_values(ascending=False)
    # Sort Dataframe, u can use a string or a list of columns:
    movies.sort_values(["genre", "title"], ascending=True, inplace=True)
    return movies.head()

def class_eight_nine():
    """
    How do I filter rows of a pandas DataFrame by column value?
    How do I apply multiple filter criteria to a pandas DataFrame?
    """
    movies = pd.read_csv("./data/imdbratings.csv")
    # Just the condition returns boleans for each row
    # | = or; & = and
#    movies = movies[(movies["duration"]>=200) & (movies["star_rating"]>=8.5)][["title", "genre"]]
    # Maybe the best way to filter columns and luck foranother is using loc
#    movies = movies.loc[movies["duration"]>=200, "genre"]
    # If you want to filter using the same condition (| or &) for differents results in the same column:
    movies = movies[movies["genre"].isin(["Crime", "Drama", "Action"])]
    return movies.head()

def class_ten():
    """
    Your pandas question answered!
    """
    # Reading just N columns from csv file
    ufo = pd.read_csv("./data/uforeports.csv", usecols=[0,4]) # You can use the name too
    # Reading less rows
    ufo = pd.read_csv("./data/uforeports.csv", nrows=3)
    # Interating by serie:
    #for c in ufo.City:    print(c)
    # Interating by dataframe:
    #for index, row in ufo.iterrows():   print(index, row.City, row.State)
    # Drop non-numeric columns:
    drinks = pd.read_csv("./data/drinks.csv")
    drinks = drinks.select_dtypes(include=[np.number]) #.dtypes just to know if we're really calling just numbers
    return drinks

def class_eleven():
    """
    How do I use the "axis" parameter in pandas?
    """
    drinks = pd.read_csv("./data/drinks.csv")
    # For column use 1 and 0 for row:
    drinks.drop("continent", axis=1, inplace=True)
    drinks.drop(2, axis=0, inplace=True)
    return drinks.head()
    # Anothe function to use is the mean
    drinks.mean(axis=0) # by column or axis="index"
    drinks.mean(axis=1) # by row or axis="columns"

def class_twelve():
    """
    How do I use string methods in pandas?
    """
    orders = pd.read_table("./data/chiporders.csv")
    orders.head()["item_name"].str.upper()
    orders[orders["item_name"].str.contains("Chicken")]
    orders["choice_description"].str.replace("[", "").str.replace("]", "")
    orders["choice_description"].str.replace("[\[\]]", "") # or using reguçar expression
    return orders.head()

def class_thirteen():
    """
    How do I change the data type of a pandas Series?
    """
    drinks = pd.read_csv("./data/drinks.csv")
    drinks = drinks["beer_servings"] = drinks["beer_servings"].astype(float)
    # Define the columns types when open a archive:
    drinks = pd.read_csv("./data/drinks.csv", dtype={"beer_servings": float})
    orders = pd.read_table("./data/chiporders.csv")
    #orders.item_price.str.replace("$", "").astype(float)
    # If you want to transform a column in a binary
    orders = orders.item_name.str.contains("Chicken").astype(int)
    return orders.head()

def class_fourteen():
    """
    When should I use a 'groupby' in pandas?
    """
    drinks = pd.read_csv("./data/drinks.csv")
    drinks["beer_servings"].mean()
    drinks.groupby("continent")["beer_servings"].mean()
    # for each continent is the same as
    drinks[drinks["continent"]=="Africa"]["beer_servings"].mean()
    # You can aggregate different functions
    #drinks.groupby("continent ")["beer_servings"].agg(["count", "min", "max", "mean"])
    # Class tips
    drinks = drinks.groupby("continent").mean()
    return drinks

def class_fifteen():
    """
    How do I explore a pandas Series?
    """
    movies = pd.read_csv("./data/imdbratings.csv")
    # Some stats
    movies.genre.describe()
    # Count the number of values in a column
    movies.genre.value_counts()
    # and you can turn it porcentage
    movies.genre.value_counts(normalize=True)
    # If you would like to know the unique values
    movies.genre.unique()
    # and the number of unique values?
    movies.genre.nunique()

def clas_sixteen():
    """
    How do I handle missing values in pandas?
    """
    ufo = pd.read_csv("./data/uforeports.csv")
    # If your data has NaN you can search for it using: (boolean result)
    ufo.isnull()
    ufo.notnull()
    # It is useful because you can know the number of missing values by column for example
    ufo.isnull().sum() # sum all values 1 (true) in a column
    # If you want to know the rows
    ufo[ufo.City.isnull()]
    # To drop rows if NaN
    ufo.dropna(how=any)
    # Drop just if all row has NaN
    ufo.dropna(how=all)
    # You can consider just some columns
    ufo.dropna(subset=["City", "Shape Reported"], how=any) # or all
    # Bonus
    ufo["Shape Reported"].value_counts(dropna=False)
    # Change your NaN to another data
    ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)

def class_seventeen():
    """
    What do I need to know about pandas index? (part 1)
    """
    drinks = pd.read_csv("./data/drinks.csv")
    drinks.index
    drinks.columns
    drinks.shape

    #movies = pd.read_table("./data/movieusers.txt", header=None, sep="|")
    drinks[drinks.continent=="South America"]
    # You can use loc to choose your index and column to obtain a result
    drinks.loc[23, "beer_servings"]
    # Sometimes you don't know the index for a place, so put the place as an index
    drinks.set_index("country", inplace=True)
    # Now you can choose the place instead a default index number
    drinks.loc["Brazil", "beer_servings"]
    # Is not necessary a name for a index columns
    drinks.index.name = None
    # But maybe itt can be usefull in other situation
    drinks.index.name = "country"
    drinks.reset_index(inplace=True)
    # The numerical summary of the numerical columns
    drinks.describe()
    # So, you can interact with resulted dataframes
    drinks.describe().loc["25%", "beer_servings"]

def class_eighteen():
    """
    What do I need to know about pandas index? (part 1)
    """
    drinks = pd.read_csv("./data/drinks.csv")
    drinks.set_index("country", inplace=True)
    # You can manipilate series from results
    drinks.continent.value_counts()
    drinks.continent.value_counts().values
    drinks.continent.value_counts()["Africa"]
    drinks.continent.value_counts().sort_values()

    people = pd.Series([3000000, 85000], index=["Albania", "Andorra"], name="population")
    drinks.beer_servings * people
    return pd.concat([drinks, people], axis=1).head()

def class_nineteen():
    """
    How do I select multiple rows and columns from a pandas DataFrame?
    loc, iloc, ix
    """
    ufo = pd.read_csv("./data/uforeports.csv")
    # Filtering rows and selecting columns by label
    ufo.loc[0, :]
    ufo.loc[[0,1,2], :]
    ufo.loc[0:2, :] # including both sides in slicing
    ufo.loc[:, "City":"State"]

    ufo[ufo.City=="Oakland"]
    ufo.loc[ufo.City=="Oakland", :]

    # Filtering rows and columns by integer
    ufo.iloc[:, 0:4] # exclude the last number in a slicing
    ufo.iloc[0:3, :]

    # Mix labels and integers in selection
    drinks = pd.read_csv("./data/drinks.csv", index_col="country")
    drinks.ix["Albania", 0]
    drinks.ix[1, "beer_servings"]
    drinks.ix["Albanin":"Andorra", 0:2]
    drinks.ix[0:2, 0:2] # labels are include in index

def class_twenty():
    """
    When should I use the "inplace" parameter in pandas?
    """
    ufo = pd.read_csv("./data/uforeports.csv")
    ufo.drop("City", axis=1, inplace=True)
    ufo.dropna(how=any)
    # Use it to know the impact of what you did, brefore using inplace argument
    ufo.shape

    ufo.fillna(method="bfill")
    ufo.fillna(method="ffill")

def class_twenty_one():
    """
    How do I make my pandas DataFrame smaller and faster?
    """
    drinks = pd.read_csv("./data/drinks.csv")
    # To know the memory usage by column objects
    drinks.memory_usage(deep=True)
    # I want to know my possible strings in a column to transform in integers
    sorted(drinks.continent.unique())
    # Pandas already has how transform it
    drinks["continent"] = drinks.continent.astype("category")
    # It still the same superficiale
    drinks.continent.head()
    # But not for real, and using less memory
    drinks.continent.cat.codes.head()
    drinks.memory_usage(deep=True)
    # You have to be careful with columns with a lot of different values
    drinks["country"] = drinks.country.astype("category")
    drinks.memory_usage(deep=True)
    # So, let's organize the category order
    df = pd.DataFrame({"ID": [100, 101, 102, 103], "quality": ["good", "very good", "good", "excellent"]})
    df.sort_values("quality") # alfabetic order
    df["quality"] = df.quality.astype("category", categories=["good", "very good", "excellent"]) # order by category
    df.sort_values("quality") # sorting by category

def class_twenty_two():
    """
    How do I use pandas with scikit-learn to create Kaggle submissions?
    """
    train = pd.read_csv("./data/kaggletrain.csv")
    feature_col = ["Pclass", "Parch"]
    X = train.loc[:, feature_col]
    Y = train.Survived

    from sklearn.linear_model import LogisticRegression
    logreg = LogisticRegression()
    logreg.fit(X, Y)

    test = pd.read_csv("./data/titanic_test.csv")
    X_new = test.loc[:, feature_cols]
    new_pred_class = logreg.predict(X_new)

    pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).set_index("PassengerId").to_csv("sub.csv")

    train.to_pickle("train.pk1")

    return train.head()

def class_twenty_three():
    """
    More of your pandas questions answered!
    """

if __name__ == "__main__":
    print(class_twenty_two())
