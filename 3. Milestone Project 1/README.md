### Lære om user story:
# Dette prosjektet har følgende "user story"
# Legge til nye fimler i en damling.
## så jeg kan legge inn hvilke filmer jeg har.
# Liste alle filmene jeg har i samlingen min.
## Så jeg kan se hvilke filmer jeg allerede har.
# Mulighet til å søke på film tittler
## Så jeg kan finne en bestemt film enkelt, når samlingen øker.
## Eksempel:
 as a [type of user], I want [goal] so that I [receive benefit]. End user goal: _______________________________ End business goal: _____________________________ Acceptance criteria: * product defines any initial functionality requirements they can think of * this is a loose outline that will be finalized through wireframes, flows and discussions * acceptance criteria must be finalized before dev starts Measurement of success: ___________________________ * Measurement of success is the way in which we will prove the story was successful in meeting the user and business goal defined above. This will initially be left blank and will be determined through conversations with research, ux and product. This must be finalized before dev starts.

“Stories are deliberately not fleshed out in detail until they are ready to be developed, you only need enough understanding to allow prioritization with other stories.” - Kent Beck

A well-formed user story will follow the INVEST mnemonic.

I – Independent
Stories are easiest to work with if they are independent. That is, we'd like them to not overlap in concept, and we'd like to be able to schedule and implement them in any order.
N – Negotiable
A good story is negotiable. It is not an explicit contract for features; rather, details will be co-created by the customer and programmer during development. A good story captures the essence, not the details. Over time, the card may acquire notes, test ideas, and so on, but we don't need these to prioritize or schedule stories.
V – Valuable
A story needs to be valuable. We don't care about value to just anybody; it needs to be valuable to the customer. Developers may have (legitimate) concerns, but these framed in a way that makes the customer perceive them as important. This is especially an issue when splitting stories.
Think of a whole story as a multi-layer cake, e.g., a network layer, a persistence layer, a logic layer, and a presentation layer. When we split a story, we're serving up only part of that cake. We want to give the customer the essence of the whole cake, and the best way is to slice vertically through the layers. Developers often have an inclination to work on only one layer at a time (and get it "right"); but a full database layer (for example) has little value to the customer if there's no presentation layer.
E – Estimable
A good story can be estimated. We don't need an exact estimate, but just enough to help the customer rank and schedule the story's implementation. Being estimable is partly a function of being negotiated, as it's hard to estimate a story we don't understand. It is also a function of size: bigger stories are harder to estimate.
Finally, it's a function of the team: what's easy to estimate will vary depending on the team's experience. (Sometimes a team may have to split a story into a (time-boxed) "spike" that will give the team enough information to make a decent estimate, and the rest of the story that will actually implement the desired feature.)
S – Small
Good stories tend to be small. Stories typically represent at most a few person-weeks worth of work. (Some teams restrict them to a few person-days of work.) Above this size, and it seems to be too hard to know what's in the story's scope. Saying, "it would take me more than a month" often implicitly adds, "as I don't understand what-all it would entail." Smaller stories tend to get more accurate estimates.
T – Testable
A good story is testable. Writing a story card carries an implicit promise: "I understand what I want well enough that I could write a test for it." Several teams have reported that by requiring customer tests before implementing a story, the team is more productive.
"Testability" has always been a characteristic of good requirements; actually writing the tests early helps us know whether this goal is met. If a customer doesn't know how to test something, this may indicate that the story isn't clear enough, or that it doesn't reflect something valuable to them, or that the customer just needs help in testing. A team can treat non-functional requirements (such as performance and usability) as things that need to be tested. Figure out how to operationalize these tests will help the team learn the true needs.
User story outline

User Story
End user goal
End business goal
Acceptance Criteria /this isn't finalized until the story is ready for development/
Measurement of Success /this is added after conversations with product, ux and research/
User story dos and don’ts

### Implementasjons oppgaver:
# Bestemme hvor man skal lagre filmene.
# Bestemme hvilke data man skal lagre pr. film.
# vise en meny og la brukerne velge et alternativ.
# implementere hvert behov etter tur, hver som en separat funksjon.
# Sørge for at brukerne kan avslutte ptogrammet ved å taste "q" i menyen.

### Hva vi skal gjøre i dette prosjektet:
## Normalt ville dette blitt lagret i en database, men det vet vi ikke hvordan vi skal gjøre enda.
## Så nå lagres dette i en Python liste.
# Dette er lett.
# Men filmer forsviner når applikasjonene avslutter.

### Hva skal vi lagre for hver film.
## vi lager en "dictonary" for hver film.
## i den lagrer vi film tittel, direktør og året den ble utgitt.

### vise en meny
## få user input.
## kjøre det som en loop så vi kan få input igjen og igjen.