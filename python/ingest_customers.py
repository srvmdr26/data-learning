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
        "Ethan", "Mia", "Lucas", "Isabella", "James"
    ],
    "last_name": [
        "Clark", "Walker", "Hall", "Young", "King",
        "Wright", "Lopez", "Hill", "Green", "Adams"
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
        "james@example.com"
    ],
    "city": [
        "Dallas", "Austin", "Chicago", "Dallas", "Seattle",
        "Denver", "Austin", "Fort Worth", "Chicago", "Dallas"
    ],
    "state": [
        "TX", "TX", "IL", "TX", "WA",
        "CO", "TX", "TX", "IL", "TX"
    ],
    "signup_date": [
        "2026-05-10", "2026-05-12", "2026-05-15",
        "2026-05-18", "2026-05-20", "2026-05-22",
        "2026-05-25", "2026-05-27", "2026-05-29",
        "2026-06-01"
    ]
}

df = pd.DataFrame(data)

df["signup_date"] = pd.to_datetime(df["signup_date"])

df.to_sql(
    "customers_python",
    engine,
    if_exists="replace",
    index=False
)

print(f"Successfully loaded {len(df)} rows into PostgreSQL.")