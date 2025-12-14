import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="fraud_detection",
        user="postgres",
        password="password"
    )
    cursor = conn.cursor()
    print("PostgreSQL Connected")
except Exception as e:
    print("Connection Error:", e)
