from unicodedata import numeric


print()

# string capitailze( string where the first character is upper case,
#  and the rest is lower case.)

# txt = "hello and welcome to my world."
# x = txt.capitalize()
# print(x)

# txt = "python is fun!"
# x = txt.capitalize()
# print(x)

# txt = "150 is my age"
# x = txt.capitalize()
# print(x)

# # string casefold(LOWER/CASE)
# txt = "HELLO AND WELCOME TO MY WORLD!"
# x = txt.casefold()
# print(x)

# srring center()
# txt = "banan"
# x = txt.center(20,"k")
# print(x) 

# txt = "i love apple, apple are my favorite fruit"
# x = txt.count("apple",10,24)
# print(x)

# txt = "my name is stale"
# x = txt.encode()
# print(x)

# txt = "my name is triom"

# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors= "namereplace"))
# print(txt.encode(encoding="ascii",errors="replce"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


# txt = "Hello welcome to my world."
# x = txt.endswith(".")
# print(x)

# txt = "Hello welcome to my world"
# x = txt.endswith("my world", 5, 11)
# print(x)

# txt = "t\tr\ti\to\tm"
# x = txt.expandtabs(2)
# print(x)

# txt = "T\tr\ti\to\tm"

# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))

# txt = "hello welcom to my world"
# x = txt.find("welcome")
# print(x)

# txt = "hello welcome to my world"
# x = txt .find("e")
# print(x)

# txt = "hello welcome to my world"
# x = txt.find("e",5,10)
# print(x)

# txt = "hello welcome to my world."
# print(txt.find("q"))
# print(txt.index("q"))

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=49))

# txt1 = "my anme is {fname}, i'm {age}".format(fname="TRIOM",age=21)
# txt2 = "my name is {0},i'm {1}".format("TRIOM",21)
# txt3 = "my name is {}, i'm {}".format("TRIOM",21)
# print(txt1)
# print(txt2)
# print(txt3)

# txt = "hello welcome to my wrold"
# x = txt.index("welcome")
# print(x)

# txt = "Hello welcome to my world"
# x = txt.index("e")
# print(x)

# txt = "Hello welcome to my world"
# x = txt.index("e")
# print(x)

# txt = "hello welcome to my world"
# x = txt.index("e", 5, 10)
# print(x)

# txt = "hello welcome to my world"
# print(txt.find("q"))
# print(txt.index("q"))
# 

# isalunm method

# txt = "company 12"
# x = txt.isalnum()
# print(x)

# txt = "company12"
# x = txt.isalnum()
# print(x)

# isalpha

# txt = "companyX"
# x = txt.isalpha()
# print(x)

# txt = "company10"
# x = txt.isalpha()
# print(x)

# txt = "company10"
# x = txt.isascii()
# print(x)

# txt = "1234"
# x = txt.isdecimal()
# print(x)

# a = "\u0030"
# b = "\u0047"
# print(a.isdecimal())
# print(b.isdecimal())

# txt = "50800"
# x = txt.isdigit()
# print(x)

# a = "\u0030"
# b = "\u00b2"
# print(a.isdigit())
# print(b.isdigit())

# txt = "demo"
# x = txt.isidentifier()
# print(x)

# a = "myfolder"
# b = "demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# string islower

# txt = "hello world!"
# x = txt.islower()
# print(x)

# a = "hello world!" 
# b = "helo 123"
# c = "mynameispeter"

# # print(a.isupper())
# # print(b.isupper())
# # print(c.isupper())

# txt = "565543"
# x = txt.isnumeric()
# print(x)

# txt = "hello! are you #1?"
# x = txt.isprintable()
# print(x)

# txt = "hello!\nAre you #1"
# x = txt.isprintable()
# print(x)

# txt = "  "
# x = txt.isspace()
# print(x)

# txt = "  s  "
# x = txt.isspace()
# print(x)


# txt = "hello and welcome to my world!"
# x = txt.istitle()
# print(x)

# a = "HELLO AND WELCOME TO WY WORLD"
# b = "HELLO"
# c = "22 NAMES"
# d = "THIS IS %'!?"

# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

# a = "hello world?" 
# b = "hello 123"
# c = "MY NAME IS PETER"

# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# mytuple = ("john","peter","vicky")
# x = '|'.join(mytuple)
# print(x)

# mydict = {"name":"john","country":"noeway"}
# myseparator = "TEST"

# x = myseparator.join(mydict)
# print(x)


