from click import DateTime
import sqlite3
from .DatabaseConnection import DatabaseConnection
from os import path
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path):
        #Check if the database exists
        db_exists = path.exists(db_path)
        #Create the object that represents the connection to the database
        self.DatabaseConnection = DatabaseConnection(db_path)
        #if the database does not exist before a connection object is made, init the tables
        if not db_exists:
            self.Init_Database()

    def Init_Database(self):
        with self.DatabaseConnection as conn:
            #create the table for the parent metadata class as well as the child classes
            conn.executescript("""
            CREATE TABLE IF NOT EXISTS MetaData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            file_path TEXT NOT NULL,
            file_size INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
            
            CREATE TABLE IF NOT EXISTS GameData(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT,
            FOREIGN KEY (id) REFERENCES MetaData(id) ON DELETE CASCADE);
                """)

    def insert_metadata(self, title, description, file_path, file_size):
        try:
            with self.DatabaseConnection as conn:
                conn.execute(
                    """
                    Insert INTO MetaData (title,description,file_path,file_size,created_at,updated_at)
                    VALUES(?,?,?,?,?,?)
                    """, (title, description,file_path,file_size, datetime.now(), datetime.now()))
            return conn.lastrowid
        except sqlite3.Error as e:
            print(f"SQL Exception: {e}")
            return False

    def delete_data(self, id):
        with self.DatabaseConnection as conn:
            conn.execute("""
            DELETE FROM MetaData WHERE id = ?
            """, (id,))
            return conn.rowcount > 0

    def update_metadata_full(self, data):
        """Update all metadata fields"""
        with self.DatabaseConnection as conn:
            conn.execute("""
                           UPDATE MetaData
                           SET title       = ?,
                               description = ?,
                               updated_at  = CURRENT_TIMESTAMP
                           WHERE id = ?
                           """, data)

            return conn.rowcount > 0


    def insert_game(self, image_url, metadata_id):
        try:
            with self.DatabaseConnection as conn:
                conn.execute("""
                INSERT INTO GameData(image_url,id)
                VALUES(?,?)
                """,(image_url,metadata_id))
                return True
        except sqlite3.Error as e:
            print(f"SQL Exception: {e}")
            return False

    def select_all_games(self):
        try:
            with self.DatabaseConnection as conn:
                conn.execute("""
                SELECT * FROM GameData g
                JOIN MetaData m on g.id = m.id
                ORDER BY m.created_at DESC
                """)
                return conn.fetchall()
        except sqlite3.Error as e:
            print(f"SQL exception: {e}")
            return None

    def select_game(self, id):
        try:
            with self.DatabaseConnection as conn:
                conn.execute("""
                SELECT * FROM GameData g
                JOIN MetaData m on g.id = m.id
                WHERE g.id = ?
                """, (id,))
                return conn.fetchone()
        except sqlite3.Error as e:
            print(f"SQL Exception: {e}")
            return None

    def update_game(self, data):
        with self.DatabaseConnection as conn:
            conn.execute("""
            UPDATE GameData
            SET image_url = ?
            WHERE id = ?
            """, data)
            return conn.rowcount > 0
