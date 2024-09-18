
def new_list():
    newlist = {
        'elements':[],
        'size': 0,        
    }
    return newlist

def get_element(my_list, pos):
    return my_list['elements'][pos-1]
    
def is_present(my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def is_empty(my_list):
    return my_list['size'] == 0

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][0]
    else:
        return -1
    
def last_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][-1]
    else:
        return -1

def get_element(my_list, pos):
    return my_list['elements'][pos - 1]

def remove_first(my_list):
    size = my_list['size']
    if size == 0:
        return None
    first = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return first

def remove_last(my_list):
    size = my_list['size']
    if size == 0:
        return None
    last = my_list['elements'].pop()
    my_list['size'] -= 1
    return last

def insert_element(my_list, element, pos):
    my_list['elements'].insert(pos - 1, element)
    my_list['size'] += 1
    return my_list

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    for i in range(size):
        if cmp_function(element, my_list['elements'][i]) == 0:
            return i
    return -1

def delete_element(my_list, pos):
    size = my_list['size']
    if pos < 1 or pos > size:
        return 
    element = pos - 1
    my_list['elements'].pop(element)
    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    element = pos - 1
    my_list['elements'][element] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    element1 = pos1 - 1
    element2 = pos2 - 1
    my_list['elements'][element1], my_list['elements'][element2] = my_list['elements'][element2], my_list['elements'][element1]
    return my_list

def sub_list(my_list, pos, numelem):
    size = my_list['size']
    element = pos - 1
    end_element = min(element + numelem, size)
    sublist = my_list['elements'][element:end_element]
    return {
        'size': len(sublist),
        'elements': sublist,
        'type': "ARRAY_LIST"
    }
