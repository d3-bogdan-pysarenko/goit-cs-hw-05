-- Отримати всі завдання, які ще не завершено
SELECT * 
FROM 
    tasks 
WHERE 
    status_id != (
        SELECT 
            id 
        FROM 
            status 
        WHERE 
            name = 'completed'
        );
