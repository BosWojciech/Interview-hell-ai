import psycopg

def connect_db():
    return psycopg.connect(
        dbname="interviewhellai",
        user="postgres",
        password="zaq12WSX",
        host="localhost",
        port="5432"
    )
