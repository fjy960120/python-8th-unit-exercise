"""8.5.1"""
def make_pizza(*toppings):
    print("You choosed toppings:")
    for i in toppings:
        print("\t"+ i.title())
make_pizza('mushroom')
make_pizza('extra cheese','dasa')
"""8.5.2"""
def make_new_pizza(size,*top):
    print("\n你选择的披萨尺寸是：")
    print("\t"+ size.title())
    print("你选择的披萨配料是：")
    for i in top:
        if i != 'q':
            print("\t" + i.title())
size = input("请输入你想要的披萨尺寸：")
top = []
biaozhi = True
while biaozhi:
    i = input("你想要加入的配料：")
    top.append(i)
    if i == 'q':
        biaozhi = False
make_new_pizza(size,*top)
"""8.5.3"""
def user_profile(frist,last,**user_info):
    profile = {}
    profile['frist_name'] = frist
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
build_profile = user_profile('albert','esinten',location='beijing',field='physics')
print(user_profile)
"""8.5.1练习"""
def make_sandwish(*topping):
    print("\n你选择的配料有：")
    for i in topping:
        if i != 'wanbi':
            print("\t"+i.title())
tops = []
logo = True
while logo:
    print("\n")
    j = input("你想要加入的配料：")
    tops.append(j)
    if j == ' w':
        logo = False

make_sandwish(*tops)
"""8.5.2练习"""
def user_information(frist,last,**users):
    information = {}
    information['frist_name'] = frist
    information['last_name'] = last
    for k,j in users.items():
        information[k]=j
    return information
users = user_information('lily','edward',father='jack',sister='icy',mother='alice',)
print(users)
#lily_information = users
#user_information(lily_information)