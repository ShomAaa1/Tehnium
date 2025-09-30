INSERT INTO users (name, email)
VALUES
  ('12345', 'test1@example.com'),
  ('Sasssha', 'test1@example.com'),
  ('Maaaax', 'test2@example.com');

INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at)
VALUES
  ( (SELECT id FROM users WHERE name='12345'), 1, (SELECT id FROM dictionaries WHERE name='In Progress'), 10, NOW() ),
  ( (SELECT id FROM users WHERE name='Maaaax'), 2, (SELECT id FROM dictionaries WHERE name='In Progress'), 30, NOW() );

SELECT DISTINCT u.id, u.name, u.email, r.title AS resource_title, d.name AS status_name
FROM users u
JOIN user_resource_progress urp ON u.id = urp.user_id
JOIN dictionaries d ON urp.status_id = d.id
JOIN resources r ON urp.resource_id = r.id
WHERE d.name = 'In Progress'
  AND (
        u.name ~ '^[0-9]+$'    -- имя только из цифр
        OR u.name ~ '(.)\1\1'  -- три одинаковых символа подряд
      );

INSERT INTO users (name, email)
VALUES ('123456', 'bad.user@example.com');

INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
VALUES (
    (SELECT id FROM users WHERE name = '123456'),
    (SELECT id FROM resources LIMIT 1),
    (SELECT id FROM dictionaries WHERE code = 'cmp'), -- статус Completed
    100,
    CURRENT_DATE,
    CURRENT_DATE
);

WITH user_progress AS (
    SELECT
        u.id AS user_id,
        u.name AS user_name,
        r.title AS resource_title,
        urp.progress_percent
    FROM user_resource_progress urp
    JOIN users u ON urp.user_id = u.id
    JOIN resources r ON urp.resource_id = r.id
)
SELECT
    user_id,
    user_name,
    resource_title,
    progress_percent,
    COUNT(*) OVER (PARTITION BY user_id) AS total_resources,          -- 1. количество ресурсов
    AVG(progress_percent) OVER (PARTITION BY user_id) AS avg_progress, -- 2. средний прогресс
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY progress_percent DESC) AS resource_order, -- 3. номер по убыванию
    progress_percent - LAG(progress_percent) OVER (PARTITION BY user_id ORDER BY progress_percent DESC) AS diff_from_prev -- 4. разница с предыдущим
FROM user_progress
ORDER BY user_id, resource_order;

CREATE OR REPLACE VIEW user_progress_overview AS
WITH user_progress AS (
    SELECT
        u.id AS user_id,
        u.name AS user_name,
        COUNT(*) AS total_resources,
        COUNT(*) FILTER (WHERE d.code = 'cmp') AS completed_resources,
        ROUND(AVG(urp.progress_percent)::numeric, 1) AS avg_progress
    FROM users u
    JOIN user_resource_progress urp ON u.id = urp.user_id
    JOIN dictionaries d ON urp.status_id = d.id
    GROUP BY u.id, u.name
)
SELECT *
FROM user_progress;

SELECT * FROM user_progress_overview;

