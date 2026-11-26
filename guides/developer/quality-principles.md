# Principles for Building Quality Software and Apps

A short working map of the design, testing and operability principles that show up again and again when building tools and apps, including where those principles pull in opposite directions.

Sections:

- [A working map](#a-working-map)
- [Keep it simple](#keep-it-simple)
- [Structure and boundaries](#structure-and-boundaries)
- [SOLID](#solid)
- [Contracts, predictability and failure](#contracts-predictability-and-failure)
- [Verification](#verification)
- [Operability](#operability)
- [Where principles pull against each other](#where-principles-pull-against-each-other)
- [Using these with AI coding agents](#using-these-with-ai-coding-agents)
- [Quick reference](#quick-reference)
- [Sources](#sources)

## A working map

Software quality is less a matter of memorising acronyms than of making small, consistent choices: keep each piece simple and focused, depend on abstractions rather than details, build only what you need now, and make the running system easy to change, test and operate. This paper is a practical landscape, written for someone building AI-first products and an AI software development team, who wants working awareness rather than an academic survey.

Principles are not laws. They often conflict, and the skill is judging which one to favour in the moment. Robert C. Martin put it plainly: following the rules on the paint can will not teach you how to paint, but you had better know them before you decide when to break them. For a wider map of named principles beyond this core set, see the [Developer Guide](developer-guide.md).

Where an idea here matches one of the principles this repo uses for building with agents, the text links to it, so you can see the idea turned into a rule an agent can follow. All of them are on the [principles page](../../docs/principles.html).

## Keep it simple

Most lasting systems stay changeable because they stay small in the places that matter. These ideas are the everyday discipline behind that.

### KISS

Keep It Simple, Stupid: prefer the design that works and remains easy to understand. Cleverness is a cost. In practice, a clear loop often beats a framework, and a single well-named function often beats a hierarchy built for a future that has not arrived.

On this site: principle [3.8](../../docs/principles/3.8.html), prefer clarity over cleverness.

### YAGNI

You Aren't Gonna Need It, from Extreme Programming and explained clearly by Martin Fowler at [https://www.martinfowler.com/bliki/Yagni.html](https://www.martinfowler.com/bliki/Yagni.html), says not to build a capability you only presume you will need. Even when the guess is right, the extra code delays useful work and makes every later change harder. YAGNI does not excuse neglect: refactoring, tests and continuous delivery are what make waiting cheap.

On this site: principle [3.1](../../docs/principles/3.1.html), write the minimum that solves the stated problem, with no speculative features, options or hooks.

### DRY

Don't Repeat Yourself, from Andy Hunt and Dave Thomas in The Pragmatic Programmer, is not merely a ban on copy-paste. Their wording is: every piece of knowledge must have a single, unambiguous, authoritative representation within a system. The acid test is whether one change of intent forces you to edit several places or formats. See [https://pragprog.com/tips/](https://pragprog.com/tips/).

### The Rule of Three, and WET

Don Roberts's rule, popularised in Fowler's Refactoring, is "three strikes and you refactor": write it once, tolerate a second copy, and extract a shared abstraction on the third. The counter-slogan WET, often rendered as Write Everything Twice, is a reminder that premature DRY creates the wrong abstraction. Duplicated knowledge is the problem; similar-looking code is only a clue.

### The Boy Scout Rule

Leave the campground cleaner than you found it. Robert C. Martin uses this in Clean Code for opportunistic, in-scope tidy-ups: a clearer name, a split method, a bit of duplication removed. Small continuous care beats occasional grand rewrites. Fowler describes the same habit as opportunistic refactoring.

On this site: principle [3.10](../../docs/principles/3.10.html), refactor in small behaviour-preserving steps, kept separate from feature changes.

## Structure and boundaries

Good structure lets you change one decision without unpicking the rest. These principles are about where knowledge lives and how much one part may know about another.

### Separation of concerns

Edsger Dijkstra, in EWD447 ([https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)), described studying one aspect of a problem in isolation while remembering that other aspects exist. In software this becomes a practical habit: keep business rules, presentation, persistence and orchestration behind clear boundaries so each can change for its own reason.

On this site: principles [2.3](../../docs/principles/2.3.html) (keep framework, persistence and vendor details out of business logic) and [2.4](../../docs/principles/2.4.html) (separate orchestration from reusable service operations).

### Encapsulation and information hiding

David Parnas argued in 1972 that you should decompose a system so each module hides a design decision likely to change, and expose as little of the interior as possible. Encapsulation is the mechanism; information hiding is the criterion. Hide the data layout, the algorithm, the file format or the sequence, not just the field names.

On this site: principle [2.1](../../docs/principles/2.1.html), design deep modules: a lot of behaviour behind a small interface.

### Loose coupling and high cohesion

From structured design: put work that changes together in the same module (high cohesion), and keep the links between modules few, explicit and stable (loose coupling). A service that must know another service's tables, retries and UI quirks is tightly coupled no matter how clean the folder names look.

### Law of Demeter

Don't talk to strangers. A method should speak to itself, its arguments, objects it creates, and its immediate collaborators, not walk a chain such as `order.getCustomer().getAddress().getZip()`. Long chains couple you to someone else's internals and break when that shape changes.

### Composition over inheritance

The Gang of Four asked designers to favour object composition over class inheritance. Combine small, focused parts that you can swap, rather than building deep is-a trees that become rigid the first time a new case does not fit. Inheritance remains useful for a true subtype with a shared contract; it is a poor way to reuse a handful of methods.

### Program to an interface, not an implementation

Also from the Gang of Four: depend on a contract, not on a concrete class. Callers can then be tested with fakes, and implementations can be replaced, without editing every client. For agents and humans alike, invent the interface when you have more than one implementation, or a real testing need, not as ceremony.

On this site: principle [2.5](../../docs/principles/2.5.html), add a layer, interface or abstraction only when you can name the concrete benefit it brings today.

## SOLID

Robert C. Martin collected five class-design principles that Michael Feathers later arranged to spell SOLID. Martin's own summary, at [http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod](http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod), is still the cleanest short statement. They are about managing dependencies so code stays flexible, rather than about drawing domain models.

### Single Responsibility Principle

A class, or more usefully a module, should have one and only one reason to change. If payroll calculations and paycheck layout change for different business reasons, they do not belong in the same unit. The aim is not tiny files; it is isolating change.

### Open-Closed Principle

You should be able to extend behaviour without modifying the working core. New cases arrive as new code, not as edits scattered through a switch you are afraid to touch. Use this when the axis of change is already visible; do not pre-build a plugin system for a single case.

### Liskov Substitution Principle

Named for Barbara Liskov: a derived type must be substitutable for its base type without surprising callers. If a square cannot honour the contract of a rectangle, it should not inherit from it. Subtypes that throw unexpected errors, or weaken guarantees, break the abstraction.

### Interface Segregation Principle

Make fine-grained, client-specific interfaces. Callers should not depend on methods they do not use, because those unused methods still couple them to changes they do not care about. Several small contracts beat one fat one.

### Dependency Inversion Principle

Depend on abstractions, not on concretions. High-level policy should not import low-level detail; both should depend on a contract the policy owns. This is why a domain service talks to a repository interface, not to a particular database driver.

## Contracts, predictability and failure

### Design by Contract

Bertrand Meyer's idea: a component advertises preconditions it requires, postconditions it promises, and invariants it maintains. Callers and implementers can then be checked against the same agreement. It is the intellectual cousin of Liskov substitution, and a useful prompt when writing tests or API docs: what must be true before, and what is guaranteed after.

On this site: principles [2.9](../../docs/principles/2.9.html) (define the contract first) and [2.15](../../docs/principles/2.15.html) (state failure modes, retryability, timeouts and versioning in the contract).

### Principle of least astonishment

Software should behave as a careful user or caller would expect. A function named `getUser` should not write to the database; error shapes should be consistent; a Cancel button should sit where the platform puts it. Predictable systems are faster to learn and safer to automate.

On this site: principles [3.6](../../docs/principles/3.6.html) (separate commands from queries; no hidden side effects) and [2.10](../../docs/principles/2.10.html) (one consistent error shape).

### Fail fast

Jim Shore's 2004 IEEE Software column, archived at [https://www.martinfowler.com/ieeeSoftware/failFast.pdf](https://www.martinfowler.com/ieeeSoftware/failFast.pdf), argues that you should detect invalid input or broken assumptions immediately and visibly, rather than limp on with corrupted state. Failures that surface at the boundary are cheap; failures that explode three services later are not. Failing fast is for operators and developers; user-facing paths still need a clear, controlled response.

On this site: principle [6.3](../../docs/principles/6.3.html), validate all external input at the boundary.

### Convention over configuration

Popularised by Ruby on Rails and set out in the Rails Doctrine at [https://rubyonrails.org/doctrine](https://rubyonrails.org/doctrine): agree a sensible default once, and only declare the exceptions. Conventions remove boring decisions and let deeper abstractions grow, but they become a trap when the domain is genuinely unusual and you follow the template anyway.

## Verification

Tests are how you keep YAGNI and evolutionary design honest. Without them, "build only what you need" becomes "hope nothing breaks".

### The test pyramid

Mike Cohn described the test automation pyramid in Succeeding with Agile; Martin Fowler's summary is at [https://martinfowler.com/bliki/TestPyramid.html](https://martinfowler.com/bliki/TestPyramid.html). Write many small, fast unit tests, fewer coarser integration or API tests, and very few broad end-to-end tests. High-level tests are a second line of defence: when one fails, add or fix a unit test so the same bug stays dead. A pyramid of meaningful checks beats a high coverage number built from trivial assertions.

Ham Vocke's follow-up, The Practical Test Pyramid at [https://martinfowler.com/articles/practical-test-pyramid.html](https://martinfowler.com/articles/practical-test-pyramid.html), is the best short guide to applying this without getting stuck on Cohn's original layer names.

On this site: the [Verify (testing)](../../docs/categories/verify.html) category, especially principles [4.7](../../docs/principles/4.7.html) (balance the test pyramid by size and cost) and [4.6](../../docs/principles/4.6.html) (coverage is not quality).

## Operability

Design principles decide whether code is easy to change. Operability principles decide whether the running app is easy to deploy, scale, diagnose and trust. The Twelve-Factor App, written by Adam Wiggins and collaborators from experience on the Heroku platform, is the starting methodology for software delivered as a service: [https://12factor.net/](https://12factor.net/).

| Factor | In short |
| --- | --- |
| I. Codebase | One codebase in revision control, many deploys. Do not maintain a different repo per environment. |
| II. Dependencies | Declare and isolate dependencies. Never rely on implicit system-wide packages. |
| III. Config | Store config in the environment, not in the code. Secrets and host settings stay out of the repo. |
| IV. Backing services | Treat databases, queues and caches as attached resources you can swap by changing config. |
| V. Build, release, run | Keep those stages strictly separate. Never patch code at runtime; releases are immutable and can be rolled back. |
| VI. Processes | Run the app as stateless, share-nothing processes. Persist anything that must survive in a backing service. |
| VII. Port binding | The app is self-contained and exports itself by binding a port, rather than depending on a pre-injected web server. |
| VIII. Concurrency | Scale out by running more processes, not by making a single process larger. |
| IX. Disposability | Start quickly and shut down gracefully, so deploys, crashes and scaling events are routine. |
| X. Dev/prod parity | Keep development, staging and production close in time, people and tools. |
| XI. Logs | Treat logs as event streams on standard output. The environment routes and stores them. |
| XII. Admin processes | Run migrations and one-off tasks as one-off processes against the same release and environment as the app. |

### Observability

Charity Majors defines observability as the power to ask new questions of a running system without shipping new code or gathering new data first. Monitoring watches for known problems with pre-agreed alerts; observability is how you investigate unknown ones, using high-cardinality events rather than only pre-aggregated metrics. Her short manifesto is at [https://www.honeycomb.io/blog/observability-a-manifesto](https://www.honeycomb.io/blog/observability-a-manifesto). In practice, bake structured logs, useful traces and a few well-chosen metrics into the code as you write it, not as an afterthought.

On this site: the [Debug and observe](../../docs/categories/debug-and-observe.html) category, for example principles [5.8](../../docs/principles/5.8.html) (structured logs) and [5.14](../../docs/principles/5.14.html) (instrument boundaries and failure points).

### Idempotency

An operation is idempotent if doing it once or several times leaves the same result. Networks, timeouts and clients will retry; a payment, provision or "create" endpoint that is not idempotent will double-charge or double-create. Design writes so a retry is safe, often with an idempotency key, and pair that with retries that back off rather than stampede.

On this site: principle [2.13](../../docs/principles/2.13.html), make retried writes safe with idempotency keys derived from intent.

## Where principles pull against each other

**Judgement is the point.** Principles describe a tension more often than they give a single right answer. Learn both sides, then choose for this change, in this codebase, at this moment.

DRY versus the Rule of Three is the most common everyday clash. Duplicated knowledge will drift, but an abstraction built from one or two examples often encodes the wrong boundary and becomes harder to undo than the copies were. Wait until the third case shows what is genuinely shared.

YAGNI versus extensibility, and versus the Open-Closed Principle, is the strategic clash. Do not add hooks, layers or "flexibility" for a future feature. Do invest in the conditions that make a later change cheap: tests, small modules, clear boundaries and regular refactoring. Fowler's test is sharp: if the work only pays off when the future feature arrives, wait; if it makes today's code easier to change, it is not a YAGNI violation.

Convention versus explicit configuration, and KISS versus completeness, follow the same pattern. Defaults and simple paths should carry the common case. Be ready to be explicit, or a little more thorough, when the domain, the failure mode or the security boundary actually requires it.

## Using these with AI coding agents

If you are encoding these ideas as agent skills or always-on rules, a short, opinionated subset beats a catalogue. Every skill description sits in context on every turn, so prefer a handful of rules the agent must follow, and keep the rest on demand.

This repo does exactly that: one skill per principle, loaded only by the phase that needs it. [Using the agents and commands](using-the-agents.md) explains how the agents load them, and the [skills page](../../docs/skills.html) lists them all.

### Prefer surgical change

Ask for the smallest change that satisfies the request. That is KISS, YAGNI and the Boy Scout Rule in one instruction, and it counters the agent's habit of scaffolding frameworks and helpers "just in case".

On this site: principles [3.1](../../docs/principles/3.1.html) (write the minimum) and [3.2](../../docs/principles/3.2.html) (every changed line traces to the request).

### Do not abstract on the first copy

Tell the agent to wait for a third example before extracting a shared helper, and to distinguish duplicated knowledge from code that only looks similar.

On this site: principle [2.5](../../docs/principles/2.5.html), add an abstraction only when you can name the concrete benefit it brings today.

### Demand meaningful tests

A coverage number is easy to game. Ask for tests that would fail if the behaviour were wrong, sitting mainly at the unit and API layers of the pyramid, not a trail of trivial assertions.

On this site: principles [4.2](../../docs/principles/4.2.html) (test behaviour through public interfaces), [4.3](../../docs/principles/4.3.html) (no tautological tests) and [4.7](../../docs/principles/4.7.html) (balance the test pyramid).

### Bake in operability

Observability, structured logging, fail-fast validation at boundaries, and idempotent writes are thin in many public skill catalogues, and they are exactly where a custom skill set for building services adds the most value.

On this site: principles [5.8](../../docs/principles/5.8.html) (structured logs), [6.3](../../docs/principles/6.3.html) (validate input at the boundary) and [2.13](../../docs/principles/2.13.html) (idempotent retried writes).

## Quick reference

"Watch for" is the usual way the principle is misapplied.

| Theme | Principle | Means | Watch for |
| --- | --- | --- | --- |
| Simplicity | KISS | Prefer the simplest design that works and stays easy to change. | Simple is not the same as short or clever. |
| Simplicity | YAGNI | Do not build a feature or hook you only presume you will need later. | Refactoring and tests are not YAGNI violations. |
| Simplicity | DRY | Each piece of knowledge should live in one authoritative place. | Do not abstract coincidental similarity too early. |
| Simplicity | Rule of Three | Tolerate duplication twice; refactor when a third copy appears. | Three is a heuristic, not a quota. |
| Simplicity | Boy Scout Rule | Leave each file a little cleaner than you found it. | Keep the change small and in scope. |
| Structure | Separation of concerns | Deal with one aspect of a problem at a time, behind a clear boundary. | Too many layers can hide the real work. |
| Structure | Information hiding | Hide design decisions likely to change behind a small interface. | Do not leak storage, algorithms or sequencing. |
| Structure | Coupling and cohesion | Keep related work together; keep unrelated modules loosely tied. | A tidy folder tree is not the same as low coupling. |
| Structure | Law of Demeter | Talk only to immediate collaborators, not through long object chains. | A little chaining can be clearer than a forest of wrappers. |
| Structure | Composition over inheritance | Build behaviour by combining small parts rather than deep class trees. | Inheritance still fits a true is-a relationship. |
| Structure | Program to an interface | Depend on a contract, not on a concrete class. | Do not invent an interface for a single implementation. |
| SOLID | SRP | A module should have one reason to change. | One reason is not the same as one function. |
| SOLID | OCP | Extend behaviour without editing the working core. | Do not add extension points you do not need yet. |
| SOLID | LSP | A substitute must honour the contract of what it replaces. | Subtypes that weaken guarantees break callers. |
| SOLID | ISP | Give clients small interfaces they actually use. | Fat interfaces force unused dependencies. |
| SOLID | DIP | Depend on abstractions, not on concrete details. | The abstraction should be yours, not a vendor's leftover. |
| Contracts | Design by Contract | State preconditions, postconditions and invariants, then enforce them. | A comment is not a contract unless it is checked. |
| Contracts | Least astonishment | Names and APIs should do what a careful reader expects. | A getX that writes to a database is a surprise. |
| Contracts | Fail fast | Detect bad state early and make the failure visible. | Do not confuse failing fast with crashing users. |
| Contracts | Convention over configuration | Agree sensible defaults so only the exceptions need declaring. | Know when the domain is unusual enough to stray. |
| Testing | Test pyramid | Many fast unit tests, fewer integration tests, very few end-to-end tests. | Coverage percentage is not the same as meaningful tests. |
| Operability | Twelve-factor app | Treat config, build/release/run, logs and process shape as first-class. | The factors are a method for services, not a scorecard. |
| Operability | Observability | Ask new questions about production without shipping new instrumentation first. | Dashboards of known metrics are not the whole job. |
| Operability | Idempotency | Repeating an operation leaves the same result as doing it once. | Retries are unsafe until the write is idempotent. |

## Sources

Canonical or close-to-canonical starting points, checked for this paper. Books are named in the text where the idea has no equally good public page.

1. [The Twelve-Factor App](https://12factor.net/): 12factor.net
2. [The Principles of OOD](http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod): butunclebob.com
3. [Yagni](https://www.martinfowler.com/bliki/Yagni.html): martinfowler.com
4. [Pragmatic Programmer tips, including DRY](https://pragprog.com/tips/): pragprog.com
5. [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html): martinfowler.com
6. [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html): martinfowler.com
7. [Fail Fast](https://www.martinfowler.com/ieeeSoftware/failFast.pdf): Jim Shore, IEEE Software
8. [The Rails Doctrine](https://rubyonrails.org/doctrine): rubyonrails.org
9. [Observability: A Manifesto](https://www.honeycomb.io/blog/observability-a-manifesto): honeycomb.io
10. [On the role of scientific thought (EWD447)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html): cs.utexas.edu
11. [On the Criteria To Be Used in Decomposing Systems into Modules](https://dl.acm.org/doi/10.1145/361598.361623): ACM / Parnas, 1972
