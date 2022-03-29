from tkinter import *
import sqlite3

win = Tk()
win.title("database")
win.iconbitmap(None)
win.geometry("400x400")

# Database

# step1.create a Database or connect to
conn = sqlite3.connect('address_book.txt')

# step1.create a cursor
c = conn.cursor()

# step.3 create a table
'''
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name  text,
        address text,
        city text,
        state text,
        zip code integer
) """)
'''


def update():
    # step1.create a Database or connect to
    conn = sqlite3.connect('address_book.txt')

    # step1.create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET first_name = :first,last_name = :last,address = :address,city = :city,
    state = :state,zipcode = :zipcode WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()
    win.deiconify()


# create a function for update a record
# we have create a new window called editor
def edit_():
    win.withdraw()
    global editor
    editor = Tk()
    editor.title("update")
    editor.iconbitmap(None)
    editor.geometry("400x300")

    # step1.create a Database or connect to
    conn = sqlite3.connect('address_book.txt')

    # step1.create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    # Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # step.2 create text box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=2, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # step.2 create text box label
    f_name_label_editor = Label(editor, text="first name")
    f_name_label_editor.grid(row=0, column=0)
    l_name_label_editor = Label(editor, text="last name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="your city")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="state")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="zip code")
    zipcode_label_editor.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create a save button To Save edited record
    save_btn = Button(editor, text="save Record", command=edit_)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


# step .6 create a delete function to delete records
# there are many common records(name) so we have used oid(primary key number) for deleting a records

def delete():
    # create a Database or connect to
    conn = sqlite3.connect('address_book.txt')

    # create a cursor
    c = conn.cursor()

    # delete records fro data base
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# step.4
def submit():
    # create a Database or connect to
    conn = sqlite3.connect('address_book.txt')

    # create a cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear text boxes
    f_name.delete((0, END))
    l_name.delete((0, END))
    address.delete((0, END))
    city.delete((0, END))
    state.delete((0, END))


# step5.create query function
def query():
    # create a Database or connect to
    conn = sqlite3.connect('address_book.txt')

    # create a cursor
    c = conn.cursor()

    # query the data base
    c.execute("SELECT * ,oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop Through Results
    print_records = ''
    for record in records:
        # print_records += str(record) + "\n"
        # print_records += str(record[1]) + "\n"
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(win, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# step.2 create text box

f_name = Entry(win, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(win, width=30)
l_name.grid(row=1, column=1)
city = Entry(win, width=30)
city.grid(row=2, column=1)
address = Entry(win, width=30)
address.grid(row=3, column=1)
state = Entry(win, width=30)
state.grid(row=4, column=1)
zipcode = Entry(win, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(win, width=30)
delete_box.grid(row=9, column=1, pady=5)

# step.2 create text box label

f_name_label = Label(win, text="first name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(win, text="last name")
l_name_label.grid(row=1, column=0)
address_label = Label(win, text="address")
address_label.grid(row=2, column=0)
city_label = Label(win, text="your city")
city_label.grid(row=3, column=0)
state_label = Label(win, text="state")
state_label.grid(row=4, column=0)
zipcode_label = Label(win, text="zip code")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(win, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# step 2.Create Submit Button
submit_btn = Button(win, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# step.5 Create a Query Button
query_btn = Button(win, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# step.6 Create A Delete Button
delete_btn = Button(win, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# step.7 create a update button

edit_btn = Button(win, text="edit Record", command=edit_)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# step.1 commit changes
conn.commit()

# close connection
conn.close()

win.mainloop()
