FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-venv git ca-certificates jq ripgrep && rm -rf /var/lib/apt/lists/*
RUN npm install -g @openai/codex@0.118.0 @anthropic-ai/claude-code@2.1.98 @mariozechner/pi-coding-agent@0.73.0
RUN mkdir -p /home/node/workspace && chown node:node /home/node/workspace
COPY --chown=node:node AGENTS.md /home/node/workspace/AGENTS.md
COPY --chown=node:node AGENTS.md /home/node/workspace/CLAUDE.md
USER node
ENV PYTHONUNBUFFERED=1
WORKDIR /home/node/workspace