print ()

# age = int(input("entar you age"))
# if age>18:
#     print("i have aplly")
#     print("i have good day")

# age = int(input("entar your age"))
# if age>18:
#     print(" i have aplly yore license ")
# else:
#     print("i have no aplly ilncese")

# boy = "treu"
# girl = "treu"
# if boy == "True" and  girl == "treu":
#     print("entar all of  boy")
# elif boy != "true" and girl == "true": 
#     print("etar all of girl")
# elif boy == "treu" and girl != "true":
#     print("entar all of boy and girl")
# else:
#     print("i have good day boy and girl")


# age = 23
# won_car = 'treu'
# if (age >=18):
#     if (won_car == 'false'):
#         print('drive in car')
#     else:
#         print('yor new car apply')
# else:
#     print("on car apply ")

# for x in range(10):
#     print("2*",x,"=",2*x)

# l = 1
# while l<6:
#     print(l)
#     l+=1

# 

# i = 1
# while i<10:
#     print(i)
# #     i += 1

# w = 0
# while w <10:
#     print(w)
#     if w == 6:
#         break
#     w += 1

# capitalize () converts the first charater  t0 upper case.
# # txt = "hello plz com to my home welcome"
# x = txt.capitalize()
# print(x)

# casefold string into lawar case.
# txt = "hello plz com to my home welcome"
# y = txt.casefold()
# print(y)

# center returns a centerd string
# txt = "banana"
# y = txt.center(20,"0")
# print(y)

# count 

# txt = "i love hello,hello and my hello favoeite,hello"
# x = txt.count('hello',10,20)
# print(x)

# encode 
# txt = "my name is triom sondigla"
# y = txt.encode()
# print(y)

# txt = "my name is triom"

# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith = 
# txt = "hello welcome to my world."
# x = txt.endswith(".")
# print(x)

# txt = "hello welcome to my world"
# y = txt.endswith("my world.")
# print(y)


# txt = "hello welcome to my world"
# l = txt.endswith("my world.""5")
# print(l)

# expandtabs 
# txt = "H\te\tl\tl\to"
# x = txt.expandtabs(2)
# print(x)

# txt = "H\te\tl\tl\to"

# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))

# find 
# x = txt.find("welcome")
# x = txt.find("e")
# x = txt.find ("e",5,10)

# txt ="hello, welcome to my world."
# print(txt.find("q"))
# print(txt.index("q"))

# index ()
# x = txt.index("welcome")
# x = txt.index("e",5,10)
# txt = "hello,welcome to my word !"
# print (txt.find("q"))
# print(txt.index("q"))

# format 
# txt = "for only {price :.2f}dollars!"
# print(txt.format(price=49))



# endswith  
# txt = "hello welcome to my world"
# x = txt.endswith(".")
# print(x)

# txt = "hello welcome to my world"
# y = txt.endswith("my world.")
# print(y)

# expandtabs
# txt = "H\te\tl\tl\to"
# x = txt.endswith("2")
# print(x)

# txt = "H\te\te\tl\to"
# x = txt.expandtabs
# print(txt)

# txt = "h\te\te\tl\to/

# txt ="h\te\te\tl\to"
# x = txt.expandtabs
# print(txt.expandtabs(2))


# txt ="h\te\te\tl\to"
# x = txt.expandtabs
# print(txt.expandtabs(4))


# txt ="h\te\te\tl\to"
# x = txt.expandtabs
# print(txt.expandtabs(10))

# find
# txt = "hello welcome to my world"
# y = txt.endswith ("my world.""5.11")
# print(y)

# txt = "hello,welcome to my woad"
# x= txt.find("welcome")
# print(x)

# # index

# txt = "hello, welcome to my word!"
# x = txt.index("welcome")
# print(x)

# # format 
# txt = "for only {price:.2f}dallars!"
# print(txt.format(price=50))

# isalnum 
# txt = "company12"
# txt = "company 12"
# x = txt.isalnum()
# print(x)

# txt = "companyx"
# txt = "company 10"
# x = txt.isalpha()
# print(x)

# isascii 
# txt = "company123"
# x = txt.isascii()
# print(x)

# txt = "1234"
# y = txt.isascii()
# print(y)

# # isdecimal
# txt = "1234"
# s = txt.isdecimal()
# print(s)

# isdigit
# txt = "50800"
# x = txt.isdigit
# print(x)

