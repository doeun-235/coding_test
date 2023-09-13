-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, left(DATE_OF_BIRTH,10) as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' and TLNO is not null and DATE_OF_BIRTH like "%-03-%"
order by MEMBER_ID