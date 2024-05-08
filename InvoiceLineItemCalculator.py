#Cesar Murillo
#CIS 261
#Week 6 Invoice Calculator



def get_price():
    while True:
        try:
            return float(input("Please Enter Price: "))
        except ValueError:
            print("Invalid Format. Please Enter A Valid Number.")
            
def get_quantity():
    while True:
        try:
            return int(input("Please Enter Quantity: "))
        except ValueError:
            print("Invalid Format. Please Enter A valid Quantity.")
            
def main():
    print("Welcome To The Invoice Line Item Calculator\n")
    
    while True:
        price = get_price()
        quantity = get_quantity()
    
        total = price * quantity

        print(f"\nPrice: {price:.2f}",
              f"\nQuantity: {quantity}",
              f"\nTotal: ${total:.2f}\n")
    
        answer = input("Do You Want To Enter Another Item? (Y/N): ").lower()
        if answer != 'y':
            break
    
if __name__ == "__main__":
    main()