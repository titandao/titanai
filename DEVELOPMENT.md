# 本地开发指南

## 项目状态

### ✅ 已完成
- **Rust**: 构建和测试通过 (2 tests)
- **Python**: 构建和测试通过 (4 tests)
- **npm**: 构建和测试通过 (2 tests)
- **Web**: 构建成功

## 快速开始

### 1. 环境准备

```bash
# 进入项目目录
cd /home/workspace/multiplatform-sdk

# 安装Python依赖
pip install -e python/

# 安装npm依赖
cd npm && npm install && cd ..
cd web && npm install && cd ..
```

### 2. 运行测试

```bash
# Rust测试
source $HOME/.cargo/env
cargo test

# Python测试
cd python && pytest

# npm测试
cd npm && npm test
```

### 3. 构建项目

```bash
# Rust构建
cargo build --release

# npm构建
cd npm && npm run build

# Web构建
cd web && npm run build
```

### 4. 本地运行Web应用

```bash
cd web
npm run dev
# 访问 http://localhost:3000
```

## 发布到GitHub

### 步骤1: 连接GitHub

```bash
# 认证GitHub CLI
gh auth login

# 创建远程仓库
gh repo create multiplatform-sdk --public --source=. --remote=origin

# 推送代码
git push -u origin master
```

### 步骤2: 配置GitHub Secrets

在GitHub仓库设置中添加以下Secrets:

** crates.io (Rust)**
- `CRATES_TOKEN`: 从 https://crates.io 获取

**PyPI (Python)**
- `PYPI_USERNAME`: PyPI用户名
- `PYPI_PASSWORD`: PyPI密码或API token

**npm**
- `NPM_TOKEN`: 从 https://www.npmjs.com 获取

**Vercel**
- `VERCEL_TOKEN`: Vercel API token
- `VERCEL_ORG_ID`: Vercel组织ID
- `VERCEL_PROJECT_ID`: Vercel项目ID

### 步骤3: 发布

```bash
# 创建版本标签
git tag v0.1.0

# 推送标签触发自动发布
git push origin v0.1.0
```

GitHub Actions将自动：
1. 运行所有测试
2. 发布到crates.io
3. 发布到PyPI
4. 发布到npm
5. 部署Web应用到Vercel

## 项目结构

```
multiplatform-sdk/
├── rust/                 # Rust crate
│   ├── src/
│   │   └── lib.rs
│   └── Cargo.toml
├── python/               # Python package
│   ├── src/
│   │   └── multiplatform_sdk/
│   ├── tests/
│   └── pyproject.toml
├── npm/                  # npm package
│   ├── src/
│   ├── tests/
│   └── package.json
├── web/                  # Next.js web app
│   ├── src/
│   └── package.json
└── .github/
    └── workflows/
        ├── ci.yml        # CI测试
        └── release.yml   # 自动发布
```

## 下一步

1. 根据需求修改SDK功能
2. 添加更多测试用例
3. 完善API文档
4. 自定义Web应用页面
5. 配置Vercel部署
