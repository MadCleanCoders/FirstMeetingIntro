#Example of the S in SOLID principles



#Bad example, Multiple responsability class
class MultipleResponsabilityService:

    def get_customer_data(self, id):
        return 1

    def get_product_price(self, product_id):
        return 1

    def get_arturo_iq(self, awesomeness_index):
        return 1



#Cool example
class CustomerService:

    def get_customer_data(self, id):
        return 1

class ProductService:

    def get_product_price(self, product_id):
        return 1

class ArturoService:

    def get_product_price(self, product_id):
        return 1