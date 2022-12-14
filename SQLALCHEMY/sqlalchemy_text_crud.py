from sqlalchemy import create_engine,text

connection_string = "sqlite:/// Northwind_small.sqlite"
engine = create_engine(connection_string,echo = False)

def create():
    insert = text("""
                    INSERT INTO "main"."Employee"
                    ("LastName","FirstName","Title","BirthDate")
                    VALUES(:last, :first, :title, :dob);
                    """)

    with engine.connect() as con:
        con.execute(insert,{"last":"Davolio","first":"Nancy","title":"Sales","dob":"1980-05-06"})
        new_id = con.execute(text("SELECT last_insert_rowid() AS Id;")).first()
        print(new_id)
        return new_id["Id"]

def read(id):
    select = text("""
                    SELECT Id,LastName, FirstName , Title , BirthDate
                    FROM Employee
                    WHERE LastName = :last AND FirstName IS NOT :first AND Id = :id 
                """)

    with engine.connect() as con:
        for row in con.execute(select, {"last":"Davolio","first":"Robert","id":{id}}):
            print(row)
            print(row['LastName'])

def update(id):
    update = text("""
                    UPDATE Employee
                    SET LastName = :last,
                    FirstName = :first
                    WHERE Id = :id
                """)

    with engine.connect() as con:
        con.execute(update,{"last":"D'Avolio","first":"Patricia","id":id})

    with engine.connect() as con2:
        for row in con2.execute("SELECT Id,LastName,FirstName FROM Employee WHERE id = :id",{"id":id}):
            print(row)

def delete(id):
    delete = text("""
                    DELETE FROM Employee WHERE Id = :id
                """)
            
    connection_string = "sqlite:/// Northwind_small.sqlite"
    engine = create_engine(connection_string,echo = False)
    with engine.connect() as con:
        con.execute(delete,{"id":id})
