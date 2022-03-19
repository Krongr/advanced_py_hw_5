from datetime import datetime as dt
from datetime import date as d

def logger(path_to_file:str=''):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(
                f'{path_to_file}\{d.today()}_log.txt', 
                'a', 
                encoding='utf-8'
            ) as log:
                log.write(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: "
                    f"'{old_function.__name__}' started with "
                    f"folowing arguments: {args}, {kwargs}. "
                    f"Function returned: {result}\n")
            return result
        return new_function
    return _logger