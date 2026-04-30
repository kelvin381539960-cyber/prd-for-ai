---
module: security
title: Security 身份认证模块
version: "1.0"
source_doc: "AIX Security 身份认证需求V1.0 (1).docx"
last_updated: "2025-11-28"
author: "@Yifeng Wu 吴忆锋"
status: active
countries: [VN, PH, AU]
depends_on: [account]
---

# Security 身份认证模块

## 模块概述

本模块定义 AIX 应用的身份认证服务（IVS），覆盖多种认证方式的全局规则、页面交互及外部接口依赖。AIX 客户端通过 H5 内嵌 WebView 方式接入身份认证服务。

## 文档索引

| 文件 | 内容 |
|------|------|
| [global-rules.md](global-rules.md) | 全局规则：认证方式定义、场景矩阵、优先级、有效期、状态机、通用弹窗 |
| [otp-verification.md](otp-verification.md) | OTP 认证页面（短信验证码） |
| [email-otp-verification.md](email-otp-verification.md) | Email OTP 认证页面（邮箱验证码） |
| [login-passcode-verification.md](login-passcode-verification.md) | Login Passcode 认证页面（密码验证） |
| [biometric-verification.md](biometric-verification.md) | Biometric 设备生物识别认证 |
| [face-authentication.md](face-authentication.md) | 活体识别认证（DTC 侧人脸识别） |
| [api-reference.md](api-reference.md) | 外部接口依赖 + 错误码映射 |

## 引用资料

| 类型 | 链接 |
|------|------|
| PM | @Yifeng Wu 吴忆锋 |
| Figma | https://www.figma.com/design/LxHqrwdNow4AnEZG3Sj9bF/→-AIX-Dev-Handoff-20 |
| 翻译文案 | AIX 翻译文案管理-多维表 |
| BRD | N/A |
| 技术方案 | AIX System Design v0.1(Draft) |

## 需求变更日志

| 变更时间 | 变更人 | 变更内容 | 备注 |
|----------|--------|----------|------|
| 2025-10-21 | @Yifeng Wu 吴忆锋 | 初稿 | |
| 2025-11-04 | @Yifeng Wu 吴忆锋 | 【7.1.1 流程说明】增加跳过认证逻辑，如果是bio登录场景，可以跳过认证 | |
| 2025-11-06 | @Yifeng Wu 吴忆锋 | 【活体认证】模块已更新完毕 @Xin Wang 王鑫 @Liang Wu 吴亮 | |
| 2025-11-28 | @Yifeng Wu 吴忆锋 | 1、验证处理规则：调整描述4种失败场景；影响范围：8.2.1 OTP Verify Page、8.3.1 Email OTP Verify Page、8.4.2 Login Passcode Verify Page。2、进入页面自动触发otp规则：进入页面后，自动触达发送otp的请求。影响范围：8.2.1 OTP Verify Page、8.3.1 Email OTP Verify Page @Dongjie Tan 谭东杰 @Xin Wang 王鑫 @Bowen Li (Eli) @Lei Zhang 张雷 | |

## 项目背景

为满足全球用户对一体化、便捷安全数字金融服务的需求，本项目旨在开发一款创新的移动应用。该应用将整合先进的支付与账户管理技术，致力于为用户提供全新的移动端金融管理体验。

## 项目目的

- 构建基础：建立安全、便捷的用户注册登录与账户体系。
- 核心功能：实现充值、提现、转账、消费等关键支付功能。
- 安全保障：通过多层验证与风控策略，确保用户资产与信息安全。
- 体验优化：提供流畅直观的操作流程，提升用户留存。

## 客户端对接方式

AIX 客户端需通过 H5 内嵌 WebView 的方式接入以下两类服务：

1. **AIX 身份认证服务**（如 OTP、邮箱验证、登录密码等）
2. **DTC 身份核验服务**（如活体人脸识别、KYC 等）

## 国家线支持

| VN | PH | AU |
|----|----|----|
| ✅ | ✅ | ✅ |
