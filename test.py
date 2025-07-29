# my_dict = {
#     "sach":10,
#     "vo":9

# # }

# # print(my_dict.popitem())

# hoa_qua =('cam','chanh', 'dau')
# hoa_qua =list(hoa_qua)
# hoa_qua = tuple(hoa_qua)
# hoa_qua.pop()\
# ds = [1,2,3,4,5,1,2,2]
# ds = set(ds)
# print(ds)


# ds =  {
#     "cam":5,
#     "dau":6,
#     "duahau":7
# }

# ds.setdefault("cam",1)
# print(ds)
import math

a_list = [1,2,3,4,5]
b_list =[]
# for i in a_list:
#     i = math.pow(i,2)
#     b_list.append(int(i))
# print(b_list)

b_list = [i*i for i in a_list if i%2==0] # pythonic
print(b_list)