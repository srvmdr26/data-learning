import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass

password = getpass("PostgreSQL password: ")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/data_learning"
)

df = pd.read_csv("data/customers.csv")

df["signup_date"] = pd.to_datetime(df["signup_date"])

# Read emails already stored in PostgreSQL
existing = pd.read_sql(
    "SELECT email FROM customers_python",
    engine
)

# Keep only customers that are not already in the database
df_new = df[~df["email"].isin(existing["email"])]

print(f"New rows to insert: {len(df_new)}")

# Insert only the new customers
df_new.to_sql(
    "customers_python",
    engine,
    if_exists="append",
    index=False
)

print(f"Successfully loaded {len(df_new)} new rows into PostgreSQL.")