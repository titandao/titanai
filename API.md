# TitanAI API 文档

## 📚 API 总览

TitanAI SDK 提供跨平台一致的 API 接口。本文档详细描述所有平台的 API 用法。

## 🎯 核心 API

### `TitanAI` 类

主类，提供所有核心功能。

#### 构造函数

##### Rust
```rust
use titan_ai::TitanAI;

// 默认配置
let sdk = TitanAI::new();

// 自定义配置
let sdk = TitanAI::with_config(TitanAIConfig {
    timeout: Some(5000),
    debug: true,
});
```

##### Python
```python
from titanai import TitanAI

# 默认配置
sdk = TitanAI()

# 自定义版本
sdk = TitanAI(version="0.1.0")
```

##### TypeScript
```typescript
import { TitanAI } from 'titanai';

// 默认配置
const sdk = new TitanAI();

// 自定义配置
const sdk = new TitanAI({
  version: '0.1.0',
  timeout: 5000,
  debug: true,
});
```

---

### `process()` 方法

处理输入数据并返回 JSON 字符串。

#### 参数

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| data | T (泛型) | 是 | 要处理的数据 |

#### 返回值

`string` - JSON 格式的字符串

#### 示例

##### Rust
```rust
use serde_json::json;

let sdk = TitanAI::new();

// 处理对象
let result = sdk.process_data(&json!({
    "name": "TitanAI",
    "version": "0.1.0"
}));
println!("{}", result);
// 输出: {"name":"TitanAI","version":"0.1.0"}

// 处理数组
let result = sdk.process_data(&json!([1, 2, 3]));
println!("{}", result);
// 输出: [1,2,3]
```

##### Python
```python
sdk = TitanAI()

# 处理字典
result = sdk.process({"name": "TitanAI", "version": "0.1.0"})
print(result)
# 输出: {"name": "TitanAI", "version": "0.1.0"}

# 处理列表
result = sdk.process([1, 2, 3])
print(result)
# 输出: [1, 2, 3]

# 处理字符串
result = sdk.process("Hello, TitanAI!")
print(result)
# 输出: "Hello, TitanAI!"
```

##### TypeScript
```typescript
const sdk = new TitanAI();

// 处理对象
const result = sdk.process({ name: 'TitanAI', version: '0.1.0' });
console.log(result);
// 输出: {"name":"TitanAI","version":"0.1.0"}

// 处理数组
const result = sdk.process([1, 2, 3]);
console.log(result);
// 输出: [1,2,3]

// 泛型类型
interface UserData {
  id: number;
  name: string;
}
const result = sdk.process<UserData>({ id: 1, name: 'TitanAI' });
```

---

### `validate()` 方法

验证数据是否可以序列化为 JSON。

#### 参数

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| data | any | 是 | 要验证的数据 |

#### 返回值

`boolean` - 数据是否有效

#### 示例

##### Rust
```rust
let sdk = TitanAI::new();

// 有效数据
let valid = sdk.validate(&json!({"key": "value"}));
assert!(valid);

// 无效数据会导致编译错误（Rust 的强类型系统）
```

##### Python
```python
sdk = TitanAI()

# 有效数据
valid = sdk.validate({"key": "value"})
assert valid  # True

# 无效数据
class CustomObject:
    pass

obj = CustomObject()
valid = sdk.validate(obj)
print(valid)  # False
```

##### TypeScript
```typescript
const sdk = new TitanAI();

// 有效数据
const valid = sdk.validate({ key: 'value' });
console.log(valid);  // true

// 无效数据（JavaScript 中大部分数据都是有效的）
const valid2 = sdk.validate([1, 2, 3]);
console.log(valid2);  // true
```

---

### `getVersion()` 方法

获取 SDK 版本号。

#### 返回值

`string` - 版本号字符串

#### 示例

##### Rust
```rust
let sdk = TitanAI::new();
let version = sdk.get_version();
println!("Version: {}", version);
// 输出: Version: 0.1.0
```

##### Python
```python
sdk = TitanAI()
version = sdk.get_version()
print(f"Version: {version}")
# 输出: Version: 0.1.0
```

##### TypeScript
```typescript
const sdk = new TitanAI();
const version = sdk.getVersion();
console.log(`Version: ${version}`);
// 输出: Version: 0.1.0
```

---

## 🔧 配置选项

### `TitanAIConfig` 接口

#### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| version | string | "0.1.0" | SDK 版本 |
| timeout | number | null | 超时时间（毫秒） |
| debug | boolean | false | 调试模式 |

#### 示例

