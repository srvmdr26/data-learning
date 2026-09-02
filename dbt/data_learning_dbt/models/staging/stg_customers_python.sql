select
    first_name,
    last_name,
    lower(email) as email,
    city,
    upper(state) as state,
    signup_date
from {{ source('raw', 'customers_python') }}