# txt = "50800"
# x = txt.isdigit()
# print(x)

# a = "\u0030"
# b = "\u00b2"

# print(a.isdigit())
# print(b.isdigit())

# isidentifie

# txt = "Demo"
# x = txt.isidentifier()
# print(x)

# txt = "50800"
# x = txt.isdigit()
# print(x)

# a = "\u0030" 
# b = "\u00b2"

# print(a.isdigit())
# print(b.isdigit())

# txt = "hello world!"
# x = txt.islower()
# print(x)


# a = "hello world!" 
# b = "hello 123"
# c = "mynaeisper"

# print(a.islower())
# print(b.islower())
# print(c.islower())

#capitalize 
# txt = "I HAVE GOOD DAY all OF YOU"
# x = txt.capitalize()
# print(x)

# casefold
# txt = "I HAVE GOOD MORNING all OF YOU"
# x = txt.casefold()
# print(x)

# center 
# txt = "banana"
# x = txt.center(30)
# print(x)

# count 
# txt = "i hello apples, hello are my favorite hello"
# x = txt.count("hello")
# print(x)

# encode
# txt = "my name is meetji"
# x = txt.encode()
# print(x)

# txt = "hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

# txt = "H\te\tl\tl\to"
# x = txt.expandtabs(2)
# print(x)

# find 
# txt = "hello,welcome to my world."
# x = txt.find("o")
# print(x)

# # format
# txt = "for only {price:.2f} dollars!"
# print(txt.format(price = 59))

# index 
# txt = "hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

# txt = "hello , welcome to my world."
# x = txt.index("e")
# print(x)

# format 

# txt = "company12"
# x = txt.isalnum()
# print(x)

# isalnum 
# txt = "abc123"
# x = txt.isalnum()
# print(x)

# txt = "xcv 123"
# x = txt.isalnum()
# print(x)

# isalpha 
# txt  = "companyX"
# x = txt.isalpha()
# print(x)

# txt = "company10"
# x = txt.isalpha()
# print(x)

# isascii

# txt = "company123"
# x = txt.isascii()
# print(x)

# isdecimal
# txt = "123e"
# n = txt.isdecimal()
# print(n)

# a = "\u0030" 
# b = "\u0047"

# print(a.isdecimal())
# print(b.isdecimal())

# lower case 

# txt = "hello world!"
# x = txt.islower()
# print(x)

# a = "Hello world!"  
# b = "hello 132"
# c = "mynameisPeter"

# print(a.islower())
# print(b.islower())
# print(c.islower())


# # isnumeric
# txt = "565543"
# x = txt.isnumeric()
# print(x)

# a = "\u0030"
# b = "\u00b2"
# c = "10km2"
# d = "-1"
# e = "1.5"

# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())

# # capitalize  upper sumall
# txt = "I HAVE GOOD ALL OF YOU"
# x = txt.capitalize()
# print(x)
 
#  casefold lower capital
# txt = " I HAVE ALL OF YOU GOOD DAY"
# y = txt.casefold()
# print(y)

# center 
# txt = "triom"
# x = txt.center(5)
# print(x)

# count 

# txt = "i im triom,my name is triom"
# z = txt.count("r")
# print(z)

# # encode 
# txt = "my name in triom"
# c = txt.encode()
# print(c)

# endswith 
# txt = "i have,good hello world."
# b = txt.endswith(".")
# print(b)

# txt = "hello world,i have good day."
# m = txt.endswith(".")
# print(m)

# expandtabs 
# txt = "H\te\tl\tl\to"
# m = txt.expandtabs(2)
# print(m)

# find

# txt = "i_have_welcome_my_home"
# d = txt.find("my")
# print(d)

# format 
# txt = "for only {price:.2f} dollars!"
# print(txt.format(price = 400))

# index 
# txt = "i have all of you my home welcome"
# s = txt.index("home")
# print(s)

# isalnum 
# txt = "abc 12"
# k = txt.isalnum()
# print(k)

# isalpha
# txt = "werty12"
# l = txt.isalpha()
# print(l)

# isascii
# txt = "123company"
# x = txt.isascii()
# print(x)

# isdecimal
# txt = "123 456"
# x = txt.isdecimal()
# print(x)

# isdigit
# txt = "12345"
# x = txt.isdigit()
# print(x)

# isidentifier
# txt = "triom"
# s = txt.isidentifier()
# print(s)

# islower
# txt = "triom sondigla"
# k = txt.islower()
# print(k)

