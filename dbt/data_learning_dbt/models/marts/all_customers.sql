select
    first_name,
    last_name,
    email,
    city,
    state,
    signup_date,
    'original' as source
from {{ ref('stg_customers') }}

union all

select
    first_name,
    last_name,
    email,
    city,
    state,
    signup_date,
    'python' as source
from {{ ref('stg_customers_python') }}