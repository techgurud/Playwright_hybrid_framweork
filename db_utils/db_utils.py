import cx_Oracle

class OracleDBUtils:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
        self.connection = None

    def establish_connection(self):
        try:
            self.connection = cx_Oracle.connect(self.username, self.password, self.dsn)
            print("Database connection established")
        except cx_Oracle.DatabaseError as e:
            print(f"Error establishing database connection: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No database connection established")
            return None

        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")
            self.connection = None

# def to count the number of rows in a table
def count_rows(self, table_name):
    query = f"SELECT COUNT(*) FROM {table_name}"
    result = self.execute_query(query)
    if result:
        return result[0][0]
    return None

def insert_row(self, table_name, columns, values):
    columns_str = ", ".join(columns)
    values_str = ", ".join([f":{i}" for i in range(1, len(values) + 1)])
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    params = dict(enumerate(values, start=1))
    self.execute_query(query, params)

def update_row(self, table_name, set_columns, set_values, where_column, where_value):
    set_str = ", ".join([f"{column} = :{i}" for i, column in enumerate(set_columns, start=1)])
    query = f"UPDATE {table_name} SET {set_str} WHERE {where_column} = :{len(set_columns) + 1}"
    params = dict(enumerate(set_values, start=1))
    params[len(set_columns) + 1] = where_value
    self.execute_query(query, params)

def delete_row(self, table_name, where_column, where_value):
    query = f"DELETE FROM {table_name} WHERE {where_column} = :1"
    self.execute_query(query, (where_value,))

def drop_table(self, table_name):
    query = f"DROP TABLE {table_name}"
    self.execute_query(query)

def create_table(self, table_name, columns):
    columns_str = ", ".join(columns)
    query = f"CREATE TABLE {table_name} ({columns_str})"
    self.execute_query(query)

def truncate_table(self, table_name):
    query = f"TRUNCATE TABLE {table_name}"
    self.execute_query(query)

def commit(self):
    if self.connection:
        self.connection.commit()

def rollback(self):
    if self.connection:
        self.connection.rollback()

def __del__(self):
    self.close_connection()

# def to verify the data count from source to destination table
def verify_data_count(source_db, destination_db, source_table, destination_table):
    source_count = source_db.count_rows(source_table)
    destination_count = destination_db.count_rows(destination_table)
    assert_equal(source_count, destination_count)

# def to verify the data from source to destination table
def verify_data(source_db, destination_db, source_table, destination_table):
    source_data = source_db.execute_query(f"SELECT * FROM {source_table}")
    destination_data = destination_db.execute_query(f"SELECT * FROM {destination_table}")
    assert_equal(source_data, destination_data)


# Path: utils/db_utils.py


# Compare this snippet from utils/playwright_utils.py:
# from playwright.sync_api import sync_playwright
#            
