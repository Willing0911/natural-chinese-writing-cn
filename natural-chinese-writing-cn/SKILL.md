---
name: natural-chinese-writing-cn
description: Audit, rewrite, or draft natural Chinese prose for student-facing and customer-facing materials, service introductions, course content, reports, social/video scripts, and professional documents. Use when the user asks to 去AI味、降低AI腔、更像真人、学生直接可读、口语化、优化表达逻辑, or wants to reduce repeated “不是/不会/不仅/而是”, formulaic headings, bold-label lists, over-neat parallelism, empty slogans, abstract promotional language, or other templated AI writing patterns. Also use as a final quality gate for substantial Chinese prose intended for external readers. Preserve facts and the intended register; improve reader experience rather than trying to evade AI detectors.
---

# Natural Chinese Writing CN

把文本改成“一个具体的人写给一个具体的人”，而不是把词语随机替换得更口语。先修复信息顺序、读者关系和段落推进，再处理句式和词汇。

## Core constraints

1. Preserve every supported fact, date, number, commitment, citation, and necessary boundary. Never invent detail to create “人味”.
2. Treat the user's own writing sample as the highest-priority voice reference. Match its sentence length, vocabulary, paragraph openings, punctuation, and degree of formality.
3. Keep the register appropriate. Student-facing material can be direct and warm; legal, academic, technical, and policy text may need neutral precision.
4. Treat AI-like patterns as editing signals, not proof of authorship. Look for clusters and repetition rather than banning a word in isolation.
5. Optimize for readers, not detector scores. Do not promise to bypass AIGC or AI detectors.

## Choose a mode

- **rewrite**: Default. Return the revised text and, when useful, a short summary of the main logic changes.
- **audit**: Flag patterns and explain their reader impact without changing the text.
- **file edit**: Edit the requested file in place. Preserve frontmatter, links, code, tables, citations, and protected facts.
- **embedded gate**: When another task invokes this skill before delivery, run the audit internally and return only the clean final prose.

## Workflow

### 1. Lock the reader and purpose

Determine:

- who will read it;
- what they already know;
- what they should understand, feel, decide, or do after reading;
- the intended voice and delivery surface.

If these are obvious from context, proceed without asking. If one missing choice would materially change the result, ask one concise question.

### 2. Make an information inventory

Before rewriting, separate:

- facts and commitments that must survive;
- judgments that need support;
- boundaries that must remain visible;
- repeated or decorative wording that can be cut;
- source structure that may be freely reorganized.

Preserve information, not the original shape. Merge, split, or reorder paragraphs when that improves the reader's path.

### 3. Audit six layers

1. **Value order**: Does the text lead with disclaimers, definitions, or what the service “is not” before explaining its value?
2. **Paragraph movement**: Does each paragraph add a fact, decision, example, action, or consequence? Cut restatements.
3. **Sentence shape**: Flag stacked negation, “不是……而是……”, rigid parallelism, slogan-like conclusions, abstract noun chains, and repeated openers.
4. **Document skeleton**: Flag identical section templates, excessive headings, bold-label vertical lists, forced groups of three, and list-heavy explanation.
5. **Voice and rhythm**: Check whether sentence lengths, transitions, and certainty are unnaturally uniform. Preserve purposeful irregularity.
6. **Delivery residue**: Remove chatbot greetings, meta-announcements, placeholders, internal citation tokens, tool/process language, and production notes from external copy.

Read [references/patterns.md](references/patterns.md) when the draft has several interacting patterns or the user asks for an audit. Read [references/examples.md](references/examples.md) when rewriting service, student, course, or report content.

### 4. Rewrite from the reader's path

Prefer this sequence for student and customer materials:

**current question → how support works → concrete deliverable → observable outcome → necessary boundary**

Apply it as a reasoning sequence, not a repeated template. Vary the wording and paragraph form across sections.

Use these techniques:

- Lead with the outcome or decision the reader cares about.
- Name the actor, action, object, and result when the source supports them.
- Move necessary boundaries next to the decision they affect, or consolidate them once near the end.
- Replace negative contrast with a positive claim whenever the contrast adds no real information.
- Use lists only for genuinely parallel items. Use paragraphs for explanation and transitions.
- Keep useful repetition of a technical term; avoid synonym cycling for its own sake.
- Prefer concrete nouns and verbs over stacks such as “赋能、打造、构建、全面提升”.
- End on a concrete next step, result, or unresolved decision rather than a generic uplifting sentence.

### 5. Run a second-pass audit

Read the rewrite aloud mentally and check:

- Does the opening answer “这和我有什么关系” quickly?
- Can any paragraph be cut without losing information?
- Do three or more sections begin or end the same way?
- Are boundaries repeated more than once?
- Does every strong claim have source support?
- Does the text sound like the intended person and context?

For Markdown or text files, optionally run:

```bash
python3 scripts/audit_cn_style.py path/to/draft.md --format text --fail-on high
```

The script is a heuristic quality gate. Review its findings in context; do not mechanically obey every flag.

## Pattern priorities

Fix in this order:

1. fabricated or unsupported content;
2. reader-value order and repeated disclaimers;
3. paragraph-level repetition and template skeletons;
4. vague actors, abstract claims, and missing actions;
5. sentence rhythm, transitions, punctuation, and word choice.

Lexical cleanup alone cannot rescue weak logic.

## Output requirements

- Deliver the revised text without an essay about AI writing.
- Summarize changes in no more than five bullets unless the user requested a detailed audit.
- In file or embedded mode, keep audit notes out of the reader-facing artifact.
- When the source contains uncertain or missing facts, retain the uncertainty in natural language instead of filling the gap.

## Quality gate

The final text should pass all seven checks:

1. **Reader fit**: audience, purpose, and action are clear.
2. **Directness**: the value or conclusion appears before defensive explanation.
3. **Progression**: each paragraph moves the idea forward.
4. **Specificity**: supported actors, actions, dates, evidence, and outcomes replace empty abstractions.
5. **Natural variation**: structure and rhythm vary for a reason, not randomly.
6. **Trust**: the text respects the reader and states boundaries once, clearly.
7. **Fidelity**: facts and source meaning remain intact.

## Research basis

See [references/sources.md](references/sources.md) for the reviewed public skills and the design choices adopted or rejected here.
