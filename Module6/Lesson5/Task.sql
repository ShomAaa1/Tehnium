CREATE OR REPLACE PROCEDURE update_progress_bulk(
    p_resource_id INT,
    p_increment INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_updated_count INT;
BEGIN
    -- обновляем прогресс
    UPDATE user_resource_progress
    SET progress_percent = LEAST(progress_percent + p_increment, 100)
    WHERE resource_id = p_resource_id;

    -- сколько строк обновили
    GET DIAGNOSTICS v_updated_count = ROW_COUNT;

    -- выводим сообщение
    RAISE NOTICE 'Обновлено % строк(и) по ресурсу %', v_updated_count, p_resource_id;
END;
$$;
CALL update_progress_bulk(1, 15);

-- задание 2
CREATE OR REPLACE FUNCTION get_user_skill_level(p_user_id int, p_skill_id int)
RETURNS int AS $$
DECLARE
    v_level int;
BEGIN
    SELECT MAX(level)
    INTO v_level
    FROM user_skills
    WHERE user_id = p_user_id AND skill_id = p_skill_id;

    IF v_level IS NULL THEN
        RETURN 0;
    END IF;

    RETURN v_level;
END;
$$ LANGUAGE plpgsql;

SELECT get_user_skill_level(3, 9);

-- задание 3
CREATE TABLE user_skills_log (
    id int,
    user_id int,
    skill_id int,
    level int,
    updated_at timestamp,
    operation text
);

CREATE OR REPLACE FUNCTION log_user_skills_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO user_skills_log (id, user_id, skill_id, level, updated_at, operation)
        VALUES (NEW.id, NEW.user_id, NEW.skill_id, NEW.level, NEW.updated_at, 'insert');
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO user_skills_log (id, user_id, skill_id, level, updated_at, operation)
        VALUES (NEW.id, NEW.user_id, NEW.skill_id, NEW.level, NEW.updated_at, 'update');
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_user_skills_log
AFTER INSERT OR UPDATE ON user_skills
FOR EACH ROW
EXECUTE FUNCTION log_user_skills_changes();

SELECT * FROM user_skills_log;

INSERT INTO user_skills (id, user_id, skill_id, level, updated_at)
VALUES (100, 1, 2, 5, NOW());

SELECT * FROM user_skills_log WHERE id = 100;

UPDATE user_skills
SET level = 7, updated_at = NOW()
WHERE id = 100;

SELECT * FROM user_skills_log WHERE id = 100 ORDER BY updated_at;

-- задание 4
CREATE INDEX idx_user_skills_user_id ON user_skills(user_id);

EXPLAIN ANALYZE
SELECT * FROM user_skills WHERE user_id = 1 AND skill_id = 2;

CREATE INDEX idx_user_skills_user_skill ON user_skills(user_id, skill_id);

EXPLAIN ANALYZE
SELECT * FROM user_resource_progress WHERE resource_id = 5 AND progress_percent < 100;

CREATE INDEX idx_progress_resource_percent
ON user_resource_progress(resource_id, progress_percent);
EXPLAIN ANALYZE
SELECT * FROM user_resource_progress WHERE resource_id = 5 AND progress_percent < 100;

EXPLAIN ANALYZE
SELECT * FROM users WHERE LOWER(email) = 'test@email.com';

CREATE INDEX idx_users_email_lower ON users(LOWER(email));
EXPLAIN ANALYZE
SELECT * FROM users WHERE LOWER(email) = 'test@email.com';

EXPLAIN ANALYZE
SELECT user_id, progress_percent
FROM user_resource_progress
WHERE resource_id = 5;

CREATE INDEX idx_progress_resource_cover
ON user_resource_progress(resource_id, user_id, progress_percent);
EXPLAIN ANALYZE
SELECT user_id, progress_percent
FROM user_resource_progress
WHERE resource_id = 5;
