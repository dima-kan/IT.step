-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою
-- у вказаному діапазоні.

-- SELECT NAME
-- FROM GRADES
-- WHERE MIN_MARK < 80 AND  MIN_MARK > 70


-- ■ Показати інформацію про студентів, яким виповнилося 20 років.

-- UPDATE GRADES
-- SET BIRTHDAY = '2006-05-26'

-- SELECT NAME, AGE(BIRTHDAY)
-- FROM GRADES
-- WHERE AGE(BIRTHDAY) >= INTERVAL'20 years'


-- ■ Показати інформацію про студентів з віком, у вказаному діапазоні.


-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.

-- SELECT NAME
-- FROM GRADES
-- WHERE NAME ILIKE  'АНДРІЙ%'


-- ■ Показати інформацію про студентів, в номері яких
-- є три сімки.

-- SELECT NAME,PHONE
-- FROM GRADES
-- WHERE PHONE ILIKE '%7%7%'
-- WHERE PHONE ILIKE '%7%7%7%'



-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.


-- SELECT NAME,EMAIL
-- FROM GRADES
-- WHERE EMAIL ILIKE 'S%'



-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати мінімальну середню оцінку по всіх студентах.

-- SELECT MIN(AVARAGE_MARK)
-- FROM GRADES
-- ■ Показати максимальну середню оцінку по всіх студентах.

-- SELECT MAX(AVARAGE_MARK)
-- FROM GRADES

-- ■ Показати статистику міст. Має відображатися назва
-- міста та кількість студентів з цього міста.

-- SELECT CITY, COUNT(*) AS STUDENT_COUNT
-- FROM GRADES
-- GROUP BY CITY;


-- ■ Показати статистику студентів. Має відображатися
-- назва країни та кількість студентів з цієї країни.

-- SELECT COUNTRY, COUNT(*) AS COUNTRY_COUNT
-- FROM GRADES
-- GROUP BY COUNTRY;

-- ■ Показати кількість студентів з мінімальною середньою
-- оцінкою з математики.

-- SELECT AVARAGE_MARK, COUNT(*) AS STUDENT_COUNT
-- FROM  GRADES
-- WHERE MIN_SUBJECT = 'Математика'
-- GROUP BY AVARAGE_MARK



-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.

-- SELECT AVARAGE_MARK, COUNT(*) AS STUDENT_COUNT
-- FROM  GRADES
-- WHERE MAX_SUBJECT = 'Математика'
-- GROUP BY AVARAGE_MARK

-- ■ Показати кількість студентів у кожній групі.

-- SELECT GROUP_NAME, COUNT(*) AS student_count
-- FROM GRADES
-- GROUP BY GROUP_NAME

-- ■ Показати середню оцінку групи.


-- SELECT GROUP_NAME, AVG(AVARAGE_MARK) AS AVG_GROUP_MARK
-- FROM GRADES
-- GROUP BY GROUP_NAME



-- SELECT *
-- FROM GRADES
-- WHERE AVARAGE_MARK = (SELECT MAX(AVARAGE_MARK) FROM GRADES )




-- SELECT CITY, COUNT(*)
-- FROM GRADES
-- GROUP BY CITY



-- WITH CITY_NAME AS (
-- 	SELECT CITY, COUNT(*)
-- 	FROM GRADES
-- 	GROUP BY CITY
-- )


-- SELECT MAX(COUNT)
-- FROM CITY_NAME

WITH GROUP_INFO AS (
	SELECT GROUP_NAME,AVG(AVARAGE_MARK) AS GROUP_GRADE
	FROM GRADES
	GROUP BY GROUP_NAME
)



SELECT GROUP_NAME,GROUP_GRADE
FROM GROUP_INFO
WHERE GROUP_GRADE = (
	SELECT MAX(GROUP_GRADE)
	FROM GRADES
)

