# TitanAI SDK

<div align="center">

![TitanAI Logo](https://img.shields.io/badge/TitanAI-Multi--Platform%20SDK-blue?style=for-the-badge)

**统一的多平台 AI 开发工具包**

[![Rust](https://img.shields.io/badge/Rust-1.75%2B-orange?logo=rust)](https://www.rust-lang.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3%2B-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[English](#english) | [中文](#中文)

</div>

---

## 中文

### 📖 项目简介

TitanAI SDK 是一个跨平台的 AI 开发工具包，提供统一的 API 接口，支持 Rust、Python 和 TypeScript/JavaScript 三大主流开发语言。集成 TitanDAO 生态，为 Web3 和 AI 应用开发提供强大支持。

### ✨ 核心特性

- 🦀 **Rust 原生实现** - 高性能、内存安全的底层引擎
- 🐍 **Python 绑定** - 简洁易用的 Python 接口，支持 AI/ML 生态
- 📦 **npm 包** - TypeScript 优先，完美支持前后端开发
- 🌐 **Web 应用** - Next.js 构建的现代化 Web 界面
- 🔄 **统一 API** - 跨平台一致的 API 设计
- 🧪 **完整测试** - 每个平台都有全面的单元测试
- 📚 **详细文档** - 完善的 API 文档和使用示例
- 🚀 **CI/CD 集成** - GitHub Actions 自动化测试和发布

### 🏗️ 项目架构

```
titanai/
├── 📁 rust/                 # Rust 核心实现
│   ├── src/
│   │   └── lib.rs          # 核心逻辑
│   ├── Cargo.toml          # Rust 配置
│   └── README.md           # Rust 文档
│
├── 📁 python/              # Python 包
│   ├── src/titanai/        # 源代码
│   │   ├── __init__.py    
│   │   └── core.py         # 核心实现
│   ├── tests/              # 测试文件
│   ├── pyproject.toml      # Python 配置
│   └── README.md           # Python 文档
│
├── 📁 npm/                 # npm 包
│   ├── src/
│   │   └── index.ts        # TypeScript 实现
│   ├── tests/              # 测试文件
│   ├── package.json        # npm 配置
│   ├── tsconfig.json       # TypeScript 配置
│   └── README.md           # npm 文档
│
├── 📁 web/                 # Web 应用
│   ├── src/app/            # Next.js 应用
│   ├── public/             # 静态文件 (TitanDAO 页面)
│   ├── package.json        # Web 配置
│   └── README.md           # Web 文档
│
├── 📁 .github/workflows/   # CI/CD 配置
│   ├── ci.yml              # 持续集成
│   └── release.yml         # 自动发布
│
├── 📄 README.md            # 项目主文档
├── 📄 ARCHITECTURE.md      # 架构文档
├── 📄 API.md               # API 文档
├── 📄 CONTRIBUTING.md      # 贡献指南
├── 📄 DEVELOPMENT.md       # 开发指南
├── 📄 LICENSE              # MIT 许可证
└── 📄 .gitignore           # Git 忽略配置
```

### 🚀 快速开始

#### Rust

```toml
# Cargo.toml
[dependencies]
titan-ai = "0.1.0"
```

```rust
use titan_ai::TitanAI;

fn main() {
    let sdk = TitanAI::new();
    let result = sdk.process_data(&json!({"key": "value"}));
    println!("{}", result);
}
```

#### Python

```bash
pip install titanai
```

```python
from titanai import TitanAI, process_data

# 使用类
sdk = TitanAI()
result = sdk.process({"key": "value"})
print(result)

# 使用便捷函数
result = process_data([1, 2, 3])
print(result)
```

#### npm / TypeScript

```bash
npm install titanai
```

```typescript
import { TitanAI, process } from 'titanai';

// 使用类
const sdk = new TitanAI();
const result = sdk.process({ key: 'value' });
console.log(result);

// 使用便捷函数
const result = process([1, 2, 3]);
console.log(result);
```

### 📦 发布包

| 平台 | 包名 | 版本 | 链接 |
|------|------|------|------|
| Rust | `titan-ai` | [![crates.io](https://img.shields.io/crates/v/titan-ai.svg)](https://crates.io/crates/titan-ai) | [crates.io](https://crates.io/crates/titan-ai) |
| Python | `titanai` | [![PyPI](https://img.shields.io/pypi/v/titanai.svg)](https://pypi.org/project/titanai/) | [PyPI](https://pypi.org/project/titanai/) |
| npm | `titanai` | [![npm](https://img.shields.io/npm/v/titanai.svg)](https://www.npmjs.com/package/titanai) | [npm](https://www.npmjs.com/package/titanai) |

### 🛠️ 本地开发

#### 环境要求

- **Rust**: 1.75+ 
- **Python**: 3.8+
- **Node.js**: 18+
- **npm**: 9+

#### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/titandao/titanai.git
cd titanai

# 安装 Python 依赖
cd python
pip install -e ".[dev]"

# 安装 npm 依赖
cd ../npm
npm install

# 安装 Web 依赖
cd ../web
npm install

# 返回根目录
cd ..
```

#### 运行测试

```bash
# 测试 Rust
cargo test

# 测试 Python
cd python && pytest

# 测试 npm
cd npm && npm test

# 测试所有
make test
```

#### 构建项目

```bash
# 构建 Rust
cargo build --release

# 构建 Python
cd python && pip install -e .

# 构建 npm
cd npm && npm run build

# 构建 Web
cd web && npm run build

# 构建所有
make build
```

### 📚 API 文档

详细 API 文档请查看 [API.md](API.md)

#### 核心 API

##### `TitanAI` 类

所有平台共享的核心类：

```typescript
class TitanAI {
  constructor(config?: TitanAIConfig)
  
  process<T>(data: T): string
  getVersion(): string
  validate(data: unknown): boolean
}
```

##### 配置选项

```typescript
interface TitanAIConfig {
  version?: string;      // SDK 版本
  timeout?: number;      // 超时时间 (ms)
  debug?: boolean;       // 调试模式
}
```

### 🤝 贡献指南

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

#### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 📝 开发指南

详细的开发指南请查看 [DEVELOPMENT.md](DEVELOPMENT.md)

包含内容：
- 开发环境配置
- 代码规范
- 测试指南
- 发布流程

### 🐛 问题反馈

发现 Bug 或有新功能建议？请创建 [Issue](https://github.com/titandao/titanai/issues)

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

### 🙏 致谢

- [TitanDAO](https://www.titandao.xyz/) - Web3 生态支持
- Rust 社区
- Python 社区
- TypeScript 社区

### 📊 项目状态

![GitHub stars](https://img.shields.io/github/stars/titan/titanai?style=social)
![GitHub forks](https://img.shields.io/github/forks/titan/titanai?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/titan/titanai?style=social)

---

## English

### 📖 Introduction

TitanAI SDK is a cross-platform AI development toolkit providing unified API interfaces for Rust, Python, and TypeScript/JavaScript. Integrated with the TitanDAO ecosystem, it offers powerful support for Web3 and AI application development.

### ✨ Key Features

- 🦀 **Rust Native** - High-performance, memory-safe core engine
- 🐍 **Python Bindings** - Simple Python interface supporting AI/ML ecosystem
- 📦 **npm Package** - TypeScript-first, perfect for frontend and backend
- 🌐 **Web App** - Modern web interface built with Next.js
- 🔄 **Unified API** - Consistent cross-platform API design
- 🧪 **Well Tested** - Comprehensive unit tests for each platform
- 📚 **Documented** - Complete API documentation and examples
- 🚀 **CI/CD** - GitHub Actions for automated testing and publishing

For detailed documentation, please see the Chinese section above or refer to individual documentation files:
- [API.md](API.md) - API Documentation
- [ARCHITECTURE.md](ARCHITECTURE.md) - Architecture Overview
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing Guide
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development Guide

---

<div align="center">

**Made with ❤️ by Titan DAO**

[Website](https://www.titandao.xyz/) | [Documentation](https://github.com/titandao/titanai) | [Issues](https://github.com/titandao/titanai/issues)

</div>
