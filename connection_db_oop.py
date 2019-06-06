import pyodbc


class Conct_MS_SQL:
    #when intialize we make the connection
    def __init__(self, server = 'localhost,1433', database = 'Northwind',username = 'SA',password = 'Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.dockr_conct = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.dockr_conct.cursor()

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_products(self):
        # Query the DB for all produtcs, iterate and fecth on, going to actually print
        query_rows = self.__sql_query("SELECT * FROM Products")
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print(row)

    def average_unit_price(self):
        query_rows = self.__sql_query("SELECT * FROM Products")
        all_unit_price = []
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            all_unit_price.append(row.UnitPrice)
        average_u_price = sum(all_unit_price)/len(all_unit_price)
        return average_u_price

# filter/search products by name
    def search_products_by_name(self,product_name):
        query_rows = self.__sql_query(f"SELECT * FROM Products WHERE ProductName = '{product_name}'")
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print(row)

# filter customers via company name
    def filter_cust_by_company_name(self, company_name):
        query_rows = self.__sql_query(f"SELECT * FROM Customers WHERE CompanyName = '{company_name}'")
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print(row)

# filter customers via country
    def filter_cust_by_country(self, country):
        query_rows = self.__sql_query(f"SELECT * FROM Customers WHERE Country = '{country}'")
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print(row)







    def read_all(self, location = ''):
        pass

    def read_one(self, name):
        pass

    def create_one(self, product_name, product_price):
        pass

    def destroy(self, id):
        pass

