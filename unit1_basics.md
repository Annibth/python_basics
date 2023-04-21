# Python

## Über Python

+ Scriptsprache
  + Interpreter 
    + Zeile für Zeile übersetzung des Script in Binärcode
    + langsamer
  + dynamische Typisierung
    + Interpreter schließt selbst auf Typ einer Variable
    + Typ im Verlauf des Programmes änderbar
+ reduzierte Syntax
  + nah an englischer Sprache
  + leicht zu lernen 
    + einsteigergeeignet - erste Kontakte mit Programmierung, Programmierparadigmen
+ direkt, unkompliziert, einfach aber mächtig
  + perfekt für schnelles Prototyping
  + verwendung in Webentwicklung, Data Science, Machine Learning, ...


## Arbeit mit Python

### 1. Interaktiver Modus

+ direkte Interaktion mit Interpreter in Kommandozeile
+ REPL = Read Evaluate Print Loop
+ testen kleiner Codestücke
+ nicht persistent (keine Wiederverwendung möglich)

1. **Starten:** Kommandozeilenbefehl: 
```zsh
$ python3
```
2. **Arbeiten:** Code direkt im Terminal schreiben (Zeilenumbruch = SHift + Enter)
3. **Beenden:** "exit()" + Enter


### 2. Ausführen von Dateien

+ Trennung von Bearbeitung und Ausführung
+ persistent

1. **Schreiben** des Codes in IDE oder Editor
2. **Speichern** als .py Datei (zB.: hello_world.py)
3. **Ausführen:**
  + Navigation in korrektes Verzeichnis
  + Kommandozeilenbefehl:
  ```zsh
  $ python3 *datei_name.py* 
  ```

## Syntax

+ Kontrollfluss durch Einrückung strukturiert
  + weitgehend ohne Semikolons, Klammerung
  + Grad der Einrückung definiert Blöcke/ Scopes
+ Kommentare
  + einzeilig: ***#*** Kommentar
  + mehrzeilig: ***"""*** ... ***"""***

## Variablen

+ repräsentieren Werte im Speicher
+ Name:
  + eindeutig
  + ermöglicht Zugriff
  + A-Z, a-z, _
    + PascalCase: SomeUselessVariableName
    + camelCase: someUselessVariableName
    + snake_case: some_useless_variable_name
+ Typ:
  + dynamisch, änderbar
  + mit ***type(*** _varName_ ***)*** bekommt man den Typ der entsprechenden Variable
