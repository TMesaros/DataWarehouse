from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_mysqldb import MySQL, MySQLdb
import datetime
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "YouNeedToEnterSomethingHereButForOurAppItDoesNotMatter"

# Keep session persistent if browser closes - disable this line if you want a fresh session every time you access from a new browser
app.permanent_session_lifetime = timedelta(days=1)

# TO DO: Replace MYSQL_USER and MYSQL_PASSWORD with your local values, replace MYSQL_DB with whatever you called the local DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'StephaneValerie2023!'
app.config['MYSQL_DB'] = 'cs6400_su24_team001'

mysql = MySQL(app)

# default routing for localhost, will redirect to login screen
@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
#login using a session
def login():
    if request.method == "POST":
        session.permanent = True
        EmployeeID = request.form["e_id"]
        password = request.form["pw"]
        print("Employee ID: ", EmployeeID, "\nPassword: ", password)
 
        # Check if Employee ID is valid - comment out the next three lines if you want to test without havnig to enter a valid user
        if len(EmployeeID) > 7 or not EmployeeID.isdigit():
            flash("Employee ID must be a maximum of seven numeric characters")
            return redirect(url_for("login"))


        # Create a cursor which can pull data from the SQL database - Note the parameter passed to the cursor is important - if lets you 
        # reference the result as a dictionary using the column names. Without it you have to reference columns by numberical index i.e. [0], [1] etc
        # instead of ['LastName'] or whatever. That being said, the "outer" value returned is still a list of tuples, so to get the first
        # database row returned you need to do something like I did below with "user = result_set[0]"

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE EmployeeID = %s", (EmployeeID,))
        result_set = cursor.fetchall()
        user = result_set[0]

        # Need to update this since SSN should be stored as a string rather than INT
        stored_pw = str(user["SSN"][-4:]) + '-' + user["LastName"]
        print(stored_pw)
       # validaes password - comment out if you want to test without having to enter a valid password
        if stored_pw != password:
            flash("Invalid password")
            return redirect(url_for("login"))
        

        session["EmployeeID"] = EmployeeID
        session["FirstName"] = user["FirstName"]
        session["LastName"] = user["LastName"]

        flash("Login successful")

        cursor.close()

        return redirect(url_for("mainmenu"))
# if user already in session direct to user page, otherwise direct to login page
    else:
        if "EmployeeID" in session:
            flash("Already logged in")
            return redirect(url_for("mainmenu"))
        return render_template("login.html")

