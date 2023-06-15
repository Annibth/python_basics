# Objektorientierte Programmierung

## Was ist Objektorientierte Programmierung

- Programmierparadigma
- basierend auf Objektorientierung:
  - Abstraktion komplexer Systeme
    - Zusammenspiel von Objekten
    - dementsprechende Architektur der Software

Beispiel:


## Konzepte der Objektorientierung

### Klassen

- auch Objekttyp genannt
- Blaupausen für ähnliche Objekte
  - Attribute = Eigenschaften
    - können wiederum Objekte sein
  - Methoden = Verhaltensweisen
- __init__()- Funktion:
  - Erzeugung von Objekten
  - "Konstruktor"
  - automatisch beim Erstellen eines Objektes aufgerufen
  - legt Attribute fest, die eine Instanz dieser Klasse hat

Definition:
```py
class ClassName: 
    def __init__(self, attribute1, attribute2):
        #Attribute der Klasse
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    #Methode
    def change_attribut1(self, argument1):
        self.attribute1 = argument1
        return
```

### Objekte

- konkrete Instanzen von Klassen
- haben bestimmten Zustand
  - Eigenschaften nehmen konkrete Werte an
- werden zur Laufzeit erzeugt

```py
#Erstellen eines neuen Objekts mitt den Attributen A (attribute1) und B (attribute2)
object1 = ClassName("A", "B")

#Aufrufen einer Funktion auf dem Objekt
objekt1.change_attribute1("C")
```

***Achtung*** 
- Instanzen einer Klasse können im Kontrollfluss erst nach der Definition der entsprechenden Klasse erzeugt werden.

- Ist ein Attribut wiederum ein Objekt & die Parameter der __init__() Funktion typisiert, muss die Klasse, die den Typ des "Objekt- Attributs" festlegt im Kontrollfluss vorher definiert werden.
*Beispiel:*

```py
# Funktioniert nicht:
class A:
    def __init__(self, attributB:B):
        self.attributB = attributB

class B: 
    def __init__(self) ->None :
        pass
```

```py
#Funktioniert:
class B: 
    def __init__(self) ->None :
        pass

class A:
    def __init__(self, attributB:B):
        self.attributB = attributB
```

### Vererbung