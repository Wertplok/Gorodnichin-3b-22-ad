array = [5, 7, 11 ,13, 15, 20]

filter_list = [*filter(lambda x: x > 10, array)]
result = sum(filter_list)/len(filter_list)

