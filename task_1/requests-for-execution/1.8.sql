-- Знайти користувачів з певною електронною поштою
SELECT * 
FROM 
    users 
WHERE 
    email 
    LIKE 
    '%@example.org';
