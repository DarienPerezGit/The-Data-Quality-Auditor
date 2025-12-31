-- Demostración de validación vía SQL
-- 1. Encontrar duplicados
SELECT id, COUNT(*) 
FROM sales_table 
GROUP BY id 
HAVING COUNT(*) > 1;

-- 2. Encontrar emails inválidos
SELECT * FROM sales_table 
WHERE email NOT LIKE '%_@__%.__%';

-- 3. Calcular total de ventas limpias (filtrando errores)
SELECT SUM(ventas) as Revenue_Total
FROM sales_table
WHERE ventas > 0;
