# Kontrollfluss - Statements & Funktionen

## Statements

### 1. IF-Statement

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

### 2. WHILE-Statement

+ wiederholte Codeausführung
+ geknüpft an Bedingung

```py
while condition :
    statement       #ausgeführt, solange condition == True
    break
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*

### 3. For-Statement

+ wiederholte Codeausführung
+ iterierend über Datenstruktur

```py
for x in interable:
    statement       #für jedes x in Interable ausgeführt
    continue
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*

### 4. Match-Statement

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

## Funktionen

+ Auslagerung von Code mit gleicher Funktion
+ wird nur ausgeführt, wenn die Funktion aufgerufen wird
+ zweiseitig:
  + Definition:
    + Name, Parameter, Code, Rückgabewert
  + Aufruf:
    + Argumente

### Definition

```py
def function_name(parameter1, parameter2):
    #code follows, using parameter1 and parameter2 as variables
    return #can return a value
```

+ Funktionskopf:
  + keyword ***def***
  + Funktionsname *function_name*
    + eindeutige Identifikation der Funktion
    + mit diesem wird aufgerufen
  + Parameter:
    + in Klammern hinter dem Funktionsnamen
    + Typzuweisung möglich ```parameter1:int```
+ Code, der die Methode implementiert
  + abhängig von Parametern
+ Rückgabe:
  + Wert steht hinter ***return*** Keyword
  + nur ein Wert
  + Typisierung möglich
    + direkt hinter Kopf der Funktion
```py
def funtion_name() -> int :
  return 3
```

### Aufruf

+ mittels Funktionsname
+ Übergabe der Parameter nach Definition
  + Art der Identifikation
    + *siehe Tabelle 1*
  + Anzahl zu übergebender Parameter muss der in der Definition festgelegten Anzahl entsprechen
+ Rückgabewert in Variable speichern (sofern er weiterverwendet werden soll)
```py
def sum_of(a:int, b:int ) ->int :
  return a+b

c = sum_of(3,4)
```

*Tabelle 1:*
| Reihenfolge | Key_Value |
| --- | --- |
| Übergabereihenfolge der Argumente legt fest, welcher Parameter der Funktion welchen Wert annimmt  | - Wertzuweisung erfolgt über die Bezeichnung des Parameters |
| ertser Parameter = erstes Argument, ... | Parameter enspricht immer dem Wert er ihm bei Funktionsaufruf per Wertzuweisung zugeordnet wird |
| *Beispiel A* | *Beispiel B* |

*Beispiel A:*
```py
  def function(a,b,c):
    return
    
  functon("!" , "?" , "#" )
  #a entspricht "!", b entspricht "?", c entspricht "#"
```
*Beispiel B:*
```py
   def function(a,b,c):
    return
  
  function(c = "?", b = "!", a = "#")
  #a wird "#" zugewiesen, egal in welcher Reihenfolge die Parameter übergeben werden
```

## Zusatz:
Je nach Anwendung kann es sein, dass **nicht von vornherein bekannt** ist, **wie viele Parameter** der Funktion übergeben werden. Abhängig von der Zuweisung zwischen Parametern und Argumenten (Reihenfolge oder Key-Value) kann man dann folgende Syntax verwenden:

### Identifikaton mittels Reihenfolge - *args

  + Übergabe eines Tupels von Parametern
    + müssen entsprechend behandelt werden ([unit_2](unit2_types_collections.md))

```py
def functon_a(*args):
  for arg in args:
    continue
  return
```

```py
  function_a(1,2,3,4,5)
```
funktioniert ebenso wie:
```py 
  function(1,2)
```

### Identifikation mittels Key-Value - **kwargs

+ Übergabe eines Dictionarys ([unit_2](unit2_types_collections.md)) von
  + Key = jeweilige Bezeichnung des Parameters
  + Value = Wert dieses Parameters

```py
def functon_b(**kwargs):
  return
```

```py
function_b(a=1, b=2, c=3, d=4, e=5, f=6)
```
*kwargs.keys() würde in der Funktion (a,b,c,d,e,f) zurückgeben, kwargs.values() gibt (1,2,3,4,5,6) zurück*

funktioniert ebenso wie:
```py
function_b(a=2, b=4, c=6)
```
*kwargs.keys() würde also (a,b,c) zurückgeben, kwargs.values() gibt (2,4,6) zurück*

----

## Aufgaben

1. Lege dir eine Liste mit mindestens 5 Strings an. Iteriere danach über die Liste und füge an jedes String Element ein "!" an. Lass dir danach die Liste ausgeben. 

2. Erstelle eine Liste von Integer/Float Werten. Berechne den Mittelwert der in der Liste enthaltenen Elemente und gib diesen aus. Caste den Mittelwert zu einem Integer und prüfe ob das resultierende Ergebnis gerade oder ungerade ist. 

3. Benutze das "match"-Statement und schreibe ein Programm, welches prüft ob ein gegebener Integer Wert gerade oder ungerade ist. Je nach Fall soll ein entsprechender String ausgegeben werden.

4. Schreibe ein Programm, was die ersten 100 Primzahlen ausgibt. Du kannst dabei folgende Funktion verwenden: 
```python
def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(1, (n ** 0.5)+1):
        if n%i == 0:
            return False
        else:
            return True
```

5. Schreibe eine Funktion, welche einen String als Argument bekommt und für diese beurteilt, ob es sich um ein Palindrom handelt. z.B. sollte die Funktion für "Anna" den Wert True und für "Elia" den Wert "False" zurückgeben.

6. Implementiere eine lineare Suche. Bei der linearen Suche wird ein Array mit Werten nach einem bestimmten Wert durchsucht. Wenn der gesucht Wert gefunden wurde gib den Index zurück, an welchem sich der Wert befindet. __Hinweis:__ Die Funktion enumerate() kann helfen, was macht sie?

7. __(Zusatz - schwer):__ Recherchiere, wie die binäre Suche funktioniert. Implementiere eine Funktion, welches die Liste [2,1,5,6,3,8,9,3,2,5,6,1] durchsucht und den Index zurückgibt, an dem das Element 6 auftaucht. Was sind Anforderungen an die Liste vor Beginn der Suche?