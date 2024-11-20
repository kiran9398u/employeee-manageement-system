from tkinter.messagebox import showerror, showinfo, askyesno
from customtkinter import *
from PIL import Image
from tkinter import ttk

import database
def delete_all():
    result = askyesno("Confirm", "Do you really want to delete all the records?")
    if result:
        database.delete_all_records()
        treeview_data()

def show_all():
    treeview_data()
    searchEntry.delete(0, END)
    search_Box.set("Search by")

def search_employee():
    if searchEntry.get() == "":
        showerror("Error", "Enter value to search")
    elif search_Box.get() == "Search by":
        showerror("Error", "Please select an option")
    else:
        searched_data = database.search(search_Box.get(), searchEntry.get())
        tree_view.delete(*tree_view.get_children())
        for employee in searched_data:
            tree_view.insert("", END, values=employee)

def delete_employee():
    selected_items = tree_view.selection()
    if not selected_items:
        showerror("Error", "Select data to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        showinfo("Success", "Data is deleted")

def update_employee():
    selected_item = tree_view.selection()
    if not selected_item:
        showerror("Error", "Select data to update")
    else:
        database.update(
            idEntry.get(), nameEntry.get(), phoneEntry.get(),
            role_Box.get(), gender_Box.get(), salaryEntry.get()
        )
        treeview_data()
        clear()
        showinfo("Success", "Data is updated")

def selection(event):
    selected_items = tree_view.selection()
    if selected_items:
        row = tree_view.item(selected_items)["values"]
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        role_Box.set(row[3])
        gender_Box.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):
    if value:
        tree_view.selection_remove(tree_view.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    role_Box.set("Web Developer")
    gender_Box.set("Male")
    salaryEntry.delete(0, END)

def treeview_data():
    employees = database.fetch_employees()
    tree_view.delete(*tree_view.get_children())
    for employee in employees:
        tree_view.insert("", END, values=employee)

def add_employee():
    if idEntry.get() == "" or phoneEntry.get() == "" or nameEntry.get() == "" or salaryEntry.get() == "":
        showerror("Error", "All fields are essential")
    elif database.id_exists(idEntry.get()):
        showerror("Error", "ID already exists")
    elif not idEntry.get().startswith("EMP"):
        showerror("Error", "Invalid ID format. Use 'EMP' followed by a number (e.g., 'EMP001')")
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), role_Box.get(), gender_Box.get(),
                        salaryEntry.get())
        treeview_data()
        clear()
        showinfo("Success", "Data is added successfully")

# Main window setup
main_window = CTk()
main_window.title("Main Window")
main_window.geometry("930x580")
main_window.resizable(0,0)
main_window.configure(fg_color=("#2B2D30"))

# Logo
logo = CTkImage(Image.open("img.png"), size=(938, 158))
logoLabel = CTkLabel(main_window, image=logo, text="")
logoLabel.grid(row=0, column=0, columnspan=2)

# Left Frame for Input fields
leftFrame = CTkFrame(main_window)
leftFrame.grid(row=1, column=0)

idLabel = CTkLabel(leftFrame, text="Id", font=("arial", 18, "bold"))
idLabel.grid(row=1, column=0, padx=(0, 10), sticky="w", pady=5)

idEntry = CTkEntry(leftFrame, font=("arial", 18, "bold"), width=180)
idEntry.grid(row=1, column=1)

nameLabel = CTkLabel(leftFrame, text="Name", font=("arial", 18, "bold"))
nameLabel.grid(row=2, column=0, padx=(0, 10), pady=15, sticky="w")

nameEntry = CTkEntry(leftFrame, font=("arial", 18, "bold"), width=180)
nameEntry.grid(row=2, column=1)

phoneLabel = CTkLabel(leftFrame, text="Phone", font=("arial", 18, "bold"))
phoneLabel.grid(row=3, column=0, padx=(0, 10), sticky="w")
phoneEntry = CTkEntry(leftFrame, font=("arial", 18, "bold"), width=180)
phoneEntry.grid(row=3, column=1)

roleLabel = CTkLabel(leftFrame, text="Role", font=("arial", 18, "bold"))
roleLabel.grid(row=4, column=0, padx=(0, 10), sticky="w")

