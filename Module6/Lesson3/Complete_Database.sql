-- Родительские категории
INSERT INTO dictionaries (name, code, description)
VALUES
  ('Progress Status', 'prs', 'Статусы изучения ресурсов'),
  ('Resource Type', 'res', 'Типы образовательных ресурсов'),
  ('Skill Type', 'skl', 'Типы навыков'),
  ('Grade', 'grd', 'Грейды ролей');

-- Статусы прогресса
INSERT INTO dictionaries (name, code, description, parent_id)
VALUES
  ('Planned', 'pln', 'Планируется к изучению', (SELECT id FROM dictionaries WHERE code = 'prs')),
  ('In Progress', 'prg', 'В процессе изучения', (SELECT id FROM dictionaries WHERE code = 'prs')),
  ('Completed', 'cmp', 'Завершено', (SELECT id FROM dictionaries WHERE code = 'prs'));

-- Типы ресурсов
INSERT INTO dictionaries (name, code, description, parent_id)
VALUES
  ('Video', 'vid', 'Видеоматериал', (SELECT id FROM dictionaries WHERE code = 'res')),
  ('Article', 'art', 'Статья или пост', (SELECT id FROM dictionaries WHERE code = 'res')),
  ('Course', 'crs', 'Полноценный курс', (SELECT id FROM dictionaries WHERE code = 'res'));

-- Типы скиллов
INSERT INTO dictionaries (name, code, description, parent_id)
VALUES
  ('Hard Skill', 'hrd', 'Технический навык', (SELECT id FROM dictionaries WHERE code = 'skl')),
  ('Soft Skill', 'sft', 'Гибкий навык', (SELECT id FROM dictionaries WHERE code = 'skl'));

-- Грейды ролей
INSERT INTO dictionaries (name, code, description, parent_id)
VALUES
  ('Junior', 'jr', 'Начальный уровень', (SELECT id FROM dictionaries WHERE code = 'grd')),
  ('Middle', 'mid', 'Средний уровень', (SELECT id FROM dictionaries WHERE code = 'grd')),
  ('Senior', 'sr', 'Продвинутый уровень', (SELECT id FROM dictionaries WHERE code = 'grd')),
  ('Lead', 'ld', 'Руководящий уровень', (SELECT id FROM dictionaries WHERE code = 'grd'));

-- Разработчик
INSERT INTO roles (name, description, grade_id)
VALUES
  ('Junior Developer', 'Начинающий разработчик', (SELECT id FROM dictionaries WHERE code = 'jr')),
  ('Middle Developer', 'Разработчик среднего уровня', (SELECT id FROM dictionaries WHERE code = 'mid')),
  ('Senior Developer', 'Опытный разработчик', (SELECT id FROM dictionaries WHERE code = 'sr')),
  ('Lead Developer', 'Технический лидер команды разработки', (SELECT id FROM dictionaries WHERE code = 'ld'));

-- Аналитик
INSERT INTO roles (name, description, grade_id)
VALUES
  ('Junior Analyst', 'Начинающий аналитик', (SELECT id FROM dictionaries WHERE code = 'jr')),
  ('Middle Analyst', 'Аналитик среднего уровня', (SELECT id FROM dictionaries WHERE code = 'mid')),
  ('Senior Analyst', 'Опытный аналитик', (SELECT id FROM dictionaries WHERE code = 'sr')),
  ('Lead Analyst', 'Руководитель аналитического направления', (SELECT id FROM dictionaries WHERE code = 'ld'));

-- Тестировщик
INSERT INTO roles (name, description, grade_id)
VALUES
  ('Junior Tester', 'Начинающий тестировщик', (SELECT id FROM dictionaries WHERE code = 'jr')),
  ('Middle Tester', 'Тестировщик среднего уровня', (SELECT id FROM dictionaries WHERE code = 'mid')),
  ('Senior Tester', 'Опытный тестировщик', (SELECT id FROM dictionaries WHERE code = 'sr')),
  ('Lead Tester', 'Руководитель команды тестирования', (SELECT id FROM dictionaries WHERE code = 'ld'));


