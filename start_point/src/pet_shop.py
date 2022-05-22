# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]


def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


def add_or_remove_cash(total_cash, price):
    price = 10
    total_cash["admin"]["total_cash"] += price
    return total_cash


# def add_or_remove_cash(total_cash, price):
#     price = 10
#     total_cash["admin"]["total_cash"] -= price
#     return total_cash


def get_pets_sold(total):
    return total["admin"]["pets_sold"]


def increase_pets_sold(pets_sold, pets):
    pets = 2
    pets_sold["admin"]["pets_sold"] += pets
    return pets_sold


def get_stock_count(total_stock):
    return len(total_stock["pets"])


def get_pets_by_breed(pet_shop, breed):
    breed_list = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)

    return breed_list


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customers, num):
    customers["cash"] -= num


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)
