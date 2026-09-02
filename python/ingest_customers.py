import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass

password = getpass("PostgreSQL password: ")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/data_learning"
)

data = {
    "first_name": [
    "Emma", "Liam", "Olivia", "Noah", "Ava",
    "Ethan", "Mia", "Lucas", "Isabella", "James",
    "Sophia"
],
    "last_name": [
    "Clark", "Walker", "Hall", "Young", "King",
    "Wright", "Lopez", "Hill", "Green", "Adams",
    "Martinez"
],
    "email": [
        "emma@example.com",
        "liam@example.com",
        "olivia@example.com",
        "noah@example.com",
        "ava@example.com",
        "ethan@example.com",
        "mia@example.com",
        "lucas@example.com",
        "isabella@example.com",
        "james@example.com",
"sophia@example.com"
    ],
    "city": [
        "Dallas", "Austin", "Chicago", "Dallas", "Seattle",
        "Denver", "Austin", "Fort Worth", "Chicago", "Dallas", "Dallas"
    ],
    "state": [
        "TX", "TX", "IL", "TX", "WA",
        "CO", "TX", "TX", "IL", "TX", "TX"
    ],
    "signup_date": [
        "2026-05-10", "2026-05-12", "2026-05-15",
        "2026-05-18", "2026-05-20", "2026-05-22",
        "2026-05-25", "2026-05-27", "2026-05-29",
        "2026-06-01", "2026-06-05"
    ]
}

df = pd.DataFrame(data)

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