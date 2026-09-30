# Slide backlog — Einen Hazard von Hand bauen (up_2026)

Ideas from the walkthrough "add `hardware_dependency` by hand, step by step".
Deck: `folien-rse-annotations.qmd` (new section after "Refactoring-Lehrstücke").
The hazard is coded manually, not generated — the slides follow the same steps.

## Motivation

- **Die Hardware ist Teil der Methode.** Code, der eine GPU voraussetzt, läuft auf
  dem Laptop der Gutachterin nicht — oder anders (Fließkomma, cuDNN-Nichtdeterminismus).
  Ein Paper, das die Hardware nicht nennt, ist so nicht reproduzierbar.
- **Beispiel:** zwei kleine Tensoren auf `/GPU:0` addieren. Ohne GPU scheitert
  TensorFlow — gut so: lieber laut scheitern als still auf die CPU ausweichen.

## Schritte

1. Zielcode schreiben: das Beispiel, das erkannt werden soll
   (`examples/gpu_tensors.py`). Der Scanner importiert nie — TensorFlow muss für die
   Erkennung nicht installiert sein.
2. Vorher: `python -m rse_annotations examples --coverage` — `gpu_tensors.py` taucht auf,
   aber ohne Hazard. Folie: Screenshot *vorher* (später gegen *nachher* stellen).
3. Neuer Decorator `@hardware_dependency` in `decorators/markers.py`: **eine Funktion**,
   markiert mit `@_concern`, der Docstring ist der Hilfetext. Mehr nicht — Enum-Member
   (`HazardDecorator.HARDWARE_DEPENDENCY`), Export aus `rse_annotations` und Erkennung
   durch den Scanner ergeben sich daraus.
   Folie: **Nicht jede Gefahr ist erkennbar — manche muss man erklären.** Ob Code eine GPU
   braucht, sieht man dem AST nicht zuverlässig an (Gerät aus Config, Umgebungsvariable,
   Bibliothek wählt still). Die Verantwortung liegt bei der Person, die den Code schreibt:
   sie *markiert* die Abhängigkeit. Gegenüberstellung: *erkannte* Hazards (`stochastic`,
   `model_call`) vs. *deklarierte* Hazards (`hardware_dependency`).
4. Zielcode markieren: `@hardware_dependency` über `def add_on_gpu`
   (`from rse_annotations import hardware_dependency`).
5. Nachher: `python -m rse_annotations examples --coverage` — neue Zeile
   `@hardware_dependency 1`, `gpu_tensors.py` zu 100 % abgedeckt. Folie: *vorher* | *nachher*
   nebeneinander.

## Folie: Das Decorator-Muster

- **In Python:** `@hardware_dependency` über `def add_on_gpu` ist nur Kurzschrift für
  `add_on_gpu = hardware_dependency(add_on_gpu)`. Ein Decorator ist eine Funktion, die eine
  Funktion bekommt und eine Funktion zurückgibt.
- **Zwei Arten:**
  - *Markierender* Decorator (unser Fall): hängt Metadaten an (`fn.__rse_decorator__`),
    trägt sie in ein Register ein und gibt die Funktion **unverändert** zurück — kein
    Laufzeit-Overhead, darf im Produktivcode bleiben.
  - *Umhüllender* Decorator: gibt eine neue Funktion zurück, die vor/nach dem Aufruf etwas
    tut (Logging, Zeitmessung, Caching — `functools.lru_cache`, `functools.wraps`).
- **Mit und ohne Argumente:** `@data_input` und `@data_input(fields=...)` funktionieren
  beide. Trick in `_mark`: kommt keine Funktion (`fn is None`), wird ein Decorator
  zurückgegeben, der auf die Funktion wartet.
- **Selbstregistrierung:** `@_concern` ist selbst ein (markierender) Decorator — er trägt
  jede Decorator-Funktion in eine Liste ein. Alles andere (Enum, Hilfetexte, Exporte) wird
  daraus abgeleitet: *eine* Stelle für eine neue Rolle. Dasselbe Idiom wie `@app.route` in
  Flask oder `@pytest.fixture`.
- **Bezug zum GoF-Decorator** (Gamma et al. 1994): dort umhüllt ein Objekt ein anderes mit
  derselben Schnittstelle, um Verhalten hinzuzufügen. Python-Decorators sind verwandt,
  aber allgemeiner (sie dürfen auch nur markieren).
- **Bezug zu AOP** (Folie *Querschnittsbelange*, erstes Deck): der Decorator ist der
  *Join Point*, den die Autorin selbst setzt; die Prüfungen der Plugins sind der *Advice*.
- Code-Beispiel für die Folie: `_concern`, `_mark` und `hardware_dependency` aus
  `decorators/markers.py`.
