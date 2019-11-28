'''pair location searcher'''

dic_location = {j+i:'default' for i in '123456789' for j in 'ABCDEFGH'}

def main(user_choice):
    '''main function for finding pair location or submit your location'''
    print('--------------------------------------')
    if user_choice == 'Find':
        choose_choices(input('if you want to find only your pair says "Pair" if you want to see all location says "All" : '))
        #find only your Pair _OR_ See all location
        print('--------------------------------------')
    elif user_choice == 'Tell':
        upload_location()
        print('save your location complete')
        print('--------------------------------------')
    elif user_choice == 'Clear':
        clear_data()
        print('Clear all Data complete')
        print('--------------------------------------')
    else:
        print('ERROR please try again only "Find" "Tell" or "Clear"')
        print('--------------------------------------')
    main(input('if you want to find pair says "Find" but if you want to tell your location says "Tell" or "Clear" to clear all data : '))

def choose_choices(user_choice):
    '''choose find one location  or  see all location'''
    if user_choice == 'Pair':
        print('--------------------------------------')
        find_pair(input('your pair_ID : '))
    elif user_choice == 'All':
        print('--------------------------------------')
        show_all_location()
    else:
        print('ERROR please try again only "Pair" or "All"')
        print('--------------------------------------')
        choose_choices(input('if you want to find only your pair says "Pair" if you want to see all location says "All" : '))

def find_pair(pair_id):
    '''find pair location'''
    pair_id = filter_id(pair_id, 'pair')
    print('--------------------------------------')
    if check_id_in_dic(pair_id) == True:
        pair_location = search_from_dic(pair_id)
        print(pair_location)
    else:
        print('Not found')

def check_id_in_dic(stu_id, dic=dic_location):
    '''check that stu_ID has a location or not'''
    if stu_id in dic.values():
        return True
    return False

def search_from_dic(pair_id, dic=dic_location):
    '''search location in dic that student ID = pair ID'''
    for location, stu_id in dic.items():
        if stu_id == pair_id:
            return location

def upload_location(dic=dic_location):
    '''Upload your current location to dic_location'''
    your_id = filter_id(input('Your ID : '))
    print('--------------------------------------')
    your_location = filter_location(input('Your location from A1 - A9, B1 - B9, .... H1 - H9 : '))
    print('--------------------------------------')
    if check_id_in_dic(your_id) == True:
        your_pre_location = search_from_dic(your_id)
        dic[your_pre_location] = 'default'
    dic[your_location] = your_id

def filter_id(stu_id, words=''):
    '''filter stu_id that is not number and number of characters is not 8'''  
    if len(stu_id) == 8 and stu_id.isnumeric():
        return stu_id
    print('ERROR please tell your {0}_ID again Ex 62070068 : '.format(words))
    print('--------------------------------------')
    return filter_id(input('Your {0}_ID : '.format(words)), words)

def filter_location(your_position, dic=dic_location):
    '''filter your location that is not in dic_location'''
    if your_position in dic:
        return your_position
    print('ERROR please tell your location again')
    print('--------------------------------------')
    return filter_location(input('Your location from A1 - A9, B1 - B9, .... H1 - H9 : '))

def show_all_location():
    '''show all location'''
    print()
    all_row_left = range(0, 65, 8)
    for row_left in all_row_left:
        show_row(row_left)
        print('\n')

def show_row(row_left):
    '''show 1 row'''
    row_right = row_left + 7
    row = list(dic_location.items())[row_left:row_right+1]
    for location, stu_id in row:
        if stu_id == 'default':
            print('   ' + location, end='         ')
        else:
            print(stu_id, end='      ')

def clear_data():
    '''clear all data in dic_location'''
    for location in dic_location:
        if dic_location[location] != 'default':
            dic_location[location] = 'default'

def test():
    '''tester'''
    dic_test = {'A1':'62070068', 'A2':'default', 'A3':'62070038'}
    assert check_id_in_dic('62070068', dic_test) == True
    assert check_id_in_dic('62070190', dic_test) == False
    assert search_from_dic('62070068', dic_test) == 'A1'
    assert search_from_dic('62070038', dic_test) == 'A3'
    assert filter_id('62070068') == '62070068'
    assert filter_id('62070038') == '62070038'
    assert filter_location('A1', dic_test) == 'A1'
    assert filter_location('A2', dic_test) == 'A2'

test()
main(input('if you want to find pair says "Find" but if you want to tell your location says "Tell" or "Clear" to clear all data : '))
