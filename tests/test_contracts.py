import json
from pathlib import Path

from ecp.contracts import ExecutionRequest, ExecutionResult, LaneDecision, TaskProposal
from ecp.contracts.execution_result import Artifact
from ecp.validation.json_schema import validate_contract
from ecp.vocabulary.artifact import ArtifactType
from ecp.vocabulary.lane import LaneType
from ecp.vocabulary.status import ExecutionStatus


def test_models_import_and_construct():
    tp = TaskProposal(title="T", objective="O")
    ld = LaneDecision(task_id="tp-1", lane=LaneType.CODING_AGENT)
    erq = ExecutionRequest(task_id="tp-1", lane_decision_id="ld-1", scope="s")
    ers = ExecutionResult(
        request_id="erq-1",
        ok=True,
        status=ExecutionStatus.SUCCEEDED,
        artifacts=[Artifact(artifact_type=ArtifactType.OUTPUT, uri="file://out.txt")],
    )

    assert tp.contract_kind == "task_proposal"
    assert ld.contract_kind == "lane_decision"
    assert erq.contract_kind == "execution_request"
    assert ers.contract_kind == "execution_result"


def test_examples_validate_against_json_schema():
    examples_dir = Path("examples/v0.1")
    for path in examples_dir.glob("*.json"):
        payload = json.loads(path.read_text())
        validate_contract(payload["contract_kind"], payload)


def test_roundtrip_serialization_dict_shape():
    result = ExecutionResult(request_id="erq-9", ok=False, status=ExecutionStatus.FAILED)
    payload = result.to_dict()

    assert payload["schema_version"] == "0.1"
    assert payload["contract_kind"] == "execution_result"
    assert payload["status"] == "failed"
