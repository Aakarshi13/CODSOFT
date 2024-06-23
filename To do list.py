import tkinter as tk                
from tkinter import ttk     
from tkinter import messagebox          
import sqlite3 as sql                 
  

def add_task():  
      
    task_string = task_field.get()  
      
    if len(task_string) == 0:  
          
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        
        tasks.append(task_string)  
          
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
          
        list_update()  
          
        task_field.delete(0, 'end')  
  

def list_update():  
    
    clear_list()  
    
    for task in tasks:  
         
        task_listbox.insert('end', task)  
 
def delete_task():  
      
    try:  
          
        the_value = task_listbox.get(task_listbox.curselection())  
         
        if the_value in tasks:  
            
            tasks.remove(the_value)  
         
            list_update()  
             
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
  
def delete_all_tasks():  
     
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')   
    if message_box == True:  
           
        while(len(tasks) != 0):  
             
            tasks.pop()  

        the_cursor.execute('delete from tasks')  

        list_update()  
  

def clear_list():  
    
    task_listbox.delete(0, 'end')  
  

def close():  
     
    print(tasks)  
     
    guiWindow.destroy()  
  
 
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  
  
if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List")  
    guiWindow.geometry("1000x1000")  
    guiWindow.resizable(100, 0)  
    guiWindow.configure(bg = "#5EFF33")  
  
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    tasks = []  
      
    header_frame = tk.Frame(guiWindow, bg = "#C733FF")  
    functions_frame = tk.Frame(guiWindow, bg = "#C733FF")  
    listbox_frame = tk.Frame(guiWindow, bg = "#C733FF")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Brush Script MT", "45"),  
        background = "#FF33B8",  
        foreground = "#8B4513"  
    )  
    header_label.pack(padx = 80, pady = 80)  
  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Slab Serif", "20", "bold"),  
        background = "#33AFFF",  
        foreground = "#000000"  
    )  
    task_label.place(x = 40, y = 40)  
      
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Balloon", "15"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 40, y = 80)  


    def create_button_style():
     return {
        "width": 20,
        "height": 3,
        "font": ("Forte",10 ),
        "bg": "#E74C3C",
        "fg": "white",
        "bd": 5,
    }
    
    add_button = tk.Button(  
        functions_frame,  
        text = "ADD TASK",  
        command = add_task,
        **create_button_style()
         )

    
    del_button = tk.Button(  
        functions_frame,  
        text = "DELETE TASK",
        command = delete_task ,
        **create_button_style()
    )
    
    del_all_button = tk.Button(
        functions_frame,  
        text = "DELETE All TASKS",    
        command = delete_all_tasks,
        **create_button_style()
    )

    
    exit_button = tk.Button(  
        functions_frame,  
        text = "EXIT",
        command = close,
        **create_button_style()
    )

    
    add_button.place(x = 30, y = 120)
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)
    
       
    guiWindow.grid_rowconfigure(1, weight=1)
    guiWindow.grid_columnconfigure(0, weight=1)


    task_listbox = tk.Listbox(
     listbox_frame,  
     width=70,  
     height=16,
     selectmode='SINGLE',  
     background="#E3CF57",  
     foreground="#000000",  
     selectbackground="#CD853F",  
     selectforeground="#FEFFF0",
     font='Goodtimes'
)
    task_listbox.grid(row=0, column=0, sticky="nsew")

  
    #listbox_frame.grid_rowconfigure(0, weight=1)
    #listbox_frame.grid_columnconfigure(0, weight=1)

    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()  
