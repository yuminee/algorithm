select product_id, year as first_year, quantity, price
from Sales
where (year, product_id) in (
    select min(year) as first_year, product_id
    from Sales
    group by product_id
)