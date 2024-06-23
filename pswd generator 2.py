import random                             
import tkinter as tk                       
from tkinter import *                    
from tkinter import messagebox as mb     
  
  
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
  
    # defining the list of characters that will be used to generate the password  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
  
    # using the random.sample() method to return a list of randomly get_length characters from the list of characters.  
    selected_char = random.sample(list_of_chars, len)  
  
    # converting the list into the string  
    pass_str = "".join(selected_char)  
      
    # displaying the generated password string in the label  
    pass_label.config(text = pass_str)  
  
    # printing the password string in command line  
    print("Generated Password is :", pass_str, "\n")  
  
# defining a function to check if the user has selected any option  
def selection():  
    '''''This function will check if the user has selected 
    any option and call the generate_password() function 
    by passing the appropriate length'''  
  
    # retrieving the length of the password  
    len = length.get()  
    # if the length is not 0 calling the generate_password(len) function  
    if len != 0:  
        generate_password(len)  
    # else displaying the error message using the messagebox's showerror() method  
    else:  
        mb.showerror("Invalid Selection", "Length of Password is not defined.")  
  
# defining a function to retrieve the length of the password  
def get_length():  
    '''''This function will retrieve the length of the password 
    from the selected option and print it in Command Line'''  
  
    # printing the selected length of the password for the user   
    print("Selected Length of Password :", length.get(), "characters")  
  
# defining a function to reset everything  
def reset():  
    "This function will reset everything in the application"  
  
    # setting the initial value of the password's length  
    length.set(0)  
    # setting the initial value of the label  
    pass_label.config(text = "")  
  
# main function  
if __name__ == "__main__":  
    # creating a window using the Tk() class  
    gui_root = Tk()  
    # setting the title of the window  
    gui_root.title("Random Password Generator")  
    # configuring the size and position of the window  
    gui_root.geometry("500x450+400+200")  
    # setting the background color of the window  
    gui_root.config(bg = "#03345D")  
     
  
    # creating some frames  
    heading_frame = Frame(gui_root, bg = "#EAAD91")  
    radiobtn_frame = Frame(gui_root, bg = "#F3A4E3")  
    button_frame = Frame(gui_root, bg = "#E6E6FA")  
    result_frame = Frame(gui_root, bg = "#E6E6FA")  
  
    # using the pack() method for the placement of the frames  
    heading_frame.pack(fill = "both")  
    radiobtn_frame.pack(pady = 10)  
    button_frame.pack(pady = 10)  
    result_frame.pack(pady = 10)  
  
    
    # adding the label to display the heading      
    heading = Label(  
        heading_frame,  
        text = "RANDOM PASSWORD GENERATOR",  
        font = ("Stencil", "20"),  
        bg = "#EAAD91",  
        fg = "#E9EC19"  
        )  
  
    # adding the label to display sub-heading  
    subheading = Label(  
        heading_frame,  
        text = "Customize the Length of the Password:",  
        font = ("Bahnschrift SemiBold", "16"),  
        bg = "#4B0082",  
        fg = "#FFFFFF"  
        )  
      
    # using the pack() method to set the position of the above labels  
    heading.pack(pady = 10)  
    subheading.pack(fill = "both")  
   
    length = IntVar()  
    # setting an initial value of the IntVar object  
    length.set(0)  
  
     
    # 4 Characters Length  
    radiobuttonOne = Radiobutton(  
        radiobtn_frame,  
        text = '4 Characters',  
        variable = length,  
        value = 4,  
        font = ("Trajan", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
    # 6 Characters Length  
    radiobuttonTwo = Radiobutton(  
        radiobtn_frame,  
        text = '6 Characters',  
        variable = length,  
        value = 6,  
        font = ("Trajan ", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
    # 8 Characters Length  
    radiobuttonThree = Radiobutton(  
        radiobtn_frame,  
        text = '8 Characters',  
        variable = length,  
        value = 8,  
        font = ("Trajan", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
    # 10 Characters Length  
    radiobuttonFour = Radiobutton(  
        radiobtn_frame,  
        text = '10 Characters',  
        variable = length,  
        value = 10,  
        font = ("Trajan", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
    # 12 Characters Length  
    radiobuttonFive = Radiobutton(  
        radiobtn_frame,  
        text = '12 Characters',  
        variable = length,  
        value = 12,  
        font = ("Trajan", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
    # 16 Characters Length  
    radiobuttonSix = Radiobutton(  
        radiobtn_frame,  
        text = '16 Characters',  
        variable = length,  
        value = 16,  
        font = ("Trajan", "14"),  
        bg = "#F3A4E3",  
        command = get_length  
        )  
  
    # using the grid() method to set the position of the above radio buttons in grid format  
    radiobuttonOne.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonTwo.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonThree.grid(row = 1, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonFour.grid(row = 1, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonFive.grid(row = 2, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonSix.grid(row = 2, column = 1, padx = 10, pady = 2, sticky = W)  
  
    
    get_pass = Button(  
        button_frame,  
        text = "Get Password",  
        font = ("Bahnschrift SemiBold", "12"),  
        width = 14,  
        bg = "#32CD32",  
        fg = "#FFFFFF",  
        activebackground = "#006400",  
        activeforeground = "#FFFFFF",  
        relief = GROOVE,  
        command = selection  
        )  
    # button to clear everything  
    clear_all = Button(  
        button_frame,  
        text = "Reset",  
        font = ("Bahnschrift SemiBold", "12"),  
        width = 14,  
        bg = "#FF0000",  
        fg = "#FFFFFF",  
        activebackground = "#8B0000",  
        activeforeground = "#FFFFFF",  
        relief = GROOVE,  
        command = reset  
        )  
      
    get_pass.grid(row = 0, column = 0, padx = 5, pady = 2)  
    clear_all.grid(row = 0, column = 1, padx = 5, pady = 2)  
  
   
    pass_label = Label(  
        result_frame,  
        text = "",  
        font = ("Arial Black", "20", "bold"),  
        bg = "#E6E6FA",  
        fg = "#000000"  
        )  
  
 
    pass_label.pack()    
    gui_root.mainloop()  