##### Rust
```rust
use titan_ai::{TitanAI, TitanAIConfig};

let config = TitanAIConfig {
    timeout: Some(5000),
    debug: true,
};
let sdk = TitanAI::with_config(config);
```

##### Python
```python
from titanai import TitanAI

# Python 目前通过构造函数参数配置
sdk = TitanAI(version="0.1.0")
```

##### TypeScript
```typescript
import { TitanAI, TitanAIConfig } from 'titanai';

const config: TitanAIConfig = {
  version: '0.1.0',
  timeout: 5000,
  debug: true,
};
const sdk = new TitanAI(config);
```

---

## 🛠️ 工具函数

### `process_data()` - 便捷函数

不需要创建实例，直接处理数据。

#### 示例

##### Python
```python
from titanai import process_data

result = process_data({"key": "value"})
print(result)
# 输出: {"key": "value"}
```

##### TypeScript
```typescript
import { process } from 'titanai';

const result = process([1, 2, 3]);
console.log(result);
// 输出: [1,2,3]
```

---

## 📊 类型定义

### TypeScript 类型

```typescript
// 主配置接口
export interface TitanAIConfig {
  version?: string;
  timeout?: number;
  debug?: boolean;
}

// 处理结果
export interface ProcessResult {
  success: boolean;
  data: string;
  error?: string;
}

// 验证规则
export type ValidationRule = 
  | StringRule
  | NumberRule
  | ObjectRule;

interface StringRule {
  type: 'string';
  minLength?: number;
  maxLength?: number;
}

interface NumberRule {
  type: 'number';
  min?: number;
  max?: number;
}

interface ObjectRule {
  type: 'object';
  properties?: Record<string, ValidationRule>;
}
```

### Python 类型提示

```python
from typing import Any, Dict, Optional, TypedDict

class TitanAIConfig(TypedDict, total=False):
    version: str
    timeout: int
    debug: bool

class ProcessResult(TypedDict):
    success: bool
    data: str
    error: Optional[str]
```

