import re

def validate_phone_number(phone_number):
    pattern = r"^(\+?234|0)([789]\d{9})$"
    return re.match(pattern, phone_number)

def get_mobile_network(phone_number):
    first_digits = phone_number[0:4]
    if first_digits in ['0803', '0806', '0814', '0810', '0813', '0814', '0816', '0703', '0706', '0903', '0906']:
        return 'MTN'
    elif first_digits in ['0809', '0817', '0818', '0908', '0909']:
        return '9mobile'
    elif first_digits in ['0802', '0808', '0812', '0708', '0701', '0902', '0901', '0907']:
        return 'Airtel'
    elif first_digits in ['0805', '0807', '0811', '0815', '0705', '0905']:
        return 'GLO'
    else:
        return 'Unknown'

def main():
    while True:
        phone_number = input("Enter your Nigerian phone number: ")
        if validate_phone_number(phone_number):
            network = get_mobile_network(phone_number)
            print("Mobile Network: " + network)
            break
        else:
            print("Invalid phone number. Please try again.")

if __name__ == "__main__":
    main()
