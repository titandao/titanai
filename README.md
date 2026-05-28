<h1 align="center">TitanAI</h1>

English / [简体中文](./README_CN.md)

A local-first AI chat web application. Works with LM Studio, Ollama, or any OpenAI-compatible API.

---

## Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) 18+ and [Yarn](https://yarnpkg.com/)
- (Optional) [LM Studio](https://lmstudio.ai) or [Ollama](https://ollama.ai) for local models

### Local Development

```shell
# 1. Install dependencies
yarn install

# 2. Create .env.local

# Option A: Use LM Studio (local, free, offline)
#    OPENAI_API_KEY=sk-1234
#    BASE_URL=http://localhost:1234/v1
#    CUSTOM_MODELS=-all,+google/gemma-4-e2b

# Option B: Use remote API (OpenAI, etc.)
#    OPENAI_API_KEY=sk-xxxx
#    BASE_URL=https://api.openai.com

# 3. Start dev server
yarn dev
```

> **LM Studio**: Load a model → Click "Start Server" (default port 1234) → Set `BASE_URL=http://localhost:1234/v1`. LM Studio doesn't validate the API key.

### Docker (Build Locally)

```shell
# 1. Build image from local files
docker build -t titanai .

# 2. Run container
docker run -d -p 7777:3000 \
   -e OPENAI_API_KEY=sk-1234 \
   -e BASE_URL=http://host.docker.internal:1234/v1 \
   -e CUSTOM_MODELS=-all,+google/gemma-4-e2b \
   titanai
```

Or with docker-compose:

```shell
echo "OPENAI_API_KEY=sk-1234" > .env
docker compose up -d
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | ✅ | API Key (use `sk-1234` for LM Studio) |
| `BASE_URL` | ❌ | API base URL, default `https://api.openai.com` |
| `CODE` | ❌ | Access password, comma separated |
| `CUSTOM_MODELS` | ❌ | Custom model list: `+` add, `-` hide, `=` rename |

### Feature Flags

| Variable | Description |
|----------|-------------|
| `ENABLE_MCP` | Set `true` to enable MCP protocol |
| `HIDE_USER_API_KEY` | Set `1` to hide user API key input |
| `DEFAULT_MODEL` | Change default model |

---

## Features

- **Local-first**: LM Studio, Ollama, or any OpenAI-compatible backend
- **Privacy**: All data stored locally in browser
- **Markdown**: LaTeX, Mermaid, code highlighting
- **Masks**: Reusable prompt templates
- **Plugins**: Web search, calculator, and more
- **Artifacts**: Preview AI-generated content in a separate window
- **MCP**: Model Context Protocol tool calling
- **Dark mode**: Light/dark theme

---

## License

[MIT](https://opensource.org/license/mit/)
