import getpass
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def collect_user_data():
    """Collect user data from input."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    return {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "address": address
    }

def anonymize_data(data):
    """Anonymize sensitive fields (simple masking)."""
    # Mask email and phone for privacy
    data['email'] = "****" + data['email'][-4:]
    data['phone'] = "****" + data['phone'][-4:]
    return data

def save_data_to_file(data, password_hash, filename="userdata.txt"):
    """Save anonymized data and password hash to a file."""
    with open(filename, "w") as f:
        f.write("# User Data (Anonymized)\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write(f"\n# Password Hash\npassword_hash: {password_hash}\n")

def main():
    print("Welcome! Please enter your details.")
    user_data = collect_user_data()
    user_data = anonymize_data(user_data)
    # Prompt user to create a password for file protection
    password = getpass.getpass("Create a password to protect your data file: ")
    password_hash = hash_password(password)
    save_data_to_file(user_data, password_hash)
    print("Your data has been saved and protected with your password.")

if __name__ == "__main__":
    main()