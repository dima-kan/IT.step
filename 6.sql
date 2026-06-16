-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	FINANCING INT NOT NULL DEFAULT 0 CHECK (FINANCING >= 0),
-- 	NAME VARCHAR(100) NOT NULL UNIQUE  CHECK (LENGTH(NAME) > 0)
-- )

-- INSERT INTO Departments (Financing, Name)
-- VALUES
--     (150000, 'Computer Science'),
--     (120000, 'Mathematics'),
--     (95000, 'Physics'),
--     (110000, 'Chemistry'),
--     (130000, 'Economics'),
--     (100000, 'Law'),
--     (85000, 'History'),
--     (140000, 'Engineering')

-- CREATE TABLE Faculties (
--     ID SERIAL PRIMARY KEY,
--     DEAN VARCHAR(255) NOT NULL CHECK (LENGTH(DEAN) > 0),
--     NAME VARCHAR(100) NOT NULL UNIQUE CHECK (LENGTH(NAME) > 0)
-- )

-- INSERT INTO Faculties (Dean, Name)
-- VALUES
--     ('Ivan Petrenko', 'Computer Science'),
--     ('Olena Kovalenko', 'Mathematics'),
--     ('Mykola Shevchenko', 'Physics'),
--     ('Tetiana Bondarenko', 'Chemistry'),
--     ('Andrii Melnyk', 'Economics'),
--     ('Natalia Tkachenko', 'Law')


-- CREATE TABLE Groups (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(10) NOT NULL UNIQUE CHECK (LENGTH(NAME) > 0),
--     RATING INT NOT NULL CHECK (RATING BETWEEN 0 AND 5),
--     YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5)
-- );

-- INSERT INTO Groups (Name, Rating, Year)
-- VALUES
--     ('CS101', 5, 1),
--     ('CS201', 4, 2),
--     ('MTH101', 5, 1),
--     ('PHY301', 3, 3),
--     ('ECO401', 4, 4),
--     ('LAW501', 5, 5);


-- CREATE TABLE TEACHERS (
--     ID SERIAL PRIMARY KEY,
--     EMPLOYMENTDATE DATE NOT NULL CHECK (EMPLOYMENTDATE >= '1990-01-01'),
--     ISASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
--     ISPROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
--     NAME VARCHAR(255) NOT NULL CHECK (LENGTH(NAME) > 0),
--     POSITION VARCHAR(255) NOT NULL CHECK (LENGTH(POSITION) > 0),
--     PREMIUM INT NOT NULL DEFAULT 0 CHECK (PREMIUM >= 0),
--     SALARY INT NOT NULL CHECK (SALARY > 0),
--     SURNAME VARCHAR(255) NOT NULL CHECK (LENGTH(SURNAME) > 0)
-- );


-- INSERT INTO TEACHERS (
--     EMPLOYMENTDATE,
--     ISASSISTANT,
--     ISPROFESSOR,
--     NAME,
--     POSITION,
--     PREMIUM,
--     SALARY,
--     SURNAME
-- )
-- VALUES
-- ('1995-02-15', FALSE, TRUE, 'Ivan', 'Professor', 5000, 40000, 'Petrenko'),
-- ('1998-06-20', FALSE, TRUE, 'Olena', 'Professor', 4500, 38000, 'Kovalenko'),
-- ('2001-09-01', TRUE, FALSE, 'Andrii', 'Assistant', 1000, 18000, 'Melnyk'),
-- ('2003-11-12', FALSE, FALSE, 'Mykola', 'Lecturer', 1500, 22000, 'Shevchenko'),
-- ('2005-04-10', TRUE, FALSE, 'Tetiana', 'Assistant', 1200, 19000, 'Bondarenko'),
-- ('1997-08-18', FALSE, TRUE, 'Serhii', 'Professor', 6000, 42000, 'Tkachenko'),
-- ('2008-03-22', FALSE, FALSE, 'Natalia', 'Lecturer', 1800, 23000, 'Savchenko'),
-- ('2010-05-14', TRUE, FALSE, 'Oksana', 'Assistant', 900, 17000, 'Kravchenko'),
-- ('2002-01-30', FALSE, FALSE, 'Volodymyr', 'Senior Lecturer', 2500, 26000, 'Marchenko'),
-- ('1994-12-05', FALSE, TRUE, 'Yurii', 'Professor', 7000, 45000, 'Polishchuk'),

