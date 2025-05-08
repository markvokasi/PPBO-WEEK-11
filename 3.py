class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class View(object):
    def title_services(self):
        print("Services Provided:")

    def title_pricing(self):
        print("Pricing for Services:")

    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'], 
                  svc, "messages you pay $", 
                  Model.services[svc]['price'])

class View2(object):
    def title_services(self):
        print("Layanan yang Tersedia:")

    def title_pricing(self):
        print("Harga untuk Layanan:")
        
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'], 
                  svc, "pesan Anda membayar Rp", 
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self, bahasa):
        self.model = Model()
        if bahasa == "1":
            self.view = View()
        elif bahasa == "2":
            self.view = View2()
        else:
            print("Error, choose the language number!")
            exit()

    def tampilkan(self):
        services = self.model.services.keys()
        self.view.title_services()
        self.view.list_services(services)
        self.view.title_pricing()
        self.view.list_pricing(services)

    def tawar_harga(self):
        print("What service do you want to bid? email, sms, or voice :", end=" ")
        layanan = input().lower()
        if layanan not in self.model.services:
            print("Service not available.")
            return
        try:
            harga_baru = int(input("Enter the price you want (in $): "))
            self.model.services[layanan]['price'] = harga_baru
            print("Price according to your bid:")
            services = self.model.services.keys()
            self.view.title_pricing()
            self.view.list_pricing(services)
        except ValueError:
            print("Invalid price entered.")

print("What language do you choose? [1]English [2]Indonesia:", end=" ")
bahasa = input()
controller = Controller(bahasa)
print()
controller.tampilkan()
print()
controller.tawar_harga()

