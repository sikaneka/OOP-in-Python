import sqlite3
import argparse
from datetime import datetime

DB_FILE = 'todo.db'

def connect_db():
    """Connect to the SQLite database and create the tasks table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending',  -- 'pending' or 'completed'
        created_date TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn, cursor

def add_task(cursor, conn, title, description=''):
    """Insert a new task into the database."""
    created_date = datetime.now().isoformat()
    try:
        cursor.execute(
            "INSERT INTO tasks (title, description, created_date) VALUES (?, ?, ?)",
            (title, description, created_date)
        )
        conn.commit()
        print(f"Task added successfully! ID: {cursor.lastrowid}")
    except sqlite3.IntegrityError as e:
        print(f"Error adding task: {e}")

def list_tasks(cursor, status_filter=None):
    """Query and display tasks, optionally filtered by status."""
    if status_filter:
        cursor.execute(
            "SELECT id, title, description, status, created_date FROM tasks WHERE status = ? ORDER BY id",
            (status_filter,)
        )
    else:
        cursor.execute("SELECT id, title, description, status, created_date FROM tasks ORDER BY id")
    
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found.")
        return
    
    print("\nYour Tasks:")
    print("-" * 60)
    for row in rows:
        id, title, desc, status, date = row
        desc = desc[:50] + '...' if desc and len(desc) > 50 else desc or ''
        print(f"ID: {id} | Title: {title} | Status: {status} | Created: {date[:10]} | Desc: {desc}")

def complete_task(cursor, conn, task_id):
    """Update a task's status to 'completed'."""
    try:
        cursor.execute(
            "UPDATE tasks SET status = 'completed' WHERE id = ?",
            (task_id,)
        )
        if cursor.rowcount == 0:
            print(f"No task found with ID {task_id}.")
            return
        conn.commit()
        print(f"Task {task_id} marked as completed!")
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")

def delete_task(cursor, conn, task_id):
    """Delete a task by ID."""
    try:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print(f"No task found with ID {task_id}.")
            return
        conn.commit()
        print(f"Task {task_id} deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting task: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple SQLite To-Do List App")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('-d', '--description', help='Task description (optional)')

    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('-s', '--status', choices=['pending', 'completed'], help='Filter by status')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark task as completed')
    complete_parser.add_argument('id', type=int, help='Task ID')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    args = parser.parse_args()

    if args.command == 'add':
        conn, cursor = connect_db()
        add_task(cursor, conn, args.title, args.description or '')
        conn.close()

    elif args.command == 'list':
        conn, cursor = connect_db()
        list_tasks(cursor, args.status)
        conn.close()

    elif args.command == 'complete':
        conn, cursor = connect_db()
        complete_task(cursor, conn, args.id)
        conn.close()

    elif args.command == 'delete':
        conn, cursor = connect_db()
        delete_task(cursor, conn, args.id)
        conn.close()

    else:
        parser.print_help()

if __name__ == '__main__':
    main()