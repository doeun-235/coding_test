SELECT INFO.INGREDIENT_TYPE, SUM(HALF.TOTAL_ORDER) AS TOTAL_ORDER  
FROM FIRST_HALF HALF
JOIN ICECREAM_INFO INFO ON INFO.FLAVOR=HALF.FLAVOR
GROUP BY INGREDIENT_TYPE