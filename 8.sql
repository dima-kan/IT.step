-- CREATE TABLE CURATORS (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(30) NOT NULL,
--     SURNAME VARCHAR(50) NOT NULL
-- );

-- INSERT INTO CURATORS (NAME, SURNAME) VALUES
-- ('Олена', 'Ковальчук'),
-- ('Іван', 'Шевченко'),
-- ('Марія', 'Бондаренко'),
-- ('Андрій', 'Ткаченко'),
-- ('Наталія', 'Кравченко'),
-- ('Сергій', 'Мельник'),
-- ('Тетяна', 'Шевчук'),
-- ('Володимир', 'Петренко'),
-- ('Ірина', 'Романенко'),
-- ('Олександр', 'Гриценко');



-- CREATE TABLE FACULTIES (
--     ID SERIAL NOT NULL PRIMARY KEY,
--     FINANCING INT NOT NULL DEFAULT 0 CHECK (FINANCING >= 0),
--     NAME VARCHAR(100) NOT NULL UNIQUE
-- );

-- INSERT INTO FACULTIES (FINANCING, NAME) VALUES
-- (1500000, 'Факультет інформаційних технологій'),
-- (1200000, 'Факультет математики та інформатики'),
-- (900000,  'Факультет економіки'),
-- (1100000, 'Факультет права'),
-- (800000,  'Факультет філології'),
-- (1000000, 'Факультет інженерії'),
-- (950000,  'Факультет біології'),
-- (700000,  'Факультет історії');



-- CREATE TABLE DEPARTMENTS (
--     ID  SERIAL  PRIMARY KEY,
--     FINANCING INT NOT NULL DEFAULT 0 CHECK (FINANCING >= 0),
--     NAME VARCHAR(40) NOT NULL UNIQUE,
--     FACULTYID INT NOT NULL,
--     FOREIGN KEY (FACULTYID) REFERENCES FACULTIES(ID)
-- );

-- INSERT INTO DEPARTMENTS (FINANCING, NAME, FACULTYID) VALUES
-- (300000, 'Кафедра програмної інженерії', 1),
-- (250000, 'Кафедра комп’ютерних наук', 1),
-- (200000, 'Кафедра прикладної математики', 2),
-- (180000, 'Кафедра математичного аналізу', 2),
-- (220000, 'Кафедра економіки підприємства', 3),
-- (210000, 'Кафедра фінансів', 3),
-- (230000, 'Кафедра кримінального права', 4),
-- (190000, 'Кафедра цивільного права', 4),
-- (170000, 'Кафедра української філології', 5),
-- (160000, 'Кафедра іноземної філології', 5),
-- (240000, 'Кафедра машинобудування', 6),
-- (260000, 'Кафедра електроніки', 6),
-- (150000, 'Кафедра біотехнологій', 7),
-- (140000, 'Кафедра генетики', 7),
-- (130000, 'Кафедра історії України', 8),
-- (120000, 'Кафедра всесвітньої історії', 8);


-- CREATE TABLE GROUPS (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(30) NOT NULL UNIQUE,
--     YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5),
--     DEPARTMENTID INT NOT NULL,
--     FOREIGN KEY (DEPARTMENTID) REFERENCES DEPARTMENTS(ID)
-- );

-- INSERT INTO GROUPS (NAME, YEAR, DEPARTMENTID) VALUES
-- ('PI-21', 2, 1),
-- ('PI-22', 1, 1),
-- ('CS-11', 3, 2),
-- ('CS-12', 2, 2),
-- ('PM-31', 4, 3),
-- ('PM-32', 3, 3),
-- ('MA-21', 2, 4),
-- ('MA-22', 1, 4),
-- ('EC-11', 1, 5),
-- ('EC-12', 2, 5),
-- ('FN-21', 2, 6),
-- ('FN-22', 3, 6),
-- ('CR-31', 4, 7),
-- ('CR-32', 3, 7),
-- ('CL-11', 1, 8),
-- ('CL-12', 2, 8);


