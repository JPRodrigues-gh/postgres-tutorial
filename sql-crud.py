from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instruction from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# creat a class-based model for the "Favorite_Places" table
class Favorite_Places(base):
    __tablename__ = "Favorite_Places"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens actual session by calling the Session() subclass defined above
session = Session()

# creating the database using the declarative_base subclass
base.metadata.create_all(db)

# creating records for our "Programmer" table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners = Programmer(
    first_name="Tim",
    last_name="Berners",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

jp_rodrigues = Programmer(
    first_name="JP",
    last_name="Rodrigues",
    gender="M",
    nationality="World",
    famous_for="Programmer"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners)
# session.add(jp_rodrigues)

# Update a single record
# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "World President"

# creating records for our "Favorite_Places" table
portugal = Favorite_Places(
    country_name="Portugal",
    capital_city="Lisbon",
    population="10310000"
)

spain = Favorite_Places(
    country_name="Spain",
    capital_city="Madrid",
    population="47350000"
)

south_africa = Favorite_Places(
    country_name="South Africa",
    capital_city="Johannesburg",
    population="59310000"
)

# add each instance of our "Favorite_Places" to our session
# session.add(portugal)
# session.add(spain)
# session.add(south_africa)

# commit our session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == 'F':
#         person.gender = "Female"
#     elif person.gender == 'M':
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# deleting multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )

favorite_places = session.query(Favorite_Places)
for favorite_place in favorite_places:
    print(
        favorite_place.id,
        favorite_place.country_name,
        favorite_place.capital_city,
        favorite_place.population,
        sep=" | "
    )
