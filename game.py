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

def kamen_nozhnici_bumaga():
    while True:
        choices = {
        '1': 'Камень',
        '2': 'Ножницы', 
        '3': 'Бумага'}

        wins = 0
        loses = 0

        print("Игра: Камень, Ножницы, Бумага")
        
        while True:
            print(f"\nСчёт: {wins} - {loses}")
        
            try:
                player_choice = input("Твой выбор:\n1 - Камень\n2 - Ножницы\n3 - Бумага\n0 - Выход из игры\n")
            
                if player_choice == '0':
                    print(f"Финальный счёт: {wins} - {loses}")
                    return
                
                
                if player_choice not in choices:
                    print("Неверный выбор!")
                    continue
                
                computer_choice = str(random.randint(1, 3))
            
                print(f"Ты выбрал: {choices[player_choice]}")
                print(f"Компьютер выбрал: {choices[computer_choice]}")
            
                if player_choice == computer_choice:
                    print("Ничья!")
                elif (player_choice == '1' and computer_choice == '2') or \
                    (player_choice == '2' and computer_choice == '3') or \
                    (player_choice == '3' and computer_choice == '1'):
                    print("Ты победил!")
                    wins += 1
                else:
                    print("Ты проиграл!")
                    loses += 1
                
            except (ValueError, KeyError):
                print("Ошибка! Пожалуйста, введи 1, 2, 3 или 0 для выхода из игры")
            except KeyboardInterrupt:
                print("\nИгра прервана!")
                break

while True:
    try:
        vibor = int(input("\nВыберите во что хотите поиграть:\n1 - Угадай число\n2 - Камень-ножницы-бумага\n3 - Выйти из консоли\n"))
        if vibor == 1:
            random_number()
        if vibor == 2:
            kamen_nozhnici_bumaga()
        if vibor == 3:
            print("\nСпасибо за вашу игру!")
            break
        
    except ValueError:
        print("Ошибка! Такой команды нет.")
