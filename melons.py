
class AbstractMelonOrder:
    """Parent class for melons"""

    def __init__(self, species, qty):
        self.shipped = False
        self.species = species
        self.qty = qty
    

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        intl_small_order_fee = 3

        if self.qty < 10 and self.order_type == 'international': 
            total = total + intl_small_order_fee

        return total


    def mark_shipped():
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):   
    """A melon order for the gov't"""

    order_type = 'government'
    passed_inspection = False
    tax = 0    

    def mark_inspection(passed):
        """Record if melon passed inspection"""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = 'domestic'
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = 'international'
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)

        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


order0 = InternationalMelonOrder('watermelon', 1, "AUS")
order1 = InternationalMelonOrder('watermelon', 20, "AUS")
order2 = DomesticMelonOrder('Christmas Melon', 1)
order3 = GovernmentMelonOrder('watermelon', 1)
print(order0.get_total())
print(order1.get_total())
print(order2.get_total())
print(order3.get_total())
