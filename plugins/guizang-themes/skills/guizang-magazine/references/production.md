# Production Notes · Guizang Magazine

## 目标

保证这个 theme 在 HTML / PDF / PPTX 三端都能稳定输出，不因为追求风格而破坏可读性和构建稳定性。

## 常见坑

### 1. deck 风格不能直接搬进 A4

`guizang-ppt-skill` 是横向 slide 结构。迁移到文档时，必须把风格语法拆开来用：

- chrome / foot
- kicker / headline / lead
- stat card
- rule line
- image frame

不要直接把整页 slide HTML 粘到文档模板里。

### 2. 主题预设不要混搭

同一份交付只能用一套 preset。`ink` 和 `paper` 交叉混搭很容易脏。

### 3. 图片高度优先精确控制

PDF 模板里尽量：

- 固定高度
- `object-fit: cover`
- `object-position: top center`

避免奇怪比例导致分页不稳定。

### 4. mono 文字不能太多

mono 只给：

- 页码
- 标签
- 日期
- 页眉页脚 metadata

正文大量使用 mono 会直接破坏阅读体验。

### 5. PPTX 的中文字体要单独设

`python-pptx` 里中英文字体分槽。改 `slides.py` 时，如果只改 `run.font.name`，中文常常会 silently fallback。

### 6. verify 的 demo 要同步

如果 `build.py --verify` 指向 demo HTML，那么样式改完以后 demo 也要更新，不然会出现“模板是新的，验证源还是旧的”。

## 调样式时的优先级

1. 先保页数
2. 再保标题气压
3. 再保正文可读
4. 最后才是装饰性细节

## 推荐命令

```bash
python3 scripts/build.py one-pager
python3 scripts/build.py long-doc
python3 scripts/build.py letter
python3 scripts/build.py slides
python3 scripts/build.py --check
```
