#Python project - E commerce
print("WELCOME TO EC-COM CONSOLE!")
import csv
#Services provided:
#1) FOR CUSTOMER - a)BROWSE - ORDER/ADD TO KART b)CANCEL ORDER c)MY ORDERS
#2)FOR DISTRIBUTOR: 1)CHECK ORDERS FROM CUSTOMER 2)CHECK PRODUCT INVENTORY

ud=input("Enter user type:")
#LOGIN AND REGISTER 
FILENAME = 'User_Data.csv'
action = input("Enter 'register' or 'login': ").lower()
if action == 'register':
    email = input("Enter email: ")
    password = input("Enter password: ")
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password])
        print("Registration successful")
elif action == 'login':
    email = input("Enter email: ")
    password = input("Enter password: ")
    login_successful = False
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[0] == email and i[1] == password:
                    login_successful = True
                    break
    except:
        pass
    if login_successful:
        print("Login successful")
    else:
        print("Invalid credentials")
else:
    print("Invalid action")
def customer():
    global products
    kart=[]
    to_order=[]
    service = input("Enter Service type:")
    #CATEGORIES : PRODUCTS
    cat_d = {'electronics' : ['phones','laptops','power banks','charger','tablets','headphones'],
    'clothingm' : ['winter','summer','hoodies','turtlenecks'],
    'clothingf' : ['winter','summer','hoodies','turtlenecks','skirts','tops'],
    'accessories' : ['watches','bracelets','earrings','keychains'],
    'decor': ['mirror','table lamps'],
    'toys' : ['cars','trains',],
    'cosmetics' : ['serum','powder'],
    'appliances' : ['fridge','tv','washing machine']}
    #LIST AND NAMES OF PRODUCTS [NESTED DICTIONARY]
    products={'phones': {
      "1_Smartphone_X": 53185,
      "2_Budget_Phone_Y": 13247,
      "3_Gaming_Phone_Z": 88200,
      "4_Refurbished_Phone": 31003},
    'laptops': {
      "1_Ultrabook_Pro": 115161,
      "2_Student_Model_Air": 57590,
      "3_Gaming_Rig_GTX": 168249,
      "4_Chromebook_Basic": 26488},
    'power_banks': {
      "1_10000mAh_Slim": 2215,
      "2_20000mAh_Fast": 3987,
      "3_Solar_Power_Bank": 4916,
      "4_Mini_Keyring_Bank": 1416},
    'charger': {
      "1_20W_USB-C_Adapter": 1769,
      "2_Dual_Port_Travel": 2652,
      "3_Wireless_Charging_Pad": 3455,
      "4_Car_Charger_Quick": 1285},
    'tablets': {
      "1_Tablet_Pro_A": 61922,
      "2_Kids_Tablet_Safe": 10634,
      "3_Mini_Tablet_E": 22064,
      "4_Drawing_Tablet_Pen": 39870},
    'headphones': {
      "1_Noise_Cancelling_Elite": 17693,
      "2_Wireless_Earbuds_Sport": 5310,
      "3_Studio_Monitor_Headset": 10632,
      "4_Wired_Budget_Set": 1769},
    'winter': {
      "1_Puffer_Jacket": 7965,
      "2_Wool_Trench_Coat": 13290,
      "3_Thermal_Base_Layer": 3144,
      "4_Fleece_Lined_Pants": 5759},
    'summer': {
      "1_Linen_Shirt": 3987,
      "2_Swim_Trunks": 2657,
      "3_Graphic_Tee": 1772,
      "4_Cargo_Shorts": 3410},
    'hoodies': {
      "1_Cropped_Fleece_Hoodie": 3987,
      "2_Oversized_Pullover": 4607,
      "3_Lightweight_Zip_Up": 3449,
      "4_Embroidered_Hoodie": 5316},
    'turtlenecks': {
      "1_Body_Fit_Jersey_Turtleneck": 2215,
      "2_Cable_Knit_Turtleneck": 5759,
      "3_Silk_Blend_Turtleneck": 7531,
      "4_Long_Sleeve_Ribbed_Turtleneck": 3101},
    'skirts': {
      "1_Pleated_Midi_Skirt": 3987,
      "2_Mini_A_Line_Skirt": 2658,
      "3_Pencil_Skirt_Work": 4873,
      "4_Wrap_Maxi_Skirt": 4347},
    'tops': {
      "1_V_Neck_Knit_Top": 2658,
      "2_Spaghetti_Strap_Cami": 1595,
      "3_Off_Shoulder_Top": 3101,
      "4_Button_Down_Blouse": 3719},
    'watches': {
      "1_Smartwatch_Series_5": 22150,
      "2_Classic_Leather_Strap": 7531,
      "3_Dive_Watch_Automatic": 39870,
      "4_Digital_Sport_Watch": 3101},
    'bracelets': {
      "1_Silver_Bangle_Cuff": 6645,
      "2_Beaded_Stretch_Bracelet": 1329,
      "3_Charm_Bracelet_Starter": 4430,
      "4_Leather_Wrap_Bracelet": 2658},
    'earrings': {
      "1_Diamond_Studs_05ct": 10632,
      "2_Hoops_Gold_Plated": 2215,
      "3_Dangling_Statement_Pair": 3544,
      "4_Pearl_Drops_Simple": 5316},
    'keychains': {
      "1_Metal_Bottle_Opener_Keyring": 1063,
      "2_Personalized_Leather_Fob": 1949,
      "3_Plush_Animal_Keychain": 709,
      "4_Multitool_Carabiner_Keyfob": 1595},
    'mirror': {
      "1_Full_Length_Wall_Mirror": 8771,
      "2_Round_Vanity_Mirror": 3987,
      "3_Decorative_Sunburst_Mirror": 6645,
      "4_LED_Bathroom_Mirror": 13290},
    'table_lamps': {
      "1_Mid_Century_Desk_Lamp": 5759,
      "2_Crystal_Bedside_Lamp": 7531,
      "3_Industrial_Table_Lamp": 3544,
      "4_Adjustable_Reading_Lamp": 4873},
    'cars': {
      "1_Remote_Control_Buggy": 4428,
      "2_Set_of_10_Diecast_Cars": 1767,
      "3_Build_Your_Own_Car_Kit": 3101,
      "4_Large_Toy_Truck_Dumper": 2215},
    'trains': {
      "1_Electric_Train_Set_Deluxe": 7088,
      "2_Wooden_Train_Track_Expansion": 2658,
      "3_Collectible_Locomotive": 3987,
      "4_Battery_Operated_Metro_Set": 3101},
    'serum': {
      "1_Vitamin_C_Serum_30ml": 2650,
      "2_Hyaluronic_Acid_Serum": 3101,
      "3_Retinol_Anti_Aging_Serum": 3987,
      "4_Niacinamide_Blemish_Serum": 1993},
    'powder': {
      "1_Translucent_Setting_Powder": 1769,
      "2_Pressed_Compact_Powder": 1550,
      "3_Mineral_Loose_Powder": 2215,
      "4_Banana_Baking_Powder": 1321},
    'fridge': {
      "1_Double_Door_Frost_Free": 66450,
      "2_Single_Door_Compact": 30999,
      "3_Side_By_Side_Inverter": 132900,
      "4_Mini_Bar_Fridge_Office": 17720},
    'tv': {
      "1_55_Inch_Smart_4K_LED": 44174,
      "2_32_Inch_HD_Smart_TV": 22150,
      "3_75_Inch_OLED_Premium": 221500,
      "4_Portable_Projector_TV": 15948},
    'washing_machine': {
      "1_Fully_Automatic_Top_Load": 39870,
      "2_Semi_Automatic_Twin_Tub": 17720,
      "3_Front_Load_Inverter_8kg": 57590,
      "4_Portable_Mini_Washer": 10632}}
    try:
        #BROWSING ITEMS AS PER CATOGORIES AND SUB CATEGORIES
        if service.lower()  ==  "browse" :
            print("Categories : Electronics/ClothingM/ClothingF/Accessories/Decor/Toys/Cosmetics/Appliances")
            cat = input("Enter category type:")
            for i in cat_d.keys():
                if cat.lower() == i:
                    print(cat_d[i])
                    subcat = input("Enter the product from the given list:")
                    if subcat in products.keys():
                        print(products[subcat])
                    break
                else:
                    continue
    except:
        #EXCEPTION HANDLING
        print("Invalid Category")
    #ORDER CANCEL PROCEDURE
    if service.lower() == 'cancel':
        s = input("Are you sure you want to cancel the order?")
        if s.lower() == 'yes':
            for i in to_order:
                to_order.pop()
                if len(to_order) == 0:
                    print("Item is deleted")
    #ORDER CHECK
    if service.lower() == 'orders':
        print('Your orders:',to_order)
    try:
        #ADDING PRODUCTS TO KART
        code = int(input("Enter code of desired product:"))
        action = input("kart/Order:")
        temp = products[subcat]
        for i in temp:
            if i[0] == f"'{code}'" and action.lower() == 'kart' :
                kart.append(i)
                with open('kart.csv', mode='w',newline = '') as file:
                            writer = csv.writer(file)
                            writer.writerow([email,i])
                break
            elif i[0] == f"'{code}'" and action.lower() == 'order':
                to_order.append(i)
                x = input(f"Do you wanna order '{to_order}'?:(YES/NO)")
                if x.lower() == 'yes':
                    #MODE OF PAYMENT = CASH ON DELIVERY / UPI
                    payment = input("Enter mode of payment: (COD/UPI)")
                    if payment.lower() == 'cod':
                        with open('orders.csv', mode='a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([email,i,payment])
                    print("Your order is succesful")
                    if payment.lower() == 'upi':
                        upi_id = int(input("Enter UPI id:"))
                        with open('orders.csv', mode='a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([email,i,payment,upi_id])

                        print("Your order is succesful")
                    else:
                        print("invalid payment method")
                break
    except:
        print("Enter valid input")
    #ORDER CANCEL PROCEDURE
    if service.lower() == 'cancel':
        s = input("Are you sure you want to cancel the order?")
        if s.lower() == 'yes':
            for i in to_order:
                to_order.pop()
                if len(to_order) == 0:
                    print("Item is deleted")
    #ORDER CHECK
    if service.lower() == 'orders':
        print('Your orders:',to_order)
    print("Thanks for shoppin with us!!!")

def distributor():
    global products
    #FOR DISTRIBUTOR: 1)CHECK ORDERS FROM CUSTOMER 2)CHECK PRODUCT INVENTORY
    x=input("Action:")
    #check orders
    if action.lower() == 'orders':
         with open('orders.csv', mode='r', newline='') as file:
             reader = csv.reader(file)
             print(reader)
    #check products
    elif action.lower() == 'inventory':
        print(products)
         
if ud.lower() == 'customer' and login_successful == True:
    customer()
elif ud.lower() =='distributor' and login_successful == True:
    distributor()
else:
    print("Invalid Action")

        
    
    



