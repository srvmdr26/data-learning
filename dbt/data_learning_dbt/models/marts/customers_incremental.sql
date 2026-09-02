{{
    config(
        materialized='incremental',
        unique_key='email'
    )
}}

select
    first_name,
    last_name,
    email,
    city,
    state,
    signup_date,
    source
from {{ ref('all_customers') }}

{% if is_incremental() %}

where email not in (
    select email
    from {{ this }}
)

{% endif %}