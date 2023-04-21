# Datentypen & -strukturen

## 1. Numerische Typen

|   | Ganzzahlen - Integer | Gleitkommazahlen - Float | Komplexe Zahlen |
| ------------------- | ------------------- | ---------------- | --------------|
| | ```a = 20``` | ```b = 3.6``` | ```c = 5 + 2j```|
| kann zu ... konvertiert werden | float, complex | int, complex | |

*Hinweis: Konvertierung mittels int(b), complex(a),...*
```py
a = 3.14
b = complex(a)
c = int(a)
```

## 2. Texte- Strings

```py
string_a = "Hello"
```

+ eigentlich Liste von Buchstaben
+ Konkatenation:
  + string_a **+** string_b
  + nicht mit Zahlenwerten möglich!
+ Formatierung
  + nur Momentaufnahme, keine dauerhafte Änderung des Strings
  + Placeholder {} für Zahlenwert
    + string_c = "I am {} years old"
  + string_c.format(a)
+ viele Funktionen für Strings:

  ```py
  string_a.count("a")
  string_a.upper()
  ...
  ```

## 3. BOOLE'sche Werte

+ *True*  
  + 1 bzw ≠0
  + alle nicht leeren Strukturen
+ *False*
  + 0
  + leere Strukturen (Listen, Sets, Tupel,...)

*Hinweis:  ***bool(*** variable ***)*** gibt BOOLE'schen Wert einer Variable zurück*

## 4. Listen

```py
list = [ ]
```

+ änderbar, geordnet, mit Duplikaten
+ Zugriff:
  + ```list[ index ]```
+ Hinzufügen
  + am Ende: ```list.append(item)```
  + an bestimmter Stelle: ```list.insert(index, item)```
+ Entfernen
  + bestimmtes Element: ```list.remove(item)```
  + an bestimmter Stelle: ```list.pop(index)```*(mit Rückgabewert)* ODER ```del list[index]```
+ Bearbeiten
  + ```list[index]= item```
+ viele weitere Funktionen:
  + clear(), sort(), reverse(),...

```py
list = [1,2,3,4]
first = list[0]
last = list[3]
list.append(6)
list[4] = 5
```

## 5. Tupel

```py
tupel = ()
```

+ geordnet, nicht änderbar, mit Duplikaten
+ Zugriff:
  + ```tupel[index]```
+ Entpacken:

```py
tupel = (1,2,3) 
(a,b,c) = tupel
(x,y*) = tupel
```

*a ist erstes Tupelelement, b zweites,...*  
*y ist Liste der restlichen Elemente*

+ Bearbeiten:
  + nicht änderbar, daher Work-Around: Umwandlung in Liste

```py
tupel_list = list(tupel)
   #bearbeiten
tupel = tupel (tupel_list)
```

## 6. Sets

```py
set = {}
```

+ ungeordnet, Elemente nicht änderbar, keine Duplikate
+ Hinzufügen:
  + ```set.add(item)```
+ Entfernen:
  + ```set.remove(item)``` nur, wenn Element in Set
  + ```set.discard(item)``` egal, ob Element vorhanden oder nicht

## 7. Dictionary

```py
dict = { a : b}
```

+ Speicherung von Key-Value - Paaren
+ geordnet, änderbar, keine Duplikate
+ Zugriff:
  + ```dict[key]```
  + ```dict.get(key)``` 
+ Hinzufügen oder Bearbeiten:
  + je nachdem, ob der key bereits vorhanden ist oder nicht
  + ```dict[key] = value```
  + ```dict.update({ key : value })```
+ Entfernen
  + ```del dict[key]```
  + ```dict.pop(key)```
+ weitere Funktionen:
  + keys(), values(), ...


## Überblick zu Datenstrukturen

| | Liste | Tupel | Set | Dictionary |
|---|---|---|---|---|
| Initialisierung | list = [] | tupel = () | set = {} | dict = {} |
| Ordnung | ja | ja | nein | ja |
| Änderbarkeit | ja | nein | nein | ja |
| Duplikate | ja | ja | nein | nein | 

*Hinweis: geordnet/ ungeordnet bezieht sich auf eine feste Reihenfolge der Elemente innerhalb der Struktur, nicht auf eine Sortierung*

*Hinweis: änderbar/ nicht änderbar bezieht sich auf die Bearbeitung der Elemente, nicht der Datenstruktur selbst. Sets gelten als nicht änderbar, können aber bspw. um Elemente erweitert werden.*
  
----

## Aufgaben

### Zahlen

+ Schreibe ein Programm, dass zwei Zahlen addiert und ausgibt. Versuche auch die Datentypen int und float zu mischen, von welchem Datentyp ist das Ergebnis?

+ Schreibe ein Programm, dass zwei Gleitkommazahlen addiert und das Ergebnis als Ganzzahl ausgibt. Probiere ob du es gezielt schaffst die Zahl einmal abgerundet und einmal aufgerundet auszugeben. Recherchiere nach den passenden Funktionen.

### Strings

+ Schreibe ein Programm, dass zwei Strings konkateniert und ausgibt. Was passiert wenn man string1 += string2 berechnet und ausgeben lässt?

+ Definiere dir einen String und probiere aus, was die Funktionen count(), find(), split(), upper(), lower() tun!

count(“…“)
find(“…“)
split(“…“)
upper( )
lower( )

### Listen

+ Schreibe eine Liste und füge alle Module hinzu, die du in diesem Semester belegst. Gib danach das letze Modul aus, welches du der Liste hinzugefügt hast. Gib auch die Anzahl aller Listenelemente aus.

+ Erstelle eine Liste aus mindestens 4 verschieden Datentypen. Gib für 2 Listenelemente den Typ aus. Wie kannst du auf Listenelemente zugreifen?

### Sets

+ Versuche aus einer von dir neu angelegten oder bereits vorhanden Liste ein Set zu extrahieren. Worin besteht der Unterschied zu einer List?

+ Gebe dir die Anzahl an Einträgen des Sets aus, füge dann ein Element hinzu, welches schon vorhanden ist (recherchiere, wie das geht) und gib erneut die Länge aus, was passiert?
Füge nun ein neues Element hinzu, was beobachtest du jetzt?

### Tupel

+ Erstelle ein Tupel mit 3 Einträgen und versuche einen Eintrag zu verändern. Ist dies möglich? Was gibt der Interpreter aus? Erstelle nun ein Tupel ohne es mit Werten zu initialisieren, wie kann man das realisiren?

### Dictinary

+ Erstelle zunächst ein leeres Dictionary (Welche 2 Methoden kann man dafür anwenden? Gibt es eine, die "schöner" ist?). Füge dann 5 Vorlesungen sowie den Professor hinzu der diese hält. Gib für 2 Vorlesungen aus, von welchem Professor sie gehalten werden. 

+ Eine Lehrveranstaltung kann ab sofort von mehreren Professoren gehalten werden. Ändere das Dictionary entsprechend ab, welche Datenstruktur eignet sich zum Ablegen mehrerer Vorlesungen?

+ (Zusatz:) Finde raus wie man sich alle keys und alle values eines vorhanden Dictionarys ausgeben lassen kann und teste es an deinem eigenen Beispiel.
