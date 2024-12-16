import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="interview_hell",
        user="postgres",
        password="zaq12WSX",
        host="localhost",
        port="5432"
    )
