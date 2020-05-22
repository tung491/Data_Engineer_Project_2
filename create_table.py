from cassandra.cluster import Cluster
from sql_queries import *


def create_database():
    """
    Create keyspace udacity and return session
    :return: session
    """
    cluster = Cluster()
    session = cluster.connect()
    session.execute("DROP KEYSPACE IF EXISTS udacity")
    session.execute("""
                    CREATE KEYSPACE IF NOT EXISTS udacity
                    WITH REPLICATION = 
                    {'class': 'SimpleStrategy', 'replication_factor': 1}
                    """)
    session.set_keyspace('udacity')

    return cluster, session


def drop_tables(session):
    """
    Drop all tables in udacity datable
    :param session:
    :return: None
    """
    for query in drop_table_queries:
        session.execute(query)


def create_tables(session):
    """
    Create tables in udacity database
    :param session:
    :return: None
    """
    for query in create_table_queries:
        session.execute(query)


def main():
    """
    - Drops (if exists) and Creates the sparkify database.

    - Establishes connection with the sparkify database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    cluster, session = create_database()
    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == '__main__':
    main()
