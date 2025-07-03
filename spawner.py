import random

random.seed()

def spawn_customer():
    """
    Generates a random budget for a customer.

    This function simulates the generation of a random budget for a customer by
    returning a randomly selected integer within a specified range. The budget
    represents the available funds allocated to the customer.

    :return: An integer representing the budget randomly generated for the customer.
    :rtype: int
    """
    random_budget = random.randrange(1, 100)
    return random_budget
