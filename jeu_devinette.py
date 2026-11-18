import random
guess=0
secret_number=random.randint(1,100)
attempts=0
print("مرحبا بك في لعبة التخمين !! ")
print("لقد اخترت رقماً بين 1 و 100، حاول تخمينه.")

while guess != secret_number:
        guess = int(input("أدخل تخمينك: "))
        attempts+=1

        if guess < secret_number:
            print("الرقم السري أكبر! حاول مرة أخرى.")
        elif guess > secret_number:
            print("الرقم السري أصغر! حاول مرة أخرى.")
        else:
            print("لقد نجحت في تخمين العدد ")
            print("عدد المحاولات:", attempts)
