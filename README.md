# 25BAS10052_RudraMishra_VITBHOPAL_VITYATHIPROJECT-2025-26

#  VmazON E-commerce Application

This is a basic, console-based E-commerce simulation project written in Python. It allows users to register, log in, view available products, add items into a cart, place orders, and check their order status. It also provides a basic distributor view for inventory and customer orders.


##  Features

Services to the Customers
* **Authentication:** Users can **Register** anew account or **Login** using stored credentials that are saved in `User_Data.csv`.
* **Browse & Shop:** Customer can browse the product by categorized major groups; for example, Electronics, ClothingsM, Accessories.
* **Cart & Order:** Items can either be added to a temporary cart or ordered directly.
* Order Management:
* **Cancel Order:** The option to cancel the last order placed.
* **My Orders:** See the list of ordered items.

* **Payment** - This supports simulated **Cash On Delivery COD** and **UPI** payment methods.
Distributor Services

* **Check Orders:** List all successful customer orders - read from `orders.csv`.

* **Inventory Check:** Display the full product catalog and prices.

---
## How to Run the Project

1. Introduction

* **Python:** You will need to have Python installed (version 3.x is fine).
* **CSV Files:** The system depends on the existence of external CSV files for data persistence. These will be created automatically upon the first successful action in case of registration, adding to cart, or placing an order.
2. File Structure

| `Project.py` | Main Python code containing all the logic. |
| `User_Data.csv` | Stores customer login credentials (`email`, `password`). |
| `kart.csv` | Stores items that were added to the cart. |
| `orders.csv` | Stores all successful order details (`email`, `product`, `payment_mode`, `[upi_id]`). |
Execution
1. Save the following Python code into a file such as `vmazon.py`:
2. Open a terminal or command prompt.

3. Change into the directory where you've saved your file.

4. To run the application, use the following:

Sample Workflow
1. **Hello**: You will see the welcome message.
2. **User Type:** Please enter either `customer` or `distributor`.
3. **Authentication**: Enter `register` or `login`.
* *(If you enter `customer` and successfully `login`)*
4.  **Service Type:** Enter `browse`, `orders`, or `cancel`.
5. **Browsing:**
* Enter Service type: `browse`
Category type: `electronics`
* Enter the product from the list below: `phones`

* App displays list of available phones and their prices.

6. **Action:**

* Enter code of desired product: `1`
* kart/Order: `Order`
* Do you wanna order '.': `yes`
* Enter mode of payment: `COD`
