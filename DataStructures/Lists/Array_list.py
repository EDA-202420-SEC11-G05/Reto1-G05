def new_list():
    newlist = {
        "elements" : [],
        "size" : 0,
    }
    return newlist

def get_element(mylist, pos):
    return mylist['elements'][pos-1]

def is_present(mylist, element, cmp_function):
    size = mylist["size"]
    if size>0:
        keyexist = False
        for keypos in range (0,size):
            info = mylist["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist == True
                break
        if keyexist:
            return keypos
    return -1

def add_first(mylist,element):
    return set.add_element(mylist["elements"][0],element)


def size(mylist):
    return set.size(mylist["elements"])

def add_last(mylist,element):
    return set.add_element(mylist["elements"][size(mylist)-1],element)

def first_element(mylist):
    return set.get_first_element(mylist["elements"])