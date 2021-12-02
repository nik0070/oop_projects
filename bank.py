class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedIn = False
        self.cash = 100
    
    def register(self, name, ph, password):
        conditions = True

        if len(str(ph)) < 10 or len(str(ph)) > 10:
            print('wrong phone no.')
            conditions = False

        if len(str(password)) < 5 or len(str(password)) > 10:
            print('invalid password')
            conditions = False
 
        if conditions = True:
            print('Account created successfully')
            cash = self.cash
            self.client_details_list = [name, ph, password, cash]
            with open(f'{name}.txt', 'w') as f:
                for details in self.client_details_list:
                    f.write(str(details)+'\n')

    def login(self, name, ph, password):
        with open(f'{name}.txt', 'r') as f:
            details = f.read()
            self.client_details_list = details.split('\n')
            if str(ph) in self.client_details_list:
                if str(password) in self.client_details_list:
                    self.loggedIn = True

            if self.loggedIn == True:
                print(f'{name} is logged in.')
                self.cash = self.client_details_list[3]
                self.name = name
            else:
                print('invalid details!')

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split('\n')

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(client_details_list[3]), str(self.cash)))
            print("Amount added")
        else:
            print("Enter a valid amount")

        
            
                
            



