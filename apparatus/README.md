# apparatus/

Operational results that fall out of `core/`. These are the mechanisms — the parts you implement and
enforce. Each depends on core; none is depended on *by* core.

- **encode-verify** · *encode ground you control; verify ground you don't* — and verify on a schedule, because their truth moves on their clock
- **closure-principle** · *an actor's own output is not ground* — poisoned ground, estimator divergence, and why a tool with a state file can delete your database
- **adversarial-ground** · the attack surface of an actor is its ground, not its logic — the same mechanism across intelligence, cybersecurity, and immunology
- **the-skill-floor** · a skill is specification without verification, therefore floor-exposed; trustworthiness is the fraction of behaviour that ships a fail-closed verifier

All three are instances of one discipline: **re-read the world every time, and never mistake your
record of the world for the world.**
