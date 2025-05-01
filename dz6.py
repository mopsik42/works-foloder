predl=input("введите предложение:")
predl.find(input("введите слово которое нужно найти:"))
nyjnoe_word=predl[predl-1]  
start_index=predl.find(nyjnoe_word)
end_index=predl.find(nyjnoe_word)-1
print(f"начало слова {start_index} конец слова {end_index}")
  