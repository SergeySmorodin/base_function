-- Создание таблицы Исполнитель 
CREATE TABLE Artist (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Создание таблицы Жанр 
CREATE TABLE Genre (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Создание таблицы Исполнитель_Жанр 
CREATE TABLE ArtistGenre (
    ID SERIAL PRIMARY KEY,
    ArtistID INT REFERENCES Artist(ID) ON DELETE CASCADE,
    GenreID INT REFERENCES Genre(ID) ON DELETE CASCADE,
    UNIQUE (ArtistID, GenreID)  
);

-- Создание таблицы Альбом
CREATE TABLE Album (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    ReleaseYear INT
);

-- Создание таблицы Исполнитель_Альбом 
CREATE TABLE ArtistAlbum (
    ID SERIAL PRIMARY KEY,
    ArtistID INT REFERENCES Artist(ID) ON DELETE CASCADE,
    AlbumID INT REFERENCES Album(ID) ON DELETE CASCADE,
    UNIQUE (ArtistID, AlbumID)
);

-- Создание таблицы Трек 
CREATE TABLE Track (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Duration INT,  
    AlbumID INT REFERENCES Album(ID) ON DELETE CASCADE
);

-- Создание таблицы Сборник 
CREATE TABLE Compilation (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    ReleaseYear INT
);

-- Создание таблицы Сборник_Трек
CREATE TABLE CompilationTrack (
    ID SERIAL PRIMARY KEY,
    CompilationID INT REFERENCES Compilation(ID) ON DELETE CASCADE,
    TrackID INT REFERENCES Track(ID) ON DELETE CASCADE,
    UNIQUE (CompilationID, TrackID)  
);