### Rust 类型

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TitanAIConfig {
    pub timeout: Option<u64>,
    pub debug: bool,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ProcessResult {
    pub success: bool,
    pub data: String,
    pub error: Option<String>,
}
```

---

## 🚨 错误处理

### Rust

```rust
use titan_ai::{TitanAI, TitanAIError};

let sdk = TitanAI::new();

match sdk.process_data(&data) {
    Ok(result) => println!("Success: {}", result),
    Err(TitanAIError::InvalidData(msg)) => eprintln!("Invalid data: {}", msg),
    Err(TitanAIError::Timeout) => eprintln!("Operation timed out"),
    Err(e) => eprintln!("Error: {:?}", e),
}
```

### Python

```python
from titanai import TitanAI, TitanAIError

sdk = TitanAI()

try:
    result = sdk.process(data)
    print(f"Success: {result}")
except TitanAIError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### TypeScript

```typescript
import { TitanAI, TitanAIError } from 'titanai';

const sdk = new TitanAI();

try {
  const result = sdk.process(data);
  console.log('Success:', result);
} catch (error) {
  if (error instanceof TitanAIError) {
    console.error('TitanAI Error:', error.message);
  } else {
    console.error('Unexpected error:', error);
  }
}
```

---

## 🔌 高级用法

### 异步处理（未来支持）

#### TypeScript (已支持)
```typescript
const sdk = new TitanAI();

// 异步处理
const result = await sdk.processAsync(largeData);
```

#### Python (未来支持)
```python
import asyncio
from titanai import TitanAI

async def main():
    sdk = TitanAI()
    result = await sdk.process_async(large_data)
    print(result)

asyncio.run(main())
```

#### Rust (未来支持)
```rust
use titan_ai::TitanAI;

async fn process_data() -> Result<String, TitanAIError> {
    let sdk = TitanAI::new();
    sdk.process_data_async(&data).await
}
```

### 批量处理

```typescript
import { TitanAI } from 'titanai';

const sdk = new TitanAI();

// 批量处理
const items = [
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  { id: 3, name: 'Item 3' },
];

const results = items.map(item => sdk.process(item));
console.log(results);
```

### 流式处理（未来支持）

```typescript
import { TitanAI } from 'titanai';

const sdk = new TitanAI();

// 流式处理
const stream = sdk.processStream(dataStream);
for await (const chunk of stream) {
  console.log(chunk);
}
```

---

## 📝 最佳实践

### 1. 实例复用

❌ **不推荐**：
```typescript
// 每次都创建新实例
function processData(data: any) {
  const sdk = new TitanAI();
  return sdk.process(data);
}
```

✅ **推荐**：
```typescript
// 复用实例
const sdk = new TitanAI();

function processData(data: any) {
  return sdk.process(data);
}
```

### 2. 错误处理

✅ **推荐**：
```typescript
import { TitanAI, TitanAIError } from 'titanai';

const sdk = new TitanAI();

try {
  const result = sdk.process(data);
  return result;
} catch (error) {
  if (error instanceof TitanAIError) {
    // 处理 TitanAI 特定错误
    logger.error('TitanAI error:', error.message);
    throw new ApplicationError(error.message);
  }
  throw error;  // 重新抛出未知错误
}
```

### 3. 类型安全

✅ **推荐**：
```typescript
import { TitanAI } from 'titanai';

interface UserData {
  id: number;
  name: string;
  email: string;
}

const sdk = new TitanAI();

// 使用泛型确保类型安全
function processUser(user: UserData): string {
  return sdk.process<UserData>(user);
}
```

### 4. 配置管理

✅ **推荐**：
```typescript
// config.ts
import { TitanAIConfig } from 'titanai';

export const titanaiConfig: TitanAIConfig = {
  timeout: 5000,
  debug: process.env.NODE_ENV === 'development',
};

// main.ts
import { TitanAI } from 'titanai';
import { titanaiConfig } from './config';

const sdk = new TitanAI(titanaiConfig);
```

---

## 🔍 调试

### 启用调试模式

```typescript
const sdk = new TitanAI({ debug: true });

// 调试日志会输出到控制台
const result = sdk.process({ key: 'value' });
// [TitanAI Debug] Processing data: {"key":"value"}
// [TitanAI Debug] Result: {"key":"value"}
```

### Python 调试

```python
import logging
from titanai import TitanAI

# 设置日志级别
logging.basicConfig(level=logging.DEBUG)

sdk = TitanAI()
result = sdk.process({"key": "value"})
```

---

## 📚 完整示例

### TypeScript - Web 应用

```typescript
import { TitanAI } from 'titanai';

class DataService {
  private sdk: TitanAI;
  
  constructor() {
    this.sdk = new TitanAI({
      timeout: 5000,
      debug: process.env.NODE_ENV === 'development',
    });
  }
  
  async processUserData(userId: string): Promise<string> {
    try {
      const userData = await this.fetchUser(userId);
      return this.sdk.process(userData);
    } catch (error) {
      console.error('Failed to process user data:', error);
      throw error;
    }
  }
  
  private async fetchUser(userId: string) {
    // 获取用户数据
    return { id: userId, name: 'User' };
  }
}

export const dataService = new DataService();
```

### Python - 数据处理脚本

```python
from titanai import TitanAI
import json

def process_file(file_path: str) -> dict:
    """读取并处理 JSON 文件"""
    sdk = TitanAI()
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    result = sdk.process(data)
    return json.loads(result)

if __name__ == '__main__':
    result = process_file('data.json')
    print(json.dumps(result, indent=2))
```

### Rust - 命令行工具

```rust
use titan_ai::TitanAI;
use std::fs;

fn process_file(path: &str) -> Result<String, Box<dyn std::error::Error>> {
    let sdk = TitanAI::new();
    let content = fs::read_to_string(path)?;
    let json: serde_json::Value = serde_json::from_str(&content)?;
    
    let result = sdk.process_data(&json)?;
    Ok(result)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} <file.json>", args[0]);
        std::process::exit(1);
    }
    
    match process_file(&args[1]) {
        Ok(result) => println!("{}", result),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

---

## 🆕 版本历史

### v0.1.0 (当前版本)
- ✅ 基础 `process()` 方法
- ✅ 数据验证
- ✅ 版本获取
- ✅ 跨平台支持

### v0.2.0 (计划中)
- 🔄 异步处理
- 🔄 流式处理
- 🔄 批量操作

### v1.0.0 (未来)
- 📋 插件系统
- 📋 自定义序列化器
- 📋 中间件支持

---

## ❓ 常见问题

### Q: 如何处理大文件？

A: 对于大文件，建议：
1. 使用流式处理（未来版本）
2. 分块处理数据
3. 增加超时时间

### Q: 支持哪些数据类型？

A: 支持 JSON 可序列化的所有类型：
- 对象/字典
- 数组/列表
- 字符串
- 数字
- 布尔值
- null

### Q: 如何处理循环引用？

A: 目前不支持循环引用。建议：
1. 重构数据结构
2. 使用 ID 引用替代对象引用
3. 自定义序列化逻辑

---

## 📞 获取帮助

- 📖 [文档](https://github.com/titandao/titanai)
- 🐛 [问题反馈](https://github.com/titandao/titanai/issues)
- 💬 [讨论区](https://github.com/titandao/titanai/discussions)
