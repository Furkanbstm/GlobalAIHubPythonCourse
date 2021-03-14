list_of_evens = [0, 2, 4]
list_of_odds = [1, 3, 5]
list_of_both = list_of_evens + list_of_odds

list_of_both = list_of_evens + list_of_odds

list_of_merge = list_of_both.sort()

final_liste = list(list_of_both)

final_list = list([ i*2 for i in list_of_both])


for i in final_list:
    print(i)