class Contact:
   def __init__(self, name, phone_number, email, address):
      self.name=name
      self.phone_number=phone_number
      self.email=email
      self.address=address
   def _str_(self):
        return f"Name:{self.name},Phone:{self.phone_number},Email:{self.email},Address:{self.address}"
class ContactBook:
    def __init__(self):
      self.contacts=[]
    def add_contact(self,name,phone_number,email,address):
        """Add a new contact"""
        contact=Contact(name,phone_number,email,address)
        self.contacts.append(contact)
        print(f"Added{name} to contacts")
    def search_contact(self, search_query):
        """Search for a contact by name or phone number"""
        found=False
        for contact in self.contacts:
            if search_query.lower()in contact.name.lower() or search_query in contact.phone_number:
                print(contact)
                found=True
        if not found:
            print(f"No contacts found with '{search_query}")
    def update_contact(self,name,phone_number,email,address):
        """Update contact details"""
        updated=False
        for contact in self.contacts:
            if contact.name==name:
                contact.phone_number=phone_number
                contact.email=email
                contact.address=address
                print(f"Updated details for {name}")
                updated=True
            if not updated:
                print(f"{name}not found in contacts")
    def delete_contact(self,name):
        """Delete a contact by name"""
        deleted=False
        for index,contact in enumerate(self.contacts):
            if contact.name==name:
                del self.contacts[index]
                print(f"{name}deleted from contacts")
                deleted=True
                break
            if not deleted:
                print(f"{name}not found in contacts")
    def display_contacts(self):
        """Display all contacts"""
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found")
def main():
       contact_book=ContactBook()
       while True:
           print("\nWelcome to the Contact Book!")
           print("1. Add a contact")
           print("2. Search for a contact")
           print("3. Update contact details")
           print("4. Delete a contact")
           print("5. Display all contacts")
           print("6. Exit")
           choice=input("Enter your choice(1-6):").strip()
           if choice=='1':
               name=input("Enter name:").strip()
               phone_number=input("Enter phone number:").strip()
               email=input("Enter email:").strip()
               address=input("Enter address:").strip()
               contact_book.add_contact(name,phone_number,email,address)
           elif choice=='2':
               search_query=input("Enter name or phone number to search:").strip()
               contact_book.search_contact(search_query)
           elif choice=='3':
               name=input("Enter name of contact to update:").strip()
               phone_number=input("Enter new phone number:").strip()
               email=input("Enter new email:").strip()
               address=input("Enter new address:").strip()
               contact_book.update_contact(name,phone_number,email,address)
           elif choice=='4':
               name=input("Enter name of contact to delete:").strip()
               contact_book.delete_contact(name)
           elif choice=='5':
               contact_book.display_contacts()
           elif choice=='6':
               print("Exiting the Contact Book.bye!")
               break
           else:
                print("Invalid choice.Please enter a number from 1 to 6")
if __name__=="__main__" :
    main()
                
                  
                  
                


