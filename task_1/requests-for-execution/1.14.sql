-- Отримати користувачів та кількість їхніх завдань

SELECT 
    users.id, 
    users.fullname, 
    COUNT(tasks.id) AS task_count
FROM 
    users
LEFT JOIN 
    tasks 
    ON 
    users.id = tasks.user_id
GROUP BY 
    users.id, 
    users.fullname;
