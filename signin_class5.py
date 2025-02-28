from prettytable import PrettyTable

users = []
class Auth:

    def __init__(self):
        pass

    def signup(self):
        """Function to handle user signup."""
        while True:
            email = input("Enter your email to sign up: ").strip()
            if email in [user["e"] for user in users]:
                print("This email is already registered. Try signing in.")
                continue
            password = input("Create a password: ")
            confirm_password = input("Confirm your password: ")

            if password != confirm_password:
                print("Passwords do not match. Try again.")
                continue

            if email.endswith("@gmail.com"):
                user = {"e": email, "p": password}
                users.append(user)
                print("Signup successful! You can now sign in.")
                break
            else:
                print("Enter a valid Gmail address.")

    def signin(self):
        """Function to handle user sign-in."""
        while True:
            email = input("Enter your email to sign in: ").strip()
            password = input("Enter your password: ")

            for user in users:
                if user["e"] == email and user["p"] == password:
                    print("Sign in successful! Welcome.")
                    return

            print("Incorrect email or password. Please try again.")

class details:
    def display_users(self):
        """Display users in a table format using PrettyTable."""
        table = PrettyTable()
        table.field_names = ["Email", "Password"]  
        for user in users:
            table.add_row([user["e"], user["p"]])
        print(table)

class Main:
        def main():
            auth = Auth()
        while True:
            print("\n1. Sign up")
            print("2. Sign in")
            print("3. Display Users")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                Auth.signup()
            elif choice == "2":
                Auth.signin()
            elif choice == "3":
                Auth.display_users()
            elif choice == "4":
                print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main.main()
        