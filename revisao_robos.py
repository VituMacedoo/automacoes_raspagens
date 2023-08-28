#!/usr/bin/env python
# coding: utf-8

# # Revisão pyautogui

# In[24]:


get_ipython().system('pip install pyautogui')


# In[25]:


import pyautogui as py


# In[27]:


py.sleep(2)
#print(py.position())


# In[32]:


py.moveTo(x=719, y=1049)
py.click(x=719, y=1049)


# In[33]:


py.sleep(4)
#print(py.position())
py.click(x=736, y=143)
py.typewrite("Chrome")
py.press("enter")


# In[34]:


py.typewrite("valor dolar")
py.press("enter")
py.sleep(5)


# Abrindo programas com o executar

# In[58]:


#Função hotkey(atalhos)
#abre o executar
py.hotkey("win", "r")

#digita o programa
py.typewrite("notepad")

#tempo de descanso
py.sleep(2)

#confirma
py.press("enter")

py.sleep(2)

#escreve
py.typewrite("Vitor Macedo")

#salvando
py.hotkey("ctrl", "s")
py.sleep(5)

#saindo das duas confirmaçoes
py.press("enter")
py.sleep(5)
py.press("enter")
py.sleep(2)

#fechando a janela
#getActiveWindow permite reconhecer a janela que está aberta
janela = py.getActiveWindow()
py.sleep(2)
janela.close()

#espera
py.sleep(5)


# Criando CheckBoxes

# In[63]:


opcao = py.confirm("Clique no botao desejado: ", buttons = ["Word","Excel","Notepad"])

#abre o executar
py.hotkey("win", "r")
if opcao == "Notepad":
    #digita o programa
    py.typewrite("notepad")

    #tempo de descanso
    py.sleep(2)

    #confirma
    py.press("enter")

    py.sleep(2)

    #escreve
    py.typewrite("Digitando no notepad!")

    #salvando
    py.hotkey("ctrl", "s")
    py.sleep(5)
    py.press("enter")
    
elif opcao == "Word":
    #digita o programa
    py.typewrite("Word")

    #tempo de descanso
    py.sleep(2)

    #confirma
    py.press("enter")
    py.sleep(2)
    
    #caixa de seleçao - documento em branco
    py.press("enter")
    py.sleep(2)

    #escreve
    py.typewrite("Digitando no word!")

    #salvando
    py.hotkey("ctrl", "b")
    py.sleep(5)
    
    py.press("enter")
elif opcao == "Excel":
    #digita o programa
    py.typewrite("Excel")

    #tempo de descanso
    py.sleep(2)

    #confirma
    py.press("enter")
    py.sleep(2)
    
    #caixa de seleçao - documento em branco
    py.press("enter")
    py.sleep(2)


    #escreve
    py.typewrite("Digitando no excel!")
    py.sleep(2)

    #salvando
    py.hotkey("ctrl", "b")
    py.sleep(5)
    
    py.press("enter")
    
    
    

