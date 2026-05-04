# Day 3: Docker & Kubernetes

## Learning objectives

- Write a **multi-stage Dockerfile** for the FastAPI app (deps layer vs code layer).
- Author minimal **Deployment + Service** YAML with **readiness** probe hitting `/health`.

## Hands-on

1. Add `Dockerfile` (if not present) building `uvicorn` entrypoint for `labs.week7.rag_service:app` or your service module.
2. `docker build` + `docker run -p 8000:8000` locally.
3. Write **resource requests/limits** assuming 2 vCPU / 4Gi — justify numbers.

## Concepts

- **GPU vs CPU** scheduling for embeddings — node selectors / tolerations.

## Done when

- [ ] `docker run` command in README snippet.
- [ ] Health probe path documented.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#cross-cutting) — Docker & Kubernetes videos
