import random

class ATM :
    def __init__(self, atmnumber, pin, Balance ):

        self.atmnumber = atmnumber
        self.pin = pin
        self.Balance = Balance

    def Withdrawal(self):

        amount = int(input(" How Much Money Would You Like To WithDraw ? : ")) 

        # def initiate():
        #     if initiateWithdrawal:
        #         self.Balance-amount
        #     elif initiateWithdrawal == False:   
        #         print('Insufficient Balance')
            # print("Balance Left:" + self.Balance)           

        if self.Balance > amount :
            initiateWithdrawal = True
            self.Balance - amount

        elif self.Balance < amount :
            initiateWithdrawal = False    
            print('Insufficient Balance')
        print('Balance:')
        print(self.Balance)    

        # def initiate(self):
        #     if initiateWithdrawal:
        #         self.Balance-amount
        #     elif initiateWithdrawal == False:   
        #         print('Insufficient Balance')
        #     print("Balance Left:" + self.Balance)    

    def CheckBalance(self):

        print(self.Balance)

atmnumber = input(" Give Your ATM Number: ")
pin = input(" Give Your ATM Pin: ")
Balance = 100000000
users = ['Kalrav','Mam','Mom']
# currentUser

if(atmnumber == 'Kalrav' and pin == 'Bhatt'):
    currentUser = users[0]

elif(atmnumber == 'Mam' and pin == 'Mam'):
    currentUser = users[1]    

elif(atmnumber == 'Mom' and pin == 'Mom'):
    currentUser = users[2]    

print(currentUser)
whatdo = input(" How Can I Help You ?(Money WithDrawal/Check Balance): ")
person = ATM(atmnumber,pin,Balance)    
if whatdo == 'Money WithDrawal':
    person.Withdrawal() 
elif whatdo == 'Check Balance':
    person.CheckBalance() 
# person.Withdrawal();          
# print(Balance)      




        
        