import sqlite3

# Create the videos table if it doesn't already exist.
def create_videos_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')
    cursor.connection.commit()  # Commit the changes to the database

# Inserts multiple video entries into the videos table.
def save_videos_to_db(video_info_list, cursor):
    cursor.executemany('''
        INSERT INTO videos (title, url)
        VALUES (?, ?)
    ''', [(video['title'], video['url']) for video in video_info_list])
    
    cursor.connection.commit()  # Commit the changes to the database


# Create the video_meta table if it doesn't already exist.
def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS video_meta (
            id TEXT PRIMARY KEY,
            publishedAt TEXT,
            channelId TEXT,
            description TEXT,
            likes INTEGER,
            dislikes INTEGER,
            views INTEGER,
            favorites INTEGER,
            comments INTEGER,
            duration TEXT,
            thumbnail TEXT
        )
    ''')
    cursor.connection.commit()  # Commit the changes to the database


# Function to insert metadata into the database
def save_to_db(meta, cursor):
    cursor.execute('''
        INSERT INTO video_meta 
        (id, publishedAt, channelId, description, likes, dislikes, views, favorites, comments, duration, thumbnail)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        meta['id'],
        meta['publishedAt'],
        meta['channelId'],
        meta['description'],
        meta['likes'],
        meta['dislikes'],
        meta['views'],
        meta['favorites'],
        meta['comments'],
        meta['duration'],
        meta.get('thumbnail', 'Not available')  # Ensure thumbnail is included
    ))
    cursor.connection.commit()

