contacts = []   # list to hold contacts

# Add contact
def add_contact(name, phone, email, address):
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✔ Contact added!")

# Show all contacts
def show_contacts():
    if not contacts:
        print("Empty. No contacts.")
        return
    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

# Search contact
def search_contact(keyword):
    results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
    if results:
        print("\n--- Found ---")
        for i, c in enumerate(results, start=1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    else:
        print("❌ Nothing found.")

# Update contact
def update_contact(index, name, phone, email, address):
    if 0 <= index < len(contacts):
        contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        print("✔ Contact updated!")
    else:
        print("❌ Invalid index.")

# Delete contact
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        print("🗑 Deleted!")
    else:
        print("❌ Invalid index.")

# Menu
def menu():
    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add")
        print("2. Show All")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Pick (1-6): ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Addr: ")
            add_contact(name, phone, email, address)

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            keyword = input("Search name/phone: ")
            search_contact(keyword)

        elif choice == "4":
            show_contacts()
            try:
                idx = int(input("Index to update: ")) - 1
                name = input("New Name: ")
                phone = input("New Phone: ")
                email = input("New Email: ")
                address = input("New Addr: ")
                update_contact(idx, name, phone, email, address)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "5":
            show_contacts()
            try:
                idx = int(input("Index to delete: ")) - 1
                delete_contact(idx)
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "6":
            print("👋 Bye!")
            break

        else:
            print("❌ Wrong input.")

# Run
if __name__ == "__main__":
    menu()
