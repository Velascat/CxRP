# CxRP Documentation

Index for the `docs/` tree. The README covers protocol scope and core contract
types; this directory holds the version-specific spec, integration guides for
each consumer, and architecture notes about boundary rules and compatibility.

## Spec

- [spec/v0.1.md](spec/v0.1.md) — Frozen v0.1 spec (retained for historical interop).
- [spec/v0.2.md](spec/v0.2.md) — Active spec.
- [spec/execution_target.md](spec/execution_target.md) — `ExecutionTargetEnvelope`
  shape: `lane` (typed) + `backend/executor` + optional `runtime_binding`.

## Architecture

- [architecture/boundary_rules.md](architecture/boundary_rules.md) — What
  belongs in CxRP vs. consumer repos; the "contract-only" line.
- [architecture/compatibility.md](architecture/compatibility.md) — Versioning,
  schema_version semantics, and the contract-evolution policy.
- [architecture/lifecycle.md](architecture/lifecycle.md) — How a CxRP message
  flows through the platform (TaskProposal → LaneDecision → ExecutionRequest →
  ExecutionResult).

## Integrations

How each consumer maps CxRP types to its internal models:

- [integrations/operations_center.md](integrations/operations_center.md)
- [integrations/operator_console.md](integrations/operator_console.md)
- [integrations/switchboard.md](integrations/switchboard.md)
