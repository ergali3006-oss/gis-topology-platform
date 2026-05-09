from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(title="GIS Topology QA/QC API", version="0.1.0")


class TopologyRunRequest(BaseModel):
    dataset_id: str
    ruleset: str | None = "default"


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/upload")
async def upload(file: UploadFile = File(...)) -> dict:
    dataset_id = str(uuid4())
    return {
        "dataset_id": dataset_id,
        "filename": file.filename,
        "status": "uploaded",
    }


@app.post("/api/scan/{dataset_id}")
def scan(dataset_id: str) -> dict:
    return {
        "dataset_id": dataset_id,
        "status": "scanned",
        "layers_detected": 0,
    }


@app.post("/api/topology/run")
def run_topology(payload: TopologyRunRequest) -> dict:
    return {
        "dataset_id": payload.dataset_id,
        "ruleset": payload.ruleset,
        "status": "queued",
    }


@app.get("/api/errors")
def get_errors() -> dict:
    return {"items": []}


@app.get("/api/reports/{dataset_id}")
def get_report(dataset_id: str) -> dict:
    return {
        "dataset_id": dataset_id,
        "formats": ["pdf", "html", "xlsx", "json"],
        "status": "not_generated",
    }
