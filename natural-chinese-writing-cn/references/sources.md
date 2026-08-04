# 公开 Skill 检索与取舍

检索日期：2026-08-04。

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

## Design conclusions

- “去 AI 味”首先是信息设计和读者关系问题，其次才是词汇问题。
- 负向句式、三段式、破折号、粗体或连接词都只能作为组合信号。
- 作者样本优先于通用规则；已有自然段落应少改。
- 具体细节必须来自原文或用户，不能为了自然度添加事实。
- 质量目标是清楚、可信、可读和有声音，不是规避检测。
