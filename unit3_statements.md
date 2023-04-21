# Kontrollfluss - Statements

## 1. IF-Statement

+ bedingte Codeausführung

```py
if  condition1  :   
  statementA           #nur ausgeführt, wenn condition1 == True 
elif condition2 :    
  statementB           #wenn condition1 == False and condition2 == True
else :      
  statementC           #wenn condition1 == False und condition2 == False
```

*auch ohne **elif** oder **else**-Zweig*


## 2. WHILE-Statement

+ wiederholte Codeausführung
+ geknüpft an Bedingung

```py
while condition :
    statement       #ausgeführt, solange condition == True
    break
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*


## 3. For-Statement

+ wiederholte Codeausführung
+ iterierend über Datenstruktur

```py
for x in interable:
    statement       #für jedes x in Interable ausgeführt
    continue
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*

## 4. Match-Statement

+ selektive Codeausführung
+ Fallunterscheidung nach wert einer Variablen

```python3
match variable:
    case case1:
        statement1
    case case2:
        statement2
    ...
```

same as:

```py
if variable == case1 :
    statement1
elif variable == case2 :
    statement2
elif ...
```
