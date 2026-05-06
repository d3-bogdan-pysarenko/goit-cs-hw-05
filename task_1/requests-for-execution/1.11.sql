-- Отримати завдання, які призначені користувачам
-- з певною доменною частиною електронної пошти

SELECT 
    tasks.*
FROM 
    tasks
JOIN 
    users 
    ON 
    tasks.user_id = users.id
WHERE 
    users.email 
    LIKE 
    '%@example.org';
