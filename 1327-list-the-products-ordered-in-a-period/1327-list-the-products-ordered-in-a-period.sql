# Products와 Orders inner join
# where 조건 order_date가 2020-02에 있고 group by product_id
# sum(unit)의 값이 100이 넘는 애들의 product_name, sum(unit) 반환

select *
from (
    select p.product_name, sum(unit) as unit
    from Products as p
    inner join Orders as j on p.product_id = j.product_id
    where j.order_date between "2020-02-01" and "2020-02-29"
    group by p.product_id
) as t
where unit >=100