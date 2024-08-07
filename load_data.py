import MySQLdb


from mysql.connector import connect, Error

with connect(
    host="localhost",
    user='cs6400',
    password='cs6400',
    database="cs6400_su24_team001",
) as connection:
    cursor = connection.cursor()

# load districts
    with open("data/District.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n")
            cursor.execute('''
                           INSERT INTO district VALUES (%s)''', (data,))
    connection.commit()
            
# Load users and user_district tables
    with open("data/User.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO user (EmployeeID, FirstName, LastName, SSN, LogAccess) VALUES (%s, %s, %s, %s, %s)''',
                           (data[0], data[1], data[2], data[3], data[4],))
            for district in data[5].split(','):
                cursor.execute('''
                               INSERT INTO user_assigned_district VALUES (%s, %s)''',
                               (district, data[0]))

    connection.commit()

# Load categories
    with open("data/Category.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n")
            cursor.execute('''
                           INSERT INTO category VALUES (%s)''', (data,))
    connection.commit()

# Load cities

    with open("data/City.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO city VALUES (%s, %s, %s)''',
                           (data[0], data[1], data[2],))

    connection.commit()

# load manufacturers
    with open("data/Manufacturer.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n")
            cursor.execute('''
                           INSERT INTO manufacturer VALUES (%s)''', (data,))
    connection.commit()

# Load products and product_category
    with open("data/Product.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')

            cursor.execute('''
                           INSERT INTO product (PID, ProductName, RetailPrice, ManufacturerName) VALUES (%s, %s, %s, %s)''',
                           (data[0], data[1], data[3], data[2],))
            for category in data[4].strip("\n").split(','):
                cursor.execute('''
                               INSERT INTO product_category VALUES (%s, %s)''',
                               (data[0], category,))
    connection.commit()

# Load stores
    with open("data/Store.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO store VALUES (%s, %s, %s, %s, %s)''',
                           (data[0], data[1], data[2], data[3], data[4],))

    connection.commit()

# Load holidays

    with open("data/Holiday.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO holiday VALUES (%s, %s, %s)''',
                           (data[0], data[1], data[2],))

    connection.commit()


# load product_sold

    with open("data/Sold.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO product_sold VALUES (%s, %s, %s, %s)''',
                           (data[2], data[0], data[1], data[3],))

    connection.commit()


# load discount

    with open("data/Discount.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO discount VALUES (%s, %s, %s)''',
                           (data[0], data[1], data[2],))

    connection.commit()


# Load report names

    with open("data/Report_Names.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n")
            cursor.execute('''
                           INSERT INTO report VALUES (%s)''', (data,))
    connection.commit()

# load audit_log

    with open("data/Audit_log.tsv", "r") as f:
        next(f)
        for line in f:
            data = line.strip("\n").split('\t')
            cursor.execute('''
                           INSERT INTO audit_log VALUES (%s, %s, %s)''',
                           (data[0], data[1], data[2],))

    connection.commit()


# Load Date?
