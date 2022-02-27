

def get_pet_shop_name(dictionary):
    return dictionary["name"]

def get_total_cash(dictionary):
    return dictionary["admin"]["total_cash"]

def add_or_remove_cash(dictionary, number):
    result = get_total_cash(dictionary) + int(number)
    dictionary["admin"]["total_cash"] = result

def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

def increase_pets_sold(dictionary, number):
    result = get_pets_sold(dictionary) + int(number)
    dictionary["admin"]["pets_sold"] = result

def get_stock_count(dictionary):
    return len(dictionary["pets"])

def get_pets_by_breed(dictionary, breed):
    list_of_pets_by_name = []
    for pet in dictionary["pets"]:
        if pet["breed"] == str(breed):
                list_of_pets_by_name.append(pet["name"])
    return list_of_pets_by_name

def find_pet_by_name(dictionary, name):
    for pet in dictionary["pets"]:
        if pet["name"] == str(name):
                return pet
    


def remove_pet_by_name(dictionary, name):
    for item in dictionary["pets"]:
        if item["name"] == str(name):
            (dictionary["pets"]).remove(item)



def add_pet_to_stock(dictionary1, dictionary2):
    return dictionary1["pets"].append(dictionary2)
    
def get_customer_cash(dictionary):
    return dictionary["cash"]

def remove_customer_cash(dictionary, cash):
    dictionary["cash"]-= int(cash)

def get_customer_pet_count(dictionary):
    return len(dictionary["pets"])

def add_pet_to_customer(dictionary_of_customer, dictionary_of_pet):
    return (dictionary_of_customer["pets"]).append(dictionary_of_pet)
    


#OPTIONAL
def customer_can_afford_pet(dictionary1, dictionary2):
    if dictionary1["cash"] >= dictionary2["price"]:
        return True
    return False

def sell_pet_to_customer(dictionary_shop, dictionary_pet, dictionary_customer):
    if dictionary_pet is None:
        return None

    if dictionary_customer["cash"] < dictionary_pet["price"]:
        return None

    add_pet_to_customer(dictionary_customer, dictionary_pet)
    increase_pets_sold(dictionary_shop, 1)
    remove_customer_cash(dictionary_customer, dictionary_pet["price"])
    add_or_remove_cash(dictionary_shop, dictionary_pet["price"])