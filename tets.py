lst = ['numpy', 'pandas', 'requests']

lst_gen = (pkg for pkg in lst)
print(lst_gen)