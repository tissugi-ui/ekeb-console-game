def create_game():
  return {
    "energy":6,
    "turns":6,
    "fixed":[],
    "charger":False,
    "clue":False
  }
def check_result(state):
  if len (state["fixed"]==3:
    print("\n===ПОБЕДА!===")
    print("все 3 ошибки исправлены.")
    print("стенд EKEB готов к демонстрации!")
    return "win"

if state["turns"]<=0:
  print("\n===ПОРАЖЕНИЕ.===")
  print("ходы закончились.")
  return "lose"

if state["energy"]<2 and not state["charger"]:
  print("энергии недостаточноба зарядки больше нет.")
  return "lose"
  return"continue"

def play_game():
  state=create_game()

print("\n===========================")
 print("EKEB:УСПЕТЬ ДО ДЕМО")
print("=============================")
print("вам нужно исправить 3 ошибки")
print("до начала демонстрации EKEB.")

while TRUE:
  print(f"энергия:{state['energy']}")
   print(f"осталось ходов:{state['turns']}")
    print(f"исправлено ошибок:{len(state['fixed'])}/3")
print("============================")

print("\n выберите действие:")
print("1.осмотреть стенд")
print("2.забрать зарядку")
print("3.использовать зарядку")
print("4.исправить ошибку")
print("5.статус/инвентарь")
print("0.вернуться в меню")

command = input("ваш выбор:").strip()
#пустой ввод
if command =="":
  print("пустой ввод.ход не расходуется.")
continue

#осмотр стенда
if command == "1":
  inspect_stand(state)

#использовать зарядку
elif command =="2":
take_charger(state)

#исправить ошибку
elif command =="4":
solve_error(state)

#показать статус
elif command == "5":
show_status(state)

#вернуться  в меню
elif command == "0"
print("возвращаемся в главное меню.")
return

# неверная команда
        else:
            print("неизвестная команда. ход не расходуется.")
            continue

        # проверяем, закончилась ли игра
        result = check_result(state)

        if result == "win" or result == "lose":
            input("\nнажмите Enter, чтобы вернуться в меню...")
            return

def show_rules():
    print("\n========== ПРАВИЛА ==========")
    print("1. у вас есть 6 ходов.")
    print("2. начальная энергия — 6.")
    print("3. нужно исправить 3 ошибки.")
    print("4. осмотр стенда даёт улику с кодом EKEB.")
    print("5. зарядку можно забрать только один раз.")
    print("6. зарядка добавляет 3 энергии, максимум — 6.")
    print("7. исправление ошибки требует 2 энергии.")
    print("8. победа — все 3 ошибки исправлены.")
    print("9. после окончания игры можно начать новую.")
    print("=============================")

def main():
    while True:
        print("\n==============================")
        print("      EKEB: УСПЕТЬ ДО ДЕМО")
        print("==============================")
        print("1. начать игру")
        print("2. правила")
        print("0. выход")

        choice = input("выберите пункт: ").strip()

        if choice == "1":
            play_game()

        elif choice == "2":
            show_rules()

        elif choice == "0":
            print("программа завершена.")
            break

 elif choice == "":
            print("пустой ввод. выберите пункт меню.")

        else:
            print("неверный выбор. попробуйте снова.")


if _name_ == "_main_":
    main()


