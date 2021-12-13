import gp

puspanathan = gp.Google_pay("puspanathang@gmail.com","8637635446","Puspanathan G")
puspanathan.open_gpay()
puspanathan.email_verification()
puspanathan.mobile_verification()
puspanathan.name_verification()
puspanathan.otp_verification(25695,25695)
puspanathan.bank_verification()
puspanathan.pancard_verification()
puspanathan.set_pin("1397")
puspanathan.enter_your_pin(3256,3256)

class Phone_pe(gp.Google_pay):
    def __init__(self, email_id, phone_number, name):
        super().__init__(email_id, phone_number, name)

    def open_phonepe(self):
        print("Phone pe")

puspanathan = Phone_pe("puspanathang@gmail.com","8637635446","Puspanathan G")
puspanathan.open_phonepe()
puspanathan.mobile_verification()
puspanathan.name_verification()
puspanathan.otp_verification(870569,870569)
puspanathan.bank_verification()
puspanathan.pancard_verification()
puspanathan.set_pin("326598")
puspanathan.enter_your_pin(3256,3256)


googlepay = [{"Name":"Ajaykumar","Gpaynumber":9945645645,"Type":"personal","Transaction":"Regular"},
             {"Name":"Abi rithanya","Gpaynumber":6458977777,"Type":"personal","Transaction":"Rare"},
             {"Name":"Aravindh","Gpaynumber":9994734564,"Type":"personal","Transaction":"Regular"},
             {"Name":"Aadharsh","Gpaynumber":9002580258,"Type":"personal","Transaction":"Regular"},
             {"Name":"Akil sree","Gpaynumber":9000365498,"Type":"personal","Transaction":"Regular"},
             {"Name":"Aswath","Gpaynumber":7878969610,"Type":"personal","Transaction":"Rare"},
             {"Name":"Anu","Gpaynumber":7871495012,"Type":"personal","Transaction":"Regular"},
             {"Name":"Ashik","Gpaynumber":6836734456,"Type":"personal","Transaction":"Rare"},
             {"Name":"Ashwin","Gpaynumber":9958720549,"Type":"personal","Transaction":"Regular"},
             {"Name":"Balu","Gpaynumber":9994053495,"Type":"personal","Transaction":"Regular"},
             {"Name":"Bannariyamman fruits","Gpaynumber":8502147496,"Type":"personal","Transaction":"Rare"},
             {"Name":"Banumathi","Gpaynumber":9595623015,"Type":"personal","Transaction":"Regular"},
             {"Name":"Chandrasekar","Gpaynumber":6835724019,"Type":"personal","Transaction":"Regular"},
             {"Name":"Chandru","Gpaynumber":9764319764,"Type":"personal","Transaction":"Regular"},
             {"Name":"Dhinesh","Gpaynumber":9363524178,"Type":"personal","Transaction":"Regular"},
             {"Name":"Dhivya","Gpaynumber":9191919283,"Type":"personal","Transaction":"Regular"},
             {"Name":"Eshwaran","Gpaynumber":9525852585,"Type":"personal","Transaction":"Rare"},
             {"Name":"Fahadh","Gpaynumber":9632548999,"Type":"personal","Transaction":"Rare"},
             {"Name":"Guru","Gpaynumber":9963520315,"Type":"personal","Transaction":"Regular"},
             {"Name":"Gayathri","Gpaynumber":6125984736,"Type":"personal","Transaction":"Regular"},
             {"Name":"Ganesh","Gpaynumber":6392857140,"Type":"personal","Transaction":"Rare"},
             {"Name":"Ganapathy","Gpaynumber":6035687241,"Type":"personal","Transaction":"Rare"},
             {"Name":"Godwin","Gpaynumber":7023654819,"Type":"personal","Transaction":"Regular"},
             {"Name":"Gopi","Gpaynumber":7139284650,"Type":"personal","Transaction":"Rare"},
             {"Name":"Gowtham","Gpaynumber":7894561230,"Type":"personal","Transaction":"Rare"},
             {"Name":"Hari","Gpaynumber":7778889994,"Type":"personal","Transaction":"Rare"},
             {"Name":"Hema","Gpaynumber":7115896230,"Type":"personal","Transaction":"Regular"},
             {"Name":"Indhu","Gpaynumber":6920335558,"Type":"personal","Transaction":"Regular"},
             {"Name":"Inika","Gpaynumber":6789135409,"Type":"personal","Transaction":"Regular"},
             {"Name":"Jayanth","Gpaynumber":6842357910,"Type":"personal","Transaction":"Rare"},
             {"Name":"Jeevitha","Gpaynumber":9517538426,"Type":"personal","Transaction":"Rare"},
             {"Name":"Kaaviyan","Gpaynumber":9173829173,"Type":"personal","Transaction":"Rare"},
             {"Name":"Kamalesh","Gpaynumber":8001122998,"Type":"personal","Transaction":"Rare"},
             {"Name":"Leo","Gpaynumber":9371280546,"Type":"personal","Transaction":"Regular"},
             {"Name":"Lilly","Gpaynumber":9638527410,"Type":"personal","Transaction":"Regular"},
             {"Name":"Madhu","Gpaynumber":9876540000,"Type":"personal","Transaction":"Regular"},
             {"Name":"Mano Priya","Gpaynumber":6458654856,"Type":"personal","Transaction":"Rare"},
             {"Name":"mavis","Gpaynumber":9988776655,"Type":"personal","Transaction":"Regular"},
             {"Name":"Nandhu","Gpaynumber":9994734564,"Type":"personal","Transaction":"Regular"},
             {"Name":"Navin","Gpaynumber":8855223365,"Type":"personal","Transaction":"Rare"},
             {"Name":"Pinguu","Gpaynumber":6598659865,"Type":"personal","Transaction":"Rare"},
             {"Name":"Pooja","Gpaynumber":7012571025,"Type":"personal","Transaction":"Regular"},
             {"Name":"Raagul","Gpaynumber":8138138138,"Type":"personal","Transaction":"Rare"},
             {"Name":"Raju","Gpaynumber":9586589658,"Type":"personal","Transaction":"Regular"},
             {"Name":"Sai","Gpaynumber":8654215000,"Type":"personal","Transaction":"Rare"},
             {"Name":"Sri","Gpaynumber":6320155997,"Type":"personal","Transaction":"Rare"},
             {"Name":"Tamil","Gpaynumber":6800025987,"Type":"personal","Transaction":"Rare"},
             {"Name":"Thulasimani","Gpaynumber":9087014956,"Type":"personal","Transaction":"Rare"},
             {"Name":"Vasuki","Gpaynumber":7789523650,"Type":"personal","Transaction":"Regular"},
             {"Name":"Vijayan","Gpaynumber":6325987451,"Type":"personal","Transaction":"Regular"},
             {"Name":"Vidhya","Gpaynumber":9523015896,"Type":"personal","Transaction":"Rare"}]

for i in googlepay:
    for j,k in i.items():
        print(f"{j}:{k}")

