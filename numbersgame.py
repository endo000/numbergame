a = input('Введи, с какого числа ты хочешь начать(от 0 до 9)\n')
length = int(input('Сколько итераций ты хочешь воспроизвести?\n'))
list_ = [a]
new_list_ = []
w = 1
for q in range(length):
    for i in range(len(list_)):
        try:
            if list_[i]==list_[i+1]:
                w += 1
            else:
                new_list_ += [w,list_[i]]
                w = 1
        except:
            new_list_ += [str(w),list_[i]]
            w = 1
    list_ = new_list_
    new_list_ = []
print('Итоговое число:',end=' ')
for i in list_:
    print(i,end='')
print()