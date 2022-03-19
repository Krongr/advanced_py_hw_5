import copy
from logger import logger


class Unpacker():
    def __init__(self, list_to_unpack):
        # self.list_to_unpack = copy.deepcopy(list_to_unpack)
        self.list_to_unpack = list_to_unpack
        self.new_list = []
        self.i = 0

    @logger(path_to_file='logs')
    def unpack(self, list_to_unpack, new_list):
        for _i in range(len(list_to_unpack)-1, -1, -1):
            if type(list_to_unpack[_i]) != list:
                new_list.append(list_to_unpack.pop(_i))
            else:        
                self.unpack(list_to_unpack[_i], new_list)
        return new_list  
    
    @logger(path_to_file='logs')
    def __iter__(self):
        self.unpack(self.list_to_unpack, self.new_list)
        self.new_list.reverse()
        return self

    @logger(path_to_file='logs')
    def __next__(self):
        i = self.i
        self.i += 1
        if i < len(self.new_list):
            return self.new_list[i]
        else:
            raise StopIteration

  
if __name__ == '__main__':  
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', ['f', ['h']], False],
        [1, 2, None],
    ]
  
    # for _i in Unpacker(nested_list):
    #   print(_i)
    
    list_comp = [i for i in Unpacker(nested_list)]
    print(list_comp)