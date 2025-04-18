import time
#Вступление
print('Добро пожаловать к вашему новому психологу. ')
time.sleep(1)
print('Правила разговора с психологом: ')
time.sleep(1)
print('Если психолог задает вам вопрос, то вы должны отвечать так, как будто с вами все хорошо, а ни то... Необязательно знать.')
time.sleep(3)
print('У вас тонкий характер и вы очень травмированы? Скрывайте это')
time.sleep(4)
print('Удачного сеанса.')
time.sleep(2)

#Первый вопрос
print('1 вопрос:')
time.sleep(1)
print('Вы готовы?')
time.sleep(2)
print('A: Да')
time.sleep(1)
print('В: Нет')
time.sleep(2)

#Исправь таймер на цикл!
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#Ответ
q1 = input('Ваш ответ? (A или B)')
time.sleep(2)
if q1 == 'A':
    print('Начнем.')
else:
    print('Эм...')
    time.sleep(1)
    print('Зачем сюда вообще пришли тогда? Все равно начнем.')
    time.sleep(1)
    
#Допиши твои вопросы ниже!
print('2 вопрос:')
time.sleep(1)
print('вы - это вы?')
time.sleep(2)
print('A: Да')
time.sleep(2)
print('В: Нет')
time.sleep(2)

#Исправь таймер на цикл!
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#Ответ
q1 = input('Ваш ответ? (A или B)')
time.sleep(2)
if q1 == 'B':
    print('Вас к экзорцисту отправить? Могу номерочек дать.')
else:
    print('Слава богу')

print('3 вопрос:')
time.sleep(1)
print('Как вообще поживаете? Все ли у вас хорошо в жизни?')
time.sleep(2)
print('A: Да')
time.sleep(2)
print('В: Нет')
time.sleep(2)
print('C: Я не могу разобраться в себе...')
time.sleep(2)

#Исправь таймер на цикл!
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#Ответ
q1 = input('Ваш ответ? (A, B или C)')
time.sleep(2)
if q1 == 'B':
    print('Так и запишу...')
elif q1 == 'A':
    print('Вот и хорошо')
else:
    print('Вы психованый? М-да...')
    time.sleep(1)
    print('В смысле не можете?')
    time.sleep(1)
    print('М-да...')

print('4 вопрос:')
time.sleep(1)
print('Замечали ли вы какие-то отклонения в себе?')
time.sleep(1)
print('Может не могли что-то решить в самый ответственный момент из-за препятствий в себе?')
time.sleep(2)
print('A: Да, было такое.')
time.sleep(2)
print('В: Нет, не встречал/а.')
time.sleep(2)
print('C: Я не могу разобраться в себе...')
time.sleep(2)

#Исправь таймер на цикл!
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#Ответ
q1 = input('Ваш ответ? (A, B или C)')
time.sleep(2)
if q1 == 'B':
    print('Мг, хорошо.')
elif q1 == 'A':
    print('Вот только не надо себя жертвой выставлять.')
else:
    print('Понятно все с вами.')
    time.sleep(1)
    print('И почему же?')
    time.sleep(3)
    print('Ладно... Следующий вопрос, раз вы молчите.')

print('5 вопрос:')
time.sleep(1)
print('Испытываете ли вы страх, когда кто-то резко двигается возле вас?')
time.sleep(2)
print('A: Да, было такое. Я думаю, что он/а хотел/а ударить меня.')
time.sleep(2)
print('В: Нет.')
time.sleep(2)
print('C: Не понял/а вопрос.')
time.sleep(2)
print('D: Мне некомфортно...')
time.sleep(2)

#Исправь таймер на цикл!
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#Ответ
q1 = input('Ваш ответ? (A, B, C или D)')
time.sleep(2)
if q1 == 'B':
    print('Понятно.')
elif q1 == 'A':
    print('Не выдумывайте себе.')
elif q1 == 'C':
    print('Пропустим значит.')
else:
    print('И зачем вы сюда пришли?')
    time.sleep(1)
    print('Неженка.')
    time.sleep(1)