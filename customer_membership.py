class Membership:

    # Inisialisasi Data
    data = {
        'Sumbul': 'Platinum',
        'Ana': 'Gold',
        'Cahya': 'Platinum'
    }

    # Init Atribut
    def __init__(self,username: str) -> None:
        self.username = username

    def show_benefit(self) -> None:

        """
        Methode yang digunakan  untuk menampilkan benefit membership 
        """

        # Init header name
        headers = ['Membership', 'Discount', 'Benefits']

        # Init data (tables)
        tables = [
            ['Platinum', '15%', 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%'],
            ['Gold', '10%', 'Benefit Silver + Voucher Ojol'],
            ['Silver', '8%', 'Voucher Makan']
        ]
        print('Benefit Membership')
        print('')
        print(tabulate(tables, headers, tablefmt='github'))


    def show_req(self) -> None:

        """
        Methode yang digunakan  untuk menampilkan requirements membership 
        """
         # Init header name
        headers = ['Membership', 'Monthly Expense (Juta)', 'Monthly Income (Juta)']

        # Init data (tables)
        tables = [
            ['Platinum', 8, 15],
            ['Gold', 6, 10],
            ['Silver', 5, 7]
        ]
        print('Requirements Membership')
        print('')
        print(tabulate(tables, headers, tablefmt='github'))

    def predict_membership(self, username: str, 
                            monthly_expense: float, 
                            monthly_income: float) -> None:
        # init parameter data for each membership
        parameter_data = [[8,15], [6,10], [5,7]]
            
        result_tmp = []
            
        for idx, _ in enumerate(parameter_data):
            # Implementasi euclidean distance 
            euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                        (monthly_income - parameter_data[idx][1])**2), 2)

            result_tmp.append(euclidean_dist)
            
        # store euclidean distance value to dictionary
        dict_result = {
            'Platinum': result_tmp[0],
            'Gold': result_tmp[1],
            'Silver': result_tmp[2]
        }

        print(f'Hasil perhitungan Euclidean Distance dari User {username} adalah {dict_result}')

        # get minimum value form result list
        get_min_dist = min(result_tmp)

        # iterate to dictionary data
        for key, value in dict_result.items():
            
            #compare with minimum data
            if value == get_min_dist:
                print(key)

                # insert predicted data to dict data
                self.data[username] = key 

    def calculate_price(self, username: str, list_harga: list) -> float:

        if username in self.data:

            # get membership
            membership = self.data.get(username)

            # create branching for each membership to get discount
            if membership == 'Platinum':
                total_price = sum(list_harga) - (sum(list_harga) * 0.15)
                
                return total_price
            
            elif membership == 'Gold':
                total_price = sum(list_harga) - (sum(list_harga) * 0.1)

                return total_price

            elif membership == 'Silver':
                total_price = sum(list_harga) - (sum(list_harga) * 0.08)
                
                return total_price

            else:
                raise Exception("Membership belum terimplementasi")
        else:
            raise Excepion("Membership tidak ada di Database")

# init object
user_1 = Membership(username = 'Febryan')

# check username
print(user_1.username)

# predict membership

user_1.predict_membership(username = 'Febryan',
                         monthly_expense = 3,
                         monthly_income = 30)

print(user_1.data)