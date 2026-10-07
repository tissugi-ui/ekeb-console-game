def chek_answer(number,answer):
  answer=answer.strip().lower()


if number ==1:
  return answer =="ekeb"

elif number == 2:
   return answer=="120"

elif numer == 3:
  return answer=="almaty"

return False


def inspect_stand(state):
  if state["clue"]:
    print("Вы уже осматривали стенд. Новой улики нет.")
    return

state["clue"]=True
state["turns"]-=1

print("Вы осмотрели стенд.")
print("Получена улика:Код доступна:EKEB")

def take_charger(state):
  if state["charger"]:
    print("Зарядку уже забрали.")
    return
          
state["charger"]=True
state[turns"]-=1

print("Вы нашли зарядку и добавили её в инвентарь")


def use-charger(state):
if not state["charger"]:
  print("В инвентаре нет зарядки.")
  return

state["charger"]=False
state["energy"]=min(6,state["energy"] +3)
state["turns']-=1

print("Зарядка использована.")
print(f"Энергия теперь:{state['energy']}")

def show_status(state);
print("\n==========СТАТУС==========")
print(f"Ходы:{state['turns']}')
print(f"Исправлено ошибок:{len(state['fixed'])}из 3")

if state["clue'];
print("Улика:Код доступа:EKEB")
else:
 print("Улик нет")

if state["charger"]:
print("Инвентарь:Зарядка")

else:
 print("Инвентарь пуст")


print("=============================")


def solve_error(state):
 print("\n==========ОШИБКИ==========")
 print("1.Ошибка А - ввести код EKEB")
 Print("2.Ошибка Б - сколько минут в 2 часах?")
 print"3.Ошибка С - привести Almaty к нижнему регистру")

  choice=input("Выберите ошибку:").strip()

   if choice not in ["1","2","3"]:
      print("Неверный номер ошибки.Ресурсы не расходуются.")
      return

    number = int(choice)

    if number in state["fixed"]:
       print("Эта ошибка уже исправлена.")
       return

    if number == 1 and not state["clue"]:

      print("Сначала нужно осмотреть стенд.")

      return

    if state["energy"]<2:

       print("Недостаточно энергии.Нужно минимум 2.")

       return

    if number ==1:
       answer = input("Сколько минут 2 часах?")

      else:
        answer = input("Введите Almaty в нижнем регистре:")

      # Любая попытка ответа тратит 2 энергии и 1 ход

      state["energy"]-=2
      state["turns"]-=1

      if check_answer(number,answer):

    state["fixed"].append(number)
        print("Правильный ответ!Ошибка исправлена.")

      else:
         print("Неверный ответ.Можно попробовать ещё раз.")
      if state

         




