<h1 align="center">TitanGPT</h1>

English / [简体中文](./README_CN.md)

A local-first AI chat web application. Works with LM Studio, Ollama, or any OpenAI-compatible API. All data is stored in your browser — no cloud, no registration required.

---

## Features

### Model Support
- **Local engines**: LM Studio, Ollama, or any OpenAI-compatible local inference server
- **Remote APIs**: OpenAI GPT-4o / o1, Anthropic Claude, Google Gemini, DeepSeek
- **Chinese LLMs**: ChatGLM, Qwen, Baidu Ernie, ByteDance Doubao, iFlytek Spark, SiliconFlow
- **Custom model list**: Add, hide, and rename models freely

### User Experience
- **Privacy-first**: Conversations and configs stay in your browser's local storage — zero server-side persistence
- **Markdown rendering**: LaTeX math, Mermaid diagrams, syntax-highlighted code blocks
- **Conversation management**: Multi-turn chats, history search, rename, export / import
- **Dark mode**: Light / Dark / Auto themes
- **i18n**: 20+ languages (English, Chinese, Japanese, Korean, French, German, Spanish, etc.)

### Advanced
- **Masks**: Reusable prompt templates with pre-set model parameters, one-click persona switching
- **Plugins**: Web search, calculator, and custom plugin extension
- **Artifacts**: Preview AI-generated HTML/SVG in a separate window, refresh and share
- **MCP (Model Context Protocol)**: Let AI call file I/O, REST APIs, and other tools
- **Real-time chat**: WebRTC-based voice conversation

---

## Quick Start

### Prerequisites

