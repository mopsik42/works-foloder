s_word=input("введите слово:")
s=""
for i in range(len(s_word)):
    s_num=ord(s_word[i])
    s_num=s_num+2
    s=s+chr(s_num)
print(s)
s_word=""
for i in range(len(s)):
    s_num=ord(s[i])
    s_num=s_num-2
    s_word=s_word+chr(s_num)
print(s_word)
    