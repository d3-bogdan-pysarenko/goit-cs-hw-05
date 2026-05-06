-- Отримати список завдань, що не мають опису

SELECT 
    users.*,
    tasks.*
FROM 
    users
INNER JOIN 
    tasks 
    ON 
    users.id = tasks.user_id
INNER JOIN 
    status 
    ON tasks.status_id = status.id
WHERE 
    status.name = 'in progress';