# isnumeric 
# txt = "507020"
# k = txt.isnumeric()
# print(k)


# isprintable

# txt = "my name is\triom sondigla"
# l = txt.isprintable()
# print(l)

# isspace

# txt = " 7 "
# v = txt.isspace()
# print(v)

# istitle
# txt = "Hello, And Welcome To My World!"
# s = txt.istitle()
# print(s)

# isupper
# txt = "TRIOm SONDIGLA"
# m = txt.isupper()
# print(m)

# join 

# mytuple = ("ravi","triom","jaydip")
# v = "#".join(mytuple)
# print(v)

# mydict = {"name":"john","country":"norway"}
# myseparator = "TEST"
# x = myseparator.join(mydict)
# print(x)

# ljust

# txt = "banana"
# x = txt.ljust(20,"0")
# print(x)

# lower 

# txt = "I HAVE NEW FRIND MY"
# z = txt.lower()
# print(z) 

# txt = "i have new frind"
# h = txt.lower()
# print(h)

# # lstrip
# txt = "           banana      "
# x = txt.lstrip()
# print("of all fruits",x,"is my favorite")

# txt = ",,,,,,,,,,ssaaww.......banana"
# x = txt.lstrip(",.asw")
# print(x)

# maketrans
# txt = "hello sam!"
# mytable = str.maketrans("s","p")
# print(txt.translate(mytable))

# partition
# txt = "i could eat bananas all day"
# x = txt.partition("apples")
# print(x)

# replace 
# txt = "i like bananas"
# x = txt.replace("bananas","apples")
# print(x)

# rfind
# txt = "mi_case,_su_case."
# x = txt.rfind("case")
# print(x)

# txt = "hello, welcome to my world."
# x = txt.rfind("e")
# print(x)

# rjust
# txt = "banana"
# x = txt.rjust(20)
# print(x,"is my favorite fruit.")

# txt = "banana"
# x = txt.rjust(20,"0")
# print(x)

# rpartition 
# txt = "i could eat bananas all day,bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)

# replit
# txt = "apple , banana, cherry"
# x = txt.rsplit(", ")
# print(x)

# txt = "apple,banana,cherry"
# x = txt.rsplit(", ", 1)
# print(x)

# rstrip
# txt = "   banana   "
# x = txt.rstrip()
# print("of all fruits", x,"is my favorite")

# split
# txt = "welcome to the my home"
# x = txt.split()
# print(x)

# splitlines
# txt = "thank you for the music\nwelcome to the jungle"
# x = txt.splitlines()
# print(x) 

# isalnum 
# txt = "company12"
# x = txt.isalnum()
# print(x)

# isalnum
# txt = "company 12"
# y = txt.isalnum()
# print(y)

# isalpha

# txt = "companyx"
# x = txt.isalpha()
# print(x)

# # isascii
# txt = "company123"
# u = txt.isascii()
# print(u)

# isdecimal
# txt = "1234765"
# o = txt.isdecimal()
# print(o)

# isdigit
# txt = "504000"
# y = txt.isdigit()
# print(y)

# isidentifier
# txt = "triom"
# g = txt.isidentifier()
# print(g)

# islower
# txt = "triomAsondigla"
# d = txt.islower()
# print(d)

# isnumeric 
# txt = "564575"
# h = txt.isnumeric()
# print(h)

# ispintable
# txt = "hello!\nAre you #1?"
# f  = txt.isprintable()
# print(f)

# isspace
# txt = "  "
# r = txt.isspace()
# # print(r)

# istitle
# txt = "hello, And Welcome To My World!"
# u = txt.istitle()
# print(u)

# isupper
# txt = "THIS Is NOW!"
# x = txt.isupper()
# print(x)

# join
# mytuple = ("john","peter","vicky")
# x = "#".join(mytuple)
# print(x)

# ijust
# txt = "banana"
# x = txt.ljust(10)
# print(x, "is my favorite fruit.")

# lower
# txt = "hello my FRIENDS"
# x = txt.lower()
# print(x)

# # lstrip
# txt = "     banana      "
# x = txt.lstrip()
# print("of all fruits",x,"is my favorite")

# maketrans
# txt = "hello sam!"
# mytable = str.maketrans("s","p")
# print(txt.translate(mytable))

# txt = "i could eat bananas all day"
# d = txt.partition("bananas")
# print(d)

# txt = "i like banans"
# x = txt.replace("banans", "apples")
# print(x)

