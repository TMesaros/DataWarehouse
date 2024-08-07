import datetime
import random
# Create sales data
# products 1-27
# stores 1-52
PRODMAX = 27
STOREMAX = 52
QUANTITYMAX = 100
PRODMIX = int(PRODMAX / 4)
STOREMIX = int(STOREMAX / 8)
discountprice = 8.00
#products_sold StoreNumber (int), PID (int), SoldDate (date), Quantity (int)
# Create discount data DiscountDate (date), PID (int), DiscountPrice (float)

f = open("salesfile.sql", "w")
sale_date = datetime.datetime(2020, 1, 1)
for i in range(1, 1000):

    sale_date += datetime.timedelta(days=1)
    datestr = "'" + sale_date.strftime("%G") + "-" + sale_date.strftime("%m") + "-" + sale_date.strftime("%d") + "'"

    prodindex = random.randrange(1, PRODMAX)
    storeindex = random.randrange(1, STOREMAX)
    for i in range(PRODMIX):
        prodindex += 1
        if prodindex > PRODMAX:
            prodindex = 1
        discount = random.randrange(1, 10)

        for j in range(STOREMIX):
            quantity = random.randrange(1, QUANTITYMAX)     
            SQLstatement = "INSERT INTO product_sold VALUES(" + str(storeindex) + ", " + str(prodindex) + ", " + datestr + ", " + str(quantity) + ");\n"
#            print(SQLstatement)
            f.write(SQLstatement)
            storeindex += 1
            if storeindex > STOREMAX:
                storeindex = 1

        if discount < 3:
            if discount == 2:
                discountprice = 8.00
            else:
                discountprice = 7.50
            SQLstatement = "INSERT INTO discount VALUES(" + datestr + ", " + str(prodindex) + ", " + str(discountprice) + ");\n"
 #           print(SQLstatement)
            f.write(SQLstatement)

f.close()






# Create auditlog entries  Date_Time (date_time), EmployeeID (string), ReportName (string)
# Report Names
# INSERT INTO report VALUES('Manufacturers Product');
# Category
#INSERT INTO report VALUES('Predicted Revenue');
#INSERT INTO report VALUES('AC Groundhog');
#INSERT INTO report VALUES('Store by Revenue by State');
#INSERT INTO report VALUES('District Volume Category');
#'Revenue by Population' 