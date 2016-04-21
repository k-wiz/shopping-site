"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self,
                 first_name, last_name, 
                 email, password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
      

    def __repr__(self):
            """Convenient method to show information about customer in console."""

            return "<Customer: %s, %s, %s, %s>" % (
                self.first_name, self.last_name, self.email, self.password)



def read_customer_from_file(filepath):
    """Read customer data and populate dictionary of customers by email.

    Dictionary will be {email: Customer object}
    """

    customer_info = {}

    for line in open(filepath):
        (first_name, last_name, email, password) = line.strip().split("|")

        customer_info[email] = Customer(first_name, last_name, email, password)

    return customer_info


def get_by_email(email):
    """Return a customer object given customer email."""

    return customer_info[email]


customer_info = read_customer_from_file("customers.txt")