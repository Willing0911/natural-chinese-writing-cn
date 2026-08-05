# 公开 Skill 检索与取舍

首次检索：2026-08-04。最近复核：2026-08-05。

## Reviewed sources

1. [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)
   - 采用：保留信息而非原结构、事实不可新增、声音校准、模式组合判断、负向排比与模板结构审校。
   - 调整：英文破折号、标题大小写和 `-ing` 规则不直接移植为中文硬规则。

2. [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)
   - 采用：直接性、节奏、信任读者、删除元话语与空泛结尾。
   - 调整：该项目主要翻译英文 Humanizer；本 Skill 重新加入中文服务材料、学生材料和商业说明场景。

3. [stephenturner/skill-deslop](https://github.com/stephenturner/skill-deslop)
   - 采用：Directness、Rhythm、Trust、Authenticity、Density 五维复盘思路。
   - 调整：不设置统一文学化声音，按学生、客户、技术、正式材料分别校准。

4. [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md)
   - 采用：AI 特征是信号而非证据、保留已经自然的段落、优先局部编辑、检查占位符和聊天工具残留。
   - 调整：不以作者识别或检测器分数作为交付目标。

5. [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill)
   - 采用：模式目录、声音配置、审校解释和迭代检查。
   - 调整：不采用为提高所谓 burstiness 而随机打乱句子的做法；变化必须服务信息轻重。

6. [redbaronyyyyy-eng/humanizer-zh-academic](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic)
   - 采用：中文整齐并列句、模板化问题陈述、画蛇添足总结句等观察。
   - 调整：该 Skill 面向学术 AIGC 检测，本 Skill 面向一般专业中文和直接阅读体验。

7. [KKKKhazix/khazix-skills 的 khazix-writer](https://github.com/KKKKhazix/khazix-skills/blob/main/khazix-writer/SKILL.md)
   - 上游状态：GitHub 历史显示 `khazix-writer` 当前版本于 2026-04-06 提交，仓库使用 MIT License。
   - 采用：区分第一手经验与可辅助扩写的背景信息；案例、类比和偏离后回到主线；多个证据按理解或影响递进；从事实、主线、声音和最终阅读感受分层终审。
   - 调整：原 Skill 是“数字生命卡兹克”的个人公众号长文文风，不直接移植其口头禅、情绪标点、固定结尾、个人经历或硬性频次指标。本 Skill 优先匹配用户自己的声音，并保留学生材料、客户说明、报告和视频脚本的语体差异。

8. 数字生命卡兹克：[《打磨三年！今天，我决定把「卡兹克风格创作.skill」开源了！》微信原链接](https://mp.weixin.qq.com/s/DRA5s4PqF3kI-hqajl3how) 与[同名公开全文页](https://www.uisdc.com/beyond-ai-writing)
   - 采用：创作 Skill 需要通过「当前规则生成—用户亲自改写—差异分析—规则回灌」持续校准；代表作的自动风格总结只是起点；证据、类比和已定角度的扩写可由 Agent 辅助，真实经验、核心判断、情绪与最终选择不得伪造；搜索证据时同时查找支持与反证；故意添加错别字不能制造真实感。
   - 调整：文中的具体模型排名、个人主观效果比例和 3–4 轮经验不作为通用性能事实。本 Skill 把 3–4 轮设为默认停止参考，同时使用留出任务和连续无高价值差异作为更稳定的停止条件。

## Design conclusions

- “去 AI 味”首先是信息设计和读者关系问题，其次才是词汇问题。
- 负向句式、三段式、破折号、粗体或连接词都只能作为组合信号。
- 作者样本优先于通用规则；已有自然段落应少改。
- 具体细节必须来自原文或用户，不能为了自然度添加事实。
- “活人感”来自真实视角、可追溯经验、负责任的判断和有主线的节奏，不是口头禅或标点套装。
- 具名创作者可以提供方法参考，不应成为可复制的人格模板。
- 一次风格归纳不足以建立稳定 Skill；同任务的人工改稿差异和留出任务更有信息量。
- 生成与事实验证应分开；创意流畅不能代替来源核验。
- 质量目标是清楚、可信、可读和有声音，不是规避检测。
