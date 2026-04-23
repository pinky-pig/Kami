# republican-newspaper 交接文档

给维护当前主题 skill 的人看。使用时优先读 `SKILL.md`、`CHEATSHEET.md` 和 `references/design.md`。

## 一句话定位

把 Kami 的中文文档排版切换成 **民国报纸 / 报纸特刊 / 号外剪报** 风格：旧报纸底、黑色铅字、竖排题名、密集分栏、剪报框、灰度照片、红印章。

## 文件职责

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 触发词、路由、工作流 |
| `CHEATSHEET.md` | 速查 token 与组件 |
| `references/design.md` | 完整视觉规范 |
| `references/writing.md` | 报纸化写作口径 |
| `assets/reference-images/` | 风格 2 参考图 |
| `assets/templates/` | 可填充模板 |
| `scripts/build.py` | 构建与 CSS/token 校验 |

## 改动原则

1. 不要把档案蓝带回来
2. 红色只给印章/邮戳
3. 报纸感来自报头、分栏、反白条、细框线，不来自脏污贴图
4. 图片保持灰度、证据感
5. 正文可密，但必须可读

## 验证

```bash
.venv/bin/python plugins/kami-themes/skills/republican-newspaper/scripts/build.py --check
.venv/bin/python plugins/kami-themes/skills/republican-newspaper/scripts/build.py --verify long-doc
```

全局 `python3` 若缺 `weasyprint/pypdf`，用仓库 `.venv`。
