
# Bewertung: Abstimmungsapp Projekt

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
- Der `DatabaseHelper` ist ein gutes Beispiel für klaren, modularen Code, der die Syntax und Semantik von Python gut nutzt. Insbesondere die Methode `create_poll` zeigt, wie effektiv mit Daten umgegangen und Interaktionen mit der Datenbank durchgeführt werden können.

### Entwurf, Programmierung und Test eines größeren Programms (10 Punkte)
- **Teamarbeit**: Da das Projekt alleine durchgeführt wurde, zeigt dies die Fähigkeit, ein größeres System selbständig zu entwerfen, zu implementieren und auf Funktionsfähigkeit zu testen. Die Komplexität und der Umfang des Codes belegen dies.

### Datenstrukturen (10 Punkte)
- **Anwendung**: Die Verwendung von JSON zur Speicherung der Umfrageantworten in der Datenbank und Dictionaries zur Verarbeitung der Stimmen in der `get_votes`-Methode zeigt eine ausgezeichnete Anwendung von strukturierten Datenstrukturen.

## METHODENKOMPETENZ (10 Punkte)

### Entwicklungsumgebung (10 Punkte)
- **Visual Studio Code with Theme and Extensions**: ![Visual Studio Code](https://github.com/LxisW/PyPoll/blob/main/images/vsc.png)
- **Git**: Einsatz von Git für Versionskontrolle und Fehlermanagement ![GIT](https://github.com/LxisW/PyPoll/blob/main/images/git.png) 
- **ChatGPT**: Benutzung von ChatGPT zur Verberssung und Strukutrierung des selbstgeschriebenen Codes ![ChatGPT](https://github.com/LxisW/PyPoll/blob/main/images/chatgpt.png)



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Da ich das Projekt alleine gemacht habe, konnte ich niemandem aus der Gruppe helfen.

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
Die Bewertung des anderen Projektes, in meinem Fall TimeTheFreeze kann man [hier](https://github.com/LxisW/PyPoll/blob/main/grading_time_the_freeze.md) finden.

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->
Da ich das Projekt alleine gemacht habe, habe ich bei der Entwicklung meiner Abstimmungsapp die Möglichkeit genutzt, meine Fähigkeiten im selbstständigen Lernen und in der Problemlösung zu vertiefen. Die Herausforderung, das Projekt allein zu bewältigen, motivierte mich, neue Technologien und Konzepte zu erforschen.

Wesentlich für meinen Fortschritt waren die offiziellen Dokumentationen von Flask und PostgreSQL. Diese haben mir das nötige Fundament geboten, um die Anwendung zu strukturieren und effizient mit Daten zu arbeiten. Bei spezifischeren Herausforderungen half mir die Community auf Stack Overflow, praktische Lösungen und bewährte Methoden zu entdecken, die meine Entwicklungserfahrung bereicherten.

Online-Tutorials auf Youtube erweiterten mein Verständnis für das Datenbankdesign und die Benutzerinteraktion. Diese Tutorial ermöglichten es mir, neue Programmierstile von anderen zu sehen und an Dinge zu denken, an die ich zuvor noch nicht gedacht hatte.

Die selbständige Realisierung dieses Projekts hat mir nicht nur technische Kenntnisse vermittelt, sondern auch gezeigt, wie wertvoll Eigeninitiative und das Streben nach Wissen in der Softwareentwicklung sind. Diese Erfahrung stärkt mein Vertrauen in meine Fähigkeit, mich neuen Herausforderungen zu stellen und zukünftige Projekte erfolgreich zu meistern.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
Selbstständige Projektumsetzung: Ich habe das Projekt von der Idee bis zur Realisierung alleine umgesetzt. Dieser Prozess hat mir gezeigt, dass ich auch komplexe Probleme, wie zum Beispiel eine Datenbankverbindung mit Flask, eigenständig lösen kann.

Flexibilität bei der Code-Entwicklung: Besonders erwähnenswert finde ich die Anpassung des Codes für die Integration neuer Funktionen, wie z.B. die Entscheidung über mehrfache Stimmen pro IP oder der Admin-Key. Dies erforderte bedeutsame Änderungen am bestehenden Code, was mir eine flexible und problemlösungsorientierte Arbeitsweise abverlangte.

Herausforderungen:

Ursprüngliche Projektplanung: Anfangs war mir unklar, welchen Umfang ich in der vorgegebenen Zeit bewältigen konnte. Dies führte zu mehrfachen Anpassungen des Projektplans für die Integration neuer Features. Die Erfahrung lehrte mich, zukünftige Projekte mit einem breiteren Planungsrahmen zu beginnen.

Anpassungen am bestehenden Code: Die Implementierung zusätzlicher Funktionen, insbesondere des IP-Filters, zeigte die Wichtigkeit einer gut vorbereiteten und strukturierten Codebasis.

Lektionen und zukünftige Strategien:

Wichtigkeit von skalierbarem Code: Die Arbeit hat die Notwendigkeit unterstrichen, Code von Beginn an flexibel und skalierbar zu gestalten, um zukünftige Erweiterungen einfacher zu integrieren.

Umfassendere Projektplanung: Die Erfahrungen haben die Bedeutung einer gründlichen Anfangsplanung hervorgehoben, um den Projektumfang realistisch einzuschätzen und Anpassungen zu vereinfachen.
