RETURN_NUMBER = 5
VALUATE_NUMBER = 10
QUERY_NUMBER = 25

# USER_NAME_ID_DICT = {'cuong': 1, 'hieu': 2, 'dung': 3, 'phu': 4}

def caculate_average_precision(r, p_at_i_array):
    return 1.0/r*sum(p_at_i_array)
# def caculate_average_precision_of_query(query):
def r_doc_number(valuate_array):
    result_array = []
    for i in range(len(valuate_array)):
        valuate = valuate_array[i]
        valuate = valuate['valuate']
        result_array.append(valuate)
    result = sum(result_array)
    if result == 0:
        return 1
    return result

class QueryResult():
    def init(self):
        self.query = None
        self.valuate_array = [{'doc': None, 'valuate': 0}]*VALUATE_NUMBER
    def get_return_array(self):
        return self.valuate_array[:RETURN_NUMBER]
    def caculate_average_precision_of_query(self):
        r = r_doc_number(self.valuate_array)
        valuate_value_array = []
        p_at_i_array = []
        for i in range(len(self.valuate_array)):
            valuate = self.valuate_array[i]
            valuate = valuate['valuate']
            valuate_value_array.append(valuate)
            if i == 0:
                p_at_i_array.append(valuate*1.0)
            else:
                p_at_i_array.append(valuate*1.0/i)
        ap = caculate_average_precision(r, p_at_i_array)
        return ap




# caculate_mean_average_precision(querys)
# valuate_array = [{'doc': None, 'valuate': False'}]*VALUATE_NUMBER
# return_array = valuate_array[:RETURN_NUMBER]
# map_valuate(querys)
# def get_id_by_user_name(user_name):
#     return USER_NAME_ID_DICT[user_name]
# def caculate_map_of_user()
def read_valuate_array_of_user(file):
    valuate_array_of_user = []
    with open(file) as f:
        values = f.readlines()
        for i in range(0,25*3, 3):
            # value = f.readlines(i+2)
            value = values[i+2]
            value_dict = [{'doc': None, 'valuate': 0}]*VALUATE_NUMBER
            # print(value.split(' ')[0])
            number = int(10*float(value.split(' ')[0]))
            # print(number)
            # print(type(number))
            for dict in value_dict[:number]:
                dict['valuate'] = 1 
            valuate_array_of_user.append(value_dict)
    return valuate_array_of_user
###########################################
def caculate_mean_average_precision_of_querys(querys, valuate_array_of_user):
    sum = 0
    for query, valuate_array in zip(querys, valuate_array_of_user):
        # query_result = new QueryResult(query, valuate_array)
        query_result =  QueryResult()
        query_result.valuate_array = valuate_array
        
        average_precision = query_result.caculate_average_precision_of_query()
        sum += average_precision
    mean = 1.0*sum/QUERY_NUMBER
    return mean

if __name__ == '__main__':
    import sys
    # user_name = sys.argv[1]
    # id = get_id_by_user_name(user_name)
    # ex: query = 'Viet Nam'
    # querys = []
    # for user_folder in folder:
    #     valuate_array_of_user = []
    #     for query in user_folder:
    #         valuate_array = read_valuate_array(query)
    #         valuate_array_of_user.append(valuate_array)
    #     map_user_value = caculate_mean_average_precision_of_querys(querys, valuate_array_of_user):
    #     print('map of user is', map_user_value)
    # querys = []
    # for query_i in range(QUERY_NUMBER):
    #     valuate_array = read_valuate_array(query_i)
    valuate_array_of_user = read_valuate_array_of_user('test.txt')
    # print(valuate_array_of_user)
    querys = 'Hello'*QUERY_NUMBER
    map_user_value = caculate_mean_average_precision_of_querys(querys, valuate_array_of_user)
    print('map of user is', map_user_value)

