# Add-Ons


## List-Sort

- ***sort()***
- alphanumerisch
  - Text: alphabetisch
  - Zahlen: numerisch, aufsteigend
- ***sort(reverse = True)***
  - umgekehrte Sortierung
- angepasste Sortierung
  - zusätzlich Funktion implementier
  - Rückgabewert = Kriterium der Sortierung
  - ***sort(key =*** *function* ***)***
  - 
```py
my_list = ["Apfel", "Banane", "Kiwi", "Wassermelone", "mango"]

#alphabetische Sortierung
my_list.sort()

#umgekehrte Sortierung
my_list.sort(reverse = True)

#Funktion, anhand der sortiert werden soll
def sort_func(s):
  if s[0] == "A":
    return ""
  else:
    return s

my_list.sort(key = sort_func)
```

## List-Comprehension

- erstellen einer neuen Liste anhand einer bestehenden
  - Filtern der bestehenden Liste
    - nur Elemente,die Bedingung erfüllen
  - Modifikation der Listenelemente
    - alte Liste unverändert
- kürzere Syntax (oneliner)


```py
old_list = ["Apfel", "Banane", "Kiwi", "Wassermelone", "mango"]
new_list = list()
for x in old_list:
    if x[0].isupper():
        new_list.append(x + "!")
```

wird zu:

```py
old_list = ["Apfel", "Banane", "Kiwi", "Wassermelone", "mango"]
new_list = [x+"!" for x in old_list if x[0].isupper()]
```

## Lambda

- anonyme Funktion
  - keinen Namen
  - temporär
- beliebig viele Argumente aber nur einen Rückgabewert
- Verwendung:
  - Funktionen höherer Ordnung
    - Funktionen, die Funktionen als Argumente erhalten
    - zB: map(), filter(), fold(),sort(),...
  - list-Comprehension
  - ...

```py
#die Funktion gibt immer der Wert einer Zahl um zwei vergrößert zurück
lambda a: a+2

my_list.sort(key = lambda a: a[len(a)-1] )

new_list = [(lambda x: x+"!")(x) for x in my_list if x[0].isupper]
```

### map()

- modifiziert jeden Wert einer gegebenen Datenstruktur anhand einer Funktion
- Argumente:
  - Funktion *(Wie werden die Elemente modifiziert?)*
  - Datenstruktur *(Welche Datenstruktur dient als Grundlage?)*
- Rückgabe:
  - map einer neuen Datenstruktur
    - Typ muss spezifiziert werden
- ***map(*** *function*, *iterable* ***)***

```py
list1 = [2,3,4,5]
list2= list(map(lambda a: a*2, list1))
print(list2)
```

### filter()

- prüft jedes Element auf eine bestimmte Bedingung
- Argumente:
  - Funktion *(Welche Bedingung muss jedes Element erfüllen?)*
  - Datenstruktur *(Was wird gefiltert?)*
    - (Listen, Tupel, Sets, ...)
- Rückgabe:
  - neue, gefilterte Datenstruktur
    - Typ mus spezifiziert werden
- ***filter(*** *function & condition*, *iterable* ***)***

```py
list1 = [2,3,4,5]
list2= list(filter(lambda a: a%2 == 0, list1))
print(list2)
```

### reduce()

- evaluiert gesamte Datenstruktur zu einem Wert
  - immer die ersten beiden Elemente
  - anhand einer gegebenen Funktion
- Argumente:
  - Funktion *(Wie werden ie Elemente verknüpft?)*
    - zweistellig
  - Datenstruktur *(Welche Datenstruktur liegt zugrunde?)*
- Rückgabe:
  - einzelner Wert
- ***reduce(*** *function*, *iterable* ***)***

*Hinweis: Für die Funktion Reduce() muss das Package **functools** importiert werden. *
```py
import functools 

list1 = [2,3,4,5]
value = functools.reduce(lambda a,b: a+b == 1, list1)
print(list2)
```
