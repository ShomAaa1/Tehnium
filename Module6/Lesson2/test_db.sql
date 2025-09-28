CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	age INT NOT NULL CHECK (age>=14)
);

CREATE TABLE courses(
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	teacher VARCHAR(100)
);

CREATE TABLE enrollments (
	id SERIAL PRIMARY KEY,
	student_id INT NOT NULL,
	course_id INT NOT NULL,
	status VARCHAR(50),
	UNIQUE(student_id, course_id),
	FOREIGN KEY (student_id) REFERENCES students(id),
	FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students (name, email, age) VALUES
('Иван Иванов', 'ivan@example.com', 18),
('Мария Петрова', 'maria@example.com', 20),
('Алексей Сидоров', 'alex@example.com', 15)

INSERT INTO courses (title, teacher) VALUES
('Математика', 'Смирнов А. А.'),
('Физика', 'Кузнецова В. Ю.'),
('Программирование', 'Иванова К. В.');

INSERT INTO enrollments(student_id, course_id, status) VALUES
(1, 1, 'В процессе'),
(1, 3, 'Завершен'),
(2, 2, 'В процессе'),
(3, 1, 'В процессе');

INSERT INTO students (name, email, age) VALUES
('Петр Петров', 'ivan@example.com', 19);

INSERT INTO students(name, email, age) VALUES
('Маленький Вася', 'vasya@example.com', 12);

INSERT INTO enrollments (student_id, course_id, status) VALUES
(2, 999, 'В процессе');

SELECT s.name AS student_name, c.title AS course_title, e.status
FROM enrollments e
INNER JOIN students s ON e.student_id = s.id
INNER JOIN courses c ON e.course_id = c.id;

INSERT INTO courses (title, teacher) VALUES
('Химия', 'Смирнова Е. А.');

SELECT c.title AS course_title, s.name AS student_name, e.status
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
LEFT JOIN students s ON e.student_id = s.id
ORDER BY c.id;

SELECT s.name AS student_name, c.title AS course_title
FROM students s
CROSS JOIN courses c;