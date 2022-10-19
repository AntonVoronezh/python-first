f = open('file.txt', 'a', encoding='utf-8')
# text = f.read(2)
# text2 = f.read(3)
# f.write('77777 \n')
# text3 = f.read()


# print(text)
# print(text2)
# print(text3)


aa = ['qqqqq', 'hhhhhh']
# for i in aa:
#     f.write(i + '\n')
f.writelines(f'{i} \n' for i in aa)
f.close()




# f2 = open('file.txt', 'r', encoding='utf-8')
# for i in f2:
#     print(i)
# f2.close()

f3 = open('file.txt', 'r', encoding='utf-8')
ddd = f3.readlines()
f3.close()
print(ddd)