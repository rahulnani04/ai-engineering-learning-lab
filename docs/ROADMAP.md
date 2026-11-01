# Learning roadmap — all concept groups

Each row is a deliverable: README explaining what/why/how/trade-offs; source code; unit and integration tests; failure scenario; 90-second verbal walkthrough. Never claim project simulation equals employer experience.

| Lab | Build | Concepts |
|---|---|---|
| 01 | Synthetic inquiry API (started) | Functions/classes/types, exceptions, decorators, contexts, generators, asyncio/threads/processes, logging, unit tests, FastAPI, Pydantic, DI, HTTP, middleware, OpenAPI, SSE, timeouts/retries/backoff, circuit breaker, pool, rate limit, cache, idempotency; Flask/Django/DRF comparison |
| 02 | Document search engine | Vectors, embeddings, cosine, exact/approx NN, HNSW, PostgreSQL full-text, pgvector, metadata filtering, hybrid search, rerank, grounding/citations |
| 03 | LLM gateway | Tokens, context window, temperature, inference, model routing, fallback, rate limits, latency/cost; system/user prompts, zero/few-shot, structured JSON Schema validation, prompt versioning/regression |
| 04 | Stateful synthetic workflow | LangGraph nodes/edges/conditions/state/typed state, supervisor/specialists, checkpoints, thread ID, human interrupt/resume, bounded retries, stop conditions |
| 05 | Tool connector and permissions | MCP host/client/server, tool/schema/resource/prompt/discovery/auth/audit; mock enterprise REST API |
| 06 | Document extraction comparison | RAG vs fine-tuning, domain extraction, LoRA/QLoRA concept, citation/permission separation |
| 07 | Containerize API | Docker, Kubernetes pod/deployment/service/ingress/namespace/configmap/secret, readiness/liveness, HPA, requests/limits; AKS vs Container Apps |
| 08 | Azure platform blueprint | Azure OpenAI, AKS, Container Apps/Jobs, Static Web Apps, ACR, PostgreSQL, APIM, Key Vault, AI Foundry, Content Safety, Databricks, Azure Monitor, App Insights; diagrams and mock adapters (not live provisioning) |
| 09 | Secure API | Entra ID, OAuth2, OIDC, JWT, RBAC, Key Vault, managed/workload identity, CSI driver, OIDC federation, VNet/subnets/private endpoint/DNS/NSG/private AKS/public access; implement local signed JWT verifier and threat tests |
| 10 | Production quality dashboard | Correctness, groundedness, retrieval relevance, tool selection, citations, latency, token usage, cost, failure rate; OpenTelemetry, App Insights, Azure Monitor, LangSmith; unit/integration/contract/e2e/regression/negative/mock/eval tests |
| 11 | Event-driven ETL | Pandas vs PySpark, Kafka producer/consumer/topic/partition/group/offset/lag, DLQ, at-least-once/idempotence, Airflow, SQL and Databricks concepts |
| 12 | Classical ML baseline | Train/validation/test, overfit/underfit, CV, hyperparameter tuning, leakage, scaling, Pandas, NumPy, sklearn, metrics, recommendations, MLflow concepts |
| 13 | React dashboard | Components, props, state, hooks, TypeScript types, API, SSE, errors and SSO integration patterns |
| 14 | Delivery pipeline | Git, Jenkins versus GitHub Actions, Jira/Agile workflow, code reviews, ADRs, runbooks, RCA, Helm, Kustomize, ArgoCD, Terraform; local CI plus infrastructure diagrams |
| 15 | AWS equivalents | Bedrock, S3, Lambda, EC2, EKS/ECS, RDS, DynamoDB, EventBridge, IAM, VPC, CloudWatch, KMS, Secrets Manager, Step Functions, SQS, API Gateway: mock adapters and comparison tables |
| 16 | GCP equivalents | Vertex AI, Gemini, Model Garden, GKE, Cloud Run, BigQuery, Storage, Pub/Sub, Logging, Secret Manager, Workload Identity: mock adapters |
| 17 | Network observability | SNMP polling/traps, MIB/OID, EMS/NMS, nGeniusOne concepts, SPL/ELK/time-series, AIOps/event correlation/anomaly detection/MTTD/MTTR; synthetic events |
| 18 | Capstone | Integrate synthetic UI, API, RAG, graph, mock tools, validation, monitoring, safe deployment and quality gates |

## Done definition for every item
- [ ] Explain it plainly without notes
- [ ] Build a working minimal example (or explicitly mark as a cloud-specific configuration concept)
- [ ] Add at least one normal test and one failure/edge test
- [ ] Show an observable result
- [ ] Compare one viable alternative and a trade-off
- [ ] Explain your personal contribution accurately
