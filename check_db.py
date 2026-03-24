#!/usr/bin/env python3
import sqlite3

def check_database():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Check tables
        tables = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        print("Tables:", [t[0] for t in tables])
        
        # Check chat_history table structure
        if 'chat_history' in [t[0] for t in tables]:
            columns = c.execute("PRAGMA table_info(chat_history)").fetchall()
            print("chat_history columns:")
            for col in columns:
                print(f"  {col[1]} ({col[2]})")
        else:
            print("No chat_history table found!")
        
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    check_database()
