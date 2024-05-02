import psycopg2  #imports psycopg2, which allow us to connect and to interact woth a PosgreSQL database
import csv # csv helps us work with data in Comma-Seperated Values format.

#folowing lines establish a connection to the PostgreSQL database named phonebook
db = psycopg2.connect( dbname = "phonebook", #database name
                    user = "postgres", # with password it provide the credentials for the database user 'postgres'
                    password = "1234",
                    host = "localhost" #indicate the location of the database.
)

#create a cursor object, which allows s to execute SQL queries on the database.
current = db.cursor  

#this block presents  a menu to the user with various options for managing phonebook entries.
#it prints a formatted string displaying the available choices.
print('''What do you want?

Press "1" to search contact by name or phone
Press "2" to add a new contact or update existing 
Press "3" to add many contacts by list
Press "4" to see first N contacts
Press "5" to delete contact by name or phone
Press "6" to add contacts from .csv file
Press "7" to change name or phone of contact
Press "8" to see all names of contacts
Press "9" to see all phones of contacts 
Press "10" to see all phonebook
''')

#prompts the user to enter a number corresponding to their desired action and stores it in the variable req.
req = input("Enter the num of the requests:")

#handles different user requests based on the value of req.
if req == '1':   #handles searching contacts by name or phone number
    n = input("Enter name or phone number:")
    sql = """
    SElECT * FROM contacts WHERE contacts.name LIKE %s OR contacts.phone LIKE %s;
"""
    current.execute(sql, (n,n))
    results = current.fetchall()
    print(results)


elif req == '2': #add new contact or updating an existing one.
    name = input("Enter name:")
    phone = input("Enter phone:")
    
    # Delete the existing contact with the given name
    delete_sql = "DELETE FROM contacts WHERE contacts.name = %s;"
    current.execute(delete_sql, (name,))
    
    # Insert the new contact
    insert_sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s);"
    current.execute(insert_sql, (name, phone))
    print("The contact was added successfully!")

elif req == '3': #add contacts from a list
#   example of list = [('v', 123), ('xij', 1331), ('hjdh', 222425626)]
    contact = input("Enter the list of contacts:")
    
    cont = []  #initializing the store the parsed contacts.
    for tup in contact.split('), ('): #loop iterates through each comma-separated elemt(tup) whitin the input string contact.
        tup = tup.replace(')','').replace('(','')  #removes any leading or trailing parentheses from the current element tup.
        cont.append(tuple(tup.split(','))) #split tup by commas, converts it into a tuple, appends ii to the cont list.
    print(cont) #displats the processed lit of contacts for verfication.
    
    sql="""
        INSERT INTO contacts VALUES(%s, %s);  
        #sql defined as an insert query with two placeholders (%S) representing the name and phone columns.
    """
    for i in range(len(cont)):  #iterates through each contact (cont[i]) in the processed list.
        current.execute(sql, (cont[i][0], cont[i][1])) 
        """"
        executes the insert query using the database cursor current.
        it unpacks cont[i],, assuming it's a tuple containing the name at index 0 
        and phone at index1, and binds them to the placeholders in the sql statement.
        """


elif req == '4': #fetching a specific number of entries
    x = input("Enter the number of contacts:") 
    sql = """
        SELECT * FROM contacts; #select all columns from the contacts table 
    """
    current.execute(sql) #execute the defined sql statement using the database cursor. Retrieves all contacts from the table.
    results = current.fetchmany(int(x)) 
    """fetchmany - method that retrieves a specific number of rows from the cursor.
    int(x) converts the user-provided number of contact (x) from a string to an integer, insuring it's a numerical value.
"""
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    #block prints a formattes header for thephonebook output, displaying column titles "name" & "phone"
    for i in range(len(results)): #iterates through the fetched results, which is a list of tuples representing each contact row.
        print('{0:20}{1:20}'.format(results[i][1], results[i][3])) #formats the output for each contact. 
        #result[i][1] & result [i][3] access the name and phone number columns of the current contact.
        #.format() - method insterts these values into the formatted string, ensuring 20 character spaces for both name, phone number.