@app.route("/mainmenu", methods=["POST", "GET"])
def mainmenu():


    if "EmployeeID" not in session:
        flash("You are not logged in")
        return redirect(url_for("login"))

    all_dists = check_user_districts(session['EmployeeID'])

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''SELECT count(*) AS storecount FROM store;''')
    store_count = cursor.fetchall()[0]['storecount']

    cursor.execute('''SELECT count(*) AS citycount FROM city;''')
    city_count = cursor.fetchall()[0]['citycount']

    cursor.execute('''SELECT count(*) AS mancount FROM manufacturer;''')
    man_count = cursor.fetchall()[0]['mancount']

    cursor.execute('''SELECT count(*) AS productcount FROM product;''')
    product_count = cursor.fetchall()[0]['productcount']

    cursor.execute('''SELECT count(*) AS catcount FROM category;''')
    cat_count = cursor.fetchall()[0]['catcount']

    cursor.execute('''SELECT count(*) AS holidaycount FROM holiday;''')
    holiday_count = cursor.fetchall()[0]['holidaycount']

    cursor.execute('''SELECT count(*) AS districtcount FROM district;''')
    district_count = cursor.fetchall()[0]['districtcount']


    cursor.execute(
        '''SELECT LogAccess FROM user WHERE user.EmployeeID = %s''',
        (session['EmployeeID'],)
    )
    audit_log_view = cursor.fetchall()[0]['LogAccess']


    return render_template("mainmenu.html", FirstName=session["FirstName"], LastName=session["LastName"], store_count=store_count, city_count=city_count, 
                           man_count=man_count, product_count=product_count, cat_count=cat_count, holiday_count=holiday_count, district_count=district_count,
                           audit_log_view=audit_log_view, all_dists=all_dists)


@app.route("/logout")
def logout():
    if "EmployeeID" in session:
        cur_user = session["FirstName"] + " " + session["LastName"]
        flash(f"You have been logged out, {cur_user}", "info")
    session.pop("EmployeeID", None)
    session.pop("LastName", None)
    session.pop("FirstName", None)
    return redirect(url_for("login"))


@app.route("/ac_report")
def ac_report():

    update_audit_log(session['EmployeeID'], "Air Conditioners on Groundhog Day?")
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        '''WITH YearlySales AS (
    	SELECT EXTRACT(YEAR FROM ps.SoldDate) AS SalesYear, sum(ps.Quantity) AS TotalQuantity 
        FROM product_sold AS ps, product_category AS pc, store AS s
        WHERE pc.CategoryName = 'Air Conditioning' AND pc.PID = ps.PID AND ps.StoreNumber = s.StoreNumber AND
        (s.DistrictNumber IN (Select DistrictNumber FROM user_assigned_district WHERE EmployeeID = %s))
        GROUP BY SalesYear
        ), GHSales AS (
	    SELECT EXTRACT(YEAR FROM ps.SoldDate) AS SalesYear, sum(ps.Quantity) AS GHQuantity
        FROM product_sold AS ps, product_category AS pc, store AS s
        WHERE pc.CategoryName = 'Air Conditioning' AND pc.PID = ps.PID AND ps.StoreNumber = s.StoreNumber AND
        (s.DistrictNumber IN (Select DistrictNumber FROM user_assigned_district WHERE EmployeeID = %s))
        AND EXTRACT(DAY FROM ps.SoldDate) = 2
        AND EXTRACT(MONTH FROM ps.SoldDate) = 2
        GROUP BY SalesYear
        )
        SELECT YearlySales.SalesYear, YearlySales.TotalQuantity, (YearlySales.TotalQuantity/365) AS AvgQuantity, GHSales.GHQuantity 
        FROM YearlySales, GHSales
        WHERE YearlySales.SalesYear = GHSales.SalesYear
        ORDER BY YearlySales.SalesYear ASC;''',
        (session['EmployeeID'], session['EmployeeID'])
        )
    result_set = cursor.fetchall()
    return render_template("ac_report.html", result_set=result_set)


@app.route("/cat_report", methods=["POST", "GET"])
def cat_report():

    update_audit_log(session['EmployeeID'], "Category Report")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute(
        '''SELECT c.CategoryName AS CategoryName, count(DISTINCT pc.PID) AS ProductNum, count(DISTINCT p.ManufacturerName) AS ManNum, avg(p.RetailPrice) AS AvgPrice
            FROM Category AS c, Product_Category AS pc, Product AS p
            WHERE c.CategoryName = pc.CategoryName AND pc.PID = p.PID
            GROUP BY c.CategoryName
            ORDER BY c.CategoryName ASC;''',
        )
    result_set = cursor.fetchall()
    for row in result_set:
        row['AvgPrice'] = round(row['AvgPrice'], 2)

    return render_template("cat_report.html", result_set=result_set)


@app.route("/dist_cat_report", methods=["POST", "GET"])
def dist_cat_report():


    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # If user clicked a drilldown, display appropriate drilldown
    if request.method == "POST" and "Drilldown" in request.form:
        cursor.execute(
            '''SELECT DISTINCT s.StoreNumber, s.CityName, s.State, EXTRACT(YEAR FROM ps.SoldDate) AS SoldYear, EXTRACT(MONTH FROM ps.SoldDate) AS SoldMonth
                FROM store AS s, district AS d, product_sold AS ps, product_category AS pc
                WHERE EXTRACT(YEAR FROM ps.SoldDate) = %s AND EXTRACT(MONTH FROM ps.SoldDate) = %s AND ps.StoreNumber = s.StoreNumber 
                AND ps.PID = pc.PID AND pc.CategoryName = %s AND s.DistrictNumber = %s
                ORDER BY StoreNumber ASC;''',
                (request.form['Year'],
                request.form['Month'],
                request.form['CategoryName'],
                request.form['DistrictNumber'])
        )
        result_set = cursor.fetchall()

        return render_template("dist_cat_drilldown.html",
                               category=request.form['CategoryName'],
                               district=request.form['DistrictNumber'],
                               sales_year=request.form['Year'],
                               sales_month=request.form['Month'],
                               result_set=result_set
                               )
            
    # Check user districts vs total districts
    cursor.execute(
        '''SELECT count(ud.DistrictNumber) AS User_Districts
        FROM user_assigned_district AS ud
        WHERE ud.EmployeeID=%s;''',
        (session['EmployeeID'],)
        )
    user_district_count = cursor.fetchall()[0]['User_Districts']
    print("User district count found for Employee ID", session['EmployeeID'], "is ", user_district_count)

    cursor.execute(
        '''SELECT count(*) as Total_Districts FROM district;'''
    )

    total_districts = cursor.fetchall()[0]['Total_Districts']
    print("Total districts: ", total_districts)
    if total_districts > user_district_count:
        flash("Attempted to access a report for which the user does not have access (Insufficient Districts)")
        return redirect(url_for("mainmenu"))

    if request.method == "GET":
        update_audit_log(session['EmployeeID'], "State with Highest Volume for each Category")


    # Select all valid year/month combinations from sales data
    cursor.execute(
        '''SELECT DISTINCT EXTRACT(YEAR FROM product_sold.SoldDate) AS SoldYear, EXTRACT(MONTH FROM product_sold.SoldDate) AS SoldMonth FROM product_sold
        ORDER BY SoldYear, SoldMonth'''
    )
    sales_dates = cursor.fetchall()

    # If month and year were submitted, query the DB for the sales data for the respective month and year
    if request.method == "POST" and "Month Year" in request.form:
        sales_month = request.form['Month Year'][:-5]
        sales_year = request.form['Month Year'][-4:]
        cursor.execute(
            '''WITH MonthSales (DistrictNumber, CategoryName, Quantity) AS
            ( SELECT s.DistrictNumber, pc.CategoryName, sum(ps.Quantity) AS SumProd
            FROM product_sold AS ps, store AS s, product_category AS pc
            WHERE ps.StoreNumber = s.StoreNumber AND ps.PID = pc.PID AND EXTRACT(YEAR FROM ps.SoldDate) = %s AND EXTRACT(MONTH FROM ps.SoldDate) = %s
            GROUP BY s.DistrictNumber, pc.CategoryName
            )
            SELECT DISTINCT m.CategoryName, max(m.Quantity) AS Quantity, m.DistrictNumber
            FROM MonthSales AS m
            WHERE Quantity >= 
            (SELECT max(Quantity)
            FROM MonthSales AS n
            WHERE m.CategoryName = n.CategoryName)
            GROUP BY CategoryName, DistrictNumber
            ORDER BY CategoryName;''',
            (sales_year, sales_month,)
        )
        result_set = cursor.fetchall()
        return render_template("dist_cat_report.html", sales_dates=sales_dates, sales_month=sales_month, sales_year=sales_year, result_set=result_set)
    return render_template("dist_cat_report.html", sales_dates=sales_dates)


@app.route("/man_prod_report", methods=["POST", "GET"])
def man_prod_report():

    if request.method == "GET":
        update_audit_log(session['EmployeeID'], "Manufacturer's Product Report")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == "POST":

        man_name = request.form["ManufacturerName"]
        tp = request.form["TotalProducts"]
        avgprice = request.form["AvgPrice"]
        minprice = request.form["MinPrice"]
        maxprice = request.form["MaxPrice"]
        cursor.execute(
            '''SELECT p.PID, p.ProductName, GROUP_CONCAT(pc.CategoryName SEPARATOR ', ') AS CategoryName, p.RetailPrice
		FROM product AS p
		INNER JOIN product_category AS pc ON p.PID = pc.PID
		WHERE p.ManufacturerName = %s
		GROUP BY p.PID, p.ProductName, p.RetailPrice
		ORDER BY p.RetailPrice DESC, p.ProductName ASC;''',
            	(man_name,)
            )
        result_set = cursor.fetchall()
        num_records = len(result_set)
        return render_template("man_prod_drilldown.html",
                                ManufacturerName=man_name,
                                TotalProducts=tp, 
                                AvgPrice=avgprice, 
                                MinPrice=minprice, 
                                MaxPrice=maxprice, 
                                result_set = result_set,
                                num_records=num_records,
        )

    cursor.execute(
        '''SELECT m.ManufacturerName, count(*) as TotalProducts, avg(p.RetailPrice) as AvgPrice, min(p.RetailPrice) as MinPrice, max(p.RetailPrice) as MaxPrice
        FROM manufacturer AS m, product AS p
        WHERE m.ManufacturerName = p.ManufacturerName
        GROUP by m.ManufacturerName
        ORDER BY AvgPrice DESC
        LIMIT 100;'''
    )
    result_set = cursor.fetchall()

    for row in result_set:
        row['AvgPrice'] = round(row['AvgPrice'], 2)

    return render_template("man_prod_report.html", result_set=result_set)

@app.route("/pred_rev_report")
def pred_rev_report():

    update_audit_log(session['EmployeeID'], "Actual versus Predicted Revenue for GPS units")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        '''
