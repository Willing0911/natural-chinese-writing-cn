# natural-chinese-writing-cn

用于审校、改写、起草和持续校准自然中文内容的 Codex Skill，适合学生材料、客户材料、服务介绍、课程内容、报告、公众号长文、视频脚本和专业文档。

它重点处理价值说明靠后、否定句式堆叠、章节结构重复、粗体标签列表、抽象宣传、助手元话语和生产残留，同时保留事实、必要边界与原有声音。目标是让内容更清楚、可信、自然，不用于模仿具名创作者或规避 AI 检测。

2026-08-05 的迭代补上了“活人感写作”真正需要的三层能力：

- 让第一人称经验、情绪、判断和引用都有可核对的来源，不靠虚构细节制造人味；
- 让案例、类比和研究材料服务于一条清晰主线，并区分学生材料、专业报告、视频脚本和个人长文的语体；
- 用同一任务的 Agent 草稿与人工定稿做差异分析，经过 3–4 轮或收敛后形成规则，再用留出任务检查过拟合。

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

需要用团队改稿持续校准时，可以这样提出：

```text
使用 $natural-chinese-writing-cn 的 calibration 模式，比较这份 Agent 草稿和人工定稿，提炼可复用规则，并标注适用范围和反例。
```

## 仓库结构

```text
natural-chinese-writing-cn/
  SKILL.md
  agents/openai.yaml
  references/
    calibration.md
  scripts/audit_cn_style.py
```

审校脚本只提供启发式信号，不能判断文本作者，也不应替代结合语境的人工判断。

## 设计参考

本次迭代参考了卡兹克公开的 [`khazix-writer`](https://github.com/KKKKhazix/khazix-skills/blob/main/khazix-writer/SKILL.md) 及其[方法说明](https://www.uisdc.com/beyond-ai-writing)，吸收其“人工改稿反哺规则、分层终审、保留真实判断”的方法，不复制个人口头禅、签名式结构或作者经历。完整取舍记录见 `natural-chinese-writing-cn/references/sources.md`。
