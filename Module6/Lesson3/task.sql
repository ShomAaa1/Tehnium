INSERT INTO users (name, email)
VALUES ('Dmitry Kuznetsov', 'dmitry.kuznetsov@example.com');

INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('Python', 'PostgreSQL', 'Teamwork')
JOIN (VALUES (3), (2), (4)) AS lvl(level) ON TRUE
WHERE u.name = 'Dmitry Kuznetsov';

INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE,
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('Python Basics', 'PostgreSQL Basics', 'Teamwork Skills')
JOIN dictionaries d ON d.code IN ('prg', 'cmp', 'pln')
JOIN (VALUES (70), (100), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Dmitry Kuznetsov';

SELECT *
FROM users
WHERE (name LIKE 'A%' OR name LIKE '%ov')
  AND email IS NOT NULL
  AND email <> '';

SELECT *
FROM (
    SELECT *
    FROM resources
    ORDER BY id DESC
    LIMIT 3
) AS last_resources
ORDER BY title ASC;

SELECT user_id, COUNT(skill_id) AS skill_count
FROM user_skills
GROUP BY user_id
HAVING COUNT(skill_id) > 2;

SELECT
    COUNT(*) AS total_users,                                -- всего пользователей
    COUNT(email) AS users_with_email,                       -- сколько указали email (NULL не учитывается)
    AVG(LENGTH(email))::NUMERIC(10,2) AS avg_email_length   -- средняя длина email
FROM users;

