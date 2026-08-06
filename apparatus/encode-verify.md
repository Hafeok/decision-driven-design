# Encode / Verify

**Apparatus.** This is the operational rule that the core principle produces once you notice that
some ground is yours and some is not. It is the spine of the reference tooling (`applications/sdlc`).

---

**Upstream basis.** This document is part of the software projection; it builds on the
principle repo's canon (`actor-indexed-determination`). The `core/NN` references below resolve
there, pinned at a version and a status in `graph/upstream.yaml`:

<!-- ddd:ref id=term:determination -->
<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=term:seam-identity -->

## The rule

> **You can encode ground you control.**
> **You must mechanically verify ground you don't.**

Ground is the read-only surface an actor inspects in order to act (`core/00`). Some of it you own —
your source, your config, your schemas. Some of it you do not — a third-party API, a live
environment, another team's service. The rule says these get different treatment, and the difference
is not stylistic.

---

## Uncontrolled ground is two facts, never one

Any ground outside your control is **two facts**:

- **Your copy** — the pinned package, the vendored schema, the generated client, the declared secret
  reference. Local, encodable, and **always at risk of being stale.**
- **The source of truth** — what the other system actually emits, or what the environment actually
  contains, *right now.* Remote, mutable, **moves without asking.**

A lockfile pins the first. **It cannot pin the second.** That gap — between your copy and the source
of truth — is where production outages live: the build stays green, every test passes, and the
service fails on the first message that carries what your copy didn't know about.

---

## Why you cannot encode your way out

The tempting shortcut: *verify once, encode the result, and read the encoding thereafter.* You did
verify, and encoding amortises — so why re-check?

Because **encoding a verification result converts a criterion into a constraint, and a criterion over
uncontrolled ground cannot be converted.** The whole content of "you don't control it" is that it
moves *after* you looked. An encoded observation of uncontrolled ground is a belief with an expiry
date and no alarm on it.

> **You cannot amortise an observation of something you do not control.**
>
> **Each act requires its own observation. That cost is irreducible — it is the price of the ground
> being someone else's.**

This is the same shape as the floor (`core/03`): a cost that cannot be moved, only paid. Trying to
amortise it does not remove the cost; it converts a *known* cost into an *unknown* risk.

---

## The instances are one rule

The rule is not about APIs. It is about *anything you do not control*, and it has at least four
instances that are the same failure in different costumes:

| Your copy | The source of truth | Fails as |
|---|---|---|
| DTO in a client package | the service's live OpenAPI | serialization error in prod |
| Bicep secret reference | the actual Key Vault | null config at startup |
| Feature-flag default | App Configuration in that environment | wrong behaviour, silently |
| Resolved resource name | what the cloud will actually accept | rejected at deploy, mid-template |

**The environment itself is ground you do not control.** Someone rotated a secret, flipped a flag,
deleted a config entry during an incident. None of it touches your repo. Your build stays green. Your
copy is now a lie.

---

## The consequence: verify on a schedule, not on build

If verification only fires when you build, it will **never fire** — because nothing on *your* side
changed; the drift is on *theirs*. A build-triggered check on uncontrolled ground is a check that
watches the wrong clock.

> Move `verify` to a **schedule** (cron), not a build trigger. This converts a **silent escape** — a
> decision collected in production — into a **visible staleness** that fires in CI on a Tuesday
> morning. Strictly better, and not because it is cheaper: because it is **visible**, and a failure
> you can see has a store watching it.

The flu vaccine is the biological instance: re-harvested annually because the virus is ground you do
not control, so the encoding goes stale and must be re-verified against a moving source of truth
(`core/06`, and `apparatus/closure-principle.md` on original antigenic sin).

---

## Relation to the closure principle

Encode/verify tells you to re-read ground you don't control. `apparatus/closure-principle.md` tells
you *why re-reading matters even for ground you think you do control*: the moment you consume your own
prior output as ground, you have closed a loop with no corrective term. The two are complementary —
one is about ground you never controlled, the other about ground you corrupted by caching your own
belief about it.

Together they yield the single discipline the tooling enforces: **re-read the world, every time; and
never mistake your record of the world for the world.**

---

## The one line

> **Encode what you own. Verify what you don't — on a schedule, because their truth moves on their
> clock, not yours — and never encode an observation of something you cannot control, because that
> just hides the staleness instead of removing it.**
