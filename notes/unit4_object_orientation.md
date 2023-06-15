# Objektorientierte Programmierung

## Was ist Objektorientierte Programmierung

- Programmierparadigma
- basierend auf Objektorientierung:
  - Abstraktion komplexer Systeme
    - Zusammenspiel von Objekten
    - dementsprechende Architektur der Software

*Beispiel:
Im Straßenverkehr agieren (mehr oder weniger kooperativ) Autos, Fahrradfahrer und Fußgänger miteinander. Diese bilden sogenannte Klassen und haben bestimmte Attribute und Funktionen. Die Klasse Auto hat  die Attribute Farbe und Marke und die Funktionalitäten Fahren oder Bremsen, Blinken oder weitere. Der Fußgänger hat hingegen die Attribute Alter, Schuhgröße und Haarfarbe und die Verhaltenweisen Gehen und Reden.

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

----

## Aufgaben

1. Definiere eine Klasse "Bankkonto". Diese Klasse soll folgende Funktionalitäten erfüllen:
  + bei der Initialisierung eines Accounts soll jeweils Vorname, Nachname und initiales Vermögen eines Anlegers spezifiziert werden können 
  + es soll Funktionen geben, welche den Namen des Kontoinhabers sowie den aktuellen Kontostand zurückgeben
  + es soll Funktionen für mögliche Transaktionen (Ein- und Auszahlung) geben, dabei sollte stets geprüft und zurückgegeben werden, ob eine Transaktion gültig ist:
    + ein negativer Kontostand darf nie entstehen
    + ab Einzahlungen von mehr als 15000 Geldeinheiten erhebt die Bank einen Bearbeitungszins von 1%, dieser soll vom Transaktionsbetrag abgezogen werden
    + nichtpositive Einzahlungen sollen einen Error werfen
  + das Konto soll auf Wunsch aktiviert und deaktiviert werden können
  + wenn man einen print() auf ein Bankkonto-Objekt aufruft soll folgende Ausgabe erscheinen: "Das ist das Bankkonto von {Vorname} {Nachname}."