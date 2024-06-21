# pip install tkinter
import tkinter as tk
from tkinter import messagebox, ttk

# Burger menu with prices
menu = {
    1: ("Aloo-Tikki", 5),
    2: ("Maharaja", 10),
    3: ("Mac-Special", 15)
}

# Function to start the application
def start_app():
    start_frame.pack_forget()
    main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    root.after(2000, ask_name)

# Function to ask for name
def ask_name():
    response = messagebox.askyesno("Name Confirmation", "Is your name Anshika?")
    if response:
        name_var.set("Anshika 😊")
    else:
        get_name()

# Function to get name from user
def get_name():
    def set_name():
        entered_name = name_entry.get()
        if entered_name.isalpha() and 2 <= len(entered_name) <= 32:
            name_var.set(f"{entered_name} 😊")
            name_popup.destroy()
        else:
            name_entry.delete(0, tk.END)
            name_entry.config(fg='red')

    name_popup = tk.Toplevel(root)
    name_popup.title("Enter Your Name")
    name_popup.geometry("300x200+%d+%d" % (root.winfo_x() + 150, root.winfo_y() + 150))
    name_popup.config(bg='lightblue')

    tk.Label(name_popup, text="Enter your name:", bg='lightblue').pack(pady=10)
    name_entry = tk.Entry(name_popup)
    name_entry.pack(pady=5)
    name_entry.focus()
    
    button_frame = tk.Frame(name_popup, bg='lightblue')
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Set Name", command=set_name).pack(side="left", padx=5)
    tk.Button(button_frame, text="Cancel", command=lambda: [name_popup.destroy(), ask_name()]).pack(side="left", padx=5)

