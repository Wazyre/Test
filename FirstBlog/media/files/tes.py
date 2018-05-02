#Part c
print("-----Part C-----\n")
#Part c 1
print("(c.1)\n")

def number_property(n: int, prop: str) -> bool:
    '''
    Checks if the inserted number matches the property inserted
    '''
    if prop == "even":
        if n%2 == 0:
            return True
        else:
            return False
    elif prop == "odd":
        if n%2 == 1:
            return True
        else:
            return False
    elif prop == "positive":
        if n >= 0:
            return True
        else:
            return False
    elif prop == "negative":
        if n < 0:
            return True
        else:
            return False
    else:
        print("Invalid Property")

assert number_property (14, "even")
assert not number_property (100, "odd")
assert number_property(33, "positive")
assert not number_property(100, "negative")

print("250 is an even number:", number_property(250, "even"))

#Part c 2
print("\n(c.2)\n")

def print_vertically() -> None:
    '''
    Prints an inserted word vertically; new line for every character
    '''
    word = input("Enter a word: ")
    for i in range(len(word)):
        print(word[i])
    return

print_vertically()

#Part c 3
print("\n(c.3)\n")

def square_root_list(ints: "List of int") -> None:
    '''
    Takes a list of inttegers, square roots them, then prints them
    '''
    for i in range(len(ints)):
        print(ints[i]**(1/2))
    return

print(square_root_list([3, 4, 5, 7, 2]))
#Part c 4
print("\n(c.4)\n")

def match_last_letter(m: str, list: "List of str") -> None:
    '''
    Prints all strings that end with the letter inserted
    '''
    for i in list:
        if m == i[-1]:
            print(i)
    return

match_last_letter('d', ["Blue", "Outsourced", "Red", "Gloomy Sunday", "Gone with the Wind",
"Superman", "Blazing Saddles"])

#Part c 5
print("\n(c.5)\n")

def print_by_area_code(list: "List of str", list2: "List of str") ->None:
    '''
    Takes two lists of numbers; if an area code is present in the second list, the
    phone number is printed
    '''
    for i in range(len(list)):
        for n in list2:
            if list[i] == n[1:4]:
                print(n)
    return
print_by_area_code(["212", "789"], ["(714)948-4212", "(212)949-8732", "(789)555-1234"])

#Part c 6
print("\n(c.6)\n")

def choose_by_area_code(list: "List of str", list2: "List of str") ->None:
    '''
    Takes two lists of numbers; if an area code is present in the second list, the
    phone number is returned
    '''
    resuult = []
    for i in range(len(list)):
        for n in list2:
            if list[i] == n[1:4]:
                result.append(n)
    return result
#Part D
print("\n-----Part D-----\n")
#Part d 1
print("\n(d.1)\n")

def is_consonant(m: str) -> bool:
    '''
    Checks if a character is a vowel or consonant
    '''
    consonant = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

    if m in consonant:
        return True
    else:
        return False

assert is_consonant('x') == True
assert is_consonant('P') == True
assert not is_consonant('a') == True
assert not is_consonant('?') == True

print(is_consonant('r'))

#Part d 2
print("\n(d.2)\n")

def print_consonants(n: str) -> None:
    '''
    Takes a string and prints its consonants
    '''
    for i in range(len(n)):
        if is_consonant(n[i]) == True:
            print(n[i])
    return

print_consonants("opening")
print()
print_consonants("assignment")

#Part d 3
print("\n(d.3)\n")

def consonants(n: str) -> str:
    '''
    Takes a string and prints another string containing its consonants
    '''
    result = ''
    for i in range(len(n)):
        if is_consonant(n[i]) == True:
            result = result + n[i]
    return result

assert consonants('University') == 'nvrst'
assert consonants('Marathon') == 'Mrthn'
print("The consonants in \'Lecture' is:", consonants('Lecture'))

#Part d 4
print("\n(d.4)\n")

def non_consonants(n: str) -> str:
    '''
    Takes a string and prints another string containing its vowels
    '''
    result = ''
    for i in range(len(n)):
        if is_consonant(n[i]) == False and n[i] not in 'yY':
            result = result + n[i]
    return result

print("The vowels in \'University' is:", non_consonants('University'))
#Part d 5
print("\n(d.5)\n")

def select_letters(m: str, n: str) -> str:
    '''
    If v is inserted, prints all vowels in second string; c is inserted, prints
    all consonants in second string
    '''
    result = ''
    if m == 'v':
        for i in range(len(n)):
            if is_consonant(n[i]) == False and n[i] not in 'yY':
                result = result + n[i]

    elif m == 'c':
        for i in range(len(n)):
            if is_consonant(n[i]) == True:
                result = result + n[i]
    return result

assert select_letters('v', 'facetiously') == 'aeiou'
assert select_letters('c', 'facetiously') == 'fctsl'

print("The vowels in \'amazingly' is:", select_letters('v', 'amazingly'))
#Part d 6
print("\n(d.6)\n")

def hide_vowels(n: str) -> str:
    '''
    Takes a string and returns the same string, but rplaces all vowels with asteriks
    '''
    result = ''
    for i in range(len(n)):
        if is_consonant(n[i]) == False and n[i] not in 'yY':
            result = result + '*'

        elif is_consonant(n[i]) == True:
                result = result + n[i]
    return result

