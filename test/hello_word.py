meas = 'hello i love you'
# print(meas)

meas = 'hi word'

name = 'jin xin chao'

print(name.title())   # title 首字母大写
print(name.upper())   # upper 字母大写
print(name.lower())   # lower 字母小写
# print(meas)

first_name = 'acd';
last_name = 'efg';
concat_name = first_name + "" + last_name;   # 字符串拼接
print(concat_name.title())
print('\tab\ncfr')

fav_a = ' abc ' #去除空格
a = fav_a.rstrip(); #去除尾部空格
b = fav_a.lstrip(); #去除前面空格
c = fav_a.strip();  #去除首尾空格

print(a+""+b+""+c)

age = 23
num = 'abc '+str(age)+' de' # 不把变量转换为字符串得话会报错
print(num)

array = ['a','b','c','d','e','f','g']
print("我要看见你是大写得"+array[-1].title()+"")
