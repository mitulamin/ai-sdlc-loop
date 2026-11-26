# Developer Guide

A field guide to named principles and methodologies you will meet in real software work, each with a short plain-English explanation and a link to a canonical source.

## How to use this guide

You will keep meeting named principles in reviews, design docs and incident write-ups. This guide is a map of the ones you are most likely to hear. For each name you get one or two plain-English sentences and a link to an official document, a canonical essay, or a well-known article. You do not need to memorise the list. Use it when a term comes up, and let the originals teach you the rest.

SOLID, YAGNI, DRY and the twelve-factor app are covered in more depth in the companion paper, [Principles for Building Quality Software and Apps](quality-principles.md). This guide goes wider, into architecture, reliability, operations, delivery, security, and the laws that shape teams.

Where a name matches one of the 103 principles this repo uses for building with agents, the entry says which one, so you can see how the idea is applied in practice. The [learning path](../../docs/path.html) walks all of them in order. If a word in an explanation is new to you, the [glossary](#words-this-guide-uses) at the end defines it.

**A field guide, not a syllabus.** No one applies all of these at once. Learn the names, follow the link when the idea shows up in your work, and ask a teammate when two principles seem to disagree.

Sections:

- [Design](#design)
- [Architecture and data](#architecture-and-data)
- [Reliability](#reliability)
- [Operations and observability](#operations-and-observability)
- [Testing and delivery](#testing-and-delivery)
- [Security](#security)
- [Team and process laws](#team-and-process-laws)
- [A good place to start](#a-good-place-to-start)
- [Words this guide uses](#words-this-guide-uses)

## Design

These ideas are about how you shape everyday code: clarity, small pieces, and habits that keep a codebase kind to the next reader, who may be you in six months.

### The Zen of Python

PEP 20 is a short list of aphorisms that ship with the Python language: readability counts, explicit is better than implicit, simple is better than complex, and errors should never pass silently. Even if you do not write Python, it is a clear statement of a style that favours clarity over cleverness. [https://peps.python.org/pep-0020/](https://peps.python.org/pep-0020/)

On this site: principle [3.8](../../docs/principles/3.8.html), prefer clarity over cleverness.

### Unix philosophy

Write small programs that do one thing well, and combine them, often through simple text interfaces, rather than building one large program that tries to do everything. The usual sources are Doug McIlroy's early Unix practice and Eric Raymond's later write-up in The Art of Unix Programming. [https://en.wikipedia.org/wiki/Unix_philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)

### The Pragmatic Programmer

Andy Hunt and Dave Thomas offer a set of working habits more than a single rule: keep knowledge orthogonal, so a change in one place does not force a change in another; fix "broken windows" before they spread; and get a thin slice working end to end with tracer bullets. Their DRY rule, that each piece of knowledge should have one authoritative home, is covered in the [companion paper](quality-principles.md). [https://pragprog.com/tips/](https://pragprog.com/tips/)

On this site: principle [3.14](../../docs/principles/3.14.html), build in thin vertical slices, is the tracer-bullet habit applied to agents.

### Clean Code

Robert C. Martin's book argues that code is clean when the next person can read, change and test it: names that say what they mean, small focused functions, no surprising side effects, and leaving the file a little better than you found it. The book is the source. [https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398548](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398548)

On this site: principles [3.4](../../docs/principles/3.4.html) (small functions at one level of abstraction) and [3.7](../../docs/principles/3.7.html) (comments explain why, never narrate what).

### Worse is better

Richard Gabriel's essay argues that a simpler design that ships and can evolve often beats a more complete, more "correct" design that arrives late. It is a useful counterweight when you are tempted to perfect an abstraction before anyone can use it. [https://www.dreamsongs.com/RiseOfWorseIsBetter.html](https://www.dreamsongs.com/RiseOfWorseIsBetter.html)

On this site: principle [3.1](../../docs/principles/3.1.html), write the minimum that solves the stated problem.

For SOLID, YAGNI, DRY, KISS, composition over inheritance and related design tensions, see the companion paper, [Principles for Building Quality Software and Apps](quality-principles.md).

## Architecture and data

These names show up when a system has more than one part, more than one model of the data, or more than one way those parts can fail to agree.

### Domain-Driven Design

Eric Evans's approach is to model the software in the language of the business, and to split a large system into bounded contexts, each with its own model, so one team's language does not leak into another's. His short official reference is the best starting summary. [https://www.domainlanguage.com/ddd/reference/](https://www.domainlanguage.com/ddd/reference/)

On this site: principles [2.16](../../docs/principles/2.16.html) (keep a glossary of the domain language) and [2.17](../../docs/principles/2.17.html) (split the domain into bounded contexts).

### CQRS

Command Query Responsibility Segregation, popularised by Greg Young and explained by Martin Fowler, means using a different model to handle writes (commands) from the model you use to handle reads (queries). It can help when those needs diverge sharply. It is extra complexity you should not add by default, and it is not the same thing as event sourcing. [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)

On this site: principle [3.6](../../docs/principles/3.6.html), separate commands from queries, is the same idea at the scale of a single function, and it is cheap enough to apply everywhere.

### Event-driven architecture

Components communicate by emitting and reacting to events, rather than calling each other directly for every change. Fowler's 2017 article is the clearest map of the variants, including simple notifications, events that carry state, and event sourcing, three ideas that are often mixed up. [https://martinfowler.com/articles/201701-event-driven.html](https://martinfowler.com/articles/201701-event-driven.html)

On this site: principle [2.18](../../docs/principles/2.18.html), derive aggregates from events and commands.

### Hexagonal architecture

Also called ports and adapters, from Alistair Cockburn: keep the core application logic in the middle, and talk to databases, user interfaces and other services through replaceable adapters. The business rules should not depend on a particular framework or datastore. [https://alistair.cockburn.us/hexagonal-architecture/](https://alistair.cockburn.us/hexagonal-architecture/)

On this site: principles [2.2](../../docs/principles/2.2.html) (choose seams deliberately) and [2.3](../../docs/principles/2.3.html) (keep framework, persistence and vendor details behind adapters).

### The CAP theorem

Eric Brewer's conjecture, later proved by Seth Gilbert and Nancy Lynch, says a distributed data system cannot simultaneously guarantee consistency, availability and partition tolerance. In real networks, partitions happen, so you have to decide how you degrade. Brewer's later essay is the best short reading, because it also explains why a blunt "pick two" is not quite right. [https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)

### ACID

Atomicity, Consistency, Isolation and Durability are the classic promises of a database transaction: a group of writes either all happen or none do, they leave the data valid, they do not trample one another, and they survive a crash. This is what you are asking for when you commit a transaction in a relational database. [https://en.wikipedia.org/wiki/ACID](https://en.wikipedia.org/wiki/ACID)

### Eventual consistency

If no new updates are made, all replicas of a piece of data will eventually agree on the last value. Werner Vogels's essay is the standard explanation: you gain availability and scale, and you accept a window in which different readers can see different answers. [https://allthingsdistributed.com/2007/12/eventually_consistent.html](https://allthingsdistributed.com/2007/12/eventually_consistent.html)

### The strangler fig pattern

Martin Fowler's name for replacing a legacy system gradually, by routing more and more work to new code until the old system can be retired, rather than attempting a risky big-bang rewrite. [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html)

## Reliability

Google's Site Reliability Engineering books are the usual home for several of these ideas. The others are named patterns for staying up when something, inevitably, goes wrong.

### SLOs and SLIs

A service level indicator is a measurement of how the service is doing for users, such as request latency or error rate. A service level objective is the target you set for that indicator. You cannot manage reliability by gut feel alone; you need a number that reflects the user experience. [https://sre.google/sre-book/service-level-objectives/](https://sre.google/sre-book/service-level-objectives/)

On this site: principle [5.7](../../docs/principles/5.7.html), define what "working" means before instrumenting.

### Error budgets

An error budget is the gap between perfect reliability and your SLO: the amount of unreliability you are willing to spend on change and risk. When the budget is gone, you slow feature work and focus on reliability. This is how SRE turns "is it safe to launch?" into a shared, numeric conversation. [https://sre.google/sre-book/embracing-risk/](https://sre.google/sre-book/embracing-risk/)

### Toil

In SRE, toil is manual, repetitive, automatable operational work that grows as the service grows and leaves no lasting improvement. The published aim at Google is to keep it below half of an SRE's time, so people can do engineering that makes the next incident less likely. [https://sre.google/sre-book/eliminating-toil/](https://sre.google/sre-book/eliminating-toil/)

### Blameless postmortems

After an incident, write down what happened, what the impact was, what caused it, and what you will change, on the assumption that everyone involved meant well and was working with the information they had. You cannot fix people; you can fix systems and processes. [https://sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/)

On this site: principle [9.5](../../docs/principles/9.5.html), ask what conditions allowed the failure, not who caused it.

### Chaos engineering

Run controlled experiments, often in production, to see whether the system still behaves when things fail: a host dies, a dependency slows, a network path drops. The aim is to find weaknesses before your users do, with a limited blast radius. [https://principlesofchaos.org/](https://principlesofchaos.org/)

### Fail fast

Detect bad input or a broken assumption immediately and make the failure visible, rather than carrying on with corrupted state. Failures that surface at the boundary are cheap; failures that explode three services later are not. [https://www.martinfowler.com/ieeeSoftware/failFast.pdf](https://www.martinfowler.com/ieeeSoftware/failFast.pdf)

On this site: principle [6.3](../../docs/principles/6.3.html), validate all external input at the boundary, is one everyday form of failing fast.

### Circuit breakers

If a dependency is failing or timing out, stop calling it for a while and fail quickly, then probe now and then to see if it has recovered. This protects both sides from a storm of retries. [https://martinfowler.com/bliki/CircuitBreaker.html](https://martinfowler.com/bliki/CircuitBreaker.html)

On this site: principle [2.7](../../docs/principles/2.7.html), design for failure.

### Bulkheads

Isolate resources so that a failure in one part of the system, such as one thread pool, queue or tenant, cannot use up everything and take the rest down with it. The name comes from the watertight compartments in a ship. [https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)

On this site: principle [2.7](../../docs/principles/2.7.html), design for failure.

### Backpressure

When a consumer cannot keep up, it should signal the producer to slow down, rather than queuing without bound until something falls over. The Reactive Manifesto is the short named source for this idea in modern service design. [https://www.reactivemanifesto.org/glossary#Back-Pressure](https://www.reactivemanifesto.org/glossary#Back-Pressure)

On this site: principle [2.8](../../docs/principles/2.8.html), bound every queue, cache, pool and result set, and decide what happens when full.

### Idempotency

An operation is idempotent if doing it once or several times leaves the same result. That is what makes retries safe for payments, creates and other writes. Stripe's API docs are a clear practical explanation. [https://docs.stripe.com/api/idempotent_requests](https://docs.stripe.com/api/idempotent_requests)

On this site: principle [2.13](../../docs/principles/2.13.html), make retried writes safe with idempotency keys derived from intent.

### Retries with backoff

Transient failures are common, so retry, but wait longer after each attempt and add jitter so every client does not retry at once. Never retry a non-idempotent write blindly. Amazon's Builders' Library essay is the standard practical guide. [https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

On this site: principle [2.7](../../docs/principles/2.7.html), which asks for bounded retries with backoff.

### The fallacies of distributed computing

Peter Deutsch and colleagues listed eight assumptions first-time builders of distributed systems make, all of which turn out false: that the network is reliable, latency is zero, bandwidth is infinite, the network is secure, the topology does not change, there is one administrator, transport is free, and the network is homogeneous. James Gosling's page preserves the list. [https://nighthacks.com/jag/res/Fallacies.html](https://nighthacks.com/jag/res/Fallacies.html)

Google also publishes a short workbook chapter on how to run an error-budget policy in practice: [https://sre.google/workbook/error-budget-policy/](https://sre.google/workbook/error-budget-policy/).

## Operations and observability

These principles are about running the system once it is in production, and about being able to ask why it misbehaved without guessing.

### Observability: logs, metrics and traces

Observability is the ability to ask new questions about a running system without first shipping new instrumentation. The usual three signals are logs (records of events), metrics (numeric aggregates over time) and traces (the path of a request across services). OpenTelemetry's primer is the official starting point for that vocabulary. [https://opentelemetry.io/docs/concepts/observability-primer/](https://opentelemetry.io/docs/concepts/observability-primer/)

On this site: the [Debug and observe](../../docs/categories/debug-and-observe.html) category, for example principles [5.8](../../docs/principles/5.8.html) (structured logs), [5.9](../../docs/principles/5.9.html) (correlation IDs) and [5.14](../../docs/principles/5.14.html) (instrument boundaries and failure points).

### Infrastructure as code

Define servers, networks and related infrastructure in versioned files, and apply those files through tools, rather than clicking in a console. The environment can then be reviewed, repeated and rolled back like application code. [https://martinfowler.com/bliki/InfrastructureAsCode.html](https://martinfowler.com/bliki/InfrastructureAsCode.html)

### Immutable infrastructure

Once a server or container is deployed, you do not patch it in place; you build a new one and replace the old. This avoids snowflake machines that nobody can reproduce. [https://martinfowler.com/bliki/ImmutableServer.html](https://martinfowler.com/bliki/ImmutableServer.html)

For how a service should treat config, logs, processes and deploys, see the twelve-factor app in the [companion paper](quality-principles.md), or read the methodology itself at [https://12factor.net/](https://12factor.net/). Google's SRE chapter on monitoring distributed systems is also a strong official companion to the observability primer: [https://sre.google/sre-book/monitoring-distributed-systems/](https://sre.google/sre-book/monitoring-distributed-systems/).

## Testing and delivery

These practices are how changes get from your laptop into production without becoming a heroics exercise, and how you tell whether the path is actually getting better.

### Test-driven development

From Kent Beck: write a small failing test, write the code that makes it pass, then refactor, in a short loop. The tests become a specification you can run, and they leave you safer to change the design. [https://martinfowler.com/bliki/TestDrivenDevelopment.html](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

On this site: principle [4.1](../../docs/principles/4.1.html), write one failing test first and watch it fail.

### Continuous integration

Every developer integrates into a shared mainline frequently, and each integration is verified by an automated build and tests. If the build breaks, fixing it is the priority. Fowler's article is still the clearest statement of the practice. [https://martinfowler.com/articles/continuousIntegration.html](https://martinfowler.com/articles/continuousIntegration.html)

On this site: principles [5.4](../../docs/principles/5.4.html) (when the build breaks, stop and fix it before writing anything new) and [7.9](../../docs/principles/7.9.html) (no quality gate is skippable).

### Continuous delivery

Keep the software in a state where you can release it at any time, with a repeatable pipeline from commit to a production-ready build. You may still choose when to go live; the point is that the path is already proven. The site for Humble and Farley's book is the usual starting point. [https://continuousdelivery.com/](https://continuousdelivery.com/)

On this site: principle [7.10](../../docs/principles/7.10.html), shift checks left and release in small, frequent batches.

### Trunk-based development

Developers merge small changes to a single trunk, often called main, at least daily, rather than living on long feature branches. It is a required practice for genuine continuous integration. [https://trunkbaseddevelopment.com/](https://trunkbaseddevelopment.com/)

On this site: principle [7.6](../../docs/principles/7.6.html), keep each change small and about one thing.

### Feature toggles

Release incomplete or risky features behind a flag so you can merge to trunk and control rollout without a long-lived branch. Fowler's article is the standard map of the different kinds of toggle and their risks. [https://martinfowler.com/articles/feature-toggles.html](https://martinfowler.com/articles/feature-toggles.html)

On this site: principle [7.11](../../docs/principles/7.11.html), give feature flags a lifecycle that ends in removing them.

### Semantic versioning

For software you publish, version numbers of the form MAJOR.MINOR.PATCH tell users what kind of change to expect: breaking changes bump major, new compatible features bump minor, and compatible fixes bump patch. [https://semver.org/](https://semver.org/)

On this site: principle [2.15](../../docs/principles/2.15.html), state failure modes, retryability, timeouts and versioning in the contract.

### DORA metrics

DORA, a long-running research program now published at dora.dev, measures software delivery with a small set of outcome metrics. The current official set is change lead time, deployment frequency, failed-deployment recovery time, change fail rate, and deployment rework rate. The point is to improve both throughput and stability, not one at the expense of the other. [https://dora.dev/guides/dora-metrics/](https://dora.dev/guides/dora-metrics/)

For how many tests to write at each level, see the test pyramid in the [companion paper](quality-principles.md), or Fowler's short summary at [https://martinfowler.com/bliki/TestPyramid.html](https://martinfowler.com/bliki/TestPyramid.html).

## Security

You do not need to become a specialist overnight, but you do need a few named habits and one standard list of the ways web apps usually go wrong.

### Defence in depth

Do not rely on a single control. Stack independent protections, such as authentication, authorisation, network rules, encryption and monitoring, so that one failure does not open the whole system. NIST's glossary is the official short definition. [https://csrc.nist.gov/glossary/term/defense_in_depth](https://csrc.nist.gov/glossary/term/defense_in_depth)

### Least privilege

Give each user, service and process only the access it needs to do its job, and no more. This limits how much damage a stolen credential or a buggy service can do. [https://csrc.nist.gov/glossary/term/least_privilege](https://csrc.nist.gov/glossary/term/least_privilege)

On this site: principle [6.2](../../docs/principles/6.2.html), sort actions into always do, ask first and never do, applies the same thinking to what an agent may do.

### OWASP Top 10

The OWASP Top 10 is the standard awareness list of the most critical risks to web applications, and the usual first security reading for application developers. The current edition is the 2025 list. [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)

On this site: the [Secure](../../docs/categories/secure.html) category, especially principle [6.3](../../docs/principles/6.3.html) (validate input, parameterise queries, encode output).

### Shift-left security

Move security checks earlier in the development lifecycle, into design, coding and the pipeline, rather than waiting for a review at the end. Issues found early, such as leaked secrets or known-vulnerable dependencies, are cheaper and less embarrassing to fix. OWASP's DevSecOps guideline is a practical starting point. [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/)

On this site: principles [6.4](../../docs/principles/6.4.html) (never commit secrets), [6.8](../../docs/principles/6.8.html) (audit dependencies before each release) and [7.10](../../docs/principles/7.10.html) (shift checks left).

For a more formal official framework, see NIST's Secure Software Development Framework: [https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-218.pdf](https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-218.pdf).

## Team and process laws

These are observations about people, organisations and time. They are not physical laws, but they have been named because teams keep rediscovering them the hard way.

### Conway's Law

Mel Conway's 1968 observation: organisations design systems that mirror their communication structure. If you want a different architecture, you often have to change how teams talk, or accept that the org chart will show up in the code. [https://melconway.com/Home/Conways_Law.html](https://melconway.com/Home/Conways_Law.html)

### Postel's law

Also called the robustness principle, from Jon Postel's TCP work: be conservative in what you send, and liberal in what you accept. It helped early internet protocols interoperate. Later guidance, including RFC 9413, cautions that being too liberal about bad input can hide bugs and create security holes, so apply it with care. The original wording is in RFC 793: [https://www.rfc-editor.org/rfc/rfc793](https://www.rfc-editor.org/rfc/rfc793)

### Hyrum's Law

With enough users of an API, they will come to depend on every observable behaviour, even the accidental ones you never promised. That is why a "harmless" implementation change sometimes breaks people, and why tests and explicit contracts matter. [https://www.hyrumslaw.com/](https://www.hyrumslaw.com/)

On this site: principle [2.12](../../docs/principles/2.12.html), prefer adding over changing.

### Gall's Law

A complex system that works has usually evolved from a simple system that worked; a complex system designed from scratch rarely does. Start simple, then grow. The usual citation is John Gall's Systemantics (1975). [https://en.wikipedia.org/wiki/John_Gall_%28author%29](https://en.wikipedia.org/wiki/John_Gall_%28author%29)

### Hofstadter's Law

It always takes longer than you expect, even when you take Hofstadter's Law into account. Coined in Douglas Hofstadter's Gödel, Escher, Bach, it is a humorous warning about estimation, not a planning method. [https://en.wikipedia.org/wiki/Hofstadter%27s_law](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

### Brooks's Law

Adding people to a late software project makes it later, because of ramp-up time and the extra communication. Fred Brooks set this out in The Mythical Man-Month; a widely used copy of the essay is here. [https://www.cs.cmu.edu/~15712/papers/mythicalmanmonth00fred.pdf](https://www.cs.cmu.edu/~15712/papers/mythicalmanmonth00fred.pdf)

### The Agile Manifesto

The 2001 manifesto values individuals and interactions, working software, customer collaboration, and responding to change, over the items on the right of each pair. The twelve principles behind it are worth reading once, if only so you can tell the original idea from later ceremony. [https://agilemanifesto.org/](https://agilemanifesto.org/)

The twelve principles behind the Agile Manifesto are at [https://agilemanifesto.org/principles.html](https://agilemanifesto.org/principles.html). For the later caution on Postel's law, see RFC 9413, Maintaining Robust Protocols: [https://www.rfc-editor.org/rfc/rfc9413.html](https://www.rfc-editor.org/rfc/rfc9413.html).

## A good place to start

If you only follow a handful of links this month, these six will repay the time. The rest will still be here when the name comes up.

1. [Principles for Building Quality Software and Apps](quality-principles.md): the companion paper on SOLID, YAGNI, DRY and the twelve-factor app
2. [The Zen of Python](https://peps.python.org/pep-0020/): peps.python.org
3. [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html): martinfowler.com
4. [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/): sre.google
5. [OWASP Top 10](https://owasp.org/www-project-top-ten/): owasp.org
6. [Manifesto for Agile Software Development](https://agilemanifesto.org/): agilemanifesto.org

## Words this guide uses

Short definitions of terms the entries above use without stopping to explain.

| Term | What it means here |
| --- | --- |
| Principle | A named rule of thumb that experienced people have found useful. It guides a choice; it does not decide it for you. |
| Methodology | A named way of working made of several practices, such as continuous delivery or the twelve-factor app. |
| Canonical source | The original or most widely accepted statement of an idea, such as the author's own essay or an official specification. |
| API | Application programming interface: the functions, endpoints or messages one piece of software offers so others can use it. |
| Contract | What a component promises to callers: its inputs, outputs, errors and limits. Tests and documentation make it explicit. |
| Production | The live system real users depend on, as opposed to your laptop, a test environment or staging. |
| Distributed system | A system whose parts run on more than one machine and talk over a network, so any message can be slow, lost or duplicated. |
| Replica | A copy of the same data kept on another machine, for speed or for safety if one machine fails. |
| Dependency | Another library, service or system your code relies on to work. |
| Trunk or mainline | The single shared branch everyone integrates into, usually called main. |
| Pipeline | The automated steps that build, test and deploy each change. |
| Refactor | Change the structure of code without changing what it does. |
| Incident | An event where the service fails or degrades for users and someone has to respond. |
| Blast radius | How much of the system, or how many users, a failure or an experiment can affect. |
| Credential | A secret that proves identity, such as a password, API key or token. |
