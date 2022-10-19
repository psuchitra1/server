from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash

from connect2db import *
from datetime import date

date_today = date.today()

app = Flask(__name__)
CORS(app)

""" Creating new users """
@cross_origin()
@app.route('/create_role', methods=['POST'])
def create_User():
        _json = request.json  # converting to json
        User_ID = _json['User_ID']
        print(User_ID, "User_ID")
        email_ID = _json['email_ID']
        print(email_ID, "email_ID")
        Password = _json['Password']
        print(Password, "PASSSWORD")
        First_Name = _json['First_Name']
        print(First_Name, "First_Name")
        Last_Name = _json['Last_Name']
        print(Last_Name, "Last_Name")
        Created_on = date_today
        print(Created_on, "Created_on")
        created_by = _json['created_by']
        print(created_by, "created_by")
        Updated_on = date_today
        print(Updated_on, "Updated_on")
        Updated_by = _json['Updated_by']
        print(Updated_by, "Updated_by")
        Role = _json['Role']
        print(Role, "Role")
        Teams = _json['Teams']
        print(Teams, "Teams")
        delete = _json['delete']
        # delete = dele.encode()
        print(delete, "deletee", delete)

        # validate the received values
        if User_ID and email_ID and Password and First_Name and Last_Name and \
                Created_on and created_by and Updated_on and Updated_by and Role and Teams and delete and request.method == 'POST':  # giving condition whether the method is post
            _hashed_password = generate_password_hash(
                Password)  # using an inbuilt function generate_password_hash the password is hashing
            # save edits

            conn = connectDB()
            cursor = conn.cursor()  # created a cursor

            query1 = ("SELECT User_ID FROM Users ")  # qurey for selecting userid id from the usertable
            print(query1, "q1111")
            cursor.execute(query1)  # executing the qurey
            db224 = cursor.fetchall()  # fetching the qurey
            print(db224, "db224")
            usrid = []  # created an empty list for adding the user ids
            for i in db224:  # iterating the fetched values
                for j in i:  # iterating the tuples
                    print(usrid, "useridd")
                    usrid.append(j)  # appending the values in to the list
                print(usrid, "idddddd")

            if User_ID in usrid:  # checking the user id is present in the list
                resp = jsonify(
                    'userid  is already exists!')  # if the userid is present in the list it will show response as this
                resp.status_code = 400  # status code made as 400
                return resp  # this response will work if this condition works

            query = ("SELECT email_ID FROM Users ")  # qurey for selecting email id from the usertable
            cursor.execute(query)  # executing the qurey
            db223 = cursor.fetchall()  # fetching the qurey
            emailid = []  # created an empty list for adding the email ids

            for i in db223:  # iterating the fetched values
                for j in i:  # iterating the tuples
                    emailid.append(j)  # appending the values in to the list

            if email_ID in emailid:  # checking the email id is present in the list
                resp = jsonify(
                    'Email is already exists!')  # if the emailid is present in the list it will show response as this
                resp.status_code = 400  # status code made as 400
                return resp  # this response will work if this condition works

            else:
                sql = "INSERT INTO Users(User_ID, email_ID, Password,First_Name ,Last_Name , Created_on , created_by , Updated_on, Updated_by,Role,Teams,delete)" \
                      " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"  # qurey for inserting values to the sql
                print(sql, "sqlll")
                data = (User_ID, email_ID, _hashed_password, First_Name, Last_Name, Created_on, created_by,
                        Updated_on, Updated_by, Role, Teams, delete)  # passing the variables from frondend to data
                print(data, "dataa")
                # connecting to psql

                cursor.execute(sql, data)  # executed the cursor with the sql qurey and the datas inserting
                conn.commit()  # commited the conn
                resp = jsonify('User added successfully!')  # created a response and jsonifed it
                resp.status_code = 200  # given a status code 200(truse) to the above response
                return resp  # returning the response if the above condition works

        else:
            res = jsonify('User is not added please check the error below!')  # created a response and jsonifed it
            res.status_code = 400  # giving error status
            return res

    """View all the users present in the database"""

