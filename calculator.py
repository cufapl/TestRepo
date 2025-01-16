def calculator():
    print("Welcome to the Basic Calculator!")
    print("Options:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            choice = int(input("\nChoose an operation (1-5): "))
            
            if choice == 5:
                print("Goodbye! 👋")
                break
            
            if choice in [1, 2, 3, 4]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == 1:
                    result = num1 + num2
                elif choice == 2:
                    result = num1 - num2
                elif choice == 3:
                    result = num1 * num2
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    result = num1 / num2
                
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please select a valid option (1-5).")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

calculator()
