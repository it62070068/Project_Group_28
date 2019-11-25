'''pair location searcher'''
def find_pair():
    '''main function for finding pair location'''
    dic_location = {i+j:'default' for i in 'ABCDEFGH' for j in '123456789'}
    while True:
        val = input('if you want to find pair says "F" but if you want to tell your positon says "T" : ')
        if val == 'F':
            pair_id = search_position(dic_location)
            if pair_id != False:
                print(search_dict(dic_location, pair_id))
            else:
                print('Not Found')
        elif val == 'T':
            your_id, your_positon = tell_position(dic_location)
            if your_id in dic_location.values():
                dic_location[search_dict(dic_location, your_id)] = 'default'
            dic_location[your_positon] = your_id
            print('save your position complete')
        else:
            print('ERROR please try again only "F" or "T"')

def search_position(dic):
    '''search positon that is pair_id in dic ?''' 
    pair_id = input('your pair_ID : ')
    if pair_id in dic.values():
        return pair_id
    else:
        return False

def tell_position(dic):
    '''tell your id'''
    your_id = input('Your ID : ')
    if len(your_id) == 8 and your_id.isnumeric():
        return your_id, check_position(dic)
    else:
        print('ERROR please tell your ID again Ex 62070068 : ')
        return tell_position(dic)

def check_position(dic):
    '''check your position that conditional'''
    your_positon = input('Your Positon from A1 - A9, B1 - B9, .... H1 - H9 : ')
    if your_positon in dic:
        return your_positon
    print('ERROR please tell your positon again')
    return check_position

def search_dict(dic, pair_id):
    '''search key in dic that value = pair_id'''
    for key, value in dic.items():
        if value == pair_id:
            return key

find_pair()