@app.route('/View_Role')
def list_users():
        conn = connectDB()  # connecting to database
        cursor = conn.cursor(
            cursor_factory=RealDictCursor)  # created a cursor and connected with the db and giving cursor_factory as
        # RealDictCursor for getting it as key value pair
        cursor.execute(
            "SELECT User_ID, email_ID, First_Name, Last_Name, Created_on, created_by,Updated_on,Updated_by,Role,Teams FROM Users")  # given a qurey inside the execute function
        rows = cursor.fetchall()  # fetching all from the cursor
        resp = jsonify(rows)  # jsonifying the fetched data from the database
        resp.status_code = 200  # if the above condition works then given status code as 200
        return resp  # returning the response

@app.route('/view-users/<id>')
def user(id):  # created a function an passing id as an argument because this id is calling in the url
        conn = connectDB()  # connecting to the database
        cursor = conn.cursor(cursor_factory=RealDictCursor)  # the database is connection is given to a cursor
        cursor.execute(
            "SELECT User_ID User_ID, email_ID email_ID, Password Password,First_Name First_Name,Last_Name Last_Name,Created_on Created_on,"
            "created_by created_by,Updated_on Updated_on,Updated_by Updated_by, Role Role,Teams Teams  FROM Users WHERE User_ID=%s",
            (id,))  # qurey for selecting the userid
        row = cursor.fetchone()  # fetching the datas of that corresponding id
        resp = jsonify(row)  # jsonifying the datas
        resp.status_code = 200  # giving the response status as 200 if the above condition works
        return resp

    """Updating users"""

@app.route('/Update_Role', methods=['PUT'])
def update_User():
        _json = request.json  # converting the request to json
        User_ID = _json['User_ID']
        print(User_ID, "User_ID")
        # email_ID = _json['email_ID']
        # print(email_ID, "email_ID")
        Password = _json['Password']
        print(Password, "PASSSWORD")
        First_Name = _json['First_Name']
        print(First_Name, "First_Name")
        Last_Name = _json['Last_Name']
        print(Last_Name, "Last_Name")
        Created_on = date_today
        print(Created_on, "Created_on")
        created_by = _json['created_by']
        print(created_by, "created_by")
        Updated_on = date_today
        print(Updated_on, "Updated_on")
        Updated_by = _json['Updated_by']
        print(Updated_by, "Updated_by")
        Role = _json['Role']
        print(Role, "Role")
        Teams = _json['Teams']
        print(Teams, "Teams")
        delete = _json['delete']
        # delete = dele.encode()
        print(delete, "deletee", delete)

        # validate the received values
        if User_ID and Password and First_Name and Last_Name and \
                Created_on and created_by and Updated_on and Updated_by and Role and Teams and delete and request.method == 'PUT':
            _hashed_password = generate_password_hash(Password)  # do not save password as a plain text so the
            # generate_password_hash will encrypt the password
            # save edits
            sql = "UPDATE Users SET Password=%s, First_Name = %s," \
                  " Last_Name = %s, Created_on = %s, created_by = %s, Updated_on = %s,Updated_by=%s, Role=%s, Teams=%s, delete=%s WHERE User_ID=%s "  # qurey for updating
            print(sql, "sqlllllll")
            data = (
                _hashed_password, First_Name, Last_Name, Created_on, created_by, Updated_on, Updated_by, Role, Teams,
                delete,
                User_ID
            )  # taking the datas from frondend and passing in to a variable
            print(data, "dataaa")
            conn = connectDB()  # connecting to the database
            cursor = conn.cursor()
            query1 = "SELECT User_ID FROM Users"  # qurey for selecting email id from the usertable
            print(query1, "qq11")
            cursor.execute(query1)  # executing the qurey
            db223 = cursor.fetchall()  # fetching the qurey
            print(db223, "db22")
            userid = []  # created an empty list for adding the email ids

            for i in db223:  # iterating the fetched values
                for j in i:  # iterating the tuples
                    userid.append(j)
            print(userid, "userrr")
            if User_ID in userid:
                cursor.execute(sql, data)  # executing the qurey and the datas from frond end
                conn.commit()
                resp = jsonify('User updated successfully!')  # jsonifying the response
                resp.status_code = 200  # making the status as 200 (true)
                conn.close()
                return resp  # if the above condition works then giving the response 200
            else:
                resp = jsonify(
                    'no userid!')  # if the userid is present in the list it will show response as this
                resp.status_code = 400  # status code made as 400
                return resp
        else:
            res = jsonify('User not found')  # jsonifying the response
            res.status_code = 400  # giving status code 400 (False)
            return res  # returning the response

    """permanently delete"""
    """this code is not needed"""