INSERT INTO skills (name, description, skill_type_id)
VALUES
-- Hard Skills
  ('SQL', 'Работа с базами данных', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('Python', 'Программирование на Python', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('Java', 'Разработка на Java', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('PostgreSQL', 'Работа с PostgreSQL', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('Docker', 'Контейнеризация приложений', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('Git', 'Система контроля версий', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('ETL', 'Построение процессов извлечения, трансформации и загрузки данных', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('JIRA', 'Управление задачами и проектами', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('Test Automation', 'Автоматизация тестирования', (SELECT id FROM dictionaries WHERE code = 'hrd')),
  ('API Testing', 'Тестирование API', (SELECT id FROM dictionaries WHERE code = 'hrd')),

-- Soft Skills
  ('Communication', 'Умение доносить мысли', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Teamwork', 'Работа в команде', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Problem Solving', 'Решение сложных задач', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Critical Thinking', 'Критическое мышление', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Time Management', 'Управление временем', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Presentation Skills', 'Публичные выступления', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Leadership', 'Навыки лидерства', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Interviewing', 'Навыки интервьюирования', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Documentation', 'Документирование процессов', (SELECT id FROM dictionaries WHERE code = 'sft')),
  ('Adaptability', 'Гибкость и адаптивность', (SELECT id FROM dictionaries WHERE code = 'sft'));



-- Developer
INSERT INTO role_skills (role_id, skill_id, required_level)
SELECT r.id, s.id, 3
FROM roles r
JOIN skills s ON s.name IN ('Python', 'Git', 'Docker', 'SQL', 'PostgreSQL', 'Teamwork', 'Problem Solving', 'Communication')
WHERE r.name LIKE '%Developer%';

-- Analyst
INSERT INTO role_skills (role_id, skill_id, required_level)
SELECT r.id, s.id, 2
FROM roles r
JOIN skills s ON s.name IN ('SQL', 'PostgreSQL', 'Critical Thinking', 'Communication', 'Documentation', 'Time Management', 'Presentation Skills', 'Interviewing')
WHERE r.name LIKE '%Analyst%';

-- Tester
INSERT INTO role_skills (role_id, skill_id, required_level)
SELECT r.id, s.id, 2
FROM roles r
JOIN skills s ON s.name IN ('Test Automation', 'API Testing', 'Git', 'JIRA', 'Problem Solving', 'Documentation', 'Adaptability', 'Teamwork')
WHERE r.name LIKE '%Tester%';

-- Дополнительно Lead-ролям можно дать Leadership, Time Management и Presentation Skills:
INSERT INTO role_skills (role_id, skill_id, required_level)
SELECT r.id, s.id, 5
FROM roles r
JOIN skills s ON s.name IN ('Leadership', 'Time Management', 'Presentation Skills')
WHERE r.name LIKE 'Lead%';



INSERT INTO users (name, email)
VALUES
  ('Anna Petrova', 'anna.petrova@example.com'),
  ('Ivan Ivanov', 'ivan.ivanov@example.com'),
  ('Maria Smirnova', 'maria.smirnova@example.com'),
  ('Alexey Sokolov', 'alexey.sokolov@example.com'),
  ('Elena Volkova', 'elena.volkova@example.com');



-- Привязка навыков к Anna Petrova (аналитик)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('SQL', 'Critical Thinking', 'Presentation Skills')
JOIN (VALUES (1), (2), (3)) AS lvl(level) ON TRUE
WHERE u.name = 'Anna Petrova';

-- Привязка навыков к Ivan Ivanov (разработчик)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('Python', 'Git', 'Docker', 'Problem Solving')
JOIN (VALUES (4), (3), (2), (4)) AS lvl(level) ON TRUE
WHERE u.name = 'Ivan Ivanov';

-- Привязка навыков к Maria Smirnova (тестировщик)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('Test Automation', 'API Testing', 'Adaptability')
JOIN (VALUES (2), (3), (4)) AS lvl(level) ON TRUE
WHERE u.name = 'Maria Smirnova';

-- Привязка навыков к Alexey Sokolov (BI/аналитик)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('SQL', 'Documentation', 'Time Management')
JOIN (VALUES (3), (2), (3)) AS lvl(level) ON TRUE
WHERE u.name = 'Alexey Sokolov';

-- Привязка навыков к Elena Volkova (техлид)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('Leadership', 'Git', 'Teamwork', 'Communication')
JOIN (VALUES (5), (3), (4), (5)) AS lvl(level) ON TRUE
WHERE u.name = 'Elena Volkova';




INSERT INTO resources (title, source, description, skill_id, resource_type_id)
VALUES
-- SQL
('SQL for Beginners', 'Codecademy', 'Интерактивный курс для начинающих',
 (SELECT id FROM skills WHERE name = 'SQL'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

('SQL Joins Explained Visually', 'Medium', 'Пошаговое объяснение JOIN-ов',
 (SELECT id FROM skills WHERE name = 'SQL'),
 (SELECT id FROM dictionaries WHERE code = 'art')),

-- Python
('Python Basics', 'Coursera', 'Основы Python с примерами',
 (SELECT id FROM skills WHERE name = 'Python'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

('Functions in Python', 'YouTube', 'Видео об использовании функций',
 (SELECT id FROM skills WHERE name = 'Python'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- Git
('Git для начинающих', 'Hexlet', 'Введение в систему контроля версий',
 (SELECT id FROM skills WHERE name = 'Git'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

('How Git Works', 'Atlassian', 'Статья о внутреннем устройстве Git',
 (SELECT id FROM skills WHERE name = 'Git'),
 (SELECT id FROM dictionaries WHERE code = 'art')),

-- Docker
('Docker Essentials', 'Udemy', 'Курс по основам контейнеризации',
 (SELECT id FROM skills WHERE name = 'Docker'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

('Docker vs Virtual Machines', 'YouTube', 'Сравнение подходов',
 (SELECT id FROM skills WHERE name = 'Docker'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- Critical Thinking
('Критическое мышление', 'Skillbox', 'Навык анализа информации',
 (SELECT id FROM skills WHERE name = 'Critical Thinking'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

-- Communication
('Effective Communication', 'LinkedIn Learning', 'Как общаться ясно и убедительно',
 (SELECT id FROM skills WHERE name = 'Communication'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- Teamwork
('Teamwork Skills', 'Harvard Business Review', 'Как эффективно работать в команде',
 (SELECT id FROM skills WHERE name = 'Teamwork'),
 (SELECT id FROM dictionaries WHERE code = 'art')),

-- Leadership
('Leadership Principles', 'MITx', 'Онлайн-курс для лидеров команд',
 (SELECT id FROM skills WHERE name = 'Leadership'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

-- Test Automation
('Intro to Test Automation', 'Test Automation University', 'Основы автоматизации',
 (SELECT id FROM skills WHERE name = 'Test Automation'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

-- API Testing
('API Testing with Postman', 'YouTube', 'Видеоурок по тестированию API',
 (SELECT id FROM skills WHERE name = 'API Testing'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- Documentation
('Writing Great Docs', 'Google Developers', 'Руководство по документации',
 (SELECT id FROM skills WHERE name = 'Documentation'),
 (SELECT id FROM dictionaries WHERE code = 'art')),

-- ETL
('ETL Concepts', 'Khan Academy', 'Понятие ETL и потоки данных',
 (SELECT id FROM skills WHERE name = 'ETL'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- PostgreSQL
('PostgreSQL Basics', 'PostgresPro', 'Курс для начинающих',
 (SELECT id FROM skills WHERE name = 'PostgreSQL'),
 (SELECT id FROM dictionaries WHERE code = 'crs')),

-- Presentation Skills
('Public Speaking 101', 'TEDx', 'Навыки публичных выступлений',
 (SELECT id FROM skills WHERE name = 'Presentation Skills'),
 (SELECT id FROM dictionaries WHERE code = 'vid')),

-- Time Management
('Time Management Techniques', 'Coursera', 'Как управлять своим временем',
 (SELECT id FROM skills WHERE name = 'Time Management'),
 (SELECT id FROM dictionaries WHERE code = 'crs'));





-- Для Anna Petrova
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('SQL for Beginners', 'SQL Joins Explained Visually', 'Effective Communication')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (50), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Anna Petrova';

-- Для Ivan Ivanov
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('Python Basics', 'Git для начинающих', 'Docker Essentials')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (40), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Ivan Ivanov';

-- Для Maria Smirnova
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('Intro to Test Automation', 'API Testing with Postman', 'Time Management Techniques')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (60), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Maria Smirnova';

-- Для Alexey Sokolov
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('PostgreSQL Basics', 'Writing Great Docs', 'SQL for Beginners')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (30), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Alexey Sokolov';

-- Для Elena Volkova
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('Leadership Principles', 'Public Speaking 101', 'Teamwork Skills')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (45), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Elena Volkova';
