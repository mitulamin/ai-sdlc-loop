# Principles for Building Quality Software and Apps

A short working map of the design, testing and operability principles that show up again and again when building tools and apps, including where those principles pull in opposite directions.

Sections:

- [A working map](#a-working-map)
- [Keep it simple](#keep-it-simple)
- [Structure and boundaries](#structure-and-boundaries)
- [SOLID](#solid)
- [Contracts, predictability and failure](#contracts-predictability-and-failure)
- [Verification](#verification)
- [Security by default](#security-by-default)
- [Operability](#operability)
- [Reliability and SRE](#reliability-and-sre)
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

### Acyclic dependencies principle

Robert C. Martin's package-level rule: the dependency graph of packages or components should have no cycles, so it forms a directed acyclic graph. If module A depends on B and B depends, directly or through others, on A, you cannot build, test or release either one alone, and a change in one ripples round the loop. Break a cycle by moving the shared piece into a new module both can depend on, or by applying the Dependency Inversion Principle so one side depends on an abstraction. A cycle checker in CI makes the rule cheap to keep. See [https://en.wikipedia.org/wiki/Acyclic_dependencies_principle](https://en.wikipedia.org/wiki/Acyclic_dependencies_principle).

On this site: principle [2.3](../../docs/principles/2.3.html), keep framework, persistence and vendor details out of business logic, behind adapters, which keeps dependencies pointing one way.

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

On this site: principle [2.3](../../docs/principles/2.3.html), keep framework, persistence and vendor details out of business logic, behind adapters.

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

### Goodhart's law

"When a measure becomes a target, it ceases to be a good measure." The wording is a popular paraphrase of economist Charles Goodhart's 1975 observation about monetary policy: once you put pressure on a statistic for control purposes, people optimise the statistic and it stops reflecting what you cared about. In engineering, a coverage percentage, a ticket count or a deployment-frequency target can all be met without improving anything. Use metrics to ask questions, pair each with a counter-measure, and look at the outcome the metric stands for. See [https://en.wikipedia.org/wiki/Goodhart%27s_law](https://en.wikipedia.org/wiki/Goodhart%27s_law).

On this site: principle [4.6](../../docs/principles/4.6.html), review suites for mock abuse, brittleness and coverage illusions; coverage is not quality.

## Security by default

Security is easiest to get right when it is a property of the design, not a layer added at the end. The [Developer Guide](developer-guide.md) covers [defence in depth](developer-guide.md#defence-in-depth) and [least privilege](developer-guide.md#least-privilege); this one idea belongs beside the design principles above.

### Secure by default

A product should be safe the moment it is installed or deployed, with no extra configuration and no extra cost: the safe option is the default, and the person who wants something riskier has to choose it knowingly. In practice that means authentication on, debug endpoints and sample credentials off, the narrowest permissions, and encryption in transit without a flag. Secure by default is one half of secure by design, which treats security as a design constraint from the start rather than a retrofit; see [https://en.wikipedia.org/wiki/Secure_by_design](https://en.wikipedia.org/wiki/Secure_by_design) and the CISA Secure by Design programme at [https://www.cisa.gov/securebydesign](https://www.cisa.gov/securebydesign). It is the security-flavoured cousin of convention over configuration, and of the principle of least astonishment: nobody should have to read a hardening guide to avoid being exposed.

On this site: principles [6.2](../../docs/principles/6.2.html) (sort actions into always do, ask first and never do) and [2.14](../../docs/principles/2.14.html) (the simple case is the default and advanced behaviour is opt-in).

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

On this site: the [Debug and observe](../../docs/categories/debug-and-observe.html) category, for example principles [5.8](../../docs/principles/5.8.html) (structured logs) and [5.14](../../docs/principles/5.14.html) (instrument boundaries and failure points). The [four golden signals](#the-four-golden-signals) give a short default list of what to measure first.

### Idempotency

An operation is idempotent if doing it once or several times leaves the same result. Networks, timeouts and clients will retry; a payment, provision or "create" endpoint that is not idempotent will double-charge or double-create. Design writes so a retry is safe, often with an idempotency key, and pair that with retries that back off rather than stampede.

On this site: principle [2.13](../../docs/principles/2.13.html), make retried writes safe with idempotency keys derived from intent.

## Reliability and SRE

Operability asks whether you can see and run the system. Reliability asks how much failure users will tolerate, and what the team does about it. Site reliability engineering (SRE) is Google's answer, written up in free books at [https://sre.google/books/](https://sre.google/books/): Site Reliability Engineering, The Site Reliability Workbook (the same ideas with worked examples), and Building Secure and Reliable Systems (reliability and security treated as one design problem). You do not need to run a Google-sized operation to use the ideas. A developer with one service and a pager can use almost all of them.

The thread running through them: reliability is a feature with a cost, you decide how much you need, you measure it from the user's side, and you spend what you have saved on change. The entries below are short; the [Developer Guide](developer-guide.md#reliability) has a one-paragraph version of each for when the name comes up in a review.

### SRE and DevOps

Google's own framing is that "class SRE implements interface DevOps". DevOps names a set of ideas: break down the wall between the people who build and the people who run, treat failure as normal, change gradually, automate, and measure everything. SRE is one concrete way of doing it, with specific practices (service level objectives, error budgets, a cap on toil, blameless postmortems) and engineers who spend part of their time writing software to run the system. Read the Workbook chapter at [https://sre.google/workbook/how-sre-relates/](https://sre.google/workbook/how-sre-relates/), and take the practices without the job title: a small team can run "you build it, you run it" with an error budget and a shared pager. For SRE as a whole, the book's introduction at [https://sre.google/sre-book/introduction/](https://sre.google/sre-book/introduction/) is the starting point.

On this site: principle [7.10](../../docs/principles/7.10.html), shift checks left and release in small, frequent batches, is the delivery half of the same bargain.

### The four golden signals

If you can only measure a few things about a user-facing service, the SRE book's monitoring chapter says to measure these four. Latency: how long requests take, with failed requests tracked separately, because a fast error can make the average look healthy. Traffic: how much demand the system is under, such as requests per second. Errors: the rate of requests that fail, including ones that return success but the wrong content. Saturation: how full the service is, measured on the resource that runs out first, because many systems slow down well before they hit 100 per cent. The set is a default to start from, not a limit; add what your system needs. See [https://sre.google/sre-book/monitoring-distributed-systems/](https://sre.google/sre-book/monitoring-distributed-systems/).

On this site: principles [5.14](../../docs/principles/5.14.html) (instrument boundaries and failure points: latency, errors, saturation) and [5.12](../../docs/principles/5.12.html) (every signal should help detect, localise or explain a problem). Add traffic alongside them: it is the denominator that turns an error count into an error rate, and a sudden drop in it is often the first sign of an outage.

### SLIs, SLOs and SLAs

These terms are easy to blur. A service level indicator (SLI) is a measurement of something users care about, such as the share of requests that succeed or complete quickly enough. A service level objective (SLO) is the target you set for that indicator over a window. A service level agreement (SLA) is a contract with users that spells out the consequences, often financial, of missing a target. If nothing happens when you miss, it is an SLO, not an SLA. Keep the SLO tighter than any SLA so you notice trouble before you owe anyone anything, and choose indicators from the user's side of the system, not from a server's own health. See [https://sre.google/sre-book/service-level-objectives/](https://sre.google/sre-book/service-level-objectives/) and, for how to pick and implement them, the Workbook chapter at [https://sre.google/workbook/implementing-slos/](https://sre.google/workbook/implementing-slos/).

On this site: principle [5.7](../../docs/principles/5.7.html), define what "working" means before instrumenting.

### Embracing risk

SRE does not aim for perfect reliability. Each extra nine of availability costs more than the last and users often cannot tell the difference, since their phone, network or browser fails more often than a well-run service does. The book's risk chapter asks you to decide how reliable the service needs to be, from what users actually need and what the business can afford, and then to spend the rest on shipping. Treat risk as something you choose and measure, not a thing to remove. See [https://sre.google/sre-book/embracing-risk/](https://sre.google/sre-book/embracing-risk/).

On this site: principle [1.8](../../docs/principles/1.8.html), size the process to the task, applies the same judgement to ceremony.

### Error budgets and error-budget policy

The error budget is what is left between perfect and your SLO: if the target is 99.9 per cent of requests succeeding, 0.1 per cent may fail. While budget remains, ship. When it is spent, shift effort from features to reliability. That turns the old argument between "ship faster" and "be safer" into a number both sides read. An error-budget policy writes the rules down before they are needed: what happens when the budget is exhausted (for example, pausing risky releases except for fixes), who can grant an exception, and how disagreements are escalated. Without a policy, the budget is a graph nobody acts on. Start from the Workbook's worked example at [https://sre.google/workbook/error-budget-policy/](https://sre.google/workbook/error-budget-policy/); the idea itself is set out in [https://sre.google/sre-book/embracing-risk/](https://sre.google/sre-book/embracing-risk/).

On this site: principles [7.9](../../docs/principles/7.9.html) (no quality gate is skippable) and [7.10](../../docs/principles/7.10.html) (release in small, frequent batches, so each release spends little budget).

### Toil

Toil is operational work that is manual, repetitive, automatable, tactical and without lasting value, and that grows in step with the service. It is not the same as work you dislike: a one-off migration, or an on-call investigation that teaches you something new, is not toil. Toil matters because it crowds out the engineering that would remove it, and because people doing it all day burn out. Google's guidance is to keep it to a minority of each engineer's time, measure it so it is visible, and automate the biggest sources first. Automating something that runs twice a year is rarely worth it; a task done daily nearly always is. See [https://sre.google/sre-book/eliminating-toil/](https://sre.google/sre-book/eliminating-toil/) and the Workbook's practical follow-up at [https://sre.google/workbook/eliminating-toil/](https://sre.google/workbook/eliminating-toil/).

On this site: principle [9.1](../../docs/principles/9.1.html), when a mistake is mechanical, build a lint, hook or CI check instead of relying on someone remembering.

### Monitoring and symptom-based alerting

The monitoring chapter's central advice is to alert on symptoms, and to use causes for diagnosis. A symptom is what a user would notice: errors, slowness, wrong answers. A cause is a database at 90 per cent CPU, which may or may not matter. A page that wakes someone should be urgent, actionable and need a human; anything else belongs on a dashboard or in a ticket. Alerting on a fast burn of your error budget, rather than on a single threshold, catches real outages quickly and ignores blips; the Workbook chapter at [https://sre.google/workbook/alerting-on-slos/](https://sre.google/workbook/alerting-on-slos/) shows how. See also [https://sre.google/sre-book/monitoring-distributed-systems/](https://sre.google/sre-book/monitoring-distributed-systems/) and the shorter practical chapter at [https://sre.google/sre-book/practical-alerting/](https://sre.google/sre-book/practical-alerting/). Noisy alerts teach people to ignore the pager, which is worse than having none.

On this site: principles [5.15](../../docs/principles/5.15.html) (every alert ships with a minimal runbook) and [5.7](../../docs/principles/5.7.html) (define what "working" means first, so you know what to alert on).

### Being on call and emergency response

Being on call is part of owning a service, and it has to be sustainable. The SRE book's chapter at [https://sre.google/sre-book/being-on-call/](https://sre.google/sre-book/being-on-call/) covers how to keep the load fair and survivable: enough people in the rotation, time to rest and to do project work, training before someone goes on the pager, and clear documentation to follow at three in the morning. Its emergency-response chapter, at [https://sre.google/sre-book/emergency-response/](https://sre.google/sre-book/emergency-response/), is a set of real outages told with what the responders did and learned. The common lessons: stay calm, tell people early, work from written procedures where you have them, and practise before you need them. The Workbook's on-call chapter at [https://sre.google/workbook/on-call/](https://sre.google/workbook/on-call/) adds worked examples. A team where one hero absorbs every page has a bus-factor problem, not a reliability strategy.

On this site: principles [5.15](../../docs/principles/5.15.html) (alerts ship with a runbook) and [5.4](../../docs/principles/5.4.html) (when something breaks, stop and fix it before writing anything new).

### Incident management

An incident is more than a technical problem; it is a coordination problem. The SRE book's chapter at [https://sre.google/sre-book/managing-incidents/](https://sre.google/sre-book/managing-incidents/) borrows from emergency services: declare the incident early, name one incident commander, and separate roles such as running the technical response, communicating with stakeholders and keeping a record, so the people fixing the problem are not also writing updates. Keep a live document of what is known and what has been tried, and hand over explicitly when people rotate. Mitigate first (roll back, shed load, fail over) and find the root cause afterwards. The Workbook's incident-response chapter at [https://sre.google/workbook/incident-response/](https://sre.google/workbook/incident-response/) walks through case studies, including ones that went badly. For security incidents and large disasters, Building Secure and Reliable Systems adds chapters on crisis management and on recovery and aftermath: [https://google.github.io/building-secure-and-reliable-systems/raw/ch17.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch17.html) and [https://google.github.io/building-secure-and-reliable-systems/raw/ch18.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch18.html).

On this site: principles [5.15](../../docs/principles/5.15.html) (runbooks) and [5.1](../../docs/principles/5.1.html) (no fixes without root-cause investigation; do that after the incident is mitigated, not during it).

### Postmortem culture

A postmortem is a written account of an incident: what happened, the impact, the timeline, the contributing causes, and the actions that will make it less likely or less damaging next time. Blameless means the document looks for the conditions that allowed a person's reasonable action to cause harm, not for someone to blame. People who fear punishment hide mistakes, and then nobody learns. A postmortem only pays off if its action items are tracked to completion and the write-up is shared widely enough that other teams learn from it. See [https://sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/) and the Workbook chapter on building the habit at [https://sre.google/workbook/postmortem-culture/](https://sre.google/workbook/postmortem-culture/).

On this site: principles [9.5](../../docs/principles/9.5.html) (ask what conditions allowed the failure, not who caused it) and [9.6](../../docs/principles/9.6.html) (group failures by the mechanism behind them).

### Capacity planning and demand forecasting

Capacity planning is making sure there will be enough of the right resources when demand arrives. The SRE book describes it as a repeating cycle: forecast demand, plan how to supply it, review the plan, then provision and configure. Forecasts need both organic growth, which you can extrapolate from traffic, and inorganic growth from launches and marketing, which you have to ask about. Plans slip and assumptions change, so revisit them. The book uses a capacity-planning tool built inside Google as its case study; read it in the software-engineering chapter at [https://sre.google/sre-book/software-engineering-in-sre/](https://sre.google/sre-book/software-engineering-in-sre/). For a smaller, worked example of sizing a service from its expected load, see the Workbook chapter at [https://sre.google/workbook/non-abstract-design/](https://sre.google/workbook/non-abstract-design/). The traffic and saturation signals are the raw data for this.

On this site: principle [2.8](../../docs/principles/2.8.html), bound every queue, cache, pool and result set, and decide what happens when full. A limit you have chosen is something you can plan capacity against.

### Handling overload and cascading failures

Every service has a load it cannot serve. What matters is what it does next. A service that tries to do everything slows down for everyone and may fall over; one that sheds the excess and keeps serving what it can degrades gracefully. The SRE book's overload chapter, at [https://sre.google/sre-book/handling-overload/](https://sre.google/sre-book/handling-overload/), covers per-client quotas, load shedding, giving lower-priority requests up first, and clients that slow themselves down when the server is struggling. Its cascading-failures chapter, at [https://sre.google/sre-book/addressing-cascading-failures/](https://sre.google/sre-book/addressing-cascading-failures/), shows how one overloaded or restarting replica pushes its load onto the rest, which then fail in turn, and how retries multiply the damage. Defences: load test past the expected peak, bound queues, cap retries, fail fast when the answer will not arrive in time, and know in advance which features you will turn off. Building Secure and Reliable Systems covers the same ground from the attacker's side in its denial-of-service chapter: [https://google.github.io/building-secure-and-reliable-systems/raw/ch10.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch10.html), and its resilience chapter covers failure domains and blast radius: [https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html).

On this site: principles [2.7](../../docs/principles/2.7.html) (design for failure: timeouts, bounded retries with backoff, circuit breakers, bulkheads) and [2.8](../../docs/principles/2.8.html) (bound every queue and decide what happens when full). The [Developer Guide](developer-guide.md#backpressure) covers backpressure.

### Load balancing

Spreading requests across replicas is what lets a service scale out and survive losing a machine, but a naive balancer can send work to a sick backend or overload the ones that are left. The SRE book covers it in two layers: how traffic reaches a datacentre at [https://sre.google/sre-book/load-balancing-frontend/](https://sre.google/sre-book/load-balancing-frontend/), and how it is shared among backends inside one at [https://sre.google/sre-book/load-balancing-datacenter/](https://sre.google/sre-book/load-balancing-datacenter/). The lessons that carry over: use health checks, prefer policies that account for how busy each backend actually is rather than plain round robin, let a backend drain gracefully before it stops, and treat the balancer itself as a component that can fail. The Workbook's managing-load chapter, at [https://sre.google/workbook/managing-load/](https://sre.google/workbook/managing-load/), shows how autoscaling and a managed load balancer fit together.

On this site: principle [2.7](../../docs/principles/2.7.html), design for failure, and [2.8](../../docs/principles/2.8.html), bound every queue and pool. Twelve-factor's disposability and concurrency factors, above, are what make a service easy to balance.

### Release engineering, progressive rollouts and canarying

Most outages follow a change, so the release process is a reliability tool. The SRE book's release-engineering chapter, at [https://sre.google/sre-book/release-engineering/](https://sre.google/sre-book/release-engineering/), argues for self-service releases, reproducible (hermetic) builds, and enforced policy in the pipeline rather than checklists. Progressive rollout limits the damage a bad change can do: release to a small slice first, watch the golden signals, and widen only if they stay healthy. A canary is that small slice. The Workbook's canarying chapter, at [https://sre.google/workbook/canarying-releases/](https://sre.google/workbook/canarying-releases/), explains how to pick the canary population, which metrics to compare against the rest of the fleet, and how to judge whether the canary passed. Building Secure and Reliable Systems adds the security view in its deploying-code chapter: [https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html). Smaller, more frequent releases are easier to test, easier to roll back and spend less error budget each.

On this site: principles [7.10](../../docs/principles/7.10.html) (release in small, frequent batches), [7.11](../../docs/principles/7.11.html) (give feature flags a lifecycle that ends in removing them) and [7.6](../../docs/principles/7.6.html) (keep each change small and about one thing).

### Simplicity

The SRE book treats simplicity as a reliability feature: every line of code, every dependency and every configuration option is a new place to fail, and a system you can understand is one you can fix at three in the morning. Its simplicity chapter, at [https://sre.google/sre-book/simplicity/](https://sre.google/sre-book/simplicity/), argues for boring, well-understood technology, small and stable APIs, deleting dead code rather than commenting it out, and small releases. A little boredom is a virtue in production. This is [KISS](#kiss) and [YAGNI](#yagni) viewed from the pager.

On this site: principles [3.1](../../docs/principles/3.1.html) (write the minimum that solves the stated problem), [3.8](../../docs/principles/3.8.html) (prefer clarity over cleverness) and [3.12](../../docs/principles/3.12.html) (never add a dependency for a few lines).

### Reliability and security together

Building Secure and Reliable Systems opens with the observation, in its first chapter at [https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html), that the goals overlap more than they conflict: both are about systems doing what they should under stress, and a design that limits blast radius, recovers quickly and is easy to reason about helps with both. Its chapters on design tradeoffs ([https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html)), resilience ([https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html)) and recovery ([https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html](https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html)) are the places to start. The book is free to read at [https://sre.google/books/](https://sre.google/books/).

On this site: principles [6.1](../../docs/principles/6.1.html) (threat-model before hardening) and [2.7](../../docs/principles/2.7.html) (design for failure). The [Secure by default](#secure-by-default) entry above is the same idea from the security side.

## Where principles pull against each other

**Judgement is the point.** Principles describe a tension more often than they give a single right answer. Learn both sides, then choose for this change, in this codebase, at this moment.

DRY versus the Rule of Three is the most common everyday clash. Duplicated knowledge will drift, but an abstraction built from one or two examples often encodes the wrong boundary and becomes harder to undo than the copies were. Wait until the third case shows what is genuinely shared.

YAGNI versus extensibility, and versus the Open-Closed Principle, is the strategic clash. Do not add hooks, layers or "flexibility" for a future feature. Do invest in the conditions that make a later change cheap: tests, small modules, clear boundaries and regular refactoring. Fowler's test is sharp: if the work only pays off when the future feature arrives, wait; if it makes today's code easier to change, it is not a YAGNI violation.

Reliability versus velocity is the clash SRE tries to settle with a number rather than an argument. More reliability costs time and money, and every release risks some of it. An error budget lets both sides read the same figure: while there is budget, ship; when it is spent, fix reliability first. The skill is choosing the target for this service, since a target that is too high wastes effort and one that is too low loses users.

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
| Structure | Acyclic dependencies | Keep the dependency graph of modules free of cycles. | Break a cycle with a shared module or an abstraction, not a hack. |
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
| Testing | Goodhart's law | A measure that becomes a target stops being a good measure. | Pair every metric with the outcome it stands for. |
| Security | Secure by default | The safe option is the default; riskier choices are deliberate opt-ins. | Defaults that need a hardening guide are not secure by default. |
| Operability | Twelve-factor app | Treat config, build/release/run, logs and process shape as first-class. | The factors are a method for services, not a scorecard. |
| Operability | Observability | Ask new questions about production without shipping new instrumentation first. | Dashboards of known metrics are not the whole job. |
| Operability | Idempotency | Repeating an operation leaves the same result as doing it once. | Retries are unsafe until the write is idempotent. |
| Reliability | SRE and DevOps | SRE is a concrete way to do DevOps: shared ownership, automation, measured reliability. | Take the practices; the job title is optional. |
| Reliability | Four golden signals | Measure latency, traffic, errors and saturation first for any user-facing service. | They are a starting set; track failed and successful latency separately. |
| Reliability | SLI, SLO, SLA | An indicator is the measurement, an objective is the target, an agreement is a contract with consequences. | An SLO with no consequence is not an SLA; keep the SLO tighter. |
| Reliability | Embracing risk | Choose how reliable the service needs to be and spend the rest on change. | Perfect reliability is the wrong target and costs more each step. |
| Reliability | Error budget and policy | The gap between 100 per cent and the SLO is spendable; the policy says what happens when it is gone. | A budget with no agreed policy is only a graph. |
| Reliability | Toil | Cap manual, repetitive, automatable work so engineering time survives. | Not all unpleasant work is toil; automate what recurs. |
| Reliability | Symptom-based alerting | Page on what users feel; use causes to diagnose. | Noisy pages teach people to ignore the pager. |
| Reliability | On call and emergency response | Keep rotations sustainable and responses calm, early and written down. | One hero taking every page is a risk, not a plan. |
| Reliability | Incident management | Declare early, name a commander, separate roles, mitigate before root-causing. | Do not let the fixers also write the updates. |
| Reliability | Postmortem culture | Write up incidents blamelessly and follow the actions through. | A document without tracked actions changes nothing. |
| Reliability | Capacity planning | Forecast demand, plan supply, review, provision, and repeat. | Forecasts miss launches; revisit the plan. |
| Reliability | Overload and cascading failures | Shed excess load, degrade gracefully, cap retries, bound queues. | Retries multiply an overload instead of curing it. |
| Reliability | Load balancing | Spread work by backend health and load, and drain gracefully. | The balancer itself can be the single point of failure. |
| Reliability | Progressive rollout and canarying | Release to a small slice, watch the signals, widen only if healthy. | A canary nobody watches is not a canary. |
| Reliability | Simplicity | Fewer parts and dependencies means fewer ways to fail. | Delete dead code; boring technology is a virtue in production. |

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
12. [Acyclic dependencies principle](https://en.wikipedia.org/wiki/Acyclic_dependencies_principle): Wikipedia
13. [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law): Wikipedia
14. [Secure by design](https://en.wikipedia.org/wiki/Secure_by_design): Wikipedia
15. [Secure by Design](https://www.cisa.gov/securebydesign): CISA
16. [Google SRE books](https://sre.google/books/): sre.google, including Building Secure and Reliable Systems
17. [Site Reliability Engineering: Introduction](https://sre.google/sre-book/introduction/): Google SRE book
18. [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/): Google SRE book
19. [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/): Google SRE book
20. [Embracing Risk](https://sre.google/sre-book/embracing-risk/): Google SRE book
21. [Eliminating Toil](https://sre.google/sre-book/eliminating-toil/): Google SRE book
22. [Being On-Call](https://sre.google/sre-book/being-on-call/): Google SRE book
23. [Emergency Response](https://sre.google/sre-book/emergency-response/): Google SRE book
24. [Managing Incidents](https://sre.google/sre-book/managing-incidents/): Google SRE book
25. [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/): Google SRE book
26. [Handling Overload](https://sre.google/sre-book/handling-overload/): Google SRE book
27. [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/): Google SRE book
28. [Load Balancing at the Frontend](https://sre.google/sre-book/load-balancing-frontend/): Google SRE book
29. [Load Balancing in the Datacenter](https://sre.google/sre-book/load-balancing-datacenter/): Google SRE book
30. [Release Engineering](https://sre.google/sre-book/release-engineering/): Google SRE book
31. [Simplicity](https://sre.google/sre-book/simplicity/): Google SRE book
32. [Software Engineering in SRE](https://sre.google/sre-book/software-engineering-in-sre/): Google SRE book, capacity planning case study
33. [Practical Alerting from Time-Series Data](https://sre.google/sre-book/practical-alerting/): Google SRE book
34. [How SRE Relates to DevOps](https://sre.google/workbook/how-sre-relates/): Google SRE Workbook
35. [Implementing SLOs](https://sre.google/workbook/implementing-slos/): Google SRE Workbook
36. [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/): Google SRE Workbook
37. [Error Budget Policy](https://sre.google/workbook/error-budget-policy/): Google SRE Workbook
38. [Eliminating Toil](https://sre.google/workbook/eliminating-toil/): Google SRE Workbook
39. [On-Call](https://sre.google/workbook/on-call/): Google SRE Workbook
40. [Incident Response](https://sre.google/workbook/incident-response/): Google SRE Workbook
41. [Postmortem Culture: Learning from Failure](https://sre.google/workbook/postmortem-culture/): Google SRE Workbook
42. [Non-Abstract Large System Design](https://sre.google/workbook/non-abstract-design/): Google SRE Workbook
43. [Managing Load](https://sre.google/workbook/managing-load/): Google SRE Workbook
44. [Canarying Releases](https://sre.google/workbook/canarying-releases/): Google SRE Workbook
45. [The Intersection of Security and Reliability](https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html): Building Secure and Reliable Systems
46. [Design Tradeoffs](https://google.github.io/building-secure-and-reliable-systems/raw/ch04.html): Building Secure and Reliable Systems
47. [Design for Resilience](https://google.github.io/building-secure-and-reliable-systems/raw/ch08.html): Building Secure and Reliable Systems
48. [Design for Recovery](https://google.github.io/building-secure-and-reliable-systems/raw/ch09.html): Building Secure and Reliable Systems
49. [Mitigating Denial-of-Service Attacks](https://google.github.io/building-secure-and-reliable-systems/raw/ch10.html): Building Secure and Reliable Systems
50. [Deploying Code](https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html): Building Secure and Reliable Systems
51. [Crisis Management](https://google.github.io/building-secure-and-reliable-systems/raw/ch17.html): Building Secure and Reliable Systems
52. [Recovery and Aftermath](https://google.github.io/building-secure-and-reliable-systems/raw/ch18.html): Building Secure and Reliable Systems