WITH RetailSales AS (
SELECT ts.PID, ts.TotalQuantity,  (p.RetailPrice * ts.TotalQuantity) AS TotalRevenue FROM 
	(SELECT ps.PID, sum(ps.Quantity) AS TotalQuantity, p.RetailPrice AS Price
	FROM product_sold AS ps, product AS p, product_category AS pc, user_assigned_district AS ud, store AS s
	WHERE ps.PID = p.PID AND ps.SoldDate NOT IN (SELECT DiscountDate FROM discount WHERE discount.PID = ps.PID)
  AND p.PID = pc.PID AND pc.CategoryName = 'GPS' AND ps.StoreNumber = s.StoreNumber AND s.DistrictNumber = ud.DistrictNumber
  AND ud.EmployeeID = %s
	GROUP BY ps.PID, Price) AS ts,
    product AS p
    WHERE p.PID = ts.PID
),
DiscountSales AS (
Select PID, sum(Quantity) AS TotalQuantity, sum(Revenue) AS TotalRevenue FROM 
	(SELECT ps.PID, ps.Quantity, (ps.Quantity * d.DiscountPrice) AS Revenue, d.DiscountPrice
	FROM product_sold AS ps, product AS p, discount AS d, product_category AS pc, user_assigned_district AS ud, store AS s 
	WHERE ps.PID = p.PID AND ps.SoldDate = d.DiscountDate AND ps.PID = d.PID AND ps.PID = pc.PID AND pc.CategoryName = 'GPS' AND ps.StoreNumber = s.StoreNumber AND s.DistrictNumber = ud.DistrictNumber
  AND ud.EmployeeID = %s
  )AS ds 
	GROUP BY PID
),

