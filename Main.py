from SpaManager import SpaManager
from Customer import Customer
from Package import Package
from Employees import Employee

user_input = input

spaManager = SpaManager()
print("\n")
print("   *****The Ultimate SPA Center***** ")
print("Select the Option from Menu")


def menu():
    print("1. Add Customer")
    print("2. Add Package")
    print("3. Show all packages")
    print("4. Show all customers")
    print("5. Find customer by name")
    print("6. Add Subscription")
    print("7. Add Payment")
    print("8. Add Employee")
    print("9. show Employee")
    print("\nEnter You Choice: ")

menu()

while(True):
    user_input = int(input())
    if user_input == 1:
        name = str(input("Enter customer's name - "))
        phoneNo = str(input("Enter customer's phone no. - "))
        joinDate = str(input("Enter joining date - "))
        customer = Customer(name, phoneNo, joinDate)
        spaManager.addCustomer(customer)

    elif user_input == 2:
        type = str(input("Enter package type - "))
        facilities = str(input("Enter facilities - "))
        cost = int(input("Enter package cost - "))
        package = Package(type, facilities, cost)
        spaManager.addPackage(package)

    elif user_input == 3:
        print("PackageID\tType\tFacilities\tCost")
        for pkgId in spaManager.packages.keys():
            package = spaManager.packages[pkgId]
            packageId = pkgId
            type = package.getType()
            facilities = package.getFacilities()
            cost = package.getCost()
            print(str(packageId) + "\t" + type + "\t" + facilities + "\t" + str(cost))

    elif user_input == 4:
        print("CustomerID\tName\tPhone\tJoining Date")
        for cusId in spaManager.customers.keys():
            customer = spaManager.customers[cusId]
            customerId = cusId
            name = customer.getName()
            phoneNo = customer.getPhoneNo()
            joinDate = customer.getJoiningDate()
            print(str(customerId) + "\t" + name + "\t" + phoneNo + "\t" + joinDate)

    elif user_input == 5:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in spaManager.customers.keys():
            customer = spaManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found").format(name)
        else:
            packageDict = spaManager.subscriptions.get(customerId)
            print ("Customer found", spaManager.customers[customerId])
            if packageDict != {}:
                print ("Subscribed to"),
                for pkgId in packageDict.keys():
                    print (spaManager.packages[pkgId], "for {0} months".format(spaManager.subscriptions[customerId][packageId]))
            else:
                print ("No subscription found for this customer")

    elif user_input == 6:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in spaManager.customers.keys():
            customer = spaManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found.").format(name)
            print ("Try adding a new customer.")
        else:
            print ("Customer found", spaManager.customers[customerId])
            if spaManager.packages.keys():
                for pkgId in spaManager.packages.keys():
                    print (pkgId, spaManager.packages[pkgId])
                packageId = int(input("Select a package: "))
                if packageId > max(spaManager.packages.keys()):
                    print ("Please select a valid package.")
                else:
                    months = int(input("Enter no. of months"))
                    spaManager.addSubscription(spaManager.customers[customerId], spaManager.packages[packageId], months)
                    print ("Subscription added.")
            else:
                print("No package exists. Try adding a package first.")

    elif user_input == 7:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in spaManager.customers.keys():
            customer = spaManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found.").format(name)
            print ("Try adding a new customer.")
        else:
            print ("Customer found", spaManager.customers[customerId])
            if spaManager.packages.keys():
                for pkgId in spaManager.packages.keys():
                    print (pkgId, spaManager.packages[pkgId])
                packageId = int(input("Select a package"))
                if packageId > max(spaManager.packages.keys()):
                    print ("Please select a valid package.")
                else:
                    if spaManager.subscriptions[customerId][packageId] > 0:
                        customer = spaManager.customers[customerId]
                        package = spaManager.packages[packageId]
                        spaManager.addPayment(customer, package, package.getCost())
                        print ("Payment added. Subscription expires in {0} months.").format(spaManager.subscriptions[customerId][packageId])
    elif user_input == 8:
        name = str(input('Enter employee name: \n'))
        phoneNo = str(input('Enter phone number: \n'))
        specialization = str(input('Specialization: \n'))
        employee = Employee(name, phoneNo, specialization)
        spaManager.addEmployee(employee)

    elif user_input == 9:
        print("EmployeeID\tName\tPhone\tspecialization")
        for emplID in spaManager.employee.keys():
            employee = spaManager.employee[emplID]
            employeeId = emplID
            name = employee.getname()
            phoneNo = employee.getPhoneNo()
            specialization = employee.getSpecialization()
            print(str(employeeId) + "\t" + name + "\t" + phoneNo + "\t" + specialization)

        spaManager()

    else:
        print("Please enter a valid number")
    menu()
