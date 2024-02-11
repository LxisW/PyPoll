
# Eigenbewertung: Abstimmungsapp Projekt

## FACHKOMPETENZ (40 Punkte)

### Grundelemente der prozeduralen Programmierung (10 Punkte)
- **Algorithmenbeschreibung**: Die Implementierung des Abstimmungssystems erfordert logische Algorithmen, um Umfragedaten zu erstellen, abzurufen, und Stimmen zu zählen. Der `DatabaseHelper` und die Routen in `app.py` zeigen, wie Algorithmen verwendet wurden, um diese Operationen durchzuführen.
- **Datentypen**: Verwendung von Strings, Booleans, Integer-Werten und JSON für die Verarbeitung und Speicherung von Daten. Die Methoden innerhalb von `DatabaseHelper` demonstrieren den Umgang mit verschiedenen Datentypen.
- **E/A-Operationen und Dateiverarbeitung**: Die Verwendung von PostgreSQL für die Datenbankinteraktionen zeigt die E/A-Operationen. 
- **Operatoren**: Im Code finden sich zahlreiche Beispiele für die Verwendung von Operatoren, wie in den Abfragen und der Logik zur Stimmenzählung.
- **Kontrollstrukturen**: Verwendung von try-except für Fehlerbehandlung, if-else für Entscheidungsfindung.
- **Funktionen**: Der `DatabaseHelper` ist voll von Funktionen, die spezifische Aufgaben erfüllen, wie `get_poll_data`, `add_vote` usw.
- **Stringverarbeitung**: Stringverarbeitung findet in der Generierung von `admin_key` mit `uuid` und der Manipulation von JSON-Daten statt.
- **Strukturierte Datentypen**: Einsatz von Listen und Dictionaries in Methoden wie `get_votes`, um die Stimmen zu zählen und Daten zu organisieren.

### Syntax und Semantik von Python (10 Punkte)
- **Stolz**: Der `DatabaseHelper` ist ein gutes Beispiel für klaren, modularen Code, der die Syntax und Semantik von Python gut nutzt. Insbesondere die Methode `create_poll` zeigt, wie effektiv mit Daten umgegangen und Interaktionen mit der Datenbank durchgeführt werden können.

### Entwurf, Programmierung und Test eines größeren Programms (10 Punkte)
- **Teamarbeit**: Da das Projekt alleine durchgeführt wurde, zeigt dies die Fähigkeit, ein größeres System selbständig zu entwerfen, zu implementieren und auf Funktionsfähigkeit zu testen. Die Komplexität und der Umfang des Codes belegen dies.

### Datenstrukturen (10 Punkte)
- **Anwendung**: Die Verwendung von JSON zur Speicherung der Umfrageantworten in der Datenbank und Dictionaries zur Verarbeitung der Stimmen in der `get_votes`-Methode zeigt eine ausgezeichnete Anwendung von strukturierten Datenstrukturen.

## METHODENKOMPETENZ (10 Punkte)

### Entwicklungsumgebung (10 Punkte)
- **Tools**: TODO

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

Da ich das Projekt alleine gemacht habe, habe ich bei der Entwicklung meiner Abstimmungsapp die Möglichkeit genutzt, meine Fähigkeiten im selbstständigen Lernen und in der Problemlösung zu vertiefen. Die Herausforderung, das Projekt allein zu bewältigen, motivierte mich, neue Technologien und Konzepte zu erforschen.

Wesentlich für meinen Fortschritt waren die offiziellen Dokumentationen von Flask und PostgreSQL. Diese haben mir das nötige Fundament geboten, um die Anwendung zu strukturieren und effizient mit Daten zu arbeiten. Bei spezifischeren Herausforderungen half mir die Community auf Stack Overflow, praktische Lösungen und bewährte Methoden zu entdecken, die meine Entwicklungserfahrung bereicherten.

Online-Tutorials auf Youtube erweiterten mein Verständnis für das Datenbankdesign und die Benutzerinteraktion. Diese Tutorial ermöglichten es mir, neue Programmierstile von anderen zu sehen und an Ding zu denken, an die man zuvor noch nicht gedacht hatte.

Die selbständige Realisierung dieses Projekts hat mir nicht nur technische Kenntnisse vermittelt, sondern auch gezeigt, wie wertvoll Eigeninitiative und das Streben nach Wissen in der Softwareentwicklung sind. Diese Erfahrung stärkt mein Vertrauen in meine Fähigkeit, mich neuen Herausforderungen zu stellen und zukünftige Projekte erfolgreich zu meistern.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

TODO