masterProduct AS (

select P.PID, PC.categoryname, P. ProductName, p.RetailPrice
from product as  p
inner join product_category as pc
on p.pid = pc.pid
where pc.categoryname = 'GPS'

)

SELECT 
    A.PID, 
    A.ProductName,
    a.RetailPrice,
    b.TotalQuantity AS RetailQuantity,
    C.TotalQuantity AS DiscountQuantity,
    (B.TotalQuantity + C.TotalQuantity) AS TotalQuantity,
    (B.TotalRevenue + C.TotalRevenue) AS ActualRevenue, 
    ((B.TotalQuantity + (C.TotalQuantity * .75)) *a.RetailPrice) AS PredictedRevenue,
    ((b.TotalRevenue + c.TotalRevenue) - ((b.TotalQuantity + (c.TotalQuantity* .75))  *a.RetailPrice)) AS Difference
FROM masterProduct AS A 
LEFT OUTER JOIN RetailSales AS B
	ON A.PID = B.PID
LEFT OUTER JOIN DiscountSales AS C
	ON A.PID = C.PID
WHERE ((b.TotalRevenue + c.TotalRevenue) - ((b.TotalQuantity + (c.TotalQuantity * .75))  *a.RetailPrice)) > 200
or ((b.TotalRevenue + c.TotalRevenue) - ((b.TotalQuantity + (c.TotalQuantity * .75)) *a.RetailPrice)) < -200
ORDER by ((b.TotalRevenue + c.TotalRevenue) - ((b.TotalQuantity + c.TotalQuantity) * .75 *a.RetailPrice)) DESC; ''',
    (session['EmployeeID'], session['EmployeeID'])
    )
    result_set = cursor.fetchall()

    for row in result_set:
        row['ActualRevenue'] = round(row['ActualRevenue'], 2)
        row['PredictedRevenue'] = round(row['PredictedRevenue'], 2)
        row['Difference'] = round(row['Difference'], 2)
# {{row['ActualRevenue']}}</td><td>{{row['PredictedRevenue']}}</td><td>{{row['Difference']}}        
    return render_template("pred_rev_report.html", result_set=result_set)

@app.route("/rev_by_pop_report")
def rev_by_pop_report():

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Check user districts vs total districts
    cursor.execute(
        '''SELECT count(ud.DistrictNumber) AS User_Districts
        FROM user_assigned_district AS ud
        WHERE ud.EmployeeID=%s;''',
        (session['EmployeeID'],)
        )
    user_district_count = cursor.fetchall()[0]['User_Districts']
    print("User district count found for Employee ID", session['EmployeeID'], "is ", user_district_count)

    cursor.execute(
        '''SELECT count(*) as Total_Districts FROM district;'''
    )

    total_districts = cursor.fetchall()[0]['Total_Districts']
    print("Total districts: ", total_districts)
    if total_districts > user_district_count:
        flash("Attempted to access a report for which the user does not have access (Insufficient Districts)")
        return redirect(url_for("mainmenu"))

    if request.method == "GET":
        update_audit_log(session['EmployeeID'], "Revenue by Population")

    cursor.execute(
        '''WITH TotalRevenue AS
        (
            (
	        SELECT ps.StoreNumber, ps.SoldDate, ps.PID, ps.Quantity, p.RetailPrice AS Price, (ps.Quantity * p.RetailPrice) AS Revenue
	        FROM product_sold AS ps, product AS p
	        WHERE ps.PID = p.PID AND ps.SoldDate NOT IN (SELECT DiscountDate FROM discount WHERE discount.PID = ps.PID)
            )
            UNION
            (
	        SELECT ps.StoreNumber, ps.SoldDate, ps.PID, ps.Quantity, d.DiscountPrice AS Price, (ps.Quantity * d.DiscountPrice) AS Revenue
	        FROM product_sold AS ps, discount as d
	        WHERE ps.PID = d.PID AND ps.SoldDate = d.DiscountDate
            )
        ),
        CitySizes (CityName, CityType) AS
        (SELECT c.CityName,
        CASE
        WHEN c.Population >= 9000000 THEN 'Extra Large'
        WHEN c.Population < 9000000 AND c.Population >= 6700000 THEN 'Large'
        WHEN c.Population < 6700000 AND c.Population >= 3700000 THEN 'Medium'
        ELSE 'Small'
        END AS CityType
        FROM city as c)
        SELECT CityType, EXTRACT(Year FROM tr.SoldDate) AS RevYear, sum(tr.Revenue) AS Revenue
        FROM CitySizes AS cs, TotalRevenue AS tr, store AS s
        WHERE cs.CityName = s.CityName AND s.StoreNumber = tr.StoreNumber
        GROUP BY RevYear, CityType
        ORDER BY RevYear ASC, CityType DESC;''')

    result_set = cursor.fetchall()
    for row in result_set:
        row['Revenue'] = round(row['Revenue'], 2)
    return render_template("rev_by_pop_report.html", result_set=result_set)

@app.route("/store_by_year_report", methods=["POST", "GET"])
def store_by_year():


    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Check user districts vs total districts
    cursor.execute(
        '''SELECT count(ud.DistrictNumber) AS User_Districts
        FROM user_assigned_district AS ud
        WHERE ud.EmployeeID=%s;''',
        (session['EmployeeID'],)
        )
    user_district_count = cursor.fetchall()[0]['User_Districts']
    print("User district count found for Employee ID", session['EmployeeID'], "is ", user_district_count)

    cursor.execute(
        '''SELECT count(*) as Total_Districts FROM district;'''
    )

    total_districts = cursor.fetchall()[0]['Total_Districts']
    print("Total districts: ", total_districts)
    if total_districts > user_district_count:
        flash("Attempted to access a report for which the user does not have access (Insufficient Districts)")
        return redirect(url_for("mainmenu"))

    if request.method == "GET":
        update_audit_log(session['EmployeeID'], "Store Revenue by Year by State")

    cursor.execute(
        '''SELECT DISTINCT State FROM city ORDER BY State ASC;'''
    )

    state_list = cursor.fetchall()
    
    if request.method == "POST":
        current_state = request.form['State']

        cursor.execute(
            '''WITH TotalRevenue (StoreYear, StoreNumber, Total_Sold, Revenue) AS
            (
                (
                SELECT EXTRACT(year FROM ps.SoldDate) as StoreYear, store.StoreNumber, 
                sum(ps.Quantity) as TotalSold, sum(ps.Quantity * d.DiscountPrice) AS 
                Revenue
                FROM product_sold AS ps, store, discount AS d
                WHERE store.State = %s AND store.StoreNumber = ps.StoreNumber AND   
	            ps.SoldDate = d.DiscountDate AND ps.PID = d.PID
                GROUP BY store.StoreNumber, StoreYear
                )
                UNION ALL
                (
                SELECT EXTRACT(year from ps.SoldDate) as StoreYear, store.StoreNumber, 
                sum(ps.Quantity) as TotalSold, sum(ps.Quantity * p.RetailPrice) AS Revenue
                FROM product_sold AS ps, store, product AS p
                WHERE store.State = %s AND store.StoreNumber = ps.StoreNumber AND ps.PID = p.PID AND
                ps.SoldDate NOT IN (SELECT discount.DiscountDate FROM discount WHERE ps.PID = discount.PID)
                GROUP BY store.StoreNumber, StoreYear
                )
            )
            SELECT tr.StoreYear, tr.StoreNumber, store.CityName, sum(tr.Revenue) AS Revenue
            FROM TotalRevenue AS tr, store
            WHERE tr.StoreNumber = store.StoreNumber
            GROUP BY tr.StoreYear, tr.StoreNumber, store.CityName
            ORDER BY StoreYear ASC, Revenue DESC;
            ''',
            (current_state, current_state,)
        )
        result_set = cursor.fetchall()
        for row in result_set:
            row['Revenue'] = round(row['Revenue'], 2)
        return render_template("store_by_year_report.html", state_list=state_list, result_set=result_set, current_state=current_state)
    return render_template("store_by_year_report.html", state_list=state_list)

@app.route("/audit_log", methods=["POST", "GET"])
def audit_log():

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute(
        '''SELECT LogAccess FROM user WHERE user.EmployeeID = %s''',
        (session['EmployeeID'],)
    )
    audit_log_view = cursor.fetchall()[0]['LogAccess']
    if not audit_log_view:
        flash("User attempted to access audit log but does not have all districts")
        return redirect(url_for("mainmenu"))

    cursor.execute(
        '''SELECT count(*) as Total_Districts FROM district;'''
    )

    total_districts = cursor.fetchall()[0]['Total_Districts']

    cursor.execute(
        '''SELECT  a.Date_Time, a.EmployeeID, a.ReportName, u.LastName, u.FirstName, count(ud.DistrictNumber) AS user_districts
            FROM audit_log AS a, user AS u, user_assigned_district AS ud
            WHERE a.EmployeeID = u.EmployeeID AND u.EmployeeID = ud.EmployeeID
            GROUP BY a.Date_Time, a.EmployeeID, a.ReportName, u.LastName, u.FirstName
            ORDER BY a.Date_Time DESC
            LIMIT 100;'''
    )

    result_set = cursor.fetchall()

    return render_template("audit_log.html", result_set=result_set, total_districts=total_districts)

@app.route("/holiday", methods=["POST", "GET"])
def holiday():

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == "POST":
        year = request.form["year"]
        month = request.form["month"]
        day = request.form["day"]
        holidayname = request.form["holiday_name"]

        if year == '' or month == '' or day == '' or holidayname == '':
            flash("Invalid input - all fields must be completed")
        elif not year.isdigit() or not month.isdigit() or not day.isdigit():
                flash("Invalid input - day/month/year must be integers for a valid date")
        else:
            year = int(year)
            month = int(month)
            day = int(day)

            if len(str(year)) > 4 or year < 0:
                flash("Invalid input - year must be a positive value of at most four digits")
            elif month < 1 or month > 13:
                flash("Invalid input - month must be a value between 1 and 12")
            elif day < 1:
                flash("Invalid input - day must be a valid positive integer")
            elif month == 2 and (year % 4) != 0 and day > 28:
                flash("Invalid input - maximum day for February in a non-leap year is 28")
            elif month == 2 and (year % 4 == 0) and day > 29:
                flash("Invalid input - maximum day for February in a leap year is 29")
            elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                flash("Invalid day for month provided")
            elif day > 31:
                flash("Invalid day for month provided")
            else:
                if day < 10:
                    day = '0' + str(day)
                else:
                    day = str(day)
                if (month < 10):
                    month = '0' + str(month)
                else:
                    month = str(month)
                year = str(year)
                while len(year) < 4:
                    year = '0' + year
                str_date = year + "-" + month + "-" + day

                try:
                    cursor.execute('''
                        INSERT INTO holiday VALUES (%s, %s, %s)
                        ''', (str_date, holidayname, session['EmployeeID'],))
                    mysql.connection.commit()
                except MySQLdb.IntegrityError:
                    msg = "Failed to insert holiday for " + holidayname + " on " + str_date
                    flash(msg)                
    cursor.execute('''
        SELECT HolidayDate, HolidayName FROM holiday;               
    ''')
    result_set = cursor.fetchall()

    user_district_all = check_user_districts(session['EmployeeID'])
    return render_template("holiday.html", user_district_all=user_district_all, user=session['EmployeeID'], result_set=result_set)

def update_audit_log(user, reportname):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    t_stamp = datetime.datetime.now()
    date_str = t_stamp.strftime('%G-%m-%d %H:%M:%S')
    print(date_str)
    cursor.execute('''INSERT INTO audit_log VALUES(%s, %s, %s)''',
                                                (date_str, user, reportname));
    mysql.connection.commit()
    cursor.close()
#    print(cursor.fetchall())
    return True

def check_user_districts(user):

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Check user districts vs total districts
    cursor.execute(
        '''SELECT count(ud.DistrictNumber) AS User_Districts
        FROM user_assigned_district AS ud
        WHERE ud.EmployeeID=%s;''',
        (user,)
        )
    user_district_count = cursor.fetchall()[0]['User_Districts']
    print("User district count found for Employee ID", session['EmployeeID'], "is ", user_district_count)

    cursor.execute(
        '''SELECT count(*) as Total_Districts FROM district;'''
    )

    total_districts = cursor.fetchall()[0]['Total_Districts']
    print("Total districts: ", total_districts)
#    cursor.close()
    if total_districts > user_district_count:
        return False
    return True

if __name__ == "__main__":
    app.run()
### Running in debug mode will cause server to restart when code change is saved
#   app.run(debug=True)