-- CREATE TABLE GROUPSCURATORS (
--     ID SERIAL PRIMARY KEY,
--     CURATORID INT NOT NULL,
--     GROUPID INT NOT NULL,
--     FOREIGN KEY (CURATORID) REFERENCES CURATORS(ID),
--     FOREIGN KEY (GROUPID) REFERENCES GROUPS(ID)
-- );


-- INSERT INTO GROUPSCURATORS (CURATORID, GROUPID) VALUES
-- (1, 1),
-- (2, 2),
-- (3, 3),
-- (4, 4),
-- (5, 5),
-- (6, 6),
-- (7, 7),
-- (8, 8),
-- (1, 9),
-- (2, 10),
-- (3, 11),
-- (4, 12),
-- (5, 13),
-- (6, 14),
-- (7, 15),
-- (8, 16);


-- CREATE TABLE TEACHERS (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(40) NOT NULL,
--     SURNAME VARCHAR(60) NOT NULL,
--     SALARY INT NOT NULL CHECK (SALARY > 0)
-- );


-- INSERT INTO TEACHERS (NAME, SURNAME, SALARY) VALUES
-- ('Іван', 'Петренко', 15000),
-- ('Олена', 'Коваль', 18000),
-- ('Андрій', 'Шевченко', 20000),
-- ('Наталія', 'Бондаренко', 17000),
-- ('Сергій', 'Мельник', 16000),
-- ('Тетяна', 'Кравченко', 19000),
-- ('Володимир', 'Ткаченко', 21000),
-- ('Ірина', 'Романенко', 17500),
-- ('Олександр', 'Гриценко', 22000),
-- ('Марія', 'Савченко', 16500);





-- CREATE TABLE LECTURES (
--     ID SERIAL PRIMARY KEY,
--     LECTUREROOM VARCHAR(40) NOT NULL,
--     SUBJECTID INT NOT NULL,
--     TEACHERID INT NOT NULL,
--     FOREIGN KEY (SUBJECTID) REFERENCES SUBJECTS(ID),
--     FOREIGN KEY (TEACHERID) REFERENCES TEACHERS(ID)
-- );

-- INSERT INTO LECTURES (LECTUREROOM, SUBJECTID, TEACHERID) VALUES
-- ('A101', 1, 1),
-- ('A102', 2, 2),
-- ('B201', 3, 3),
-- ('B202', 4, 4),
-- ('C301', 5, 5),
-- ('C302', 6, 6),
-- ('D401', 7, 7),
-- ('D402', 8, 8),
-- ('E101', 9, 9),
-- ('E102', 10, 10),
-- ('A103', 11, 1),
-- ('A104', 12, 2),
-- ('B203', 13, 3),
-- ('B204', 14, 4),
-- ('C303', 15, 5),
-- ('C304', 16, 6),
-- ('D403', 17, 7),
-- ('D404', 18, 8),
-- ('E103', 19, 9),
-- ('E104', 20, 10),
-- ('A105', 21, 1),
-- ('A106', 22, 2),
-- ('B205', 23, 3),
-- ('B206', 24, 4),
-- ('C305', 25, 5),
-- ('C306', 26, 6),
-- ('D405', 27, 7),
-- ('D406', 28, 8),
-- ('E105', 29, 9),
-- ('E106', 30, 10);

-- CREATE TABLE SUBJECTS (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(100) NOT NULL UNIQUE
-- );


-- INSERT INTO SUBJECTS (NAME) VALUES
-- ('Математичний аналіз'),
-- ('Лінійна алгебра'),
-- ('Дискретна математика'),
-- ('Алгоритми та структури даних'),
-- ('Об’єктно-орієнтоване програмування'),
-- ('Бази даних'),
-- ('Операційні системи'),
-- ('Комп’ютерні мережі'),
-- ('Архітектура комп’ютерів'),
-- ('Інженерія програмного забезпечення'),
-- ('Теорія ймовірностей'),
-- ('Статистика'),
-- ('Фізика'),
-- ('Хімія'),
-- ('Філософія'),
-- ('Історія України'),
-- ('Англійська мова'),
-- ('Українська мова'),
-- ('Економічна теорія'),
-- ('Фінанси'),
-- ('Маркетинг'),
-- ('Менеджмент'),
-- ('Кібербезпека'),
-- ('Штучний інтелект'),
-- ('Машинне навчання'),
-- ('Комп’ютерна графіка'),
-- ('Веб-розробка'),
-- ('Мобільна розробка'),
-- ('Системний аналіз'),
-- ('Теорія баз даних');


