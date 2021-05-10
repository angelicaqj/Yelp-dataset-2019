import json
import csv

## Converting JSON to CSV

# 1st dataset
yelp_business = 'yelp_academic_dataset_business.json' 

data = [] #empty list

# opening JSON file and adding by line to the empty list
for line in open(yelp_business, 'r'):
    data.append(json.loads(line))

print(data[0])

# opening CSV file for writing 
with open('yelp_business.csv', 'w') as file:

    # create the CSV writer object
    csv_business = csv.writer(file)
    # writing headers to CSV file
    csv_business.writerow(["business_id","name","city","state","postal_code","categories","stars"])

    
    for item in data:
        csv_business.writerow([item["business_id"],item["name"],item["city"],item["state"],
                               item["postal_code"],item["categories"],item["stars"]])

# 2nd dataset with the same steps
yelp_reviews = 'yelp_academic_dataset_review.json'
data = []

for line in open(yelp_reviews, 'r'):
    data.append(json.loads(line))
    
with open('yelp_reviews.csv', 'w') as file:
    csv_reviews = csv.writer(file)
    csv_reviews.writerow(["review_id","business_id","stars","text","useful","funny","cool"])

    for item in data:
        csv_reviews.writerow([item["review_id"],item["business_id"],item["stars"],item["text"],
                              item["useful"],item["funny"],item["cool"]])


## Data Wrangling

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
