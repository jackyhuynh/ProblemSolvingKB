# arg passing 101
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

def fcn_trace(func):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
    def tracer(*args, **kwargs):
        logging.info(f"{func.__name__} - begin")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} - end")
        return result
    return tracer

@fcn_trace
def set_list(lista):
    # what is list at this point?
    lista = ["A", "B", "C"]
    # what is list now?
    return lista

@fcn_trace
def add_list(listb):
    listb.append("E")
    return listb

my_list = ["D"]

print(set_list(my_list))
print(my_list)
add_list(my_list)
print(my_list)
