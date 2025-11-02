# Suppose we have the following two dictionaries that have (fictitious) 
# data on companies and the sales revenues for two consecutive years. 
# Create a merged dictionary that has the combined sales for the two years.

# Dictionary 1: Company names and sales revenue for year 1
sales_year_1 = {
    "TechNova": 1200000,
    "HealthPlus": 950000,
    "EcoGoods": 650000,
    "FinSecure": 880000,
    "EduLearn": 760000,
    "AutoDrive": 540000,
    "HomeCare": 630000,
    "Foodies": 720000,
    "TravelLux": 810000,
    "BuildIt": 940000
}


# Dictionary 2: Company names and sales revenue for year 2
sales_year_2 = {
    "TechNova": 1300000,
    "HealthPlus": 1020000,
    "EcoGoods": 670000,
    "FinSecure": 900000,
    "EduLearn": 780000,
    "AutoDrive": 560000,
    "HomeCare": 650000,
    "Foodies": 740000,
    "TravelLux": 830000,
    "BuildIt": 960000
}

# Create a merged dictionary for total sales
total_sales = {}

# Add combined sales for each company
for company in sales_year_1:
    total_sales[company] = sales_year_1[company] + sales_year_2[company]

# Print the merged dictionary
print("Combined sales for two years:")
print(total_sales)