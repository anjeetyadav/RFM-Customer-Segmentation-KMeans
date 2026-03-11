-- Total Revenue
SELECT SUM(sales) AS total_revenue
FROM ecommerce_sales;

-- Monthly Sales Trend
SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,
       SUM(sales) AS monthly_sales
FROM ecommerce_sales
GROUP BY month
ORDER BY month;

-- Top 10 Products by Revenue
SELECT product_name,
       SUM(sales) AS revenue
FROM ecommerce_sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by Category
SELECT category,
       SUM(sales) AS category_revenue
FROM ecommerce_sales
GROUP BY category
ORDER BY category_revenue DESC;

-- Top Customers
SELECT customer_id,
       SUM(sales) AS total_spent
FROM ecommerce_sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
