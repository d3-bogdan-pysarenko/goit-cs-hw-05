-- Отримати список користувачів, які не мають жодного завдання
SELECT * 
FROM 
    users 
WHERE 
    id NOT IN (
    SELECT DISTINCT 
        user_id 
    FROM 
        tasks
    );
