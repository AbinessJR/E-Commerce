/*Total Sales by Month*/
SELECT strftime('%Y-%m', sale_date) AS month, SUM(sale_amount) AS total_sales
FROM Sales
GROUP BY month;
/*Consumer Segmentation*/
SELECT CASE
    WHEN total_sales < 1000 THEN 'Low Value'
    WHEN total_sales < 5000 THEN 'Medium Value'
    ELSE 'High Value'
END AS customer_segment, COUNT(*) AS customer_count
FROM (
    SELECT customer_id, SUM(sale_amount) AS total_sales
    FROM Sales
    GROUP BY customer_id
)
GROUP BY customer_segment;
