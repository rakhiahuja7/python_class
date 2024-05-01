#question1 circle area calculator
class circle:
    def calculate_area(self):
        radius=int(input('enter radius of circle'))
        area=3.14*radius*radius
        print(area)
c=circle()
c.calculate_area()
#question2 discount percentage price calculator 
class percentage:
    def calculate_discount(self):
        original_price=int(input('enter original_price'))
        discount_percentage=int(input('enter discount percentage'))
        final_price=original_price-(discount_percentage/100)
        print(final_price)
price=percentage()
price.calculate_discount()
#question3 vowel calculator
class vowels:
    def count_vowels(self):
        word=input('enter a word')
        l=['a','e','i','o','u','A','E','I','O','U']
        for i in word:
            print(i,end='')
            print('-->',end='')
            print(l.count(i))
v=vowels()
v.count_vowels()
            

