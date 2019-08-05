"""8.4.1"""
def greet_user(names):
    for name in names:
        mas = "Hello! " + name.title() + "!"
        print(mas)
usersname = ['lily','jack','edward']
greet_user(usersname)
"""8.4.2"""
unprint_designs = ['iphone','robot','dodecahedron']
complete_models = []
while unprint_designs:
    current_models = unprint_designs.pop()
    print("Printing model:"+current_models)
    complete_models.append(current_models)
print("\nPrinted models:")
for models in complete_models:
    print("\t"+models.title())
"""8.4.3"""
def show_printing_designs(unprint_models,printed_models):
    while unprint_models:
        c_model = unprint_models.pop()
        print("\nPrinting models: "+ c_model.title())
        printed_models.append(c_model)
def show_printed_designs(printed_models):
    print("\nPrinted models: ")
    for model in printed_models:
        print("\t"+ model.title())
unprint_models = ['A','B','C']
printed_models = []
show_printing_designs(unprint_models,printed_models)
show_printed_designs(printed_models)
"""8.4.1练习"""
def show_magicians(magicians):
    for magic in magicians:
        print("\nHello! "+magic.title())
magicians=['lily','david']
show_magicians(magicians)
"""8.4.2练习"""
magicianss = ['J','k']
magiciansss = []
def make_great(magicianss):
    for a in magicianss:
        a = "The Great " + a.title()
        print(a)
        magiciansss.append(a)
make_great(magicianss)
for b in magiciansss:
    print("\t"+b.title())
"""8.4.3练习"""
def make_great_magician(magicia,the_great_magician):
    while magicia:
        c = magicia.pop()
        c = "The great " + c.title()
        the_great_magician.append(c)
    print(the_great_magician)
magician = ['daming','daling']
the_great_magician = []
make_great_magician(magician[:],the_great_magician)
print("\n")
print(magician)
