# Tool Surfaces

**Location:** `apparatus/tool-surfaces.md`. An operational consequence of the floor mechanism
(`core/10`) applied to the tools an actor is given. Depends on the encode/verify split
(`apparatus/encode-verify.md`) and the skill floor (`apparatus/the-skill-floor.md`). MCP is used as
the worked example; the classes are protocol-independent and should outlive it.

**Status:** derived. The taxonomy follows from `core/10`'s escape conditions; the MCP mapping is
descriptive of the protocol as specified.

---

## 1. The claim

> **A tool call does not merely retrieve. It *reallocates demand*. Every call either resolves
> decisions the actor would otherwise have had to make, or creates new ones by handing over
> uninterpreted content.**
>
> **Choosing an actor's tools is therefore choosing its floor** (`core/10`): the open decisions a
> toolset leaves behind are precisely the ones that escape under load.

This is why tool selection is a specification decision and not a convenience decision.

---

## 2. Three classes, by demand consequence

Classes are defined by *what a call does to the residual*, never by technology.

### Ground exporters

Return unstructured or unbounded content that the actor must interpret. The call **creates open
decisions**: *where is the relevant part, what structure does this have, what does it mean here.*
None of those has a verifier the actor holds.

Worst case on both `core/10` conditions at once — they **raise resolve load** (the content occupies
the window) *and* **add open decisions** (the interpretation is unchecked).

*Examples:* raw `resources/read`; `cat`, `grep -r`, `git log` consumed as text.

### Resolvers

Return an answer some other mechanism has already decided authoritatively. The actor reads a
**resolved fact** rather than inferring one. The decision was made — correctly, mechanically —
before the actor saw anything.

This is the encode/verify split embodied in tooling: *never re-derive what a mechanical extractor
computes exactly.* A language server has already resolved "which symbol is this"; an actor
re-inferring it from bytes is paying judgment prices for a mechanical-store decision.

*Examples:* LSP `textDocument/definition`; a typed query returning typed rows; a compiled symbol
lookup.

### Verifiers

Supply a **closing predicate on the actor's own output.** They do not provide ground; they provide a
check. Under `core/10` this is the class that converts *escape* into *retry* — the single thing that
removes floor-escape.

*Examples:* a test-runner's exit code; a type-checker's verdict; a schema validator.

---

## 3. The class is a property of ⟨tool, task, consumption⟩

**Not of the tool.** This is the load-bearing subtlety, and getting it wrong makes the taxonomy
wrong in exactly the cases people will test it on.

**Task-dependence.** `read_file` exports enormous ground when the task is *"refactor this module"* —
the actor must locate, structure, and interpret. It exports almost none when the task is *"what is
the copyright header."* Same tool, same call, different residual, because the governing decision set
differs.

**Consumption-dependence.** `pytest` consumed for its **exit code** is a *verifier* — it supplies a
closing predicate on the actor's work. The same `pytest` consumed for its **stdout** is a *ground
exporter* — a wall of text to be interpreted. **Same binary, opposite class, determined by which part
you read.**

> **A tool is not a class. A *call*, on a *task*, consumed a particular *way*, has a class.**

Two consequences follow, and they are worth stating because they cut off tempting mistakes:

**Tool authors cannot declare the class.** They do not know the task. A static label would be wrong
whenever the task moved — which is why the correct locus for classification is the harness, which
*does* know the task.

**"CLIs are the wrong surface" is too blunt to be true.** A CLI's *stdout* is a ground exporter, and
its *exit code* is a verifier. The critique that survives is narrower and better: **a CLI exposes a
human interface to a model actor** — output dense, unstructured, and optimised for a human's judgment
store, which is the wrong demand profile for a capacity-bounded actor. That is an argument about
*affordance*, not about CLIs being bad, and it disappears the moment you consume the exit code
instead of the text.

---

## 4. Worked example: MCP

MCP's six primitives, read for demand consequence.

**Server-side**

| Primitive | Demand consequence |
|---|---|
| **Resources** | **Exports ground.** Read-only content returned for the actor to interpret; every structural inference it then makes is an open decision the call created. |
| **Tools** | **Any of the three classes.** `read_file` exports, `find_definition` resolves, `run_tests` verifies — one primitive, three demand profiles. |
| **Prompts** | **Encoded decisions, shipped.** A reusable template is pre-resolved specification: the encoded store, exposed over the protocol. |

**Client-side**

| Primitive | Demand consequence |
|---|---|
| **Roots** | **Bounds the ground.** Declares what is in scope — a ground-scoping primitive, and the only one that limits volume. |
| **Sampling** | **Seam demand, made explicit.** A server that requests a completion has hit a decision it cannot resolve and hands it to a model actor. This is `core/06`'s seam, visible in a protocol. |
| **Elicitation** | **Escape prevention.** A server that cannot resolve something and *asks the user* is refusing to let the decision escape, routing it to a human judgment store instead of guessing. The matched-pair discipline, protocol-level. |

### 4.1 What no capability protocol currently declares

**MCP's type system does not distinguish the three classes.** `read_file`, `find_definition`, and
`run_tests` are all *tools*: same primitive, same schema shape, radically different consequences for
the actor's residual. The protocol declares that a capability **exists** and what arguments it takes.
It declares nothing about **what invoking it does to the caller's decision residual.**

> **Capability protocols declare capability. They do not declare demand consequence.** Two tools with
> identical schemas can leave an actor with wildly different open sets.

**And the default is floor-exposed.** A tool's `outputSchema`, where present, pins **shape** — but
shape conformance is not correctness. A tool returning shape-valid output that nothing checks for
*correctness* is **specification without verification** (`apparatus/the-skill-floor.md`), exposed over
a protocol, with the protocol's blessing. The path of least resistance — declare a schema, ship —
produces exactly the floor-exposed case.

*Stated as a structural observation, not a criticism of MCP: **no** capability protocol in current use
declares demand consequences, and it would be odd to single one out. The point is that the property is
absent from the layer, and something above the layer must supply it.*

---

## 5. What this makes possible

The harness's job, and it is **diagnostic rather than optimising** — which matters, because it
sidesteps the unmeasured `C_resolve` (`core/10` §7) entirely.

> **Compute the open decision set under a candidate toolset, and show the user what remains open.**

You do not need to know an actor's capacity to say: *"with file-reading, these seven decisions are
unverified; swap to the language server and four become mechanical; add the test runner and two more
convert from escape to retry."* That is a **ranking over toolsets**, not an absolute optimum, and
ranking is what a user actually needs.

The exercise this supports — *closing the predicate by choosing tools* — is the practical form of
`core/03`. You cannot lower a task's floor by trying harder. You lower it by **acquiring a mechanism
that resolves or verifies what was previously left to judgment.**

Three moves, in order of value:

1. **Add verifiers.** Converts escape into retry (`core/10` §3, Test 3). The only move that removes
   floor-escape rather than relocating it.
2. **Replace exporters with resolvers.** Attacks both terms of `escape = open_residual × p_err(load)`
   at once: fewer open decisions *and* lower resolve load, since the resolution happens outside the
   window.
3. **Bound the ground.** Roots-style scoping caps the volume an exporter can dump, limiting the load
   term when an exporter cannot be replaced.

---

## 6. The one line

> **Tools reallocate demand. An exporter hands the actor decisions and no checker; a resolver makes
> the decision elsewhere and returns the answer; a verifier supplies the closing predicate that turns
> escape into retry. Class is a property of the call on the task, not of the tool — and choosing the
> toolset is choosing the floor.**
