SELECT user_id, nickname, city ||' '|| street_address1 || ' ' || street_address2,
substr(tlno,0,3)||'-'||substr(tlno,4,4)||'-'||substr(tlno,8)
FROM USED_GOODS_USER
WHERE user_id IN (SELECT writer_id
        FROM used_goods_board
        GROUP BY writer_id
        HAVING count(writer_id) >= 3)
ORDER BY user_id DESC;