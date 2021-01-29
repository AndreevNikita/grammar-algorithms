# Андреев Никита и Киличева Дилфуза
# нетерминальные символы и терминальный символ
non_terminals = ["S", "B", "A", "AP",  
                  "Adv", "C"] 
terminals = ["if ****: \n", "string\n", "print(****)",  
             "for ****:\n", "import os\n",  
             "\t", "\t\t"] 
  
# грамматика (grammar) 
R = { 
     "NP": [["Det", "Nom"]], 
     "Nom": [["AP", "Nom"], ['print(****)'],  
             ['        string\n']], 
     "AP": [["Adv", "A"], ['    if ****:\n'],  
            ['        string\n']], 
     "Det": [['import os\n']], 
     "Adv": [['for ****:\n']], 
     "A": [['    if ****:\n'], ['        string\n'], ['print(****)']] 
    }



# Функция алгоритма CYK
def cyk(w): 
    n = len(w) 
      
    # Инициализация таблицы
    T = [[set([]) for j in range(n)] for i in range(n)] 
  
    # Заполнение таблицы
    for j in range(0, n): 
  
        # правила
        for lhs, rule in R.items(): 
            for rhs in rule: 
                  
                # терминал найден, добавляется терминал
                if len(rhs) == 1 and rhs[0] == w[j]: 
                    T[j][j].add(lhs) 
  
        for i in range(j, -1, -1):    
               
            for k in range(i, j + 1):      

                for lhs, rule in R.items(): 
                    for rhs in rule: 
                          
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]: 
                            T[i][j].add(lhs) 
    print(T)
  
    # если текст совпадает с правилами которые задали то будет True 
    print(T[0][n-1])
    if len(T[0][n-1]) != 0: 
        print("True") 
        
    else: 
        print("False") 
    
  
# читаем файл, задаваемый текст 
w = []
with open('text.txt', 'r') as inf:
    for line in inf:
        w.append(line)
  
# вызов функции 
cyk(w) 