# rtring

# txt = "Mi casa, su casa"
# x = txt.rfind("casa")
# print(x)

# # join
# txt = "triom"
# x = "#".join()
# print(x)

# txt = "i could eat bananas all day "
# x = txt.partition("bananas")
# print(x)
# print()


# capitalize
# txt = "I HAVE GOOD DAY"
# v = txt.capitalize()
# print(v)

# # CASEFOLD
# txt = "ALL OF YOU GOOD MORNING"
# h = txt.casefold()
# print(h)

# center
# txt = "SONDIGLA"
# u = txt.center(5)
# print(u)


# count
# txt = "i have good day all of you"
# c = txt.count("u")
# print(c)

# encode"
# txt = "my name is triom"
# b = txt.encode()
# print(b)

# endswith
# txt = "i have go to my home!."
# b = txt.endswith(".")
# print(b)

# expandtabs 
# txt = "H\te\tl\tl\to"
# h =txt.expandtabs(2)
# print(h)

# find/index
# txt = "i_have_welcome_to_my_home"
# g = txt.find("to")
# print(g)

# format()
# txt = "only {price:.3f}dheran"
# print(txt.format(price=5))

# isalnum 
# txt = "bhai321"
# f = txt.isalnum()
# print(f)

# isapha
# txt = "triomx 12"
# u = txt.isalpha()
# print(u)

# isascii
# txt  = " triom126 "
# i = txt.isascii()
# print(i)
 
# isdecimal 
# txt = "123456x"
# h = txt.isdecimal()
# print(h)

# isdigit
# txt = "1234567890"
# c = txt.isdigit()
# print(c)

# isidentifie
# txt = "triomsondigla"
# f = txt.isidentifier()
# print(f)

# islower
# txt = "i have"
# x = txt.islower()
# print(x)

# isnumeric
# txt = "564738"
# v = txt.isnumeric()
# print(v)

# isprintable
# txt = "hello! i #1 have"
# c = txt.isprintable()
# print(c)

#isspace
# txt = "  x  "
# x = txt.isspace()
# print(x)

# istitle
# txt = "i have good!"
# x = txt.istitle()
# print(x)

# isupper
# txt = "TRIOM SONDIGLA"
# x = txt.isupper()
# print(x) 

# join 
# myTuple = ["triom","sondigla","bhai"]
# x = "#".join(myTuple)
# print(x)

# name = ["bhai1","bhai2","bhai3"]
# x = "/".join(name)
# print(x)

# # ijust
# txt = "meet ji"
# x = txt.ljust(5)
# print(x,"s my brother")

# lower
# txt = "TRIOM SONDIGLA"
# x = txt.lower()
# print(x)

# lstrip
# txt = "  banana  "
# x = txt.lstrip()
# print("of all fruits", x ," is my fovorite")

# maketrans 
# txt = "hello sam!"
# mytable = txt.maketrans("s","p")
# print(txt.translate(mytable))

# partition()
# txt = "I could eat bananas all day"
# x = txt.partition("all")
# print(x)

# replace 
# txt = "I like bananas"
# x = txt.replace("bananas","apples")
# print(x)

# rfind 
# txt = "Mi casa, su casa."
# x = txt.rfind("casa")
# print(x)

# rindex 
# txt = "Mi casa, su casa."
# x = txt.rindex("casa")
# print(x)

# rjust
# txt = "banana"
# x = txt.rjust(20,".")
# print(x,"is my favorite fruit.")

# rpartition
# txt = "I could eat banana all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)

# rsplit
# txt = "apple, banana, cherry"
# x = txt.rsplit(", ")
# print(x)

# rstrip
# txt = "    banana     "
# x = txt.rstrip()
# print("of all fruits", x ,"is my favorite")

# split
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# splitlines
# txt = "Thank you for the music \nwelome to the jungle"
# x = txt. splitlines()
# print(x)

# startswith
# txt = "Hello,welcome to my world."
# x = txt.startswith("Hello")
# print(x)

# strip
# txt = "  mengo   "
# x = txt.strip()
# print("of all fruits" , x ,"is my favorite")

# swapcase
# txt = "Hello My Name Is TRIOM"
# x = txt.swapcase()
# print(x)

# print()

# title

# txt = "welcome to my world"
# x = txt.title()
# print(x)

# mydict = {83: 80}
# txt = "hello sam!"
# print(txt.translate(mydict))

