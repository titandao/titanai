<div align="center">

<h1 align="center">TitanAI</h1>

本地化 AI 聊天 Web 应用，支持 LM Studio / Ollama 等本地模型后端。

</div>

TitanAI 基于 [NextChat](https://github.com/ChatGPTNextWeb/NextChat) 定制，专注本地私有化部署。

---

## 功能特性

- **本地模型支持**：对接 LM Studio、Ollama 等本地推理引擎
- **多模型支持**：OpenAI / Claude / Gemini / DeepSeek 等远程 API 均可
- **隐私优先**：所有数据存储在浏览器本地
- **Markdown 渲染**：支持 LaTeX、Mermaid 图表、代码高亮
- **对话管理**：创建、分享、导出对话记录
- **面具 (Mask)**：预设 Prompt 模板，一键切换角色
- **插件系统**：支持联网搜索、计算器等扩展功能
- **Artifacts**：独立窗口预览和分享 AI 生成内容
- **MCP 协议**：支持 Model Context Protocol 工具调用
- **深色模式**：支持亮色/暗色主题切换

---

## 快速开始

### 前置准备

- [Node.js](https://nodejs.org/) 18+ 和 [Yarn](https://yarnpkg.com/)
- （可选）[LM Studio](https://lmstudio.ai) 或 [Ollama](https://ollama.ai) 用于本地模型

### 本地开发

```shell
# 1. 安装依赖
yarn install

# 2. 创建环境变量文件 .env.local

# 选项 A：使用 LM Studio 本地模型（推荐）
#    OPENAI_API_KEY=sk-1234
#    BASE_URL=http://localhost:1234/v1
#    CUSTOM_MODELS=-all,+google/gemma-4-e2b

# 选项 B：使用远程 API（如 OpenAI）
#    OPENAI_API_KEY=sk-xxxx
#    BASE_URL=https://api.openai.com

# 3. 启动开发服务器
yarn dev
```

> **LM Studio 使用说明**：加载模型 → 右侧面板点击 "Start Server"（默认端口 1234）→ `BASE_URL` 设为 `http://localhost:1234/v1` 即可。`OPENAI_API_KEY` 任意值均可（LM Studio 不校验）。

### Docker 部署（本地构建）

```shell
# 1. 构建本地镜像
docker build -t titanai .

# 2. 运行容器
docker run -d -p 7777:3000 \
   -e OPENAI_API_KEY=sk-1234 \
   -e BASE_URL=http://host.docker.internal:1234/v1 \
   -e CUSTOM_MODELS=-all,+google/gemma-4-e2b \
   titanai
```

或用 docker-compose：

```shell
# 创建 .env 文件，填入环境变量
echo "OPENAI_API_KEY=sk-1234" > .env
echo "BASE_URL=http://host.docker.internal:1234/v1" >> .env
echo "CUSTOM_MODELS=-all,+google/gemma-4-e2b" >> .env

# 构建并启动
docker compose up -d
```

---

## 环境变量

### 核心配置

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `OPENAI_API_KEY` | ✅ | API Key，LM Studio 可填 `sk-1234` |
| `BASE_URL` | ❌ | API 接口地址，默认 `https://api.openai.com` |
| `CODE` | ❌ | 页面访问密码，多个用逗号分隔 |
| `CUSTOM_MODELS` | ❌ | 自定义模型列表，`+` 添加、`-` 隐藏、`=` 重命名 |

### 多模型 API Key

| 变量名 | 说明 |
|--------|------|
| `GOOGLE_API_KEY` | Google Gemini |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `AZURE_API_KEY` | Azure OpenAI |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `CHATGLM_API_KEY` | 智谱 ChatGLM |
| `ALIBABA_API_KEY` | 阿里千问 |
| `BAIDU_API_KEY` + `BAIDU_SECRET_KEY` | 百度文心 |
| `BYTEDANCE_API_KEY` | 字节豆包 |
| `SILICONFLOW_API_KEY` | SiliconFlow |
| `IFLYTEK_API_KEY` + `IFLYTEK_API_SECRET` | 讯飞星火 |

### 功能开关

| 变量名 | 说明 |
|--------|------|
| `ENABLE_MCP` | 设为 `true` 启用 MCP 协议支持 |
| `HIDE_USER_API_KEY` | 设为 `1` 隐藏用户自行填入 API Key 的入口 |
| `DEFAULT_MODEL` | 更改默认模型 |
| `DISABLE_FAST_LINK` | 设为 `1` 禁用从链接解析预设 |

---

## 使用指南

### 基础对话

1. 在输入框中输入消息，按 Enter 发送。
2. 点击左上角的聊天记录按钮管理对话列表。
3. 点击右上角的设置按钮配置模型、API Key 等参数。

### 面具 (Masks)

面具是可重复使用的 Prompt 模板。点击侧边栏面具图标进入面具市场，点击"新建面具"创建自定义面具。

### 插件

支持联网搜索、计算器等扩展功能。点击输入框上方的插件按钮启用。

### MCP (Model Context Protocol)

1. 环境变量设置 `ENABLE_MCP=true`
2. 在设置页面配置 MCP 服务器
3. AI 即可通过 MCP 调用文件读写、API 请求等工具

### 数据导入导出

- **导出**：设置 → 导出数据 → JSON 文件
- **导入**：设置 → 导入数据 → 选择 JSON 文件
- **WebDAV 同步**：配置 WebDAV 地址后多设备同步

---

## 常见问题

### Docker 中连接宿主机 LM Studio

Docker 容器内使用 `host.docker.internal` 替代 `localhost`：

```shell
-e BASE_URL=http://host.docker.internal:1234/v1
```

### 如何自定义模型列表

```shell
# 隐藏所有默认模型，只显示本地模型
CUSTOM_MODELS=-all,+your-model-name

# 隐藏特定模型
CUSTOM_MODELS=-gpt-3.5-turbo

# 重命名模型
CUSTOM_MODELS=gpt-4=我的模型
```

---

## 开源协议

[MIT](https://opensource.org/license/mit/)
