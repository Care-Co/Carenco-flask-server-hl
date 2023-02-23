import numpy as np


data_list = [
                ['FF', 'C0'],
                ['FE', 'AA'],
                ['FE', '8D'],
                ['FE', '88'],
                ['FE', 'F4']]

real_list = [10.2, 69.2, 79.2, 87.1, 56.2]

total_list = []

for real_value, data_element in zip(real_list, data_list):
    first_data = int(data_element[0].upper(), 16) # * 16
    second_data = int(data_element[1].upper(), 16)# * 16
    sub_lst = [first_data, second_data]
    total_list.append(sub_lst)
    # print(first_data, second_data)
    
    # , first_data + second_data,
    #       first_data / real_value,
    #       second_data / real_value,
    #       (5000 -  (first_data + second_data)) / real_value,

    #       np.corrcoef(first_data, real_value)[0, 1],
    #       np.corrcoef(second_data, real_value),
    #       np.corrcoef(first_data + second_data, real_value)
          
    #       )

print(total_list)