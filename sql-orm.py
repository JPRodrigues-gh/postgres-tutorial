from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instruction from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create variable for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Create variable for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create variable for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("album_table.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens actual session by calling the Session() subclass defined above
session = Session()

# creating the database using the declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all rows from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=' | ')

# Query 2 - select "Name" from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select all rows from the "Artist" table
# where the "Artist" "Name" is 'Queen'
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# Query 4 - select all rows from the "Artist" table
# where the "ArtistId" is 51
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# Query 5: Select rows from the "Album" table
# where the "ArtistId" is 51
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=' | ')

# Query 6: Select tracks where Composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.Composer,
        track.UnitPrice,
        sep=' | ')