- **Node.js** 18+ ([download](https://nodejs.org/))
- **Yarn** (run `corepack enable && corepack prepare yarn@1 --activate` after installing Node.js)
- **LM Studio** ([download](https://lmstudio.ai)) — or any OpenAI-compatible API key

### Step 1: Install Dependencies

```shell
yarn install
```

### Step 2: Configure Environment

Create `.env.local` in the project root:

```shell
# Using LM Studio (recommended — free, offline)
OPENAI_API_KEY=sk-1234
BASE_URL=http://localhost:1234/v1
CUSTOM_MODELS=-all,+google/gemma-4-e2b
```

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | API key. LM Studio doesn't validate — any value works |
| `BASE_URL` | LM Studio server address (default port 1234) |
| `CUSTOM_MODELS=-all,+model` | Hide all defaults, show only your local model |

> Using a remote API? Use:
> ```shell
> OPENAI_API_KEY=sk-your-real-key
> BASE_URL=https://api.openai.com
> ```

### Step 3: Start Dev Server

```shell
yarn dev
```

Wait for `✓ Ready in` — then open `http://localhost:7777` in your browser.

### LM Studio Setup Guide

1. Open LM Studio, search and download a model (e.g. `google/gemma-4-e2b`, `Qwen2.5-7B`)
2. Switch to the right-side "Chat" panel, select your downloaded model
3. Click "Start Server" (default port 1234)
4. Verify the server is running:

```shell
curl http://localhost:1234/v1/models
```

The `id` field in the response is the exact model name to use in `CUSTOM_MODELS`.

5. In TitanGPT, select the model from the dropdown and start chatting.

> **Note**: On first launch, also check the Settings panel (top-right gear icon) to confirm the API Key and Base URL match your `.env.local`.

---

## Docker Deployment

### Build and Run

```shell
# Build image from local files
docker build -t titanai .

# Run container (mapping port 7777 on host to 3000 in container)
docker run -d -p 7777:3000 \
   --name titanai \
   -e OPENAI_API_KEY=sk-1234 \
   -e BASE_URL=http://host.docker.internal:1234/v1 \
   -e CUSTOM_MODELS=-all,+google/gemma-4-e2b \
   titanai
```

> **Important**: Inside Docker, `localhost` refers to the container, not your host machine. Use `host.docker.internal` to reach the host. Linux users need the `--add-host host.docker.internal:host-gateway` flag.

### Using docker-compose

```shell
# 1. Create .env file
cat > .env << EOF
OPENAI_API_KEY=sk-1234
BASE_URL=http://host.docker.internal:1234/v1
CUSTOM_MODELS=-all,+google/gemma-4-e2b
EOF

# 2. Build and start
docker compose up -d

# 3. View logs
docker compose logs -f

# 4. Stop
docker compose down
```

---

## Environment Variables

### Core

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | ✅ | — | API key. Use any string with LM Studio, `sk-` prefix for OpenAI |
| `BASE_URL` | ❌ | `https://api.openai.com` | API base URL. LM Studio: `http://localhost:1234/v1` |
| `CODE` | ❌ | — | Access password. Comma-separated for multiple passwords |
| `CUSTOM_MODELS` | ❌ | — | Custom model list (see syntax below) |

### `CUSTOM_MODELS` Syntax

```
+model-name      → Add model to list
-model-name      → Hide model from list
-all             → Hide all default models
model-name=Alias → Rename a model
@Azure=deploy    → Azure deployment mapping
```

Examples:

```shell
# Show only local model
CUSTOM_MODELS=-all,+google/gemma-4-e2b

# Hide specific models, add custom one
CUSTOM_MODELS=-gpt-3.5-turbo,-gpt-4,+my-custom-model

# Rename a model
CUSTOM_MODELS=gpt-4=GPT-4-Super
```

### Provider-Specific API Keys

| Variable | Provider |
|----------|----------|
| `GOOGLE_API_KEY` | Google Gemini |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `ANTHROPIC_URL` | Claude custom endpoint |
| `ANTHROPIC_API_VERSION` | Claude API version |
| `AZURE_API_KEY` | Azure OpenAI |
| `AZURE_URL` | Azure deployment URL |
| `AZURE_API_VERSION` | Azure API version |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `DEEPSEEK_URL` | DeepSeek custom endpoint |
| `CHATGLM_API_KEY` | ChatGLM |
| `CHATGLM_URL` | ChatGLM custom endpoint |
| `ALIBABA_API_KEY` | Alibaba Qwen |
| `ALIBABA_URL` | Qwen custom endpoint |
| `BAIDU_API_KEY` + `BAIDU_SECRET_KEY` | Baidu Ernie |
| `BAIDU_URL` | Ernie custom endpoint |
| `BYTEDANCE_API_KEY` | ByteDance Doubao |
| `BYTEDANCE_URL` | Doubao custom endpoint |
| `IFLYTEK_API_KEY` + `IFLYTEK_API_SECRET` | iFlytek Spark |
| `IFLYTEK_URL` | Spark custom endpoint |
| `SILICONFLOW_API_KEY` | SiliconFlow |
| `SILICONFLOW_URL` | SiliconFlow custom endpoint |
| `STABILITY_API_KEY` | Stability AI (image generation) |
| `STABILITY_URL` | Stability AI custom endpoint |

### Feature Flags

| Variable | Description |
|----------|-------------|
| `ENABLE_MCP` | Set `true` to enable MCP protocol |
| `HIDE_USER_API_KEY` | Set `1` to hide API key fields in the UI (forces env-only keys) |
| `DEFAULT_MODEL` | Set the default selected model |
| `DISABLE_GPT4` | Set `1` to hide GPT-4 models |
| `DISABLE_FAST_LINK` | Set `1` to disable config parsing from URL links |
| `ENABLE_BALANCE_QUERY` | Set `1` to show balance check in Settings |
| `DEFAULT_INPUT_TEMPLATE` | Custom default user input pre-processing template |

---

## User Guide

### Basic Chat

1. Type your message in the input box at the bottom
2. Press **Enter** to send, **Shift+Enter** for a new line
3. Click the chat icon (💬) in the top-left to manage conversation history
4. Click the gear icon (⚙️) in the top-right to open Settings
5. In Settings, switch models, adjust parameters, and configure API keys

### Settings Reference

- **Model**: Select which model to use for the current chat
- **Base URL**: Confirm the API endpoint
- **API Key**: Enter your key (if not set via environment variable)
- **Temperature**: Controls randomness (0-2). Higher = more creative
- **Top P**: Nucleus sampling, alternative to Temperature
- **Max Tokens**: Limit response length
- **Access Code**: Required if `CODE` env var is set

### Masks

Masks bundle a system prompt, model settings, and conversation config into a reusable template.

**Using a mask**:
1. Click the mask icon (🎭) in the sidebar
2. Pick a mask from the list
3. A new conversation starts with that mask pre-configured

**Creating a mask**:
1. Go to Masks, click "New Mask"
2. Fill in name, description, and system prompt
3. Set model parameters (model, temperature, etc.)
4. Save — it's ready to use

**Export / Import**: Masks can be exported as JSON files and shared.

### Plugins

Plugins extend the AI's capabilities:

- **Web Search**: Real-time internet search
- **Calculator**: Precise math computation

Click the plugins button (🧩) above the input box to enable/disable.

### Artifacts

When the AI generates HTML, SVG, or other renderable content, Artifacts opens it in a separate window for preview.

- Auto-opens with rendered output
- Refresh, copy code, or full-screen view
- Share Artifacts links with others

### MCP (Model Context Protocol)

MCP lets the AI call external tools:

1. Set `ENABLE_MCP=true` in `.env.local`
2. Open Settings → MCP Configuration
3. Add MCP servers (e.g., filesystem, REST API, database)
4. The AI can then use these tools on demand

**Common MCP servers**: file read/write, REST API calls, SQL queries.

### Data Management

- **Export**: Settings → Export → JSON file (all conversations, masks, and config)
- **Import**: Settings → Import → Select JSON file → Restore everything
- **WebDAV Sync**: Configure WebDAV to sync data across devices

---

## FAQ

### LM Studio Connection

**Q: Model list is empty?**

A: Make sure `CUSTOM_MODELS=-all,+your-model-name` is set correctly. Get the exact model name:

```shell
curl http://localhost:1234/v1/models
```

**Q: Connection refused?**

1. Did you click "Start Server" in LM Studio?
2. Is the port correct (1234 by default)?
3. Does `BASE_URL` end with `/v1`?

**Q: Docker can't reach LM Studio on the host?**

Use `host.docker.internal` instead of `localhost` inside the container. Linux users need `--add-host host.docker.internal:host-gateway`.

### Deployment

**Q: Blank page / long load time?**

The first compilation can take several seconds. Wait for `✓ Ready in` to appear in the terminal, then refresh the page.

**Q: "Port in use" error?**

```shell
# Check what's on port 7777
lsof -i:7777
# Kill it
kill -9 PID
```

**Q: Docker keeps showing "Update available"?**

Docker images track stable releases, which lag behind the latest commits by 1-2 days. This is normal and doesn't affect functionality.

### Usage

**Q: Gibberish responses?**

Lower `Temperature` to below 1 in Settings.

**Q: "Unauthorized, please enter access code"?**

If `CODE` is set, enter the access code in Settings on first use.

**Q: Lost conversations?**

Check if browser storage was cleared (incognito mode, cache cleanup). Regular exports are recommended.

**Q: "You exceeded your current quota"?**

Your API key has run out of credits or hit a rate limit. Check your API provider's dashboard.

---

## Project Structure

```
├── app/                    # Frontend source
│   ├── components/         # UI components
│   ├── locales/            # i18n language packs
│   ├── icons/              # SVG icons
│   ├── store/              # State management
│   ├── client/             # API clients
│   ├── masks/              # Preset masks
│   ├── styles/             # Global styles
│   └── utils/              # Utilities
├── public/                 # Static assets
├── docs/                   # Documentation
├── scripts/                # Scripts
├── src-tauri/              # Desktop app (Tauri)
├── Dockerfile              # Docker build
├── docker-compose.yml      # Docker Compose
└── package.json
```

---

## Development

```shell
# Install
yarn install

# Dev server with hot reload
yarn dev

# Production build
yarn build && yarn start
```

### Desktop App (Tauri)

```shell
# Dev mode
yarn app:dev

# Build installer
yarn app:build
```

---

## License

[MIT](https://opensource.org/license/mit/)
