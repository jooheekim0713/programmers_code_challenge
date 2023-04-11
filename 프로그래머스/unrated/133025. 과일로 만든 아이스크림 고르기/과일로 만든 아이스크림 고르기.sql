-- 코드를 입력하세요
SELECT B.flavor
FROM FIRST_HALF A, ICECREAM_INFO B
where A.flavor = B.flavor
      and B.ingredient_type = 'fruit_based'
      and A.total_order >= 3000;