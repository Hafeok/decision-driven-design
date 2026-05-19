# Contributing

The most useful contributions to this framework are not edits to the text — they are pressure on the ideas from domains the framework hasn't been applied to yet.

## What's most welcome

**Pressure-testing in a new domain.** If you've tried to apply this thinking somewhere — your sales process, a research pipeline, a clinical workflow, a robotics stack, anything — and found a place where the vocabulary breaks down or where you had to invent new constructs, open an issue or discussion. The framework has been pressure-tested mostly in software development; expanding the surface area is where it gets sharper.

**Counter-examples and missing cases.** Decisions that don't fit the schema. Artifacts that don't compose. Audit principles that don't hold. Roles that resist the per-role autonomy framing. These are the most useful contributions — they're how the framework finds its actual edges.

**Concrete worked examples.** A mapping of a specific real process using DDD's vocabulary, even partial. These are valuable because they reveal which constructs do real work and which are mostly scaffolding.

## What I'm less interested in

**Generic polish to the writing.** The documents are versioned artifacts and will be revised against measurement evidence — primarily, evidence from the reference implementation contacting reality and from new domains pressure-testing the constructs. Stylistic edits are welcome on issues that affect clarity but won't be the primary axis of revision.

**Adding more taxonomy without forcing function.** New entity types, new flow classes, new measurement classes — these tend to expand faster than they earn their keep. If a proposed addition can't be tied to a specific decision the framework currently can't express or a specific failure mode it currently can't catch, it's probably scaffolding.

## How to engage

- **Issues** for specific friction points, gaps, or counter-examples.
- **Discussions** for broader questions about applicability, framing, or how DDD relates to adjacent ideas (event sourcing, process mining, BPM, agentic AI frameworks, etc.).
- **Pull requests** on the documents are accepted but should be accompanied by an issue or discussion that establishes the friction motivating the change.

## On the reference implementation

The reference implementation lives at **[github.com/Hafeok/product-cli](https://github.com/Hafeok/product-cli)**. Issues specific to the implementation belong there. This repository is the framework specification; that repository is one realization of it.

## Tone

Direct is fine. The framework's stance is opinionated — it makes claims about what the unit of work is, what counts as a value action, what the audit principle should be. Disagreement that engages those claims directly is more useful than diplomatic hedging.
