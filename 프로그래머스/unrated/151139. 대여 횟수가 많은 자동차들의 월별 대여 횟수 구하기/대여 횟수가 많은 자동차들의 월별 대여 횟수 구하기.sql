SELECT  EXTRACT (MONTH FROM start_date) AS MONTH,CAR_ID, count(*) AS RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 1=1
and to_char(start_date,'yyyy-mm-dd') >= '2022-08-01'
and to_char(start_date,'yyyy-mm-dd') <= '2022-10-31' 
AND CAR_ID IN ( SELECT DISTINCT CAR_ID
                FROM
                (SELECT CAR_ID, COUNT(*)
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
               WHERE 1=1
               and to_char(start_date,'yyyy-mm-dd') >= '2022-08-01'
               and to_char(start_date,'yyyy-mm-dd') <= '2022-10-31' 
               GROUP BY CAR_ID
               HAVING COUNT(*) >= 5 ))
GROUP BY  EXTRACT (MONTH FROM start_date),CAR_ID 
ORDER BY EXTRACT(MONTH FROM start_date),CAR_ID DESC