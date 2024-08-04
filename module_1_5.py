immutable_var = (1, 2.2, 'abc', True)
print('Immutable tuple: ', immutable_var)

# immutable_var[0] = 100
# 4-ю строку будет подчеркивать желтым и выдавать ошибку, поскольку элементы кортежа нельзя изменить
# исключением является если один из элементов кортежа является списком, который можно изменить

mutable_list = [1, 2.2, 'abc', True]
mutable_list[2] = 'apple'
print('Mutable list: ', mutable_list)
