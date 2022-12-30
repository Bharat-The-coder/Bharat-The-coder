import psycopg2
try:
    conn = psycopg2.connect(database="postgres",user="postgres",password="Bharat@232",host="localhost",port='5432')
    conn.autocommit = True
    #cursor.execute("DROP Database IF EXISTS project")
    sql = "CREATE database project"
    cursor.execute(sql)
    conn.close()
except:
    print("connection failed or Database already Exists")
cursor=conn.cursor()
try:
    conn = psycopg2.connect(database="project",user="postgres",password="Bharat@232",host="localhost",port='5432')
    #Creating a database
    cursor.execute("DROP TABLE IF EXISTS product2")
    #Creating table as per requirement
    sql ='''CREATE TABLE product(
    id text NOT NULL,
    name text NOT NULL,
    type text NOT NULL,
    quantity integer NOT NULL,
    price integer NOT NULL,
    company_name text NOT NULL,
    date date NOT NULL
    );'''
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully........")
except:
    print("Eroor! while creating a table........")