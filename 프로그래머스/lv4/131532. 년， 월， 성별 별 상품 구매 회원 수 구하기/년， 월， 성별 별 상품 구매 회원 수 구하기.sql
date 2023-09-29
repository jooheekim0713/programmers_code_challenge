SELECT
    EXTRACT(YEAR FROM SALES_DATE) YEAR,
    EXTRACT(MONTH FROM SALES_DATE) MONTH, 
    GENDER, 
    COUNT(DISTINCT OS.USER_ID) USERS
FROM USER_INFO UI JOIN ONLINE_SALE OS
ON UI.USER_ID=OS.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY
    EXTRACT(YEAR FROM SALES_DATE), 
    EXTRACT(MONTH FROM SALES_DATE), 
    GENDER
ORDER BY YEAR, MONTH, GENDER ASC