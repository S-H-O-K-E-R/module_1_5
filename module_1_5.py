immutable_var = (100, 50.5, 'Hello' ,True)
#immutable_var[True] = False
#immutable_var['Hello'] = 'Hi'
#immutable_var[50.5] = 60.5
#immutable_var[100] = 200
#элементы кортежа нельзя менять в отличие от списков

mutable_list = [100, 50.5, 'Hello' ,True]
print(mutable_list)
mutable_list.append('Hi')
mutable_list.remove(50.5)
mutable_list[0] = False
print(mutable_list)