import logging
import sqlite3

from ...backend.database.query_manager import QueryManager

# logger to log things in code
logger = logging.getLogger(" manage_db ")


def setup_logger():
    """
    logger for gameLogic
    """
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


class ManageDB:
    def __init__(self, db_name, sql_dir) -> None:
        self.db_file = db_name
        self.conn = None
        setup_logger()
        self.__create_connection()
        qm = QueryManager(sql_dir)
        self.__create_tables(qm)

    def __create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(self.db_file)
            logger.debug(sqlite3.version)
        except sqlite3.Error as e:
            logger.debug(e)

    def __create_tables(self, qm):
        database = qm.database
        cursor = self.conn.cursor()

        # Split queries based on delimiter (e.g., ';')
        queries = database.split(';')

        # Execute each query
        for query in queries:
            try:
                cursor.execute(query)
                self.conn.commit()
            except sqlite3.Error as e:
                print("Error executing query:", e)

    def close_connection(self):
        if self.conn:
            self.conn.close()
