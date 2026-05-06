-- Отримати кількість завдань для кожного статусу
SELECT 
    status.name, COUNT(tasks.id) AS task_count
FROM 
    status
LEFT JOIN 
    tasks 
    ON 
    status.id = tasks.status_id
GROUP BY 
    status.name;