role_options = ["Web Developer", "SQL Developer", "Java Developer", "PHP Developer", "Python Developer", "Cloud Architect",
                "Data Engineer", "System Administrator", "Data Scientist", "Data Analyst", "Technical Support Engineer", "UI Designer"]
role_Box = CTkComboBox(leftFrame, values=role_options, width=180, state="readonly")
role_Box.grid(row=4, column=1, pady=15)
role_Box.set(role_options[0])

genderLabel = CTkLabel(leftFrame, text="Gender", font=("arial", 18, "bold"))
genderLabel.grid(row=5, column=0, sticky="w")

gender_options = ["Male", "Female"]
gender_Box = CTkComboBox(leftFrame, values=gender_options, width=180, state="readonly")
gender_Box.grid(row=5, column=1, pady=15)
gender_Box.set(gender_options[0])

salaryLabel = CTkLabel(leftFrame, text="Salary", font=("arial", 18, "bold"))
salaryLabel.grid(row=6, column=0, sticky="w")

salaryEntry = CTkEntry(leftFrame, font=("arial", 18, "bold"), width=180)
salaryEntry.grid(row=6, column=1)

# Right Frame for Treeview and Search
rightFrame = CTkFrame(main_window)
rightFrame.grid(row=1, column=1)

search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]
search_Box = CTkComboBox(rightFrame, values=search_options, state="readonly")
search_Box.grid(row=0, column=0)
search_Box.set("Search by")

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=5)

searchButton = CTkButton(rightFrame, text="Search", width=100, command=search_employee)
searchButton.grid(row=0, column=2)

showallButton = CTkButton(rightFrame, text="Show All", width=100, command=show_all)
showallButton.grid(row=0, column=3, padx=5)

tree_view = ttk.Treeview(rightFrame, show="headings")
tree_view.grid(row=1, column=0, columnspan=4)

tree_view["columns"] = ("Id", "Name", "Role", "Gender", "Salary")
tree_view.heading("Id", text="Id")
tree_view.heading("Name", text="Name")
tree_view.heading("Role", text="Role")
tree_view.heading("Gender", text="Gender")
tree_view.heading("Salary", text="Salary")

tree_view.column("Id", anchor="center", width=100)
tree_view.column("Name", anchor="center", width=100)
tree_view.column("Role", anchor="center", width=100)
tree_view.column("Gender", anchor="center", width=100)
tree_view.column("Salary", anchor="center", width=100)

style = ttk.Style()
style.configure("Treeview.Heading", font=("arial", 12, "bold"))
style.configure("Treeview", font=("arial", 12, "bold"), rowheight=30, background="#161C30", foreground="white")

scrollbar = ttk.Scrollbar(rightFrame, orient="vertical", command=tree_view.yview)
scrollbar.grid(row=1, column=4, sticky="ns")
tree_view.config(yscrollcommand=scrollbar.set)

# Button Frame for Actions
buttonFrame = CTkFrame(main_window)
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text="New Employee", font=("arial", 10, "bold"), width=160, corner_radius=15, command=lambda: clear(True))
newButton.grid(row=0, column=0, pady=20, padx=10)

addButton = CTkButton(buttonFrame, text="Add Employee", font=("arial", 10, "bold"), width=160, corner_radius=15, command=add_employee)
addButton.grid(row=0, column=1, pady=10, padx=10)

updateButton = CTkButton(buttonFrame, text="Update Employee", font=("arial", 10, "bold"), width=160, corner_radius=15, command=update_employee)
updateButton.grid(row=0, column=2, pady=10, padx=10)

deleteButton = CTkButton(buttonFrame, text="Delete Employee", font=("arial", 10, "bold"), width=160, corner_radius=15, command=delete_employee)
deleteButton.grid(row=0, column=3, pady=10, padx=10)

deleteAllButton = CTkButton(buttonFrame, text="Delete All", font=("arial", 10, "bold"), width=160, corner_radius=15, command=delete_all)
deleteAllButton.grid(row=0, column=4, pady=10, padx=10)

tree_view.bind("<<TreeviewSelect>>", selection)

treeview_data()

main_window.mainloop()
