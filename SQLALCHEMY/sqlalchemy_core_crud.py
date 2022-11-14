from sqlalchemy import MetaData,Table,Column,String,Integer,create_engine
from sqlalchemy import Text,DateTime,Boolean,select,insert,update,delete,or_,and_

connection_string = "sqlite:///Northwind_small.sqlite"
engine = create_engine(connection_string,echo = False)

metadate = MetaData()
employees = Table('Employee',metadate,
                    Column('Id',Integer,primary_key = True),
                    Column ('LastName',String(8000)),
                    Column('FirstName',String(8000)),
                    Column('BirthDate',String(8000))
                )

def show_metadata():
    for t in metadate.sorted_tables:
        print(f"Table {t.name}:")
        for c in t.columns:
            print(f"{c} ({c.type})")

def do_insert():
    stmt = employees.insert().values(
        LastName = 'Collins',
        FirstName = 'Arnold',
        BirthDate = '2000-07-04'
    )
    new_id = 0

    with engine.connect() as con:
        result = con.execute(stmt)
        new_id = result.inserted_primary_key['Id']
        print(f"New Id : {new_id}")
    
    return new_id

def select_by_id():
    stmt = employees.select().where(employees.c.Id == id)

    with engine.connect() as con:
        result = con.execute(stmt).first()
        if result:
            print(result)
        else:
            print(f" no rows found with Id == {id}")


def do_update(id):
    stmt = employees.update().values(
        FirstName = "Michael"
    ).where(employees.c.Id == id)

    with engine.connect() as con:
        con.execute(stmt)

def do_delete(id):
     stmt = employees.delete().where(employees.c.Id == id)

     with engine.connect() as con:
        con.execute(stmt)

def statment_infos():
    stmt = employees.select(employees.c.LastName,employees.c.FirstName).where(employees.c.Id == 30)
    print(f"statment with placehoder: \n{str(stmt)}")
    print(f"\nparams: \n{str(stmt.compile().params)}")


if __name__ == '__main__':
    print("---show_metadata()-----")
    show_metadata()
    print("-----do_insert()-------")
    id = do_insert
    select_by_id(id)
    print("-----do_update()--------")
    id = do_update
    select_by_id(id)
    print("---do_delete()-----")
    id = do_delete
    select_by_id(id)
    print("-------end()-------")
    

