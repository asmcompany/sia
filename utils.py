from django.db import connection, reset_queries
import time
from functools import wraps

def querry_debuger(func):
    @wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        start_q = len(connection.queries)
        start_t = time.perf_counter()

        result = func(*args, **kwargs)

        stop_t = time.perf_counter()
        stop_q = len(connection.queries)
        print()
        print(f" === {func.__name__}  ===")
        print(f'number of querries :{stop_q - start_q}')
        print(f'time taken         :{stop_t - start_t:.2f}')
        print()
        # for querry in connection.queries:
        #     print(querry)
        #     print()
        print()
        return result
    return inner_func


def sort_maker(_dict:dict):
    """ 
    given the `GET.dict` of a request, \n 
    it will return fields for sorting a QuerySet 
    """
    def sort_maker_privilege(key):
        """ this specifys the order of returned sorting keys """
        dic = {
        'price': 2 ,
        'title' : 1 ,
        }
        return dic[key.replace('-', '')]

    sorting_ = []
    
    for k, v in _dict.items():
        if v == 'asc':
            sorting_.append((k))
        elif v =='dec':
            sorting_.append(('-'+k))
    return sorted(sorting_, key=sort_maker_privilege)

