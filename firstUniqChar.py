# s = 'leetcode'

# for i 

class MyCustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]
    def __len__(self):
        return len(self.data)

# 创建一个自定义列表
my_list = MyCustomList([1, 2, 3, 4, 5])
my_list[4]
print(len(my_list))
