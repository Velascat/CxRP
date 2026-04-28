# Execution Contract Protocol (ECP)

Execution Contract Protocol is a **contract-only specification** that defines the shared language exchanged between:

- **OperatorConsole** (entrypoint)
- **SwitchBoard** (routing and lane selection)
- **OperationsCenter** (execution orchestration)

ECP defines **what systems say to each other**, not how they run.

## What ECP Is

- Versioned contract models.
- Canonical vocabulary enums.
- JSON Schemas for validation.
- Example payloads for interoperable integration.

## What ECP Is Not

ECP excludes implementation logic, including:

- execution logic
- routing logic
- scheduling/watchers
- subprocess execution
- model/provider integrations
- adapters
- queue systems

## Core Contracts (v0.1)

1. `TaskProposal` — expresses requested work intent.
2. `LaneDecision` — records chosen lane/backend by SwitchBoard.
3. `ExecutionRequest` — defines bounded work unit for execution.
4. `ExecutionResult` — reports normalized outcome (`ok`, `status`, optional `artifacts`, optional `diagnostics`).

## Repository Layout

- `ecp/contracts/`: Python contract models.
- `ecp/vocabulary/`: canonical enums (`status`, `lane`, `artifact`).
- `ecp/validation/`: schema loading and validation helper.
- `schemas/v0.1/`: JSON Schemas for the four canonical contracts.
- `examples/v0.1/`: minimal interoperable examples.
- `docs/spec/v0.1.md`: versioned normative summary.

## Inter-system Relationship

- OperatorConsole emits or captures `TaskProposal`.
- SwitchBoard consumes `TaskProposal` and emits `LaneDecision`.
- OperationsCenter consumes `TaskProposal` + `LaneDecision` and emits `ExecutionRequest`.
- Execution systems return `ExecutionResult` for downstream consumption.

## Versioning

All contracts include `schema_version = "0.1"` and `contract_kind` as canonical discriminators.
