def user_name(frist_name,last_name):
    full_name = frist_name + " " + last_name
    full_name = full_name.title()
    return full_name
musician = user_name('jimi','edward')
print(musician)
"""8.3.2"""
def get_formatted_name(frists_name,lasts_name,middles_name=''):
    fulls_name=frists_name + " " + middles_name  + " " + lasts_name
    return fulls_name.title()
musicians = get_formatted_name('jimi','lee','edward')
musicianss = get_formatted_name('lily','lee','marie')
musiciansss = get_formatted_name('jack','edward')
print(musicians)
print(musicianss)
print(musiciansss)
"""8.3.3"""
def build_person(fristss_name,lastss_name):
    person = {'frist':fristss_name,'last':lastss_name}
    return person
musicianssss = build_person('lily','mode')
print(musicianssss)
"""8.3.4"""
def formatted_name(f_name,L_name):
    full_names = f_name + L_name
    return full_names.title()
while True:
    f_name = input("请输入你的姓：")
    if f_name == 'q':
        break
    L_name = input("请输入你的名字：")
    if L_name == 'q':
        break
    name = formatted_name(f_name,L_name)
    print("\n Hello, " + name +"!")
"""8.3.1练习"""
def city_country(city_name,country_name):
    place = city_name + "," + country_name
    print(place.title())
city_country('bejing','china')
city_country('london','english')
city_country('paris','french')
"""8.3.2练习"""
def make_aldum(singer_name,cd_name,music_number=''):
    aldum = {'singer':singer_name,'CD':cd_name}
    if music_number:
        aldum['music_number'] = music_number
    return aldum
while True:
    singer_name = input("请输入歌手的名字：")
    cd_name = input("请输入专辑的名字：")
    music_number = input("请输入歌曲的数量：")
    music = make_aldum(singer_name,cd_name,music_number=music_number)
    print(music)
    break


