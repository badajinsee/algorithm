-- 코드를 입력하세요
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A RIGHT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY B.ANIMAL_ID ;
