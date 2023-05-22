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
---

## Aufgaben

### Sortierung & Comprehension

1. Lege dir eine Liste von Strings an. Schreibe nun Funktionen um folgende (aufsteigende) Sortierungen auf Listen durchzuführen: 
  + sortiere die Liste nach der Länge der Strings
  + sortiere die Strings nach der alphabetischen Reihenfolge ihrer letzten Buchstaben 
  + sortiere die Strings nach der alphabetischen Reihenfolge des mittleren Buchstabens
  + sortiere die Strings nach der Reihenfolge ihrer Hashwerte, nutzte dabei die hash(s:str) -> int Funktion um den Hash zu berechnen

2. Lege eine Liste von Paaren an, wobei jedes Paar aus zwei Zahlenwerten bestehen soll. Sortiere die Liste absteigend nach den Zahlenwerten des zweiten Tupeleintrags. 

3. Erstelle dir zunächst eine Liste von Personen. Jede Person wird durch ein Tupel repräsentiert, welches Name (String), Alter(Integer) und den Besitz eines Haustiers (bool) enthält.
  - erstelle dir eine neue Liste, die alle volljährigen Personen beinhaltet.
  - erstelle eine weitere Liste, die die Namen aller Personen enthält, die Haustiere besitzen.

### Lambda-Funktionen

1. Lege dir eine Liste von Integern an und definiere folgende Funktionen als Lambda-Funktion um sie mit map() auf deiner Liste anzuwenden:
  + berechne die Quadratwurzel jeder einzelnen Zahl
  + berechne die Dreierpotenz jeder Zahl 
  + inkrementiere die Zahl um ihr Doppeltes
  + subtrahiere von der Zahl ihre Quersumme

2. Schreibe eine Liste von beliebigen Zahlen (float & int) und berechne die Summe über alle Zahlen indem du die reduce() Funktion aus dem functools package nutzt. 

3. Erzeuge eine Liste mit zufälligen Integern (importiere dazu das modul random und nutze value = random.randint(upper, lower) um einen randomisierten Integer im Intervall [upper. lower] zu erhalten) und filtere diese Liste nach Elementen, welche gerade sind. Probiere das gleiche auch für das Filtern nach ungeraden Einträgen. 