# Cairn | General problem-solving engine

Torsionfield fork of [Cairn](https://github.com/oritera/Cairn). Upstream attribution and license are retained. This fork focuses on constructive scientific research, mathematics, engineering, software development and optimization.

A shared blackboard stores confirmed facts, proposed intents and human hints. Workers bootstrap, reason over the current graph, and explore independent directions. Completion requires evidence satisfying the stated goal. Failed experiments are useful facts; hypotheses remain provisional until tested.

The general profile replaces CTF instructions and the Kali image with a neutral worker environment. It retains the upstream graph protocol, scheduler, worker adapters and UI. Worker permissions are not bypassed by the Codex or Claude adapters.

Example problems:

- Find and prove a combinatorial identity using explicit derivations and numerical checks.
- Repair a regression in an owned repository with a failing test and a verified fix.
- Compare candidate numerical algorithms using reproducible local benchmarks.

## Getting Started

**Prerequisites**
 
- macOS or Linux
- Python ≥ 3.12
- Docker (container execution only — not needed for local mode)


### Pull required images
 
Container mode uses the general worker image built from this repository; local mode does not require it.
 
```bash
docker build -t cairn-general-worker:local container
```

Create your local dispatcher configuration and fill in your LLM endpoints and API keys:

```bash
cp dispatch.example.yaml dispatch.yaml
```
 
### Docker Compose (recommended)
 
Pull the base image used to build Cairn:
 
```bash
docker pull ghcr.io/astral-sh/uv:python3.13-trixie
```
 
```bash
docker compose up --build
```
 
This starts `cairn-server` on port `8000` and `cairn-dispatcher` once the server passes its health check. The dispatcher mounts `dispatch.yaml` from the project root and connects to Docker via the host socket. Data is persisted to `./datas/cairn/`.
 
### Manual
 
```bash
# Start the server
uv run --project cairn cairn serve
 
# Run the dispatcher
uv run --project cairn cairn dispatch --config dispatch.yaml
 
# Run startup health checks only
uv run --project cairn cairn dispatch --config dispatch.yaml --startup-healthcheck-only
```

### Local mode (no Docker)

Instead of one container per project, workers can run directly on the dispatcher host, reusing the machine's already-configured `claude` / `codex` / `pi` CLIs — no Docker, and no API keys in the config.

```bash
cp dispatch.local.example.yaml dispatch.yaml

# Start the server
uv run --project cairn cairn serve

# Run the dispatcher on the same host, where the CLIs are installed and logged in
uv run --project cairn cairn dispatch --config dispatch.yaml
```

Local mode is selected by `runtime.execution: local` (see `dispatch.local.example.yaml`). On startup the dispatcher checks each configured worker CLI is installed and runnable, and reminds you they must already be logged in. Each project gets an isolated working directory under `local.workspace_root` (default: the dispatcher's current directory). Run the dispatcher directly on the host — not inside Docker — since some agent backends can access host resources.

### Tests

Run the fast regression suite without Docker or live model endpoints:

```bash
uv run --project cairn --group dev pytest
```

## Scope

Use authorized project resources for constructive problem solving. A model's assertion of completion is not independent proof; inspect the underlying evidence.

## ⚖️ License
This project is licensed under **GNU AGPLv3** for personal and educational use.

**Commercial Use**: If you wish to use this project in a commercial or proprietary environment without the AGPL-3.0 open-source obligations, **please contact me to obtain a commercial license.**

**Contributions**: By submitting a Pull Request, you agree that your contributions may be used under both the AGPL-3.0 and the project's commercial license.
