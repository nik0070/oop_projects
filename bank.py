class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
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
                    self.loggedin = True

            if self.loggedin == True:
                print(f'{name} is logged in.')

                
            



