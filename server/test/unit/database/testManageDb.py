import unittest
import os
from server.backend.database.manage_db import ManageDB


class TestManageDB(unittest.TestCase):
    def setUp(self):
        self.sql_dir = '/mnt/d/Projects/PythonWS/SimProject/src/backend/database'
        self.db_name = 'testDb.db'
        print(self.db_name)
        self.db = ManageDB(self.db_name, self.sql_dir)

    def tearDown(self):
        pass
        # if os.path.exists(self.db_name):
        #     os.remove(self.db_name)

    def test_connection(self):
        self.assertIsNotNone(self.db.conn)
        self.assertTrue(os.path.exists(self.db_name))

    # def test_connection_closed(self):
    #     self.db.close_connection()
    #     self.assertIsNone(self.db.conn)


if __name__ == '__main__':
    unittest.main(verbosity=2)
