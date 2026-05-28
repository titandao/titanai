# 常见问题

## 如何快速获得帮助？

1. 询问 ChatGPT / DeepSeek / 百度 / Google 等。
2. 提供问题的背景信息和详细描述，高质量提问容易获得有用答案。

# 部署相关问题

## 为什么 Docker 版本一直提示更新？

Docker 版本相当于稳定版，latest 标签总是与 latest release 一致，会落后最新提交一到两天，这是正常现象。

## Docker 无法连接宿主机上的 LM Studio？

Docker 容器内不能直接使用 `localhost`，需要使用 `host.docker.internal`：

```shell
-e BASE_URL=http://host.docker.internal:1234/v1
```

macOS 和 Windows 原生支持 `host.docker.internal`。Linux 需在 docker run 时加 `--add-host host.docker.internal:host-gateway`。

## 为什么我的 LM Studio 模型在模型列表里看不到？

确保 `.env.local` 中设置了正确的 `CUSTOM_MODELS`：

```shell
# 隐藏所有默认模型，只显示 LM Studio 模型
CUSTOM_MODELS=-all,+你的模型名
```

模型名必须与 LM Studio `/v1/models` 接口返回的 `id` 完全一致。

## 怎么知道 LM Studio 里模型的名字？

在 LM Studio 启动 Server 后，在终端运行：

```shell
curl http://localhost:1234/v1/models
```

返回的 `id` 字段就是模型名。

## 为什么我的请求一直提示"出错了，稍后重试吧"？

请依次检查：

- LM Studio Server 是否已启动（右侧面板 "Start Server"）
- `.env.local` 中 `BASE_URL` 是否正确，端口是否是 LM Studio 的端口（默认 1234）
- `OPENAI_API_KEY` 不能为空（LM Studio 不校验，填 `sk-1234` 即可）
- LM Studio 是否已加载模型

## 为什么 ChatGPT 的回复会乱码？

设置界面 → 模型设置 → `temperature` 值如果大于 1 有可能造成乱码，调回 1 以内即可。

## 使用时提示"现在是未授权状态，请在设置页输入访问密码"？

项目通过环境变量 `CODE` 设置了访问密码。第一次使用时需到设置页输入访问码。

## 使用时遇到 "Loadin chunk xxx failed..."？

浏览器兼容性问题。构建时设置环境变量 `DISABLE_CHUNK=1` 即可关闭分块编译：

```shell
DISABLE_CHUNK=1 yarn build
```

注意：关闭后首次加载会变慢。

# 使用相关问题

## 环境变量 CODE 是什么？必须设置吗？

访问密码，可选。不设置则任何人都可以访问。

## 不支持流式响应？

如果用 nginx 反向代理，需要配置：

```
proxy_cache off;
proxy_buffering off;
chunked_transfer_encoding on;
tcp_nopush on;
tcp_nodelay on;
keepalive_timeout 300;
```

## 如何使用远程 API（如 OpenAI）？

在 `.env.local` 中配置：

```shell
OPENAI_API_KEY=sk-你的key
BASE_URL=https://api.openai.com
```

如果需要代理，`BASE_URL` 改为你的代理地址。

## 为什么 Token 消耗得这么快？

检查 API Key 是否泄露：去 OpenAI 官网查看消费记录。如果密码设置太短（5位以内字母），容易被爆破。

# OpenAI 相关问题

## API 是怎么计费的？

OpenAI 根据 token 数收费，详细价格见 [OpenAI 官网](https://openai.com/pricing)。
