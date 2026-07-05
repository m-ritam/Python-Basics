import pandas as pd


# STEP 1 - Creating Customer Master Data


customer_data = {
    "Customer_ID": ["CUST1001", "CUST1002", "CUST1003", "CUST1004", "CUST1005"],
    "Customer_Name": [
        "ABC Steel Ltd",
        "XYZ Pharma Ltd",
        "LMN Retail Ltd",
        "PQR Auto Ltd",
        "Sun Textiles Ltd"
    ],
    "Industry": [
        "Steel",
        "Pharma",
        "Retail",
        "Automobile",
        "Textile"
    ],
    "Region": [
        "East",
        "West",
        "South",
        "North",
        "East"
    ],
    "Credit_Score": [785, 720, 695, 640, 760]
}

customer_df = pd.DataFrame(customer_data)

print("Customer Master")
print(customer_df)

# Save to Excel
customer_df.to_excel("Customer_Master.xlsx", index=False)



# Step 2 - Creating Loan Portfolio Data


loan_data = {
    "Customer_ID": [
        "CUST1001",
        "CUST1002",
        "CUST1004",
        "CUST1006",
        "CUST1007"
    ],
    "Loan_ID": [
        "LN001",
        "LN002",
        "LN003",
        "LN004",
        "LN005"
    ],
    "Product": [
        "Term Loan",
        "Working Capital",
        "NCD",
        "LAP",
        "Home Loan"
    ],
    "Loan_Amount": [
        5000000,
        12000000,
        8000000,
        4500000,
        7000000
    ],
    "Interest_Rate": [
        9.25,
        10.50,
        8.75,
        11.20,
        8.90
    ],
    "DPD": [
        0,
        45,
        15,
        90,
        0
    ]
}

loan_df = pd.DataFrame(loan_data)

print("\nLoan Portfolio\n")
print(loan_df)

# Save to Excel
loan_df.to_excel("Loan_Portfolio.xlsx", index=False)

# Step 3- Read the excels

Customer_Master = pd.read_excel("Customer_Master.xlsx")
Loan_Portfolio = pd.read_excel("Loan_Portfolio.xlsx")

# STEP 4 - INNER JOIN

print("\nINNER JOIN (Only customers present in both files.)\n")

inner_join = pd.merge(Customer_Master, Loan_Portfolio,
                 on="Customer_ID",
                 how="inner")
print(inner_join)


# STEP 5 - LEFT JOIN

print("\nLEFT JOIN (All customers from the master file, even if they have no loan.)\n")

left_join = pd.merge(Customer_Master, Loan_Portfolio,
                 on="Customer_ID",
                 how="left")
print(left_join)


# STEP 6 - RIGHT JOIN

print("\nRIGHT JOIN (All loan records, even if the customer is missing from the master.)\n")

right_join = pd.merge(Customer_Master, Loan_Portfolio,
                 on="Customer_ID",
                 how="right")
print(right_join)


# STEP 7 - OUTER JOIN

print("\nOUTER JOIN (Everything from both files.)\n")

OUTER_join = pd.merge(Customer_Master, Loan_Portfolio,
                 on="Customer_ID",
                 how="outer")
print(OUTER_join)