-- ('2012-02-16', TRUE, FALSE, 'Iryna', 'Assistant', 1100, 17500, 'Lysenko'),
-- ('2006-07-09', FALSE, FALSE, 'Roman', 'Lecturer', 1600, 22500, 'Hrytsenko'),
-- ('2009-10-11', FALSE, FALSE, 'Dmytro', 'Senior Lecturer', 2200, 25500, 'Koval'),
-- ('1996-04-27', FALSE, TRUE, 'Liudmyla', 'Professor', 5500, 39500, 'Moroz'),
-- ('2011-09-19', TRUE, FALSE, 'Viktor', 'Assistant', 1300, 18500, 'Boiko'),
-- ('2007-06-03', FALSE, FALSE, 'Anastasiia', 'Lecturer', 1700, 23500, 'Pavlenko'),
-- ('2004-08-25', FALSE, FALSE, 'Oleksandr', 'Senior Lecturer', 2400, 27000, 'Danylchenko'),
-- ('1993-03-17', FALSE, TRUE, 'Halyna', 'Professor', 6500, 43000, 'Rudenko'),
-- ('2013-11-08', TRUE, FALSE, 'Kateryna', 'Assistant', 1000, 18000, 'Sydorenko'),
-- ('2000-05-20', FALSE, FALSE, 'Taras', 'Lecturer', 2000, 24000, 'Yaremchuk'),

-- ('1999-07-14', FALSE, TRUE, 'Maksym', 'Professor', 5000, 41000, 'Kostenko'),
-- ('2014-01-12', TRUE, FALSE, 'Svitlana', 'Assistant', 900, 17500, 'Klymenko'),
-- ('2008-09-28', FALSE, FALSE, 'Bohdan', 'Lecturer', 1500, 22000, 'Zakharchenko'),
-- ('2005-12-16', FALSE, FALSE, 'Yevhen', 'Senior Lecturer', 2300, 26500, 'Chumak'),
-- ('1992-10-06', FALSE, TRUE, 'Valentyna', 'Professor', 7200, 46000, 'Bilenko'),
-- ('2015-04-21', TRUE, FALSE, 'Alina', 'Assistant', 800, 16500, 'Mazur'),
-- ('2001-02-13', FALSE, FALSE, 'Denys', 'Lecturer', 1800, 23000, 'Kushnir'),
-- ('2007-11-27', FALSE, FALSE, 'Pavlo', 'Senior Lecturer', 2500, 28000, 'Onyshchenko'),
-- ('1991-06-18', FALSE, TRUE, 'Maria', 'Professor', 8000, 48000, 'Horbach'),
-- ('2016-09-05', TRUE, FALSE, 'Sofia', 'Assistant', 700, 16000, 'Levchenko');


-- Для бази даних Академія створіть такі запити:
-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.

-- SELECT NAME ,FINANCING ,ID
-- FROM DEPARTMENTS;

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.

-- SELECT
--     NAME AS "GROUP NAME",
--     RATING AS "GROUP RATING"
-- FROM GROUPS;


-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).

-- SELECT SURNAME,
--     SALARY * 100.0 / PREMIUM AS SALARY_TO_PREMIUM_PERCENT,
--     SALARY * 100.0 / (SALARY + PREMIUM) AS SALARY_TO_TOTAL_PERCENT
-- FROM TEACHERS;


-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».

-- SELECT
--     'The dean of faculty ' || NAME || ' is ' || DEAN || '.'
-- FROM FACULTIES;


-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.


-- SELECT SURNAME
-- FROM TEACHERS
-- WHERE ISPROFESSOR = TRUE AND SALARY > 1050;


-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 25000.

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE FINANCING < 11000 OR FINANCING > 25000;


-- 7. Вивести назви факультетів, окрім факультету «Computer
-- Science».


-- SELECT NAME
-- FROM FACULTIES
-- WHERE NAME != 'Computer Science';



-- 8. Вивести прізвища та посади викладачів, які не є професорами.

-- SELECT SURNAME ,POSITION
-- FROM TEACHERS
-- WHERE ISPROFESSOR = FALSE;

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів,
-- надбавка яких у діапазоні від 160 до 550.


-- SELECT SURNAME, POSITION, SALARY, PREMIUM
-- FROM TEACHERS
-- WHERE ISASSISTANT = TRUE
--   AND PREMIUM BETWEEN 160 AND 550;


-- 10. Вивести прізвища та ставки асистентів.


-- SELECT SURNAME, SALARY
-- FROM TEACHERS
-- WHERE ISASSISTANT = TRUE;




-- 11. Вивести прізвища та посади викладачів, які були прийняті
-- на роботу до 01.01.2000.


-- SELECT SURNAME, POSITION
-- FROM TEACHERS
-- WHERE EMPLOYMENTDATE < '2000-01-01';


-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
-- назвіть «Name of Department».

-- SELECT NAME AS "Name of Department"
-- FROM DEPARTMENTS
-- WHERE NAME < 'Software Development'

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки
-- та надбавки) не більше 20000.

-- SELECT SURNAME
-- FROM TEACHERS
-- WHERE ISASSISTANT = TRUE AND (SALARY + PREMIUM) <= 20000;

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні
-- від 2 до 4.

-- SELECT NAME
-- FROM GROUPS
-- WHERE YEAR = 3 AND RATING BETWEEN 1 AND 4;



-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550
-- або надбавкою менше, ніж 200.

-- SELECT SURNAME
-- FROM TEACHERS
-- WHERE ISASSISTANT = TRUE AND (SALARY < 550 OR PREMIUM < 200);




