-- 코드를 입력하세요
SELECT animal_id, name
FROM animal_outs
WHERE animal_id not in (SELECT animal_id 
                       FROM animal_ins)
ORDER BY animal_id, name