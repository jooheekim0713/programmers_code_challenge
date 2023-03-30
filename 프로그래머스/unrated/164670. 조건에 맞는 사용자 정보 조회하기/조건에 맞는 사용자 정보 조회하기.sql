-- 코드를 입력하세요
SELECT user_id, nickname, 
    CONCAT(city, ' ', street_address1, ' ', street_address2) '전체주소',
    CONCAT(left(tlno, 3), '-', mid(tlno, 4, 4), '-', substr(tlno,8)) '전화번호'
FROM USED_GOODS_USER
WHERE user_id IN (SELECT writer_id
        FROM used_goods_board
        GROUP BY writer_id
        HAVING count(writer_id) >= 3)
ORDER BY user_id DESC;