-- CREATE TABLE GROUPSLECTURES (
--     ID SERIAL PRIMARY KEY,
--     GROUPID INT NOT NULL,
--     LECTUREID INT NOT NULL,
--     FOREIGN KEY (GROUPID) REFERENCES GROUPS(ID),
--     FOREIGN KEY (LECTUREID) REFERENCES LECTURES(ID)
-- );




-- INSERT INTO GROUPSLECTURES (GROUPID, LECTUREID) VALUES
-- (1, 1),
-- (1, 2),
-- (2, 3),
-- (2, 4),
-- (3, 5),
-- (3, 6),
-- (4, 7),
-- (4, 8),
-- (5, 9),
-- (5, 10),
-- (6, 11),
-- (6, 12),
-- (7, 13),
-- (7, 14),
-- (8, 15),
-- (8, 16),
-- (9, 17),
-- (9, 18),
-- (10, 19),
-- (10, 20),
-- (11, 21),
-- (11, 22),
-- (12, 23),
-- (12, 24),
-- (13, 25),
-- (13, 26),
-- (14, 27),
-- (14, 28),
-- (15, 29),
-- (15, 30);



-- 1. Виведіть усі можливі пари рядків викладачів і груп.


-- SELECT T.ID, T.NAME, T.SURNAME, G.ID, G.NAME
-- FROM TEACHERS T, GROUPS G


-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких перевищує фонд фінансування факультету.


-- SELECT F.NAME
-- FROM FACULTIES F
-- JOIN DEPARTMENTS D ON D.FACULTYID = F.ID
-- WHERE D.FINANCING > F.FINANCING


-- 3. Виведіть прізвища кураторів груп і назви груп, які вони
-- курирують.
-- SELECT C.SURNAME, G.NAME
-- FROM CURATORS C
-- JOIN GROUPSCURATORS GC ON GC.CURATORID = C.ID
-- JOIN GROUPS G ON G.ID = GC.GROUPID

-- 4. Виведіть імена та прізвища викладачів, які читають лекції
-- у групі «P107».

-- SELECT T.NAME, T.SURNAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON L.TEACHERID = T.ID
-- JOIN GROUPSLECTURES GL ON GL.LECTUREID = L.ID
-- JOIN GROUPS G ON G.ID = GL.GROUPID
-- WHERE G.NAME = 'PI-21'


-- 5. Виведіть прізвища викладачів і назви факультетів, на яких
-- вони читають лекції.





-- 6. Виведіть назви кафедр і назви груп, які до них належать.

-- SELECT D.NAME, G.NAME
-- FROM DEPARTMENTS D
-- JOIN GROUPS G ON G.DEPARTMENTID = D.ID;

-- 7. Виведіть назви предметів, які викладає викладач «Samantha
-- Adams».

-- SELECT S.NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON L.TEACHERID = T.ID
-- JOIN SUBJECTS S ON S.ID = L.SUBJECTID
-- WHERE T.NAME = 'Samantha' AND T.SURNAME = 'Adams';


-- 8. Виведіть назви кафедр, на яких викладається дисципліна
-- «Database Theory».



-- 9. Виведіть назви груп, що належать до факультету «Computer
-- Science».

-- SELECT G.NAME
-- FROM GROUPS G
-- JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENTID
-- JOIN FACULTIES F ON F.ID = D.FACULTYID
-- WHERE F.NAME = 'Факультет інформаційних технологій';


-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів,
-- до яких вони належать.

-- SELECT G.NAME, F.NAME
-- FROM GROUPS G
-- JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENTID
-- JOIN FACULTIES F ON F.ID = D.FACULTYID
-- WHERE G.YEAR = 4;


-- 11. Виведіть повні імена викладачів і лекції, які вони читають
-- (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B103».





