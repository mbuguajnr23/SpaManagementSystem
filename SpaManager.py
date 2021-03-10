import SpaManager

class SpaManager:

    def __init__(self):
        self.customers = dict()
        self.packages = dict()
        self.subscriptions = dict()
        self.payments = dict()
        self.employee = dict()


    def addEmployee(self, employee):
        self.employee[employee.getemployeeID()] = employee
        #self.packages[employee.getSpecialization()] = specialization


    def addCustomer(self, customer):
        self.customers[customer.getCustomerId()] = customer
        self.subscriptions[customer.getCustomerId()] = dict()
        self.payments[customer.getCustomerId()] = dict()

    def addPackage(self, package):
        self.packages[package.getPackageId()] = package

    def addSubscription(self, customer, package, months):
        packageId = package.getPackageId()
        customerId = customer.getCustomerId()
        self.subscriptions[customerId][packageId] = months

    def addPayment(self, customer, package, amount):
        packageId = package.getPackageId()
        customerId = customer.getCustomerId()
        self.payments[customerId][packageId] += amount
        self.subscriptions[customerId][packageId] -= 1

    def save(self):
        SpaManager.dump(self, open("spa_manager.bin", "wb"))
