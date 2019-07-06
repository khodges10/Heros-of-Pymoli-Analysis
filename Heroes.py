# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load
file = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file)

# Find player count
player_count = len(purchase_data["SN"].value_counts())

# Display player count
player_count_table = pd.DataFrame({"Total Players": [player_count]})
player_count_table

# Find total # of unique items
items_count = len(purchase_data["Item ID"].unique())

# Find average puchase price
avg_price = purchase_data["Price"].mean()

# Find total # of purchases
purchase_count = purchase_data["Item ID"].count()

# Find total revenue
total_revenue = purchase_data["Price"].sum()

# Display total purchasing analysis
purchasing_total_table = pd.DataFrame({"Number of Unique Items": [items_count],
                              "Average Price": "$" + str(avg_price.round(2)),
                              "Number of Purchases": [purchase_count],
                              "Total Revenue": "$" + str(total_revenue)})
purchasing_total_table

# Group purchase data for gender
gender_stats = purchase_data.groupby("Gender")

# Gender count
gender_count = gender_stats.nunique()["SN"]

# Gender percentages
gender_percentage = gender_count / player_count * 100

# Display gender demographics
gender_demographics_table = pd.DataFrame({"Total Count": gender_count, "Percentage of Players": gender_percentage})

# Format dataframe no index name in corner
gender_demographics_table.index.name = None

# Format gender demographics table to be in descending order with two decimal places and percentage
gender_demographics_table.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})

# Gender purchase count
gender_purchase = gender_stats["Purchase ID"].count()

# Gender average purchase price
gender_avg_purchase_price = gender_stats["Price"].mean()

# Gender total purchase value
gender_purchase_total = gender_stats["Price"].sum()

# Gender average purchase total per person divided by purchase count
avg_purchase_per_person = gender_purchase_total / gender_count

# Display gender purchase analysis
gender_purchase_table = pd.DataFrame({"Purchase Count": gender_purchase, 
                                    "Average Purchase Price": gender_avg_purchase_price,
                                    "Total Purchase Value": gender_purchase_total,
                                    "Avg Purchase Total per Person": avg_purchase_per_person})

# Have "Gender" in the top left of table
gender_demographics.index.name = "Gender"

# Format gender purchase analysis with currency style
gender_purchase_table.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                    "Total Purchase Value":"${:,.2f}",
                                    "Avg Purchase Total per Person":"${:,.2f}"})

# Establish bins for ages
age_bins = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Categorize the existing players using the age bins
purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data

# Group the added "Age Group"
age_grouped = purchase_data.groupby("Age Group")

# Find total players by age 
age_count = age_grouped["SN"].nunique()

# Calculate percentages by age
age_percentage = (age_count/player_count) * 100

# Display age demographics
age_demographics_table = pd.DataFrame({"Total Count": age_count, "Percentage of Players": age_percentage})

# Format dataframe no index name in corner
age_demographics_table.index.name = None

# Format age demographics table with two decimal places
age_demographics_table.style.format({"Percentage of Players":"{:,.2f}"})

# Count purchases by age group
age_purchases = age_grouped["Purchase ID"].count()

# Average purchase price by age group 
age_avg_purchase_price = age_grouped["Price"].mean()

# Total purchase value by age group 
age_total_purchase_value = age_grouped["Price"].sum()

# Average total purchase per person by age group
age_avg_purchase_per_person = age_total_purchase_value / age_count

# Display age purchase analysis
age_purchase_table = pd.DataFrame({"Purchase Count": age_purchases,
                                 "Average Purchase Price": age_avg_purchase_price,
                                 "Total Purchase Value": age_total_purchase_value,
                                 "Average Total Purchase per Person": age_avg_purchase_per_person})

# Format dataframe no index name in corner
age_purchase_table.index.name = None

# Format age purchase analysis with currency style
age_purchase_table.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Total Purchase per Person":"${:,.2f}"})

# Group purchase data by screen name
spender_stats = purchase_data.groupby("SN")

# Total purchases by name
spender_purchase_count = spender_stats["Purchase ID"].count()

# Average purchase by name 
spender_avg_purchase_price = spender_stats["Price"].mean()

# Purchase total 
spender_total_purchase = spender_stats["Price"].sum()

# Display top spenders
top_spenders_table = pd.DataFrame({"Purchase Count": spender_purchase_count,
                             "Average Purchase Price": spender_avg_purchase_price,
                             "Total Purchase Value": spender_total_purchase})

# Sort total purchase value column in descending order 
spenders_formatted = top_spenders_table.sort_values(["Total Purchase Value"], ascending=False).head()

# Format with currency style
spenders_formatted.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})

# Create new data frame with items that relate to most popular items
items = purchase_data[["Item ID", "Item Name", "Price"]]

# Group items by "item id" and "item name" 
item_stats = items.groupby(["Item ID","Item Name"])

# Count the amount of times an item has been purchased 
item_purchase_count = item_stats["Price"].count()

# Purchase value per item 
item_purchase_value = item_stats["Price"].sum() 

# Calculate individual item price
item_price = item_purchase_value / item_purchase_count

# Display most popular items
popular_items_table = pd.DataFrame({"Purchase Count": item_purchase_count, 
                                   "Item Price": item_price,
                                   "Total Purchase Value": item_purchase_value})

# Sort purchase count column in descending order
popular_formatted = popular_items_table.sort_values(["Purchase Count"], ascending=False).head()

# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})

# Sort above table but with total purchase value column in descending order
popular_formatted = popular_items_table.sort_values(["Total Purchase Value"], ascending=False).head()

# Format most profitable items with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
