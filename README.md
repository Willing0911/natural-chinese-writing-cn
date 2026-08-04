# natural-chinese-writing-cn

用于审校、改写和起草自然中文内容的 Codex Skill，适合学生材料、客户材料、服务介绍、课程内容、报告、视频脚本和专业文档。

它重点处理价值说明靠后、否定句式堆叠、章节结构重复、粗体标签列表、抽象宣传、助手元话语和生产残留，同时保留事实、必要边界与原有声音。目标是让内容更清楚、可信、自然，不用于规避 AI 检测。

## 安装

在 Codex 中直接提出：

> 使用 skill-installer，从 `https://github.com/Willing0911/natural-chinese-writing-cn` 安装 `natural-chinese-writing-cn` 目录下的 Skill。

也可以运行 Codex 自带的安装脚本：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Willing0911/natural-chinese-writing-cn \
  --path natural-chinese-writing-cn
```

安装后，从下一轮对话开始即可调用：

```text
使用 $natural-chinese-writing-cn 审校这份学生材料，保留事实和承诺，减少模板化表达。
```

## 仓库结构

```text
natural-chinese-writing-cn/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/audit_cn_style.py
```

审校脚本只提供启发式信号，不能判断文本作者，也不应替代结合语境的人工判断。
