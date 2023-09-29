-- 코드를 입력하세요
SELECT h.flavor
FROM first_half h , icecream_info i
where h.flavor = i.flavor
and h.total_order > 3000
and i.ingredient_type = 'fruit_based'
order by total_order desc