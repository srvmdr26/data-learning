select
    state,
    count(*) as total_customers,
    min(signup_date) as first_signup_date,
    max(signup_date) as latest_signup_date
from {{ ref('stg_customers') }}
group by state
order by total_customers desc