@app.route('/delete-permanent/<id>', methods=['DELETE'])
def permanently_delete(id):  # created a function for deleting user with their corresponding
        # id so thats why the id passing as an argument it will call in the url
        id = (id)
        conn = connectDB()  # connecting to the database
        cursor = conn.cursor(
            cursor_factory=RealDictCursor)  # created a cursor function and giving cursor_factory=RealDictCursor

        cursor.execute("SELECT * FROM Users WHERE User_ID=%s", (id,))  # qurey for selecting the datas with the given id
        # and given to the cursor and it will execute
        db22 = cursor.fetchall()  # fetching all the datas of that corresponding id
        print(db22, "db22")
        if len(db22) != 0:  # checking condition if the user is not null
            cursor.execute("DELETE FROM Users WHERE User_ID=%s", id)  # qurey for deleting and it will
            # work only the value is not equal to null
            conn.commit()
            resp = jsonify('User deleted successfully!')  # response is jsonifying
            resp.status_code = 200  # giving status code as 200 (true)
            return resp  # if the above condition works thengive the response as 200
        else:
            res = jsonify("User not available with  id ", id)  # if the user is null then this response works
            res.status_code = 400  # error response
            return res

    """deleting user (changing the delete as 0) """
@app.route('/Delete_Role/<id>', methods=['PUT'])
def delete_user(id):  # created a function for deleting user with their corresponding
        # id so thats why the id passing as an argument it will call in the url
        id = int(id)
        print(id, "id")

        conn = connectDB()  # connecting to the database
        cursor = conn.cursor()  # created a cursor function and giving cursor_factory=RealDictCursor

        cursor.execute("SELECT * FROM Users  WHERE User_ID=%s",
                       (id,))  # qurey for selecting the datas with the given id
        # and given to the cursor and it will execute
        db22 = cursor.fetchall()  # fetching all the datas of that corresponding id
        print(db22, "db22")
        """test"""
        query1 = "SELECT User_ID FROM Users WHERE DELETE ='0' ;"
        print(query1, "qqq1111")
        cursor.execute(query1)
        db33 = cursor.fetchall()
        print(db33, "db3333333333")
        dele = []
        for i in db33:
            # print(i,"iii")
            for j in i:
                # print(j,"jjjj")
                dele.append(j)
        print(dele, "dele")
        if id in dele:
            print("its already deleted")
            res = jsonify('This is already deleted!')  # jsonifying the response
            res.status_code = 400  # giving status code 400 (False)
            return res

        """endtest"""
        if len(db22) != 0:  # checking condition if the user is not null
            cursor.execute("UPDATE  Users SET DELETE ='0'WHERE User_ID =%s", (id,))  # qurey for deleting and it will
            # work only the value is not equal to null
            conn.commit()
            resp = jsonify('User deleted successfully!')  # response is jsonifying
            resp.status_code = 200  # giving status code as 200 (true)
            return resp  # if the above condition works thengive the response as 200
        else:
            res = jsonify("User not available with  id ", id)  # if the user is null then this response works
            res.status_code = 400  # error response
            return res

   

