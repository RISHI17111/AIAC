import getpass
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def anonymize_email(email):
    """Anonymize email by masking part of it."""
    parts = email.split('@')
    if len(parts) == 2:
        return parts[0][:2] + "***@" + parts[1]
    return "***@***"

def anonymize_phone(phone):
    """Anonymize phone number by masking all but last 2 digits."""
    return "*" * (len(phone)-2) + phone[-2:]

def collect_user_data():
    """Collect user data from input and anonymize sensitive fields."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Anonymize sensitive fields
    email_anon = anonymize_email(email)
    phone_anon = anonymize_phone(phone)

    return {
        "Name": name,
        "Age": age,
        "Email": email_anon,
        "Phone": phone_anon,
        "Address": address
    }

def save_data_to_file(data, password_hash, filename="userdata.txt"):
    """Save anonymized user data and password hash to a file."""
    with open(filename, "w") as f:
        f.write("# User data (anonymized)\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("# Password hash for protection\n")
        f.write(f"PasswordHash: {password_hash}\n")

def main():
    print("Welcome! Please create a password to protect your data file.")
    password = getpass.getpass("Create a password: ")
    password_hash = hash_password(password)

    print("\nNow, enter your details.")
    user_data = collect_user_data()

    save_data_to_file(user_data, password_hash)
    print("Your anonymized data has been saved and protected with your password.")

if __name__ == "__main__":
    main()