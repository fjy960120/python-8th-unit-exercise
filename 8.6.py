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