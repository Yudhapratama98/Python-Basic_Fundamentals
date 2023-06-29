# BASIC dari segala basic adalah
# Variabel & data types
# Conditional Statements
# Looping Statements
# Collection Data Types (Tuple, list, Dictionary)
# Function


# OOP
# Python Class and Object
# Class itu adalah cetakan dimana nanti hasilnya adalah Object

class KueCoklatManusia:  # Ini adalah Cetakan
    def __init__(self, eyeColor, buttonColor):
        print('1 kue sedang dibuat')
        self.warnaMata = eyeColor
        self.warnaMulut = 'Putih'
        self.warnaBaju = 'Putih'
        self.warnaKancing = buttonColor


kue1 = KueCoklatManusia('Biru', 'Merah')
kue2 = KueCoklatManusia(eyeColor='Jingga', buttonColor='Abu')
kue3 = KueCoklatManusia(buttonColor='Item', eyeColor='Hejo')

print(kue1, type(kue1))
print(kue2, type(kue2))

print(kue1.__dict__, type(kue1.__dict__))
print(kue2.__dict__, type(kue2.__dict__))

kue2.warnaMata = 'Jingga'

print(kue1.warnaMata, type(kue1.warnaMata))
print(kue2.warnaMata, type(kue2.warnaMata))

# Inheritance
# Intinya, nanti sifat sifatnya diturunkan dari Parent(Makhluk Hidup) ke Child (Manusia)


class MakhlukHidup:
    def __init__(self, name, age, alive):
        self.nama = name
        self.umur = age
        self.masihHidup = alive

    def bernafas(self):
        print('{}sedang bernafas'.format(self.nama))


class Manusia(MakhlukHidup):
    def __init__(self, name, age, alive, job):
        super().__init__(name, age, alive)
        self.pekerjaan = job


manusia1 = Manusia('Yudha', 25, True, 'DataAnalyst')
manusia2 = Manusia('Yudha', 25, True, 'IT Support')

print(manusia1.__dict__)
manusia1.bernafas()
