import pandas as pd

# read business.csv data into a dataframe
df = pd.read_csv("yelp_business.csv", sep=",")

# filter the data: in the categories column
# keep only the rows that contain the keyword="Restaurant" & non-sensitive case
df = df[df["categories"].str.contains("Restaurant", case=False, na=False)]

# write buisness data back to a csv file
df.to_csv("yelp_b.csv", sep=",", index=False)

# read reviews.csv into a dataframe
df2 = pd.read_csv("yelp_reviews.csv", sep=",")

# counting the number of words in each row in the 'text' column
df2['text_count'] = df2['text'].str.count(' ') + 1

# delete text column
del df2["text"]

# write reviews data back to a csv file
df2.to_csv("yelp_r.csv", sep=",", index=False)

# merging the 2 dataframes
merged = df.merge(df2, on='business_id')

#Remove all NaN values
merged.dropna()

# new data to analyze
merged.to_csv("new_yelp.csv", sep=",", index=False)

# sample csv file 
sample = pd.read_csv("new_yelp.csv", nrows=100)
sample.to_csv("sample.csv", sep=",", index=False)
