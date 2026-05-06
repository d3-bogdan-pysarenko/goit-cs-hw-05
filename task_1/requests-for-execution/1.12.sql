-- Отримати список завдань, що не мають опису

SELECT * 
FROM 
    tasks 
WHERE 
    description 
    IS NULL 
    OR 
    description = '';
