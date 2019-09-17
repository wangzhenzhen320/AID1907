# 结论：倒序删除
list01 = [4, 54, 5, 6, 67, 17, 8]
for i in range(len(list01) - 1, -1, -1):
    if list01[i] % 2:
        del list01[i]
print(list01)

# 练习1:在控制台中循环录入字符串，如果录入空字符，则停止录入。
#      打印所有录入的内容。
list_input=[]
while True:
    str_input=input("请输入字符串：")
    if str_input==" ":
        break
    list_input.append(str_input)
str_input="_".join(list_input )
print(str_input)


#练习2
# 练习:将英文语句每个单词反转:
#  How are you  --> you are How
# 将字符串按照空格拆分为列表
# 将列表反转
# 将列表中元素拼接为字符串

message="How are you"
list_message=message.split(" ")
result="#".join(list_message[::-1])
print(result)


hobndoifsgjqag巴尔干人哈UR额合格报告【e
