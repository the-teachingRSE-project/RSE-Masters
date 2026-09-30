# Slide backlog — Responsible RSE (rwth_2026)

Ideas collected during the code walkthrough of `publications/rse_code_annotations`.
Deck: `folien-responsible-rse.qmd`. Build slides from here step by step, together.
Never state a fixed number of decorators — the set grows.

## Decorators (`rse_annotations/decorators/`)

- **Was ist ein Decorator?** `@functional` über `def f` = `f = functional(f)`.
  Läuft einmal, beim Import — nicht bei jedem Aufruf.
- **Definitionszeit vs. Aufrufzeit.** Import führt Code aus (anders als Java).
  Beim Import: Eintrag ins Register. Beim Aufruf: nichts Zusätzliches.
- **Was prüft Java, was Python?** Java-Annotationen sind reine Metadaten +
  Compiler-Prüfung; Python-Decorators sind ausführbare Funktionen.
- **Review Concerns.** Jeder Decorator markiert eine Stelle, an der das
  wissenschaftliche Ergebnis falsch werden kann (Mathematik, Umformung,
  Dateneingang, Datenausgang, …) — und sagt, worauf man prüfen soll.
- **AOP-Bild.** Concern = was prüfen; Join Point = die markierte Funktion;
  Aspekt = das Plugin, das prüft.
- **Ein neuer Decorator = eine Funktion + ein Eintrag in `DECORATORS`.**
  Single source of truth; Hilfetext = Docstring.

## Inspection (`rse_annotations/inspection/`)

- **Die Maschine schlägt vor, der Mensch entscheidet.** Quelltext + abgeleitete
  Formel zeigen → ja / nein / später.
- **Formel statt Implementierung lesen.** Eine Zeile Mathematik gegen die eigene
  Absicht prüfen. Gerendert, nicht bewiesen.
- **Review als Fakt im Repository.** `inspection.yaml` hält nur menschliche
  Urteile — "jemand hat das geprüft" wird nachvollziehbar.
- **Kein LLM prüft LLM-Code.** Bewusste Grenze des Werkzeugs.
- **Maschinelle Prüfung ≠ menschliches Urteil.** Automatische Checks (ist
  `@functional` wirklich rein? liest `@data_input` wirklich?) liefern Befunde;
  nur das Urteil eines Menschen wird als Verdict festgehalten. Beides getrennt
  halten — auch im Code.

## Core (`rse_annotations/core/`)

- **Ein Plugin = eine Responsible-RSE-Frage; das Framework bleibt gleich.**
  Lizenz, Dual Use, Footprint, … — jede Frage ist ein Plugin mit denselben
  Modi (Inspektion, Analyse, Testgenerierung). Neue Frage = neues Plugin,
  kein Umbau.

## Plugins (`rse_annotations/plugins/hazards/`)

- **Ein Plugin = eine Frage; Stub = Aufgabe.** Jede Responsible-RSE-Frage hat
  einen eigenen Ordner. Ein Stub ist ein Plugin ohne Implementierung; sein
  Docstring ist die Aufgabenstellung für Studierende.
- **Klassen sind Objekte.** Das Register ist ein Tupel von *Klassen*, nicht
  von Instanzen. Metadaten (`name`, `question`, `tier`) stehen als
  `ClassVar` an der Klasse — lesbar, ohne etwas zu instanziieren (Java:
  eher `static final` + `Class<?>`).
- **Nicht implementiert ≠ Fehler.** Ein Stub meldet `available() = False`
  und erscheint im Bericht als *skipped* mit Begründung — der Lauf bricht
  nicht ab, die Lücke bleibt sichtbar.

## Scan (`rse_annotations/scan/`)

- **Wie der Scan arbeitet (Aufrufreihenfolge).**
  1. `scan_path(root)`: alle `*.py`-Dateien finden (Tests, Caches, Vendored
     überspringen).
  2. Jede Datei mit `ast.parse` in einen Baum verwandeln — nichts wird
     importiert oder ausgeführt. Nicht parsebare Dateien werden notiert,
     nicht abgebrochen.
  3. Import-Aliase auflösen (`@f` aus `import functional as f` zählt als
     `@functional`).
  4. Jede Funktion besuchen: zählt sie mit (keine verschachtelten, Dunder-,
     `test_`-Funktionen)? Welcher Decorator steht dran? Falls keiner:
     Vorschlag aus der Form des Rumpfs. Welche Hazards?
  5. Nach allen Dateien: Hazards den Aufrufgraph hinauf vererben
     (wer eine LLM-Funktion aufruft, erbt `model_call`, markiert `indirect`);
     nie aufgerufene Validierungen markieren.
  6. Ergebnis: `CoverageReport` — Abdeckung + Kandidatenliste.
- **Vorschlag aus der Form des Rumpfs.** Liest *und* schreibt → aufteilen;
  schreibt → `@data_output`; liest → `@data_input`; nur Arithmetik →
  `@functional`; Eingabe rein, anderer Wert raus → `@mapping`; gibt nichts
  zurück → Glue-Code. Immer mit Konfidenz und Begründung — eine Arbeitsliste,
  kein Urteil.

## Refactoring-Lehrstücke (aus dem Walkthrough)

- **Magische Strings → ein Enum.** `"functional"` stand verstreut in Decorators,
  Scan, Plugins — ein Tippfehler fällt erst zur Laufzeit auf. Jetzt:
  `HazardDecorator.FUNCTIONAL`. Text nur noch an den Rändern: AST (Decorator-Name →
  `HazardDecorator(name)`), YAML, JSON. Python-Detail: `class HazardDecorator(str, Enum)` — ein
  Enum, das zugleich ein String ist, also direkt serialisierbar (Java: `enum`
  mit `name()`).
- **Komposition statt Vererbung.** Ein Hazard *verfeinert* einen Decorator
  (`statistical` → `@functional`), ist aber keine Unterklasse davon:
  `compute_dimension_icr` ist `@mapping` **und** `statistical`. Vererbung würde
  einen Widerspruch erzwingen. Darum: `HazardKind(parent=HazardDecorator.FUNCTIONAL)`
  — eine Referenz, keine Oberklasse. Zwei Achsen, unabhängig.
- **Strategy-Muster.** Jede `HazardKind` trägt ihren Detektor als Funktion
  (`detect=_detect_stochastic`). Neuer Hazard = eine Funktion + ein Eintrag in
  `HAZARD_KINDS` — dasselbe Prinzip wie bei `DECORATORS`. Die Tabellen
  (`HAZARDS`, `HAZARD_PARENT`, …) werden daraus *abgeleitet*, nie von Hand
  gepflegt.
- **Vokabular getrennt von Logik.** Welche Namen als Evidenz zählen
  (`openai`, `shuffle`, `cohen_kappa_score`, …) steht in `scan/vocabulary.py`
  — reine Daten. Neue Bibliothek beibringen = Liste erweitern, Code bleibt
  unverändert. Die Heuristik wird damit prüfbar: man sieht, *woran* der Scan
  glaubt.
- **Ein Test hält die Quellen synchron.** `HazardDecorator` und `DECORATORS` müssen
  dieselben Namen tragen — ein Test prüft das, statt es zu hoffen.
