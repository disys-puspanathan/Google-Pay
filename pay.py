class Google_pay:

    def __init__(self, email_id, phone_number, name):
        self.emailid = email_id
        self.mobile = phone_number
        self.name = name
    def open_gpay(self):
        print("Google Pay")
    def email_verification(self):
        if type(self.emailid) == str:
            if len(self.emailid) <= 30:
                print("email_id verified")
            else:
                raise ValueError("The emailid should not contain more than 30 values")
        else:
            raise TypeError("Invalid Email")
    def mobile_verification(self):
        if(len(self.mobile) == 10):
            if type(self.mobile) == str:
                print("Phone number verified")
            else:
                raise TypeError("The phone should contain only numbers")
        else:
            raise ValueError("The phone number should not be greater or lesser than 10")
    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <=20:
                print("Name Verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")
    def otp_verification(self, code, otp):
        if(otp == code):
            print("OTP Verified")
        else:
            raise ValueError("The otp you have entered is incorrect")
    def bank_verification(self):
        self.account = []
        self.account_number = 7136047821
        self.account.append(self.account_number)
        print(self.account)
        print("Bank Account Verified Successfully")
    def pancard_verification(self):
        self.pan_number = "FR03GPN785"
        if (len(self.pan_number) == 10):
            print("PAN card verified")
        else:
            raise ValueError("Invalid PAN number")
    def set_pin(self, number):
        self.pin = number
        if (len(self.pin) == 4 or len(self.pin) == 6):
            print("Your Pin is successfully created")
        else:
            raise ValueError("Invalid PIN Number")

    def enter_your_pin(self, match, pin):
        self.match = match
        self.pin = pin
        if self.match == self.pin:
            print("DONE!!")
        else:
            raise ValueError("PIN not match")
            
            
