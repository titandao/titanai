<div align="center">

<h1 align="center">TitanGPT</h1>

本地化 AI 聊天 Web 应用，支持 LM Studio / Ollama 等本地模型后端。

</div>

TitanGPT 基于 [NextChat](https://github.com/ChatGPTNextWeb/NextChat) 定制，专注本地私有化部署，所有数据存储在浏览器本地，无需云端、无需注册。

---

## 功能特性

### 模型接入
- **本地推理引擎**：对接 LM Studio、Ollama 等 OpenAI 兼容的本地推理服务
- **远程 API**：OpenAI GPT-4o / o1、Anthropic Claude、Google Gemini、DeepSeek 等
- **国内大模型**：智谱 ChatGLM、阿里千问、百度文心、字节豆包、讯飞星火、SiliconFlow
- **自定义模型列表**：自由增删改模型名称，支持模型重命名

### 用户体验
- **隐私优先**：所有对话记录、配置数据仅存储在浏览器本地，不经过任何服务器
- **Markdown 渲染**：完整支持 LaTeX 数学公式、Mermaid 流程图、代码高亮
- **对话管理**：创建多轮对话、历史记录检索、对话重命名、导出 / 导入
- **深色模式**：支持亮色 / 暗色主题一键切换，跟随系统自动适配
- **国际化**：界面支持中、英、日、韩、法、德、西等 20+ 语言

### 高级功能
- **面具 (Mask)**：预设 Prompt 模板 + 模型参数 + 对话设置，一键切换角色
- **插件系统**：内置联网搜索、计算器，支持自定义插件扩展
- **Artifacts**：AI 生成内容（HTML 页面等）在独立窗口预览、刷新、分享
- **MCP 协议**：Model Context Protocol，让 AI 调用文件读写、API 请求等外部工具
- **实时聊天**：支持 WebRTC 实时语音对话

---

## 快速开始

### 前置准备

- **Node.js** 18+（[下载](https://nodejs.org/)）
- **Yarn** 包管理器（安装 Node.js 后运行 `corepack enable && corepack prepare yarn@1 --activate`）
- **LM Studio**（[下载](https://lmstudio.ai)）用于本地运行模型
- 或者任意 OpenAI 兼容的 API Key

### 第一步：安装依赖

```shell
yarn install
```

### 第二步：配置环境变量

在项目根目录创建 `.env.local` 文件：

```shell
# 使用 LM Studio（推荐，免费离线）
OPENAI_API_KEY=sk-1234
BASE_URL=http://localhost:1234/v1
CUSTOM_MODELS=-all,+google/gemma-4-e2b
```

各参数说明：

| 参数 | 作用 |
|------|------|
| `OPENAI_API_KEY` | API 密钥，LM Studio 不校验，填任意值即可 |
| `BASE_URL` | LM Studio 服务地址，默认端口 1234 |
| `CUSTOM_MODELS=-all,+模型名` | 隐藏所有默认模型，仅显示你的本地模型 |

> 如果用远程 API，改为：
> ```shell
> OPENAI_API_KEY=sk-你的真实密钥
> BASE_URL=https://api.openai.com
> ```

### 第三步：启动开发服务器

```shell
yarn dev
```

看到 `✓ Ready in` 后，浏览器访问 `http://localhost:7777`。

首次加载时，页面会编译一会儿，之后响应会很快。

### LM Studio 详细配置

1. 打开 LM Studio，左侧搜索并下载一个模型（如 `google/gemma-4-e2b`、`Qwen2.5-7B`）
2. 切换到右侧 "Chat" 面板，选择已下载的模型
3. 点击顶部 "Start Server" 按钮（保持默认端口 1234）
4. 终端验证服务可用：

```shell
curl http://localhost:1234/v1/models
```

返回的 `id` 字段就是你在 `CUSTOM_MODELS` 中要填的模型名。

5. 在 TitanGPT 中，模型选择器选择该模型，开始对话。

> **提示**：首次启动时页面右上角设置中也需要确认 API Key 和 Base URL 与 `.env.local` 一致。

---

## Docker 部署

### 方式一：docker build 直接构建

```shell
# 构建镜像
docker build -t titanai .

# 运行容器（映射到宿主机 7777 端口）
docker run -d -p 7777:3000 \
   --name titanai \
   -e OPENAI_API_KEY=sk-1234 \
   -e BASE_URL=http://host.docker.internal:1234/v1 \
   -e CUSTOM_MODELS=-all,+google/gemma-4-e2b \
   titanai
```

> **注意**：容器内不能使用 `localhost` 访问宿主机服务，需用 `host.docker.internal`。Linux 用户需加 `--add-host host.docker.internal:host-gateway`。

### 方式二：docker-compose

```shell
# 1. 创建环境变量文件 .env
cat > .env << EOF
OPENAI_API_KEY=sk-1234
BASE_URL=http://host.docker.internal:1234/v1
CUSTOM_MODELS=-all,+google/gemma-4-e2b
EOF

# 2. 构建并启动
docker compose up -d

# 3. 查看日志
docker compose logs -f

# 4. 停止
docker compose down
```

`docker-compose.yml` 已配置端口映射 `7777:3000`，构建方式为 `build: .`（本地构建，不拉取远程镜像）。

---

## 环境变量详解

### 核心配置

| 变量名 | 必填 | 默认值 | 说明 |
|--------|------|--------|------|
| `OPENAI_API_KEY` | ✅ | 无 | API 密钥。LM Studio 用任意字符串，OpenAI 用 `sk-` 开头 |
| `BASE_URL` | ❌ | `https://api.openai.com` | API 接口地址。LM Studio 为 `http://localhost:1234/v1` |
| `CODE` | ❌ | 无 | 页面访问密码，多个密码用英文逗号分隔。不设置则任何人都可访问 |
| `CUSTOM_MODELS` | ❌ | 无 | 自定义模型列表（语法见下方） |

### `CUSTOM_MODELS` 语法

```
+模型名      → 添加模型到列表
-模型名      → 从列表隐藏模型
-所有关键字   → 隐藏所有默认模型
模型名=新名称 → 重命名模型
@Azure=部署名 → Azure 部署映射
```

示例：

```shell
# 仅显示本地模型
CUSTOM_MODELS=-all,+google/gemma-4-e2b

# 隐藏某些模型，添加自定义模型
CUSTOM_MODELS=-gpt-3.5-turbo,-gpt-4,+my-custom-model

# 重命名模型
CUSTOM_MODELS=gpt-4=GPT-4-超强版
```

### 多模型 API Key

以下变量用于同时配置多个 AI 服务商：

| 变量名 | 对应服务 |
|--------|---------|
| `GOOGLE_API_KEY` | Google Gemini |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `GOOGLE_URL` | Gemini 自定义接口地址 |
| `ANTHROPIC_URL` | Claude 自定义接口地址 |
| `ANTHROPIC_API_VERSION` | Claude API 版本 |
| `AZURE_API_KEY` | Azure OpenAI |
| `AZURE_URL` | Azure 部署地址 |
| `AZURE_API_VERSION` | Azure API 版本 |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `DEEPSEEK_URL` | DeepSeek 自定义接口 |
| `CHATGLM_API_KEY` | 智谱 ChatGLM |
| `CHATGLM_URL` | ChatGLM 自定义接口 |
| `ALIBABA_API_KEY` | 阿里千问 |
| `ALIBABA_URL` | 阿里千问自定义接口 |
| `BAIDU_API_KEY` | 百度文心 |
| `BAIDU_SECRET_KEY` | 百度文心密钥 |
| `BAIDU_URL` | 百度文心自定义接口 |
| `BYTEDANCE_API_KEY` | 字节豆包 |
| `BYTEDANCE_URL` | 字节豆包自定义接口 |
| `IFLYTEK_API_KEY` | 讯飞星火 |
| `IFLYTEK_API_SECRET` | 讯飞星火密钥 |
| `IFLYTEK_URL` | 讯飞星火自定义接口 |
| `SILICONFLOW_API_KEY` | SiliconFlow |
| `SILICONFLOW_URL` | SiliconFlow 自定义接口 |
| `STABILITY_API_KEY` | Stability AI（图片生成） |
| `STABILITY_URL` | Stability AI 自定义接口 |

### 功能开关

| 变量名 | 说明 |
|--------|------|
| `ENABLE_MCP` | 设为 `true` 启用 MCP 协议支持 |
| `HIDE_USER_API_KEY` | 设为 `1` 隐藏页面上的 API Key 输入入口，强制使用环境变量中的 Key |
| `DEFAULT_MODEL` | 更改默认选中模型 |
| `DISABLE_GPT4` | 设为 `1` 禁用 GPT-4 系列模型 |
| `DISABLE_FAST_LINK` | 设为 `1` 禁用从 URL 链接自动解析预设配置 |
| `ENABLE_BALANCE_QUERY` | 设为 `1` 在设置页面启用余额查询功能 |
| `DEFAULT_INPUT_TEMPLATE` | 自定义默认的用户输入预处理模板 |

---

## 使用指南

### 基础对话

1. 在底部输入框输入消息，按 **Enter** 发送
2. 按 **Shift + Enter** 换行
3. 点击左上角聊天图标（💬）查看历史对话列表
4. 点击右上角齿轮图标（⚙️）打开设置
5. 在设置中切换模型、调整参数、配置 API Key

### 设置页面说明

点击右上角齿轮进入设置：

- **模型选择**：选择当前对话使用的模型
- **接口地址**：确认 `BASE_URL` 是否正确
- **API Key**：填入密钥（如果未在环境变量设置）
- **Temperature**：控制回复随机性（0-2），值越大回复越有创意
- **Top P**：核采样参数，与 Temperature 二选一调整
- **最大 Token**：限制单次回复长度
- **访问密码**：如果设置了 `CODE` 环境变量，在此输入

### 面具 (Masks)

面具是**预设 Prompt 模板 + 模型参数 + 对话配置**的组合。

**使用面具**：
1. 点击侧边栏的面具图标（🎭）
2. 从列表中选择一个面具
3. 自动创建使用该面具的新对话

**创建面具**：
1. 进入面具页面，点击"新建面具"
2. 填写名称、描述、系统提示词
3. 设置模型参数（模型、Temperature 等）
4. 保存后即可使用

**导出/导入面具**：
- 面具编辑页提供下载按钮，导出为 JSON
- 可通过导入 JSON 方式分享面具

### 插件

插件扩展了 AI 的能力，使其可以调用外部工具。

**内置插件**：
- **联网搜索**：让 AI 实时搜索互联网获取最新信息
- **计算器**：精确数学计算

**使用插件**：
1. 点击输入框上方的插件按钮（🧩）
2. 选择要启用的插件
3. 输入问题，AI 会自动使用已启用的插件

### Artifacts

当 AI 生成 HTML、SVG 等代码时，Artifacts 功能会在独立窗口中渲染预览。

- 自动弹出 Artifacts 窗口展示渲染效果
- 支持刷新、复制代码、全屏查看
- 分享 Artifacts 链接给他人

### MCP (Model Context Protocol)

MCP 是让 AI 模型调用本地工具的标准协议。

**启用步骤**：
1. 在 `.env.local` 中设置 `ENABLE_MCP=true`
2. 启动项目后，进入设置 → MCP 配置
3. 添加 MCP 服务器（如文件系统、数据库等）
4. 在对话中，AI 可根据需要调用已配置的工具

**常见 MCP 服务器**：
- 文件系统操作（读写文件）
- API 请求（调用外部 REST API）
- 数据库查询

### 数据管理

**导出全部数据**：
设置 → 导出数据 → 下载 JSON 文件（包含所有对话、面具、设置）

**导入数据**：
设置 → 导入数据 → 选择 JSON 文件 → 恢复所有数据

**WebDAV 同步**：
1. 配置 WebDAV 服务器地址
2. 设置同步密码
3. 手动触发同步，在多设备间共享对话数据

---

## 常见问题

### 连接 LM Studio 相关

**Q：模型列表是空的？**

A：确保设置了 `CUSTOM_MODELS=-all,+你的模型名`。模型名通过以下命令获取：

```shell
curl http://localhost:1234/v1/models
```

**Q：请求报错连接被拒绝？**

1. 确认 LM Studio 已点击 "Start Server"
2. 确认端口正确（默认 1234）
3. 确认 `BASE_URL` 末尾包含 `/v1`

**Q：Docker 连不上宿主机 LM Studio？**

容器内用 `host.docker.internal` 代替 `localhost`：
- macOS / Windows：直接使用
- Linux：Docker run 时加 `--add-host host.docker.internal:host-gateway`

### 部署相关

**Q：yarn dev 后页面白屏或一直加载？**

首次编译需要几秒钟，等终端出现 `✓ Ready in` 后再刷新页面。

**Q：提示"端口被占用"？**

```shell
# 查看 7777 端口占用
lsof -i:7777
# 终止占用进程
kill -9 PID
```

**Q：Docker 版本提示"存在更新"？**

Docker 镜像对应稳定发布版，可能比最新代码落后 1-2 天，不影响使用。

### 使用相关

**Q：回复乱码？**

设置中降低 Temperature 到 1 以下。

**Q："未授权状态，请设置访问密码"？**

设置了 `CODE` 环境变量后，首次使用需到设置页输入访问码。

**Q：对话记录突然丢失？**

检查浏览器是否清理了 LocalStorage（无痕模式、清理缓存等）。建议定期导出备份。

**Q："You exceeded your current quota"？**

API Key 余额不足或已超限，检查 API 账户余额。

---

## 项目结构

```
├── app/                    # 前端源码
│   ├── components/         # 组件
│   ├── locales/            # 国际化语言包
│   ├── icons/              # SVG 图标
│   ├── store/              # 状态管理
│   ├── client/             # API 客户端
│   ├── masks/              # 预设面具
│   ├── styles/             # 全局样式
│   └── utils/              # 工具函数
├── public/                 # 静态资源
├── docs/                   # 文档
├── scripts/                # 脚本
├── src-tauri/              # 桌面客户端源码
├── Dockerfile              # Docker 构建
├── docker-compose.yml      # Docker Compose
└── package.json
```

---

## 开发指南

### 本地开发流程

```shell
# 1. 安装依赖
yarn install

# 2. 配置 .env.local

# 3. 启动开发服务（热更新）
yarn dev

# 4. 生产构建
yarn build && yarn start
```

### 构建桌面客户端

TitanGPT 使用 Tauri 构建桌面应用（Windows / macOS / Linux）：

```shell
# 开发模式
yarn app:dev

# 构建安装包
yarn app:build
```

### 切换语言

在页面设置中可选择界面语言，目前支持 20+ 语言。如需新增或修改翻译，编辑 `app/locales/` 下的对应文件即可。

---

## 致谢

- [NextChat](https://github.com/ChatGPTNextWeb/NextChat) — 上游开源项目

## 开源协议

[MIT](https://opensource.org/license/mit/)
