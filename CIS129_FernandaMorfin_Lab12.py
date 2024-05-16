#CIS129_FernandaMorfin_Lab12.py
# Pet class

class Pet:
    
    def __init__(self, name, typ, age):
        self.name = name
        self.type = typ
        self.age = age

   
    def set_name(self, name):
        self.name = name

    def set_type(self, typ):
        self.type = typ

    def set_age(self, age):
        self.age = age

 
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age


# Main module


print('──────▄▀▄─────▄▀▄')
print('─────▄█░░▀▀▀▀▀░░█▄')
print('─▄▄──█░░░░░░░░░░░█──▄▄')
print('█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█')
print('█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█')
print('█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█')
print('█░░║║║╠─║─║─║║║║║╠─░░█')
print('█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█')
print('█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')


def main():
    input_name = input("Enter a pet name: ")
    input_type = input("Enter a pet type: ")
    input_age = int(input("Enter a pet age: "))

    animal = Pet(input_name, input_type, input_age)

    print('─▀▀▌───────▐▀▀')
    print('─▄▀░◌░░░░░░░▀▄')
    print('▐░░◌░▄▀██▄█░░░▌')
    print('▐░░░▀████▀▄░░░▌')
    print('═▀▄▄▄▄▄▄▄▄▄▄▄▀═')

    print("Your pet name is:", animal.get_name())
    print("Your pet type is:", animal.get_type())
    print("Your pet age is:", animal.get_age())
    print(':)')

#call
if __name__ == "__main__":
    main()
