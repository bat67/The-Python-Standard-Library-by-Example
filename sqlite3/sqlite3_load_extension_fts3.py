#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Query tasks in the database.
"""

#end_pymotw_header
import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:

    # Load the full-text-search extension module
    conn.enable_load_extension(True)
    conn.load_extension('fts3.so')
    conn.enable_load_extension(False)

    cursor = conn.cursor()

    cursor.execute("""
    create virtual table searchable_task using fts3(details);
    insert into searchable_task select (id, details) from task;
    """)

    cursor.execute(
        """
        select id, details from searchable_task
        where searchable_task match ?
        """,
        ('write',),
    )
    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<20} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))
