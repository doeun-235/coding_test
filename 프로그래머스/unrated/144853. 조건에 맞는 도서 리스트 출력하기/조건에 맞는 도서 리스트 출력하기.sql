-- 코드를 입력하세요
SELECT BOOK_ID, LEFT(PUBLISHED_DATE,10) AS PUBLISHED_DATE
from BOOK
where CATEGORY = '인문' and PUBLISHED_DATE like concat("2021","%")
order by PUBLISHED_DATE