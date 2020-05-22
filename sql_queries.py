# DROP TABLES

song_library_session_drop = "DROP TABLE IF EXISTS song_library_session"
song_playlist_session_drop = "DROP TABLE IF EXISTS song_playlist_session"
user_song_history_drop = "DROP TABLE IF EXISTS user_song_history"

# CREATE TABLES

song_library_session_create = """CREATE TABLE IF NOT EXISTS song_library_session
                                  (sessionId int, itemInSession int, 
                                  artist varchar, song varchar, length float,
                                  PRIMARY KEY (sessionId, itemInSession))
                                  """

song_playlist_session_create = """CREATE TABLE IF NOT EXISTS song_playlist_session
                                  (userId int, sessionId int, 
                                  artist varchar, song varchar, itemInSession int, 
                                  first_name varchar, last_name varchar,
                                  PRIMARY KEY ((userId, sessionId), itemInSession))
                                  """

user_song_history_create = """CREATE TABLE IF NOT EXISTS user_song_history 
                                (song varchar, userId int, first_name varchar, last_name varchar,
                                PRIMARY KEY (song, userId))
                            """

# INSERT RECORDS
song_library_session_insert = "INSERT INTO song_library_session(sessionId, itemInSession, artist, " \
                              "song, length)" \
                              "VALUES (%s, %s, %s, %s, %s)"

song_playlist_session_insert = "INSERT INTO song_playlist_session(userId, sessionId, itemInSession," \
                               " artist, song, first_name, last_name)" \
                               "VALUES (%s, %s, %s, %s, %s, %s, %s)"

user_song_history_insert = "INSERT INTO user_song_history(song, userId, first_name, last_name)" \
                           "VALUES (%s, %s, %s, %s)"

# SELECT queries

query1 = "SELECT artist, song, length FROM song_library_session " \
         "WHERE sessionId=338 AND itemInSession=4;"

query2 = "SELECT artist, song, first_name, last_name FROM song_playlist_session " \
         "WHERE userId=10 AND sessionId=182"

query3 = "SELECT first_name, last_name FROM user_song_history " \
         "WHERE song='All Hands Against His Own'"

# QUERIES QUEUE
create_table_queries = [song_library_session_create, song_playlist_session_create, user_song_history_create]
drop_table_queries = [song_library_session_drop, song_playlist_session_drop, user_song_history_drop]
