# TitanAI 项目完整文档

## 📋 项目概述

TitanAI 是一个跨平台的 AI 工具包，支持 Rust、Python 和 TypeScript/JavaScript，并集成了 TitanDAO 的 Web 应用。

---

## 🏗️ 项目结构

```
titanai/
├── rust/                    # Rust crate
│   ├── src/
│   │   └── lib.rs          # 核心实现
│   ├── Cargo.toml          # Rust 配置
│   └── tests/              # Rust 测试
│
├── python/                  # Python package
│   ├── src/titanai/
│   │   ├── __init__.py     # 包入口
│   │   └── core.py         # 核心实现
│   ├── tests/              # Python 测试
│   └── pyproject.toml      # Python 配置
│
├── npm/                     # TypeScript/JavaScript package
│   ├── src/
│   │   └── index.ts        # 核心实现
│   ├── tests/              # TypeScript 测试
│   ├── package.json        # npm 配置
│   └── tsconfig.json       # TypeScript 配置
│
├── web/                     # Next.js Web 应用
│   ├── src/app/            # Next.js App Router
│   ├── public/             # 静态资源
│   │   ├── assets/         # 本地化的 TitanDAO 资源
│   │   │   ├── css/        # 样式文件
│   │   │   ├── js/         # JavaScript 文件
│   │   │   ├── images/     # 图片资源
│   │   │   ├── fonts/      # 字体文件
│   │   │   └── media/      # 媒体文件
│   │   └── *.html          # TitanDAO 页面
│   └── package.json        # Web 配置
│
├── scripts/                 # 工具脚本
│   └── download_assets.py  # 资源下载脚本
│
├── .github/workflows/       # GitHub Actions CI/CD
│   ├── ci.yml              # 持续集成
│   └── release.yml         # 自动发布
│
├── .gitignore              # Git 忽略规则
├── README.md               # 项目说明
├── ARCHITECTURE.md         # 架构文档
├── API.md                  # API 文档
└── DEVELOPMENT.md          # 开发指南
```

---

## 🚀 快速开始

### 环境要求

- **Rust**: 1.70+ (`cargo --version`)
- **Python**: 3.8+ (`python3 --version`)
- **Node.js**: 18+ (`node --version`)
- **npm**: 9+ (`npm --version`)

### 安装依赖

```bash
# Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Python (通常已预装)
pip install --upgrade pip

# Node.js
npm install -g npm@latest
```

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/titandao/titanai.git
cd titanai

# Rust
cd rust && cargo test

# Python
cd python && pip install -e ".[dev]" && pytest

# npm
cd npm && npm install && npm test

# Web
cd web && npm install && npm run dev
```

---

## 📦 各平台使用指南

### Rust

```rust
use titan_ai::TitanAI;

fn main() {
    let sdk = TitanAI::new("0.1.0");
    let result = sdk.process(serde_json::json!({
        "key": "value"
    }));
    println!("{}", result);
}
```

### Python

```python
from titanai import TitanAI

sdk = TitanAI(version="0.1.0")
result = sdk.process({"key": "value"})
print(result)
```

### TypeScript/JavaScript

```typescript
import { TitanAI } from 'titanai';

const sdk = new TitanAI({ version: '0.1.0' });
const result = await sdk.process({ key: 'value' });
console.log(result);
```

---

## 🧪 测试

### 运行所有测试

```bash
# Rust 测试
cargo test --all

# Python 测试
cd python && pytest -v

# TypeScript 测试
cd npm && npm test

# Web 构建
cd web && npm run build
```

### 测试覆盖率

- **Rust**: 2 个单元测试
- **Python**: 4 个单元测试
- **TypeScript**: 2 个单元测试

---

## 🔄 CI/CD 流程

### GitHub Actions 自动化

项目使用 GitHub Actions 实现持续集成和发布：

1. **CI (`.github/workflows/ci.yml`)**
   - 触发：Push 到 main/master，Pull Request
   - 检查：代码格式、测试、构建

2. **Release (`.github/workflows/release.yml`)**
   - 触发：创建 Git tag (v*)
   - 自动发布到 crates.io、PyPI、npm
   - 自动部署 Web 到 Vercel

### 设置发布密钥

在 GitHub 仓库设置中添加以下 Secrets：

```
CRATES_TOKEN      - crates.io API token
PYPI_USERNAME     - PyPI 用户名
PYPI_PASSWORD     - PyPI 密码
NPM_TOKEN         - npm registry token
VERCEL_TOKEN      - Vercel 部署 token
VERCEL_ORG_ID     - Vercel 组织 ID
VERCEL_PROJECT_ID - Vercel 项目 ID
```

### 发布流程

```bash
# 1. 更新版本号
# - rust/Cargo.toml
# - python/pyproject.toml
# - npm/package.json

