# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')

def query_orders(db):
    # return a list of orders displaying each column
    db = conn.cursor()
    query= '''
    SELECT * 
    FROM Orders o 
    '''
    db.execute(query)
    result = db.fetchall()
    return result

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    db = conn.cursor()
    query= '''
    SELECT *
    FROM Orders o 
    WHERE DATE(o.OrderDate)> ? 
    OR
    DATE(o.OrderDate) = ?
    '''
    db.execute(query, (date_from, date_to))
    result = db.fetchall()
    return [result[0]]
    

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    db = conn.cursor()
    query= """SELECT *,  JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) as TimeDelta
    FROM Orders o 
    ORDER BY TimeDelta ASC
    """
    db.execute(query,)
    result = db.fetchall()
    return result