# function to convert json format from list of tuples and array.
def convert_json(l_o_t, key):
    b = []
    # iterating  the list of tuples to get individual tuples.
    for item in l_o_t:
        a = {}
        # taking range from 0 to number of items in tuples - 1
        for i in range(len(item)):
            a[key[i]] = item[
                i]  # appending value to dictionary by mapping key from array to value in tuples using indexing.
        b.append(a)  # appending all dictionaries to a list.
    return b

@app.route('/list_asset/reserved', methods=['GET'])
def list_all_reserved():
        try:
            cursor = dbase.cursor()
            # To show reserved servers,fetch all the data base from the asset table where reserved=false.
            cursor.execute(
                "select asset_id,manufacturer,bmc_ip,bmc_user,asset_location,assigned_to,assigned_from,assigned_by,created_on,created_by,updated_on,updated_by,purpose,cluster_id from asset where reserved=true")
            res = cursor.fetchall()
            print(res)
            arr = [desc[0] for desc in cursor.description]  # getting column name from database
            json_data = convert_json(res, arr)
            # if json.args()
            return jsonify(json_data)
        except Exception as e:
            print(e)
        finally:
            cursor.close()

@app.route('/list_asset/pool', methods=['GET'])
def list_all_pool():
        try:
            cursor = dbase.cursor()
            # To show reserved servers,fetch all the data base from the asset table where reserved=false.
            cursor.execute(
                "select asset_id,manufacturer,bmc_ip,bmc_user,asset_location,assigned_to,assigned_from,assigned_by,created_on,created_by,updated_on,updated_by,purpose,cluster_id from asset where reserved=false")
            res = cursor.fetchall()
            print(res)
            arr = [desc[0] for desc in cursor.description]  # getting column name from database
            json_data = convert_json(res, arr)

            return jsonify(json_data)
        except Exception as e:
            print(e)
        finally:
            cursor.close()

@app.route('/my_server', methods=['GET'])
def my_server():
        try:
            cursor = dbase.cursor()
            cursor.execute("select user_id from users")
            result = cursor.fetchall()
            list_user_id = []
            for i in result:
                for j in i:
                    list_user_id.append(j)
            print(list_user_id)

            user_id = request.json.get('user_id')
            print(user_id)
            print(type(user_id))
            cursor1 = dbase.cursor()
            if int(user_id) in list_user_id:
                query = "select * from asset where reserved=%s and assigned_to=%s"
                cursor1.execute(query, [True, user_id])
                res = cursor1.fetchall()
                arr = [desc[0] for desc in cursor1.description]  # getting column name from database
                json_data = convert_json(res, arr)
                return jsonify(json_data)
            else:
                return jsonify({"error": "Invalid user_id"})
        except Exception as e:
            error = {"error": e}
            return jsonify(error)
        finally:
            cursor1.close()
