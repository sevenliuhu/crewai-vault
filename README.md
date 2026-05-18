# CrewAI 技能加密 / CrewAI Vault

> ⚠️ **引擎开发中 — 预计 2026年Q3 发布第一个版本**
> **⚠️ Engine Under Development — First Release Expected Q3 2026**

<p align="center">
  <strong>多Agent任务加密 · 密钥管理 · 安全通信</strong>
  <br />
  <strong>Multi-Agent Task Encryption · Key Management · Secure Communication</strong>
</p>

---

## 产品介绍 / Product Introduction

### 概述 / Overview

**CrewAI Vault** 是专为 [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) (51K ⭐) 生态打造的安全加密层。它为多 Agent 协作系统提供端到端加密、密钥管理和安全通信能力，确保任务数据、模型输出和 Agent 间通信的机密性和完整性。

**CrewAI Vault** is a security encryption layer built specifically for the [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) (51K ⭐) ecosystem. It provides end-to-end encryption, key management, and secure communication for multi-Agent collaboration systems, ensuring confidentiality and integrity of task data, model outputs, and inter-Agent communications.

### 为什么需要 CrewAI Vault？/ Why CrewAI Vault?

多 Agent 系统面临独特的安全挑战 / Multi-Agent systems face unique security challenges:

1. **任务数据泄露** — Agent 间传递的数据可能包含敏感信息 / Inter-Agent data may contain sensitive information
2. **密钥管理复杂** — 多个 Agent 需要不同的密钥和权限 / Multiple agents need different keys and permissions
3. **通信不可信** — Agent 间的通信可能被截获或篡改 / Inter-Agent communication may be intercepted or tampered
4. **合规要求** — 企业环境需要审计和合规保障 / Enterprise environments require audit and compliance

### 适用场景 / Use Cases

- **金融分析** — 处理敏感财务数据的多 Agent 系统 / Multi-Agent systems handling sensitive financial data
- **医疗诊断** — 患者数据保护和 HIPAA 合规 / Patient data protection and HIPAA compliance
- **法律文档** — 机密文档分析和审查 / Confidential document analysis and review
- **企业自动化** — 内部业务流程的安全自动化 / Secure automation of internal business processes

## 核心功能 / Core Features

### 🔐 任务加密 / Task Encryption

| 功能 / Feature | 说明 / Description |
|------|---------|
| 端到端加密 / E2E Encryption | Agent 间数据全程加密 / End-to-end encryption between agents |
| 粒度加密 / Granular Encryption | 按任务/消息/字段级别加密 / Per-task, per-message, per-field encryption |
| 密钥派生 / Key Derivation | 基于上下文的密钥派生 / Context-based key derivation |
| 零信任架构 / Zero Trust | 默认不信任任何 Agent / Trust no agent by default |

### 🔑 密钥管理 / Key Management

| 功能 / Feature | 说明 / Description |
|------|---------|
| 密钥生命周期 / Key Lifecycle | 自动生成、轮换、吊销 / Auto-generate, rotate, revoke |
| 分层密钥结构 / Hierarchical Keys | 主密钥→工作密钥→会话密钥 / Master → Working → Session keys |
| HSM 集成 / HSM Integration | 支持硬件安全模块 / Hardware Security Module support |
| 密钥备份 / Key Backup | 加密备份和恢复 / Encrypted backup and recovery |

### 📋 审计合规 / Audit & Compliance

| 功能 / Feature | 说明 / Description |
|------|---------|
| 操作审计 / Operation Audit | 记录所有加密/解密操作 / Log all encrypt/decrypt operations |
| 访问控制 / Access Control | 基于角色的密钥访问 / Role-based key access |
| 合规报告 / Compliance Reports | 自动生成合规报告 / Auto-generate compliance reports |
| 密钥溯源 / Key Traceability | 完整的密钥使用链 / Complete key usage chain |

## 技术架构 / Architecture

```
Agent A → Vault SDK → Encryption Layer → Vault Server → Decryption Layer → Agent B
                           ↓                       ↑
                     Key Manager ──────────► HSM / Key Store
                           ↓
                     Audit Logger → Compliance Dashboard
```

## 快速开始 / Quick Start

### 前提条件 / Prerequisites
- Python 3.9+ / Node.js 18+
- CrewAI (v0.30+)
- 4GB RAM

### 安装 / Installation

```bash
pip install crewai-vault
```

### 集成 CrewAI / CrewAI Integration

```python
from crewai import Agent, Task, Crew
from crewai_vault import VaultConfig, secure_agent

# 配置 Vault
vault = VaultConfig(
    vault_url="http://localhost:8200",
    token="your-root-token"
)

# 创建安全 Agent
analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial data securely",
    tools=[secure_agent(vault)],
    allow_delegation=True
)

# 加密的 Crew
crew = Crew(
    agents=[analyst],
    tasks=[Task(description="Analyze Q4 report")],
    encryption=vault  # 自动加密所有 Agent 通信
)
```

## API 文档 / API Documentation

```
POST /api/v1/encrypt      — 加密数据 / Encrypt data
POST /api/v1/decrypt      — 解密数据 / Decrypt data
POST /api/v1/keys/generate — 生成密钥 / Generate key
POST /api/v1/keys/rotate   — 轮换密钥 / Rotate key
GET  /api/v1/keys          — 列出密钥 / List keys
GET  /api/v1/audit/logs    — 审计日志 / Audit logs
```

## 定价方案 / Pricing

| 版本 / Plan | 价格 / Price | Agent 数量 / Agents | 加密速率 / Encryption Rate | 密钥存储 / Key Storage | 支持 / Support |
|------|------|---------|---------|------|------|
| 🌱 Sprout Free | **免费 / Free** | 3 | 1000/min | 10 keys | 社区 / Community |
| 🔑 Key | **$9.9/月** | 10 | 10000/min | 100 keys | 邮件 / Email |
| 🛡️ Shield | **$29.9/月** | 50 | 100000/min | 1000 keys | 邮件+工单 |
| 🏰 Fortress | **$99.9/月** | 200 | 无限 / Unlimited | 10000 keys | 优先工单 |
| 🏛️ Citadel | **$299.9/月** | 无限 / Unlimited | 无限 / Unlimited | 无限 / Unlimited | 专属支持 / Dedicated |

## 联系方式 / Contact

- 📧 **homo-ai@outlook.com**
- 💬 **sevenliuhu** (微信 / WeChat)

## 常见问题 / FAQ

### Q: CrewAI Vault 与标准 CrewAI 兼容吗？/ Is it compatible with standard CrewAI?
A: 完全兼容。Vault 作为插件集成，不修改 CrewAI 核心代码。Fully compatible. Vault integrates as a plugin without modifying CrewAI core code.

### Q: 加密会影响性能吗？/ Does encryption affect performance?
A: 影响极小（通常 < 5%）。采用高效的 AES-256-GCM 加密。Minimal impact (typically < 5%). Uses efficient AES-256-GCM encryption.

### Q: 密钥丢失怎么办？/ What if keys are lost?
A: 支持 M-of-N 恢复方案和备份恢复机制。Supports M-of-N recovery schemes and backup recovery mechanisms.

## 许可证 / License

本项目采用 **GNU Affero General Public License v3.0**。This project is licensed under **AGPL v3.0**.

<p align="center"><strong>Built with ❤️ by HOMO Labs</strong></p>