print("With hidden vowels, the word \'Azerbaijan' becomes:", hide_vowels('Azerbaijan'))

#Part e
print("\n-----Part E-----\n")

from collections import namedtuple
Diner = namedtuple("Diner", "name cuisine phone dish price")

# Diner attributes: name, kind of food served, phone number,
# best dish, price of that dish
diner_1 = Diner("Taillevent", "French", "343-3434", "Escargots", 24.50)
diner_2 = Diner("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
diner_3 = Diner("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
diner_4 = Diner("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
diner_5 = Diner("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen", 8.50)
diner_6 = Diner("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
diner_7 = Diner("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
diner_8 = Diner("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
diner_9 = Diner("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
diner_10 = Diner ("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
diner_11 = Diner("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
diner_12 = Diner("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
diner_13 = Diner("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
diner_14 = Diner("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
diner_15 = Diner("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
diner_16 = Diner("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
diner_17 = Diner ("Spago", "California", "333-2222", "Striped Bass", 24.50)
diner_18 = Diner("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
diner_19 = Diner("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
diner_20 = Diner("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
diner_21 = Diner("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
diner_22 = Diner("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
diner_23 = Diner("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
diner_24 = Diner ("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
diner_25 = Diner ("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
diner_26 = Diner ("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)
diner_list = [diner_1, diner_2, diner_3, diner_4, diner_5,
             diner_6, diner_7, diner_8, diner_9, diner_10, diner_11,
             diner_12, diner_13, diner_14, diner_15, diner_16, diner_17,
             diner_18, diner_19, diner_20, diner_21, diner_22, diner_23,
             diner_24, diner_25, diner_26]


def diner_change_price(diner: Diner, n: float) -> Diner:
    '''
    Takes a diner and increases its price by the number inserted
    '''
    diner = diner._replace(price = diner.price + n)
    return diner

print(diner_change_price(diner_1, 23.76))
#Part f
print("\n-----Part F-----\n")

#Part f 1
print("\n(f.1)\n")
def diner_name(diner: Diner) -> str:
    return diner.name

def alphabetical_by_name(list: "List of Diner") -> "List of Diner":
    '''
    Takes a list of diners and sorts them alphabetically
    '''
    sort_diner = sorted(list, key = diner_name)
    return sort_diner

print(alphabetical_by_name(diner_list))

#Part f 2
print("\n(f.2)\n")

def alphabetical_names(list: "List of Diner") -> "List of str":
    '''
    Takes a list of diners and returns a list containing diners' names sorted alphabetically
    '''
    names = []
    for i in range(len(list)):
        names.append(list[i].name)
    names.sort()
    return names

print(alphabetical_names(diner_list))

#Part f 3
print("\n(f.3)\n")

def all_California(list: "List of Diner") -> "List of Diner":
    '''
    Takes a list of diners and returns a list containing diners with Californian cuisines
    '''
    cali = []
    for i in range(len(list)):
        if list[i].cuisine == "California":
            cali.append(list[i])
    return cali

print(all_California(diner_list))

#Part f 4
print("\n(f.4)\n")

def select_cuisine(list: "List of Diner", m: str) -> "List of Diner":
    '''
    Takes a list of diners and returns a list containing diners with cuisines the
    same as the cuisine inserted
    '''
    cuisi = []
    for i in range(len(list)):
        if list[i].cuisine == m:
            cuisi.append(list[i])
    return cuisi

print(select_cuisine(diner_list, "Thai"))

#Part f 5
print("\n(f.5)\n")

def select_cheaper(list: "List of Diner", n: float) -> "List of Diner":
    '''
    Takes a list of diners and returns a list containing diners with prices cheaper
    than the float inserted
    '''
    cheap = []
    for i in range(len(list)):
        if list[i].price < n:
            cheap.append(list[i])
    return cheap

print(select_cheaper(diner_list, 10.00))

#Part f 6
print("\n(f.6)\n")

def average_price(list1: "List of Diner") -> float:
    '''
    Takes a list of diners and returns the average price of the diners
    '''
    sum = 0
    for i in range(len(list1)):
        sum = sum + list1[i].price
    avg = sum/len(list1)
    return avg

print(average_price(diner_list))

#PArt f 7
print('\n(f.7)\n')

print(average_price(select_cuisine(diner_list, "French")))

#Part f 8
print('\n(f.8)\n')

print(average_price(select_cuisine(diner_list, "Chinese")+select_cuisine(diner_list, "Thai")))

#Part f 9
print('\n(f.9)\n')

print(alphabetical_names(select_cheaper(diner_list, 20.00)))

#Part G
print('-----Part G-----')

import tkinter
window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(window, width=1000, height=1000)
my_canvas.pack()
def create_rectangle_from_center(x: int, y: int, height: int, width: int) -> None:
    '''
    Creates a rectangle around the center coordinates inserted with the height and width provided
    '''
    my_canvas.create_rectangle(x-(0.5*width), y-(0.5*height), x+(0.5*width), y+(0.5*height))
    return

create_rectangle_from_center(500, 500, 100, 200)