@app.route('/release_asset', methods=['PUT'])
def release():
        try:
            cursor = dbase.cursor()
            asset_id = request.json.get('asset_id')
            cursor.execute("select reserved from asset where asset_id=%s", [asset_id])
            res = cursor.fetchall()
            print(res)
            for i in res:
                for j in i:
                    if j:
                        cursor1 = dbase.cursor()
                        cursor1.execute(
                            "update asset set assigned_to=NULL,assigned_from=NULL,assigned_by=NULL,status = %s,reserved=%s where asset_id=%s",
                            [False, False, asset_id])
                        cursor1.execute(
                            "select assigned_to,assigned_from,updated_on,updated_by from asset where asset_id=%s",
                            [asset_id])
                        details = cursor1.fetchall()
                        for item in details:
                            assigned_to = item[0]
                            assigned_from = item[1]
                            updated_on = item[2]
                            updated_by = item[3]
                        cursor1.execute("select id from historic_details")
                        res1 = cursor1.fetchall()
                        l = []
                        for ii in res1:
                            for jj in ii:
                                l.append(jj)
                        l.sort()
                        id = l[-1] + 1
                        cursor1.execute(
                            "INSERT INTO Historic_details(ID,Asset_ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            [id, asset_id, assigned_to, assigned_from, updated_on, updated_by, 'releasing asset'])

                        return jsonify({"status 200": "server released!"})

                    else:
                        return jsonify({"StatusInternalServerError": "Invalid character 400",
                                        "message": "server already released!!"})
        except Exception as e:
            print(e)
            return jsonify({"StatusInternalServerError": "Invalid character 400"})

@app.route('/assign_asset', methods=['PUT'])
def assign():
        try:
            cursor = dbase.cursor()
            # getting asset id and user id from input parameters
            asset_id = request.json.get('asset_id')
            user_id = request.json.get('user_id')
            cursor1 = dbase.cursor()
            cursor.execute("select reserved from asset where asset_id=%s", [asset_id])
            res = cursor.fetchall()

            for i in res:
                for j in i:
                    if j:
                        return jsonify({"Message": "server already assigned!", "Status Code": "400 Bad Request"})
                    else:
                        cursor1.execute("select id from historic_details")
                        res1 = cursor1.fetchall()
                        l = []
                        for ii in res1:
                            for jj in ii:
                                l.append(jj)
                        l.sort()
                        id = l[-1] + 1
                        cursor1.execute("select Updated_on,Updated_by from asset where asset_id=%s", [asset_id])
                        resultt = cursor1.fetchall()
                        for data in resultt:
                            Updated_on = data[0]
                            Updated_by = data[1]
                        cursor1.execute(
                            "INSERT INTO Historic_details(ID,Asset_ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            [id, asset_id, user_id, date.today(), Updated_on, Updated_by, 'assigning server'])
                        cursor1.execute(
                            "update asset set assigned_to=%s,assigned_from=%s, assigned_by=%s,status=%s,reserved=%s where asset_id=%s",
                            [user_id, date.today(), user_id, True, True, asset_id])
                        return jsonify({"Message": "Server Assigned!", "Status Code": "200 OK"})
        except Exception as e:
            print(e)
            return jsonify({"Message": e, "Status Code": "400 Bad Request"})




#user()






@app.route('/add_server', methods=['POST'])
def add_user():
        conn = connectDB()  # called the connectDB file to connect with the database
        # connecting with the database
        # dbase = psycopg2.connect(         #the database is assigned by dbase
        #     host='localhost',
        #     dbname='server111',
        #     user='postgres',
        #     password='root',
        #     port=5433)
        conn.autocommit = True  # if you commit a database, it saves all the changes till that particular point

        #    _json = request.json  # converting to json

        if request.method == 'POST':  # using POST method to request the data
            _json = request.json
            print("sonali")
            print("_json")
            Asset_ID = _json["Asset_ID"]  # list of column data from server_table
            # id = _json["id"]
            Manufacturer = _json["Manufacturer"]
            BMC_ip = _json["BMC_ip"]
            BMC_User = _json["BMC_User"]
            BMC_password = _json["BMC_password"]
            Asset_location = _json["Asset_location"]
            # Reserved = _json["Reserved"]
            # # assigned_on = _json["assigned_on"]
            # Assigned_to = _json["Assigned_to"]
            # Assigned_from=_json["Assigned_from"]
            # Assigned_by = _json["Assigned_by"]
            Created_on = _json["Created_on"]
            Created_by = _json["Created_by"]
            OS_IP = _json["OS_IP"]
            OS_User = _json["OS_User"]
            OS_Password = _json["OS_Password"]
            # Updated_on=_json["Updated_on"]
            # Updated_by= _json["Updated_by"]
            Purpose = _json["Purpose"]
            Cluster_Id = _json["Cluster_Id"]
            # team_id = _json["team_id"]
            Delete = "0"
            # Status = _json["Status"]
            print("server_id")
            cursor = conn.cursor()  # created a cursor
            print("zdfrhv")
            query1 = "SELECT Asset_ID FROM Asset"
            print(query1, "q1111")
            cursor.execute(query1)
            fetch = cursor.fetchall()
            print(fetch, "fe1111")
            lst = []
            for i in fetch:
                for j in i:
                    lst.append(j)
                print(lst, "lsttt")
            if Asset_ID in lst:
                return "already exist"
                print("already exist")

            else:

                # values to assign in the columns
                VALUES = (Asset_ID, Manufacturer, BMC_ip, BMC_User, BMC_password,
                          Asset_location,  # Reserved,Assigned_to,Assigned_from,Assigned_by,
                          Created_on, Created_by, OS_IP, OS_User, OS_Password,  # Updated_on,Updated_by,
                          Purpose, Cluster_Id, Delete)  # Delete,Status)
                print("iohvd")
                cursor.execute(
                    'INSERT INTO Asset(Asset_ID,Manufacturer,BMC_ip,BMC_User,'
                    'BMC_password,Asset_location,Created_on,Created_by,OS_IP,OS_User,OS_Password,Purpose,Cluster_Id,delete) '
                    'values (%s, %s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', VALUES)
                # execute the values using cursor in the server_table to store all the new data
                print("awxfyn")

                # CREATE TABLE Asset(Asset_ID  SERIAL NOT NULL PRIMARY KEY,Manufacturer varchar NOT NULL, BMC_ip varchar NOT NULL, BMC_User varchar NOT NULL,
                # BMC_password varchar NOT NULL, Asset_location varchar NOT NULL,Reserved BOOL, Assigned_to int null ,Assigned_from DATE  null,Assigned_by varchar(50)  null,
                # Created_on DATE  NULL,Created_by VARCHAR(50)  NULL,Updated_on DATE  NULL,Updated_by varchar  NULL,Purpose varchar(300) NOT NULL,Cluster_Id  Varchar Not NULL, Delete BIT NOT NULL,Status BOOL NOT NULL );

                # cursor.commit()
                conn.commit()
                print("_id")
                # conn.commit()  # commit
                print("oook")
                cursor.execute('select * from asset')  # to show the data in the asset_table
                print("fjrdgchk")
                data = cursor.fetchall()  # it will fetch all the data with variable data

                print("_id")

                # serverList = []          #using the for loop to execute all data oneby one and then stored in the serverlist
                # for serverData in data:
                #     data = {"Asset_ID": serverData[0], "Manufacturer": serverData[1],"BMC_ip": serverData[2], "BMC_User": serverData[3],
                #             "BMC_password": serverData[4], "Asset_location": serverData[5],
                #             "Reserved": serverData[6],"Assigned_to":serverData[9],"Assigned_from":serverData[8],"Assigned_by":serverData[7],
                #             "Created_on":serverData[10],"Created_by":serverData[11],"Updated_on":serverData[12],"Updated_by":serverData[13],"Purpose":serverData[14],"Cluster_Id":serverData[15] ,
                #             "Delete":serverData[16],"Status":serverData[17]}

                # serverList.append(data)
                # return jsonify(serverList)            #it will show list of server with this newly added
                resp = jsonify('server added successfully!')  # created a response and jsonifed it
                resp.status_code = 200  # given a status code 200(truse) to the above response
                return resp  # returning the response if the above condition works

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/delete_server/', methods=['PUT'])
def delete_server():
        conn = connectDB()
        # conn = psycopg2.connect(host='localhost', dbname='server111', user='postgres', password='root',
        #                         # connection with database naming conn
        #                         port=5433)
        cursor = conn.cursor()  # cursor object is created
        cur = conn.cursor()
        conn.autocommit = True
        # date_object = datetime.date.today()
        # print(date_object)
        if request.method == 'PUT':  # get method is used
            # asset_id = request.args['asset_id']  #get arguments from url
            Asset_ID = request.args['Asset_ID']
            # id = request.args["id"]
            # asset_id = request.args['asset_id']
            print("abcytfhjf")  # print line just to check whether the is working ornot uptothis line
            cursor.execute("SELECT * FROM asset WHERE Asset_ID= %s",
                           Asset_ID)  # qurey for selecting the datas with the given asset_id
            # and given to the cursor and it will execute
            print("xydtrvhoi")
            data = cursor.fetchall()  # fetching all the datas of that corresponding id
            print(data, "dattttaaa")  # it will print the data with "datttaaa"
            lst = []  # here assigned the array named lst[] which stores the data
            for i in data:
                for j in i:
                    lst.append(j)  # it will append the data in sequence
            print(lst, "lsttt")  # print line
            # if asset_id in lst:
            if len(data) != 0:
                print("asset_id is there")
                cursor.execute("UPDATE  ASSET SET DELETE ='1',Reserved= False,Updated_on=%s WHERE Asset_ID =%s",
                               [date.today(),
                                Asset_ID])  # it will execute the data by serching asset_id and chng the status of the delete
                # id= json.request.get["id"]
                print("zfseyfxgfu")
                # query1= "SELECT * FROM ASSET WHERE  Asset_ID =%s",Asset_ID
                cur.execute(
                    "SELECT Asset_ID,Assigned_to,Assigned_from,Updated_on,Updated_by FROM ASSET WHERE Asset_ID =%s",
                    Asset_ID)
                print("axydt cgbi; kn/on'i")
                data = cur.fetchall()  # fetching all the datas of that corresponding id
                print(data, "dattttaa")
                remarks = "remark"

                lst = []
                for i in data:
                    for j in i:
                        lst.append(j)
                        # lst.append()
                print(lst, "lsssttttt")  # it will print the list lst
                print(lst[0], "ppppp")
                # print(lst[1],"qqqq")
                # print(lst[2],"ooo")
                # print(lst[3],"333")
                # print(lst[4],"44")
                lst2 = lst + [remarks]  # creating another list to add the string format REMARK with that list lst
                print(lst2, "l222")

                query = (lst2[0], lst2[1], lst2[2], lst2[3], lst2[4],
                         lst2[5])  # query to get all the fields starting from index 0 to 5
                # print(query,"qqq")
                # print(lst[0],"1lst")
                # print(lst[0],"9999")
                cur.execute(
                    'INSERT INTO  historic_details(Asset_ID,Assigned_to,Assigned_from,Updated_on,Updated_by,remarks)values (%s, %s ,%s ,%s ,%s,%s)',
                    query)

                print(query, "queryyyyyyyyy")  # it will print the query
                # data = query.fetchall()
                print("hgcsa xb")

                conn.commit()
                resp = jsonify('UPDATED successfully!')  # response is jsonifying
                resp.status_code = 200  # giving status code as 200 (true)
                return resp  # if the above condition works thengive the response as 200


            else:
                print("asset_id is not there")
                res = jsonify("ERROR")  # if the user is null then this response works
                res.status_code = 400  # error response
                return res

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/view_server', methods=["GET"])
def view_server():
        conn = connectDB()
        # conn = psycopg2.connect(host='localhost', dbname='server_management1', user='postgres', password='root',
        #                         # connection with database naming conn
        #                         port=5433)
        # conn = dbase.connect()
        cursor = conn.cursor()
        conn.autocommit = True

        if request.method == 'GET':  # GET method is used here
            cursor.execute('select * from asset')  # store inserver_table
            data = cursor.fetchall()  # crusor fetchs all the data
            serverl = []  # serverlist for get method with variable serverl
            for serverData in data:
                jsonData = {"Asset_ID": serverData[0], "Manufacturer": serverData[1], "BMC_ip": serverData[2],
                            "BMC_User": serverData[3],
                            # "BMC_password": serverData[4],
                            "Asset_location": serverData[5], "Reserved": serverData[6], "OS_IP": serverData[14],
                            "OS_User": serverData[15],
                            # "Created_on":serverData[10],"Created_by":serverData[11],"Updated_on":serverData[12],"Updated_by":serverData[13],
                            "Purpose": serverData[17], "Cluster_Id": serverData[18],
                            # "Delete":serverData[16],
                            "Status": serverData[19]}
                serverl.append(jsonData)  # it will show all the data stored in the database with key:value
        return jsonify(serverl)

    # api to update asset/servers

@app.route('/update_asset', methods=['PUT'])
def update_asset():
        conn = connectDB()
        if request.method == 'PUT':
            _json = request.json
            asset_id = _json["asset_id"]
            asset_location = _json["asset_location"]
            purpose = _json["purpose"]
            bmc_password = _json["bmc_password"]
            cursor = conn.cursor()
            data = (bmc_password, asset_location, purpose)
            cursor.execute('select * from asset where asset_id=%s', asset_id)
            sql_update_query = """UPDATE asset set bmc_password = %s , asset_location = %s , purpose = %s  where asset_id = %s"""
            cursor.execute(sql_update_query, (bmc_password, asset_location, purpose, asset_id))
            conn.commit()
            cursor.execute('select * from asset where asset_id = %s', asset_id)
            data = cursor.fetchall()
            resp = jsonify({'message': 'Asset updated successfully !!'})
            resp.status_code = 200
            return resp

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#infa admin
base=connectDB()
#base.autocommit = True
cursor = base.cursor()
cur = base.cursor()
app = Flask(__name__)



@app.route('/reset_password', methods=['POST'])
def Reset_password():
        id = request.json.get('id')
        password = request.json.get('password')
        if len(password) < 8 or len(password) > 16:
            return 'check password'
        else:
            uc = 0
            lc = 0
            for i in password:
                if i.isupper():
                    uc += 1
                if i.islower():
                    lc += 1
            out = re.findall("\W+", password)
            if uc >= 1 and lc >= 1 and len(out) >= 1:
                hashed_password = generate_password_hash(password)
                cur.execute('update  users SET password =%s where user_id = %s', (hashed_password, id))
                return 'successfully changed password'
            else:
                return 'check password'

@app.route('/change_password', methods=['POST'])
def change_password():
        old_password = request.json.get('old_password')
        new_password = request.json.get('new_password')
        id = request.json.get('id')
        cur.execute('SELECT * FROM users where user_id=%s', [id])
        res = cur.fetchall()
        l = []
        for i in res:
            for j in i:
                l.append(j)
        stored_password = l[2]
        result = check_password_hash(stored_password, old_password)
        if result == True:
            if len(new_password) < 8 or len(new_password) > 16:
                return ("check password")
            else:
                uc = 0
                lc = 0
                for i in new_password:
                    if i.isupper():
                        uc += 1
                    if i.islower():
                        lc += 1
                out = re.findall("\W+", new_password)
                if uc >= 1 and lc >= 1 and len(out) >= 1:
                    hashed_password = generate_password_hash(new_password)
                    cur.execute('update  users SET password =%s where user_id = %s', (hashed_password, id))
                    return '200 (Ok) successfully changed password '
                else:
                    return "check password"
        else:
            return (" 401 unauthorized")

app.route('/server_piechart', methods=['GET'])
def Server_piechart():
        conn = connectDB()
        cursor = conn.cursor()  # created a cursor
        cursor.execute('select asset_id from asset')
        res = cursor.fetchall()
        count = 0
        for i in res:
            count += 1
        total_servers = count
        cursor.execute('SELECT * FROM asset where reserved=%s', [False])
        res1 = cursor.fetchall()
        pool = len(res1)
        cursor.execute('SELECT * FROM asset where reserved=%s', [True])
        res2 = cursor.fetchall()
        servers = len(res2)
        return jsonify({"total_servers": total_servers, "total_pool_servers": pool, "total_reserved_servers": servers,
                        "status_message": 'Status OK(200) '})

@app.route('/cluster_piehart', methods=['GET'])
def cluster_piechart():
        conn = connectDB()
        cursor = conn.cursor()  # created a cursor
        cursor.execute(" SELECT  cluster_id from asset where reserved=True")
        res = cursor.fetchall()
        l = []
        for i in res:
            if i not in l:
                l.append(i)
        a = len(l)
        return jsonify({"total_clusters": a})

if __name__ == '__main__':
        app.run(port=5000, debug=True)