# upper
# txt = "hello my frinds"
# x = txt.upper()
# print(x)

# zfill
# txt = "50"
# x = txt.zfill(10)
# print(x)

# maketrans
# txt = "hello sam!"
# mytable = str.maketrans("s","p")
# print(txt.translate(mytable))

# txt = "hello triom"
# mytable = str .maketrans("t" , "T")
# print(txt.translate(mytable))

# maketrans
# txt = "hello triom"
# mytable = str.maketrans("h","H")
# print(txt.translate(mytable))

# maketrans
# txt = "Hello teiom"
# mytable = str.maketrans("teiom","TRIOM")
# print(txt.translate(mytable))

# maketrans lace() Method
# txt = "Hello bhai"
# mytable = str.maketrans("bhai","ravi")
# print(txt.translate(mytable))

# maketrans
# txt = "Hello ji"
# mytable = str.translate("ji","")
# print(txt.translate(mytable))

# maketrans
# txt = "triom sondigal"
# mytable = str.maketrans("t", "R")
# print(txt.translate(mytable))

# partition
# txt = "I colud eat bananas all day" 
# x = txt.partition("eat") 
# print(x)

# partition
# txt = "i have go to home all of you"
# x = txt.partition("home")
# print(x)

# partition
# txt = "i have good day all of you"
# x = txt.partition("have")
# print(x)

# partition
# txt = "my name is triom"
# x = txt.partition("is")
# print(x)

# partition
# txt = "triom bhai sodigal"
# x = txt.partition("bhai")
# print(x)

# replace 
# txt = "I like bananas"
# x = txt.replace("bananas","apples")
# print(x) 

# replace
# txt = "i have my good day"
# x = txt.replace("good","home")
# print(x)

# replace
# txt = "i good frind"
# x = txt.replace("good","GOOD")
# print(x) 

# replace
# txt = "triom bhai"
# x =txt.replace("bhai","sondigla")
# print(x)

# # replace
# txt = "bhai sondigla"
# x = txt.replace("bhai","MR")
# print(x)

# replace
# txt = "mr triom"
# x = txt.replace("triom","sodigla")
# print(x)

# rfind
# txt = "_Mi_casa,_su_casa."
# x = txt.rfind("casa")
# print(x)

# rfind
# txt = "Mi_casa,_su_casa."
# x = txt.rfind("su")
# print(x)

# rfind
# txt = "i_have_new_home"
# x =txt.rfind("new")
# print(x)

# rfind
# txt = "i_have_good_day"
# x = txt.rfind("have")
# print(x)

# rfind
# txt = "go_to_home."
# x = txt.rfind("to")
# print(x)

# rfind
# txt = "i have go to home"
# x = txt.rfind("go")
# print(x)

# maketrans
# txt = "hello bhai"
# mytable = txt.maketrans("h","H")
# print(txt.translate(mytable))

# pratition
# txt = "my_name_is_triom"
# x = txt.partition("_name_")
# print(x)

# replace
# txt = "i have go good day"
# x = txt.replace("go","my")
# print(x)

# rfind
# txt = "i have go to"
# x = txt.rfind("go")
# print(x)

# capitalize
# txt = "i my go to home"
# x = txt.capitalize()
# print(x)

# casefold
# txt = "go to home"
# x =  txt.casefold()
# print(x)

# center
# txt = "TRIOM"
# x = txt.center(10)
# print(x)

# endshwi
# txt = ("go to home all off you.!")
# x = txt.endswith(" . ")
# print(x)

# expandtabs
# txt = "H\te\tl\tl\to"
# x = txt.expandtabs(2)
# print(x)

# FIND
# txt = "hello all, of you all"
# x = txt.find("all")
# print(x)

# formut

# index = 
# txt = "hello my all home all of you all"
# x = txt.index("all")
# print(x)

# isalnum
# txt = "123andabc"
# x = txt.isalnum()
# print(x)

# isalpha
# txt = "rtyui"
# x = txt.isalpha()
# print(x)

# isacii
# txt = "3456ertyudfghvbn456ASDFT"
# x = txt.isascii()
# print(x)

# isdecimal
# txt = "123"
# x = txt.isdecimal()
# print(x)

# isdigit
# txt = "123456"
# x = txt.isdigit()
# print(x)

# isdentifier
# txt = "triom"
# x = txt.isidentifier()
# print(x)

# isnumeri
# txt = "1234"
# x = txt.isnumeric()
# print(x)

