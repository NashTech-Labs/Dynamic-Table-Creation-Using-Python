from connection import *

cnx = getConnection()
cursor = cnx.cursor()

DB_NAME = os.environ.get("DBNAME")

def migrations():
    TABLES = {}

    TABLES['project_details'] = (
        "CREATE TABLE `project_details` ("
        "  `project_id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `project_name` varchar(255) NOT NULL,"
        "  `repo_name` varchar(255) NOT NULL,"
        "  `branch_name` varchar(255) NOT NULL,"
        "  PRIMARY KEY (`project_id`)"
        ") ENGINE=InnoDB")
    
    # TABLES['salaries'] = (
    #     "CREATE TABLE `salaries` ("
    #     "  `emp_no` int(11) NOT NULL,"
    #     "  `salary` int(11) NOT NULL,"
    #     "  `from_date` date NOT NULL,"
    #     "  `to_date` date NOT NULL,"
    #     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    #     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    #     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    #     ") ENGINE=InnoDB")

    # TABLES['dept_emp'] = (
    #     "CREATE TABLE `dept_emp` ("
    #     "  `emp_no` int(11) NOT NULL,"
    #     "  `dept_no` char(4) NOT NULL,"
    #     "  `from_date` date NOT NULL,"
    #     "  `to_date` date NOT NULL,"
    #     "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    #     "  KEY `dept_no` (`dept_no`),"
    #     "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    #     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    #     "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    #     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    #     ") ENGINE=InnoDB")

    # TABLES['dept_manager'] = (
    #     "  CREATE TABLE `dept_manager` ("
    #     "  `emp_no` int(11) NOT NULL,"
    #     "  `dept_no` char(4) NOT NULL,"
    #     "  `from_date` date NOT NULL,"
    #     "  `to_date` date NOT NULL,"
    #     "  PRIMARY KEY (`emp_no`,`dept_no`),"
    #     "  KEY `emp_no` (`emp_no`),"
    #     "  KEY `dept_no` (`dept_no`),"
    #     "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    #     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    #     "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    #     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    #     ") ENGINE=InnoDB")

    # TABLES['titles'] = (
    #     "CREATE TABLE `titles` ("
    #     "  `emp_no` int(11) NOT NULL,"
    #     "  `title` varchar(50) NOT NULL,"
    #     "  `from_date` date NOT NULL,"
    #     "  `to_date` date DEFAULT NULL,"
    #     "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    #     "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    #     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    #     ") ENGINE=InnoDB")



    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()