-- 코드를 입력하세요
SELECT YEAR(OS.sales_date) Y, MONTH(OS.sales_date) M, UI.gender GENDER, COUNT(DISTINCT UI.user_id)
FROM USER_INFO UI, ONLINE_SALE OS
WHERE UI.user_id = OS.user_id AND GENDER is not null
GROUP BY Y,M,GENDER
ORDER BY Y,M,GENDER