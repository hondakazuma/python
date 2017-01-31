
class SubClass():

    def subclass(self):
        sub_hensu1 = "i am honda"
        sub_hensu = "you too"



class MainClass(SubClass):

    def mainclass(self):

        main_hensu1 = "hello python"
        main_hensu2 = "goodbye python"

        print(subclass.sub_hensu1)





if __name__== '__main__':
    obj1 = SubClass()
    obj2 = MainClass()

    obj2.mainclass()