# isprintabel
# txt = "i have\ngood frind #1"
# x = txt.isprintable()
# print(x)

# ispace
# txt =  " . "
# x = txt.isspace()
# print(x)

# istitle
# txt = "Triom Sondigla In Gujrat In Surat In Uttran "
# x = txt.istitle()
# print(x) 

# ispartition
# txt = "i like bike to car"
# x = txt.partition("bike")
# print(x)

# replace
# txA   qw134523678p
# \
# t = "i like bike"
# x = txt.replace("bike","car")
# print(x)

# rfind 
# txt = "i have good day"
# x = txt.rfind("good")
# print(x)

# rindex 
# txt = "i goo to home all of you"
# x = txt.rindex("all")
# print(x)

# rjust
# txt = "aPlly"
# x = txt.rjust(20)
# print(x,"is my favorite fruit")

# zfill 
# txt = "welcome to my world"
# x = txt.title()
# print(x)

# capitalize
# txt = "i have good"
# x = txt.capitalize()
# print(x)

# casefold
# txt = "Good Day All of you"
# x = txt.casefold()
# print(x)

# count
# txt = "hello bay hello girl hello all of you"
# x = txt.count("hello")
# print(x)

# endswith
# txt = "hello,boy and girl go to home."
# x = txt.endswith(".")
# print(x)

# ing
# x = 23
# print(x)

# flo 
# y = 66.78
# print(y)

# stri
# c = "triom"
# print(c)

# type cast 
# x = 12
# y = 12.8
# z ="3k"
# print(x)
# print(y)
# print(z)

# slice

# x = "triom"
# print(x[2:5])

# y = "sondigla"
# print(y[2:5])

# upper
# x = "i have go to home"
# y = x.upper()
# print(y)

# lower
# x = "I HAVE GOOD DAY"
# y = x.lower()
# print(y)

# title
# x = "i have go to home"
# y = x.title()
# print(y)

# capitalise
# x = "my bike"
# y = x.capitalize()
# print(y)

# concatenalon
# a = 12
# b = 11
# c = (a + b)
# print(c)

# logical opre
# and or not
#  l<>g
# print(12>13)
# print(13>12)
# print(12<13)
# print(13<12)

# a = 12
# b = 13
# print(bool(a))
# print(bool(b))

# a = "35.9"
# b = "33.5"
# print(bool(a))
# print(bool(b))

# py lists access
# name = ["triom","ravi","rahul"]
# print(name[1])

# # remove
# namelist = ["ajy","bhai","abhi"]
# namelist.remove("bhai")
# print(namelist)

# # change lists
# name = ["jay","ajay","abhi"]
# name[2] = "kbhi"
# print(name)

# # add 
# namelist = ["yug","meet","shahil"]
# namelist.append("ravi")
# print(namelist) 

# for loop
# name = ["triom","bhai","sondigla"]
# for x in name:
#     print(x) 

# for x in range(11):
#     print(x)

# for x in range(11):
#     print("2*",x,"=",2*x)

# l = []
# for x in range(0,101):
#     print(x)

# while loop 
# i = 1
# while i<=10:
#     print(i)
#     i+=1
# i = 0 
# while i<=10:
#     print(i)
#     i-=1

# for x in range tiom :
    # print(x)

# txt = "i like bike and car"
# x = txt.partition("bike")
# print(x)

# txt = "i like bike"
# x = txt.replace("bike","car")
# print(x)

# txt = "Hello Triom"
# x = str.maketrans("T","t")
# print(txt.translate(x))

# txt = "i like car and bike my"
# x = txt.rpartition("and")
# print(x) = "i like car and bike my"

# stplit
# txt = "apply,banana,cherry"
# x = txt.rsplit(", ")
# print(x)

# partition
# txt = "i like bike and car"
# x = txt.partition("and")
# print(x)

# relace
# txt = "i like bike"
# x = txt.replace("bike","car")
# print(x)

# rfind
# txt ="i have good day all of you"
# x = txt.rfind("good")
# print(x)

# maketrans
# txt = "hello pan!"
# x = txt.maketrans("h","H")
# print(txt .translate(x))


# append
# name = ['triom','ravi','ajay','vijay']
# name.append("mehul")
# print(name)

# clear 
# name = ["triom","ravi","ajay"]
# name.clear()
# print(name)

# copy 
fruits = ["apple","banana","cherry"]
x = fruits.copy()
print(x)



