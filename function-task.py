# Take input from the user IP address, hostname, username, and password
# Diplay the output as "Hi $hostname, your IP address is $ip address and password is $password and it should keep looping until the user decides to exit"

# Output
#Hi $host_name 
# your IP address is $ip_address
# username is $username
# password is $password

while True:
    # Take user inputs
    ip_address = input("Enter your IP address: ")
    hostname = input("Enter your hostname: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Display the output
    print(f"Hi Hostname {hostname}")
    print(f"Your IP address is {ip_address}")
    print(f"Your Username is {username}")
    print(f"your password is {password}")
    
    # Ask user whether to continue or exit
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != 'yes':
        print(" Exiting the program...")
        break
    
    

