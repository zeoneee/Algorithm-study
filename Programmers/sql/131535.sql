-- 코드를 입력하세요
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND JOINED BETWEEN '2021-01-01' AND '2021-12-31'