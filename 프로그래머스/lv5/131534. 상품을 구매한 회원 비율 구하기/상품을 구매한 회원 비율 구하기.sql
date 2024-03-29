WITH TB1 AS(SELECT USER_ID FROM USER_INFO WHERE TO_CHAR(JOINED, 'YY') = 21)
SELECT 
    EXTRACT(YEAR FROM SALES_DATE) YEAR,
    EXTRACT(MONTH FROM SALES_DATE) MONTH,
    COUNT(DISTINCT OS.USER_ID) PUCHASED_USERS,
    ROUND(COUNT(DISTINCT OS.USER_ID) / (SELECT COUNT(*) FROM TB1), 1) PUCHASED_RATIO
FROM ONLINE_SALE OS JOIN TB1 T1 ON OS.USER_ID=T1.USER_ID
GROUP BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE)
ORDER BY YEAR, MONTH