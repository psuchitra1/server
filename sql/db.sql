CREATE TABLE Users(User_Id SERIAL NOT NULL PRIMARY KEY ,Email_Id varchar(50) Not NULL,Password varchar(1000) NOT NULL,First_Name varchar(250) Not NULL,Last_Name varchar(250) NOT NULL,Created_on timestamp without time zone NOT NULL,Created_by varchar not null, Updated_on timestamp without time zone NULL,Updated_by varchar null,Role varchar(20)NOT NULL,Teams Varchar Not NULL,Delete BIT null);
CREATE TABLE Asset(Asset_Id  SERIAL NOT NULL PRIMARY KEY,Asset_Name varchar (50) NOT NULL,Manufacturer varchar NOT NULL, BMC_IP varchar NOT NULL, BMC_User varchar NOT NULL, BMC_Password varchar NOT NULL, Asset_Location varchar NOT NULL,Reserved BOOL, Assigned_to INT,FOREIGN KEY(Assigned_to) REFERENCES Users(User_Id) ,Assigned_from timestamp without time zone null,Assigned_by varchar(50)  null,Created_on timestamp without time zone NOT NULL,Created_by VARCHAR(50)  NULL,Updated_on timestamp without time zone NULL,Updated_by varchar  NULL,OS_IP inet null,OS_User varchar  NOT NULL,OS_Password varchar(1000) null, Purpose varchar(300) NOT NULL,Cluster_Id  Varchar Not NULL, Delete BIT NULL,Status BOOL  NULL );
CREATE TABLE Historic_details(Id SERIAL NOT NULL  PRIMARY KEY,Asset_Id SERIAL NOT NULL,FOREIGN KEY(Asset_Id) REFERENCES Asset(Asset_Id),Assigned_to INT,FOREIGN KEY(Assigned_to) REFERENCES Users(User_Id),Assigned_from timestamp without time zone NOT NULL,Updated_on timestamp without time zone  NULL,Updated_by varchar not null,Remarks varchar(300)NOT NULL);
CREATE TABLE Server_Request(Id SERIAL NOT NULL PRIMARY KEY,User_No INT NOT NULL,FOREIGN KEY(User_No) REFERENCES Users(User_Id), Creator varchar NOT NULL, Start_Date Date NOT NULL,End_Date Date NOT NULL,Manufacturer varchar(50) NOT NULL,Number_Of_Servers varchar(50)  NOT NULL,Operating_System varchar(100)NOT NULL,Cpu_model varchar(50)NOT NULL,CPU_Sockets varchar(50) NOT NULL,DIMM_Size varchar(50) not null ,DIMM_Capacity varchar(50)NOT NULL ,Storage_Vendor Varchar(50) NOT NULL,Storage_Controller Varchar(50)NOT NULL,Storage_Capacity varchar(50)NOT NULL,Network_Type BOOL NOT NULL,Network_speed varchar(50)NOT NULL,Number_Of_Network_Ports varchar(50) NOT NULL,Special_Switching_Needs Varchar(100),Infraadmin_Comments TEXT [] NULL,User_Comments TEXT [] NULL ,Request bool);


INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'vinee@gmail.com','$2a$08$XXzOzLBuk0VixnLikLlxUO18IBq7j8kv6vFXhrFCJaba0sV9uCw.y','Vineesha','Jasti ','12-07-2022','sushmitha','08-03-2022','sreedhar','admin','T1','0');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'samarthbr@gmail.com','$2a$14$xKApPpBb4qAjcpRqcqCZge.6rn776XIQWYbW6HmXeh45sFOzSubNS','Samarth','BR','12-03-2022','sreedhar','12-03-2022','sreedhar','admin','T1','0');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'akshaydk@gmail.com','$2a$08$J5h2GRrsk5IXhnDpmolDCODEOOKmEfzpm7r5quRHNBUPnZEnOHYJu','Akshay','DK ','08-03-2022','sreedhar','08-03-2022','sreedhar','infra_admin','T1','1');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'mani@gmail.com',' $2a$08$qyg99cBG8375DhCN8o2BWukaEI8k8UusLoS0N9OVvXjVxiy73mP8i','Mani','S ','12-07-2022','sushmitha','08-03-2022','sreedhar','user','T1','0');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'divyasuresh@gmail.com','$2a$14$C19/upt5xPh4ys1wgujWQe0kFb7iE6jlYYKkm0nhLkL6qh/FDhoaS','Divya','Suresh', '11-03-2022','sreedhar','11-03-2022','sreedhar','user','T2','1');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'hemanthKumarhj@gmail.com','$2a$08$fk38oG9BgSGuU2giyisMzuf6P3d4LB36kRhRlrddev1P/SnglsXnq','Hemanthkumar','HJ', '10-03-2022','sreedhar','10-03-2022','sreedhar','user','T3','1');
INSERT INTO Users(User_Id,Email_Id,Password,First_Name, Last_Name ,Created_on, Created_by,Updated_on,Updated_by,Role,Teams,Delete) VALUES (Default, 'pavanilokesh@gmail.com','$2a$08$.WS2ocTs1TvhAMSKJjGwK.pgi6eXL1O/Xtuk1877SE1sXP.eqy6cS','Pavani','lokesh', '09-03-2022','sreedhar','09-03-2022','sreedhar','user','T2','0');


INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'sam server','IBM','10.0.2.3','user', 'user123','BGL','yes',4,'06-03-21','SREEDHAR','06-03-21','kk','06-03-22','kk','127.6.7.8','Administrator','Umar@syed766','Linux testing','C1','0',' yes');
INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'server1','cisco','10.0.2.5','admin', 'admin123','MYS','yes',5,'07-02-22','SREEDHAR','07-03-21','kk','07-03-22','kk','127.6.7.8','Windows10','Umar@syed766','Linux testing','C2','0',' no');
INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'server_name','IBM','10.0.2.6','user', 'user123','HYD','no',6,'11-03-20','SREEDHAR','08-03-21','kk','08-03-22','kk','127.6.7.8','Windows11','Umar@syed766','Linux testing','C1','0',' no');
INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'my_server','cisco','10.0.2.7','admin', 'admin123','BGL','yes',4,'03-11-22','SREEDHAR','09-03-21','kk','09-03-22','kk','127.6.7.8','Win10','Umar@syed766','Linux testing','C4','0',' yes');
INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'IBM_server','IBM','10.0.2.7','user', 'user123','HYD','no',4,'08-03-21','SREEDHAR','10-03-21','kk','10-03-22','kk','127.6.7.8','Linux','Umar@syed766','Linux testing','C1','0',' no');
INSERT INTO Asset(Asset_Id,Asset_name,Manufacturer,BMC_IP,BMC_User,BMC_Password,Asset_Location,Reserved,Assigned_to,Assigned_from,Assigned_by,Created_on,Created_by,Updated_on,Updated_by,OS_IP ,OS_User ,OS_Password ,Purpose,Cluster_ID,Delete,Status) VALUES (Default,'IBM_server','IBM','10.0.2.7','user', 'user123','HYD','no',4,'08-03-21','SREEDHAR','10-03-21','kk','10-03-22','kk','127.6.7.8','Linux','Umar@syed766','Linux testing','C1','0',' no');

    
-- INSERT INTO Historic_details(ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (1, 4,'06-03-2022','06-07-2022','SREEDHAR', 'Server assigned to manage the cloud EC2 changes');
-- INSERT INTO Historic_details(ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (2, 5,'07-04-2022','07-08-2022','SREEDHAR', 'Assigned to manage S3 bucket');
-- INSERT INTO Historic_details(ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (3, 6,'08-05-2022','08-09-2022','SREEDHAR', 'Assigned to manages elastic ip address');
-- INSERT INTO Historic_details(ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (4, 4,'09-06-2022','09-10-2022','SREEDHAR', 'Assigned to manages the websites backend server');
-- INSERT INTO Historic_details(ID,Assigned_to,Assigned_from,Updated_on,Updated_by,Remarks) VALUES (5, 4,'10-07-2022','10-11-2022','SREEDHAR', 'Assigned to manages the websites backend server');


INSERT INTO Server_Request(Id,User_No,Creator, Start_Date,End_Date,Manufacturer,Number_Of_Servers,Operating_System,Cpu_model,CPU_Sockets,DIMM_Size,DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity,Network_Type,Network_speed ,Number_Of_Network_Ports ,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request) VALUES (Default,7,'Pavani','11-07-2022','12-07-2022','HP',2,'Linux','Intel(R)Core(TM)i7-4790CPU@3.60GHz',2,'64gb','1TB / 16 x 64GB','Samsung','SAS','1.5TB','yes','1gb',2,'no',Array[NULL], Array[NULL],True);
INSERT INTO Server_Request(Id,User_No,Creator, Start_Date,End_Date,Manufacturer,Number_Of_Servers,Operating_System,Cpu_model,CPU_Sockets,DIMM_Size,DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity,Network_Type,Network_speed ,Number_Of_Network_Ports ,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request) VALUES (Default,7,'Pavani','11-07-2022','12-07-2022','HP',2,'Linux','Intel(R)Core(TM)i7-4790CPU@3.60GHz',2,'64gb','1TB / 16 x 64GB','Samsung','SAS','1.5TB','yes','1gb',2,'no',Array[NULL], Array[NULL],True);
INSERT INTO Server_Request(Id,User_No,Creator, Start_Date,End_Date,Manufacturer,Number_Of_Servers,Operating_System,Cpu_model,CPU_Sockets,DIMM_Size,DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity,Network_Type,Network_speed ,Number_Of_Network_Ports ,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request) VALUES (Default,6,'Hemanth','11-07-2022','12-07-2022','HP',2,'Linux','Intel(R)Core(TM)i7-4790CPU@3.60GHz',2,'64gb','1TB / 16 x 64GB','Samsung','SAS','1.5TB','yes','1gb',2,'no',Array[NULL], Array[NULL],True);

-- INSERT INTO Server_Request(Id,User_No,Creator, Start_Date,End_Date,Manufacturer,Number_Of_Servers,Operating_System,Cpu_model,CPU_Sockets,DIMM_Size,DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity,Network_Type,Network_speed ,Number_Of_Network_Ports ,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request) VALUES (Default,7,'pavani','11-07-2022','12-07-2022','HP',2,'Linux','Intel(R)Core(TM)i7-4790CPU@3.60GHz',2,'64gb','1TB / 16 x 64GB','Samsung','SAS','1.5TB','yes','1gb',2,'no',Array[NULL], Array[NULL],True);
-- INSERT INTO Server_Request(Id,User_No,Creator, Start_Date,End_Date,Manufacturer,Number_Of_Servers,Operating_System,Cpu_model,CPU_Sockets,DIMM_Size,DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity,Network_Type,Network_speed ,Number_Of_Network_Ports ,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request) VALUES (Default,6,'Hemanth','11-07-2022','12-07-2022','HP',2,'Linux','Intel(R)Core(TM)i7-4790CPU@3.60GHz',2,'64gb','1TB / 16 x 64GB','Samsung','SAS','1.5TB','yes','1gb',2,'no',Array[NULL], Array[NULL],True);