# 2. 提交更改
git add .
git commit -m "chore: bump version to x.x.x"

# 3. 创建 tag
git tag vx.x.x
git push origin main --tags

# 4. GitHub Actions 自动发布
```

---

## 🌐 TitanDAO Web 集成

### 本地化资源

所有 TitanDAO 网站资源已下载到本地：

- **位置**: `web/public/assets/`
- **文件数**: 286 个文件
- **总大小**: 23 MB
- **类型**: CSS、JS、图片、字体、媒体

### 可用页面

| 页面 | 文件 | 描述 |
|------|------|------|
| 首页 | `index.html` | TitanDAO 主页 |
| 购买 | `buy.html` | 代币购买页面 |
| 燃烧 | `burn.html` | 代币燃烧机制 |
| 社区 | `clubhouse.html` | 社区中心 |
| NFT | `titanpunkz.html` | TitanPunkz NFT 系列 |
| 增强版 | `titanpunkzreloaded.html` | TitanPunkz Reloaded |
| 泳装 | `titanverseswimwear.html` | 泳装系列 |

### 访问本地页面

```bash
# 启动开发服务器
cd web && npm run dev

# 访问
# 主页: http://localhost:3000
# TitanDAO: http://localhost:3000/titandao.html
```

### 更新远程资源

如果需要重新下载资源：

```bash
python3 scripts/download_assets.py
```

---

## 📁 .gitignore 详细说明

以下目录和文件**不应该**上传到 GitHub：

### 编译输出
- `target/` - Rust 编译产物
- `__pycache__/` - Python 缓存
- `node_modules/` - Node.js 依赖
- `dist/` - 打包输出
- `.next/` - Next.js 构建

### 依赖锁文件
- `Cargo.lock` - Rust 库项目不提交
- `package-lock.json` - 应用项目可提交，库项目不提交

### IDE 配置
- `.vscode/` - VS Code 配置
- `.idea/` - IntelliJ IDEA 配置
- `*.swp` - Vim 交换文件

### 环境变量
- `.env` - 本地环境变量
- `.env.local` - 本地环境变量
- `*.local.json` - 本地配置

### 日志和缓存
- `*.log` - 日志文件
- `.pytest_cache/` - pytest 缓存
- `.mypy_cache/` - mypy 缓存

### 系统文件
- `.DS_Store` - macOS 文件
- `Thumbs.db` - Windows 文件

---

## 🔧 开发工具

### 代码格式化

```bash
# Rust
cargo fmt

# Python
pip install black
black python/

# TypeScript
npm run lint
```

### 代码检查

```bash
# Rust
cargo clippy -- -D warnings

# Python
pip install mypy
mypy python/

# TypeScript
npx tsc --noEmit
```

---

## 📊 项目状态

| 组件 | 状态 | 测试 | 文档 |
|------|------|------|------|
| Rust | ✅ 完成 | ✅ 通过 | ✅ 完整 |
| Python | ✅ 完成 | ✅ 通过 | ✅ 完整 |
| npm | ✅ 完成 | ✅ 通过 | ✅ 完整 |
| Web | ✅ 完成 | ✅ 构建 | ✅ 完整 |
| CI/CD | ✅ 配置 | - | ✅ 完整 |

---

## 🎯 下一步计划

### 短期 (v0.2.0)
- [ ] 添加更多核心功能
- [ ] 完善错误处理
- [ ] 增加集成测试

### 中期 (v0.3.0)
- [ ] WebAssembly 支持
- [ ] 插件系统
- [ ] 性能优化

### 长期 (v1.0.0)
- [ ] 分布式处理
- [ ] AI 模型集成
- [ ] 云原生支持

---

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/amazing`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing`)
5. 创建 Pull Request

---

## 📄 许可证

MIT License - 详见 LICENSE 文件

---

## 📞 联系方式

- 项目主页: https://github.com/titandao/titanai
- 问题反馈: https://github.com/titandao/titanai/issues
- TitanDAO: https://www.titandao.xyz
