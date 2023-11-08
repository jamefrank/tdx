sh_stock_list = api.get_security_list(MarkeType.shanghai.value, 0)
# sh_stock_list = api.get_security_list(MarkeType.shenzhen.value, 0)
print(len(sh_stock_list))