# Function to calculate the bill
def calculate_bill():
    try:
        items = cart_listbox.get(0, tk.END)
        is_student = student_var.get()
        delivery = delivery_var.get()
        tip = int(tip_var.get())
        
        if not items:
            raise ValueError("No items selected")

        total_price = 0
        bill_details = f"{' Final Bill '.center(30, '#')}\nsr.  name       price  quantity  total_price\n"
        item_dict = {}
        for item in items:
            name, price = item.split(" - $")
            price = int(price.split(" - X")[0])
            quantity = int(item.split(" - X")[1]) if " - X" in item else 1
            if name in item_dict:
                item_dict[name]["quantity"] += quantity
                item_dict[name]["total"] += price * quantity
            else:
                item_dict[name] = {"price": price, "quantity": quantity, "total": price * quantity}
        
        for idx, (name, info) in enumerate(item_dict.items(), 1):
            bill_details += f"{idx}.  {name}  {info['price']}$      {info['quantity']}      {info['total']}$\n"
            total_price += info["total"]

        discount = total_price * 0.20 if is_student == 1 else 0
        extra_discount = total_price * 0.20 if name_var.get().startswith("Anshika") else 0
        delivery_charge = total_price * 0.05 if delivery == 1 else 0
        final_price = total_price - discount - extra_discount + delivery_charge + tip

        bill_message = f"""
        {bill_details}
        {" ~ ".center(50, '-')}
                               {total_price}$
        Student discount 20%      -{discount}$
        {"Special discount for Anshika 20%     -" + str(extra_discount) + "$" if extra_discount else ""}
        Delivery charge 5%        +{delivery_charge}$
        Tip                         {tip}$
        {" ~ ".center(50, '-')}
        Total bill                 {final_price}$

        {"Thank you and come again".center(50)}
        """
        messagebox.showinfo("Final Bill", bill_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to reset the application
def reset_app():
    main_canvas.pack_forget()
    start_frame.pack(fill='both', expand=True)
    name_var.set("")
    cart_listbox.delete(0, tk.END)

# Function to add items to cart
def add_to_cart():
    selected_items = menu_listbox.curselection()
    for item in selected_items:
        name, price = menu_listbox.get(item).split(" - $")
        quantity = quantity_var.get()
        found = False
        for i in range(cart_listbox.size()):
            cart_item = cart_listbox.get(i)
            if cart_item.startswith(f"{name} - ${price}"):
                existing_quantity = int(cart_item.split(" - X")[1])
                new_quantity = existing_quantity + quantity
                cart_listbox.delete(i)
                cart_listbox.insert(i, f"{name} - ${price} - X{new_quantity}")
                found = True
                break
        if not found:
            cart_listbox.insert(tk.END, f"{name} - ${price} - X{quantity}")

# Create main application window
root = tk.Tk()
root.title("Burger Billing System")
root.geometry("600x600")
root.resizable(False, False)

# Adding a canvas and a scrollbar
main_canvas = tk.Canvas(root)
# main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
main_canvas.bind_all('<MouseWheel>', lambda e: main_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
main_canvas.bind_all('<Up>', lambda e: main_canvas.yview_scroll(-1, "units"))
main_canvas.bind_all('<Down>', lambda e: main_canvas.yview_scroll(1, "units"))

# Creating a frame inside the canvas
main_frame = tk.Frame(main_canvas, bg='lightyellow', width=600)
main_canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Starting frame
start_frame = tk.Frame(root, bg='lightblue')
tk.Label(start_frame, text="Welcome to the Burger Shop!", font=("Helvetica", 16), bg='lightblue').pack(pady=20)
tk.Button(start_frame, text="Continue", command=start_app, bg='green', fg='white').pack(side="left", padx=20)
tk.Button(start_frame, text="Quit", command=root.quit, bg='red', fg='white').pack(side="right", padx=20)
start_frame.pack(fill='both', expand=True)

name_var = tk.StringVar()
tk.Label(main_frame, textvariable=name_var, font=("Helvetica", 12), bg='lightyellow').grid(row=0, column=2, pady=10, sticky='e')

tk.Label(main_frame, text="Burger Menu", font=("Helvetica", 14, "bold"), bg='lightyellow').grid(row=1, column=0, columnspan=2, pady=10)
menu_listbox = tk.Listbox(main_frame, selectmode='multiple', bg='lightgreen')
for idx, item in menu.items():
    menu_listbox.insert(tk.END, f"{item[0]} - ${item[1]}")
menu_listbox.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

tk.Label(main_frame, text="Quantity", bg='lightyellow').grid(row=3, column=0, pady=5)
quantity_var = tk.IntVar(value=1)
quantity_dropdown = ttk.Combobox(main_frame, textvariable=quantity_var, values=list(range(1, 16)), state='readonly')
quantity_dropdown.grid(row=3, column=1, pady=5, padx=10)

tk.Button(main_frame, text="Add to Cart", command=add_to_cart, bg='blue', fg='white').grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(main_frame, text="Cart", bg='lightyellow').grid(row=5, column=0, pady=10)
cart_listbox = tk.Listbox(main_frame, bg='lightblue')
cart_listbox.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

tk.Label(main_frame, text="Are you a student?", bg='lightyellow').grid(row=7, column=0, pady=5)
student_var = tk.IntVar()
tk.Radiobutton(main_frame, text="Yes", variable=student_var, value=1, bg='lightyellow').grid(row=7, column=1, pady=5)
tk.Radiobutton(main_frame, text="No", variable=student_var, value=0, bg='lightyellow').grid(row=7, column=2, pady=5)

tk.Label(main_frame, text="Do you want delivery?", bg='lightyellow').grid(row=8, column=0, pady=5)
delivery_var = tk.IntVar()
tk.Radiobutton(main_frame, text="Yes", variable=delivery_var, value=1, bg='lightyellow').grid(row=8, column=1, pady=5)
tk.Radiobutton(main_frame, text="No", variable=delivery_var, value=0, bg='lightyellow').grid(row=8, column=2, pady=5)

tk.Label(main_frame, text="Do you want to give a tip?", bg='lightyellow').grid(row=9, column=0, pady=5)
tip_var = tk.StringVar(value="0")
tk.Radiobutton(main_frame, text="2$", variable=tip_var, value="2", bg='lightyellow').grid(row=9, column=1, pady=5)
tk.Radiobutton(main_frame, text="5$", variable=tip_var, value="5", bg='lightyellow').grid(row=9, column=2, pady=5)
tk.Radiobutton(main_frame, text="10$", variable=tip_var, value="10", bg='lightyellow').grid(row=9, column=3, pady=5)

tk.Button(main_frame, text="Calculate Bill", command=calculate_bill, bg='green', fg='white').grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(main_frame, text="Reset", command=reset_app, bg='orange', fg='white').grid(row=11, column=0, padx=20)
tk.Button(main_frame, text="Quit", command=root.quit, bg='red', fg='white').grid(row=11, column=1, padx=20)

# Main loop
root.mainloop()
