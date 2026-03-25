# 用户管理系统

一个基于 FastAPI + JavaScript 的完整前后端用户管理系统。

## 功能特点

- ✅ 用户注册
- ✅ 用户登录
- ✅ 个人资料管理
- ✅ 密码修改
- ✅ 账号删除
- ✅ 响应式设计
- ✅ 密码加密存储

## 技术栈

### 后端
- **FastAPI** - 高性能 Python Web 框架
- **SQLAlchemy** - ORM 数据库操作
- **Pydantic** - 数据验证
- **SQLite** - 轻量级数据库

### 前端
- **HTML5 + CSS3** - 现代化界面
- **JavaScript** - 交互逻辑
- **Fetch API** - 与后端通信

## 项目结构

```
d:\CICD\test/
├── backend/
│   ├── main.py          # FastAPI 主程序
│   ├── models.py        # 数据模型
│   ├── database.py      # 数据库配置
│   └── requirements.txt # Python 依赖
└── frontend/
    ├── index.html       # 首页
    ├── login.html       # 登录页
    ├── register.html    # 注册页
    ├── profile.html     # 用户资料页
    ├── style.css        # 样式
    └── app.js           # 前端逻辑
```

## 快速开始

### 1. 安装后端依赖

```bash
cd d:\CICD\test\backend
pip install -r requirements.txt
```

### 2. 启动后端服务

```bash
uvicorn main:app --reload
```

后端服务将在 http://localhost:8000 启动

### 3. 打开前端页面

直接在浏览器中打开 `d:\CICD\test\frontend\index.html`

## API 端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/api/register` | POST | 用户注册 |
| `/api/login` | POST | 用户登录 |
| `/api/users/{id}` | GET | 获取用户信息 |
| `/api/users/{id}` | PUT | 更新用户信息 |
| `/api/users/{id}` | DELETE | 删除用户 |

## 使用说明

1. **注册新用户**：访问注册页面，填写用户名、邮箱、密码等信息
2. **登录系统**：使用注册的用户名和密码登录
3. **管理资料**：登录后可以查看和编辑个人资料
4. **安全退出**：点击退出按钮安全退出系统

## 安全特性

- 密码使用 SHA-256 加密存储
- 前端表单验证
- 后端数据验证
- CORS 跨域支持

## 开发建议

- 生产环境请使用 HTTPS
- 建议使用更强的密码加密算法（如 bcrypt）
- 添加更多的错误处理和日志记录
- 考虑添加用户权限管理

## 许可证

MIT License