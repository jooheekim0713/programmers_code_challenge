with temp as
(
SELECT *, datediff(end_date, start_date)+1 rental_duration
from car_rental_company_rental_history H
    left join car_rental_company_car C using (car_id)
    left join car_rental_company_discount_plan P using (car_type)
where car_type = '트럭'
)
select history_id,
    case
        when rental_duration between 7 and 27 
            then round(daily_fee*rental_duration*0.95)
        when rental_duration between 30 and 89
            then round(daily_fee*rental_duration*0.92)
        when rental_duration >= 90
            then round(daily_fee*rental_duration*0.85)
        else daily_fee*rental_duration
    end as fee
from temp
group by 1
order by 2 desc, 1 desc