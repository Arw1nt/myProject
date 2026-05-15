import random

def random_number():
    while True:
        number = random.randint(1, 100)
        popitka = 0
    
        print("Я загадал число от 1 до 100 - попробуй угадать его!")
    
        while True:
            try:
                your_number = int(input("Ваше число:\n"))
                popitka += 1

                if your_number < number:
                    print("Моё число больше!")
                elif your_number > number:
                    print("Мое число меньше!")
                else:
                    print(f"Вы угадали моё число! У вас это заняло {popitka} попыток.")
                    while True:
                        play_again = input("\nХочешь сыграть ещё раз? (да/нет): ").lower()
                        if play_again in ['да', 'yes', 'y']:
                            break

                        if play_again in ['нет', 'no', 'n']:
                            print("\nСпасибо за игру!")
                            return
                        
                        else:
                            print("Пожалуйста, ответь 'да' или 'нет'")
                    break
                        
            except ValueError:
                print("Ошибка! Введи целое число!")

random_number()