elif req == '5':  #deleting contacts
    print("Enter the name or phone:")
    delete = input()
    #DELETE query targeting the contacs table. It uses WHERE clause to filter contacts based on the name.
    sql="""
        DELETE FROM contacts WHERE contacts.name = %s;
    """
    current.execute(sql, (delete,)) #executes the DELETE query using the cursor current. It binds the user's input(delete) to the placeholder (%s) in the where clause.
    
    #it defines another delete query targeting the delete query, binding the user's imput(delete) to the placeholder (%s) in the where clause.
    sql="""
        DELETE FROM contacts WHERE contacts.phone = %s;
    """
    current.execute(sql, (delete,)) #exevute this delete query, binding the user's input delete to the placeholder (%s) in the where clause.
    print("Contact", delete, "has been deleted")



elif req == '6': #importing CSV
    #insert new contacts into the contacts table. 
    #(%s) used to represent the values that wil be inserted for each column.
    sql = """
        INSERT INTO contacts (name, surname, phone) VALUES (%s, %s, %s);
    """
    with open(r'/Users/sabinatolkynbekova/Desktop/pp2_2024/lab11/contacts.csv') as f: #open the CSV file located at the specified path/ r indicates a raw string to avoid interpreting backslashes.
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 4:  # Ensure there are at least 4 elements in the row
                current.execute(sql, (row[1], row[2], row[3]))  # Assuming contactid is at index 0
            else:
                print("Invalid row format:", row)
    print("Data has been added to the phonebook")



elif req == '7': #updating names od phones
    w = input("Do you want to update name or phone:")
    if w == 'name':
        x = input("Enter the phone: ")
        y = input("Enter the new name: ")
        sql = """ #defines updae query targeting the contacts table.
            UPDATE contacts SET contacts.name = %s WHERE contacts.phone = %s;
        """
        #sets the name to the new name (%s) where the phone column matches the provided phone number (%s)
        current.execute(sql, (y, x)) #executes the UPDATE query using the cursor current
        print("Data has been updated")
    elif w == 'phone': #checks if the user enteres 'phone'
        x = input("Enter the name: ") #if true
        y = input("Enter the new phone_number: ")
        #defines UPDATE query similar to the name update
        sql = """
            UPDATE contacts SET contacts.phone = %s WHERE contacts.name = %s;
        """
        #defines update qery similar to the name update, but targeting the phone column
        current.execute(sql, (y, x)) #executes the query, binding the new phone number and name to the placeholders.
        print("Data has been updated")



elif req == '8': #displayinh all names or phone number
    sql = """
        SELECT contacts.name FROM contacts
    """
    current.execute(sql) #This retrieves all names from the contacts table.
    results = current.fetchall() #fetches all rows from the result set into a list named results.
    for i in range(len(results)):
        print(results[i][0]) #accesses the first element ([0]) of the current contact tuple




elif req == '9': #showing the entire phonebook
    sql = """
        SELECT contacts.phone FROM contacts
    """
    current.execute(sql) #retrieves all phone numbers from the contacts table.
    results = current.fetchall() #fetches all rows from the result set into a list named results.
    for i in range(len(results)):
        print(results[i][0]) #accesses the first element ([0]) of the current contact tuple (results[i])
        #print(results[i][0]) prints the extracted phone number for each contact in the phonebook.

elif req == "10": 
    sql = "SELECT * FROM contacts;" #selects all data from the phonebook.
    current.execute(sql) # retrieves all rows and columns from the contacts table.
    rows = current.fetchall() # fetches all results from the query into a list named rows.
    for row in rows:
        print(row)

else:
    print("Request is unidentified")

current.close() #close database cursor
db.commit() #commits any changes made to the database during the scprit's execution.
db.close() #closes the connection to the database.