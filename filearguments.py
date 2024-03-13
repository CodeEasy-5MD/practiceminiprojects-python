def grades(*grade):
    print("Third grade", grade[2])

grades("A", "B", "C", "D", "F")

#define function for key-value syntax
def my_name(sname, oname):
    print("Full names", sname + oname)
my_name(oname = "\tJoe ", sname = " Phil")

#default arguments
def my_country(name, country = "Kenya"):
    print("I am\t" +name+ "and I am from \t"+country)
my_country("Omondi ", "Kenya")
my_country("Valonzi ", "Uganda")
my_country("Amani ")