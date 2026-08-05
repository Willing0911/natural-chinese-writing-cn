---
name: natural-chinese-writing-cn
description: Audit, rewrite, or draft natural Chinese prose for student-facing and customer-facing materials, service introductions, course content, reports, public-account articles, social/video scripts, and professional documents. Use when the user asks to 去AI味、降低AI腔、活人感写作、更像真人、学生直接可读、口语化、优化表达逻辑, or wants to reduce repeated “不是/不会/不仅/而是”, formulaic headings, bold-label lists, over-neat parallelism, empty slogans, abstract promotional language, invented personal experience, or other templated AI writing patterns. Also use as a final quality gate for substantial Chinese prose intended for external readers. Preserve facts and the intended register; improve reader experience and the user's own voice rather than imitating a named creator or trying to evade AI detectors.
---

# Natural Chinese Writing CN

把文本改成“一个具体的人写给一个具体的人”，而不是把词语随机替换得更口语。先修复信息顺序、读者关系和段落推进，再处理句式和词汇。

## Core constraints

1. Preserve every supported fact, date, number, commitment, citation, and necessary boundary. Never invent detail to create “人味”.
2. Treat the user's own writing sample as the highest-priority voice reference. Match its sentence length, vocabulary, paragraph openings, punctuation, and degree of formality.
3. Keep the register appropriate. Student-facing material can be direct and warm; legal, academic, technical, and policy text may need neutral precision.
4. Treat AI-like patterns as editing signals, not proof of authorship. Look for clusters and repetition rather than banning a word in isolation.
5. Optimize for readers, not detector scores. Do not promise to bypass AIGC or AI detectors.
6. Build human presence from supplied evidence. Never invent a first-hand scene, emotion, opinion, failure, quote, or first-person experience to make the prose feel alive.
7. Treat a named creator as a design reference, not a voice costume. Extract high-level craft such as evidence, pacing, and point of view; do not copy signature catchphrases, fixed endings, biography, or a recognizable personal persona.

## Choose a mode

- **rewrite**: Default. Return the revised text and, when useful, a short summary of the main logic changes.
- **audit**: Flag patterns and explain their reader impact without changing the text.
- **file edit**: Edit the requested file in place. Preserve frontmatter, links, code, tables, citations, and protected facts.
- **embedded gate**: When another task invokes this skill before delivery, run the audit internally and return only the clean final prose.
- **calibration**: When the user wants to improve this or another writing Skill, or supplies an agent draft plus a human-edited version, follow [references/calibration.md](references/calibration.md). Learn from repeated choices across paired drafts instead of summarizing published samples once.

## Workflow

### 1. Lock the reader and purpose

Determine:

- who will read it;
- what they already know;
- what they should understand, feel, decide, or do after reading;
- the intended voice and delivery surface.

If these are obvious from context, proceed without asking. If one missing choice would materially change the result, ask one concise question.

For substantial long-form content, lock an internal editorial contract before drafting: **what happened or was observed → what judgment the piece owns → what the reader should understand or do**. If the source has a topic but no real angle, propose a small set of distinct angles before expanding a generic full draft.

### 2. Make an information inventory

Before rewriting, separate:

- facts and commitments that must survive;
- judgments that need support;
- evidence that supports or could change those judgments;
- boundaries that must remain visible;
- voice anchors already supplied by the user: real observations, scenes, wording habits, emotions, uncertainties, and opinions;
- repeated or decorative wording that can be cut;
- source structure that may be freely reorganized.

Preserve information, not the original shape. Merge, split, or reorder paragraphs when that improves the reader's path.

If the draft needs a personal scene or first-person judgment but the source has none, keep the language neutral or mark the missing input. Do not fill the gap with a plausible story.

When research is part of the task, look for both supporting and disconfirming evidence. Treat search results, analogy candidates, and structural options as material for judgment, not as the judgment itself. Verify factual claims separately from creative drafting.

### 3. Choose a delivery profile

Use the delivery surface to set the amount of personality and structure:

- **student or customer material**: lead with the decision, support, deliverable, and next action; keep warmth without manufacturing intimacy;
- **report or professional document**: make ownership, evidence, trade-offs, and conclusion explicit; keep useful headings and tables;
- **social or video script**: start from a concrete hook or tension, reveal evidence in a deliberate order, then land on one clear judgment or action;
- **personal long-form article**: start from a supplied observation or experience, let research and examples deepen it, and return every detour to the main question.

Do not apply one surface's signals to another. A professional report does not need slang or dramatic punctuation to sound human, and a spoken script should not read like a report outline.

### 4. Audit eight layers

1. **Value order**: Does the text lead with disclaimers, definitions, or what the service “is not” before explaining its value?
2. **Evidence ownership**: Who can truthfully say each first-person claim? Are scenes, emotions, opinions, examples, and quotes supplied or verified?
3. **Paragraph movement**: Does each paragraph add a fact, decision, example, action, or consequence? Cut restatements.
4. **Main-thread control**: After a story, analogy, background note, or example, does the text make its relevance clear and return to the reader's question?
5. **Sentence shape**: Flag stacked negation, “不是……而是……”, rigid parallelism, slogan-like conclusions, abstract noun chains, and repeated openers.
6. **Document skeleton**: Flag identical section templates, excessive headings, bold-label vertical lists, forced groups of three, and list-heavy explanation.
7. **Voice and rhythm**: Check whether sentence lengths, transitions, and certainty are unnaturally uniform. Also flag forced slang, scripted self-deprecation, repeated rhetorical questions, and decorative emotional punctuation.
8. **Delivery residue**: Remove chatbot greetings, meta-announcements, placeholders, internal citation tokens, tool/process language, and production notes from external copy.

Read [references/patterns.md](references/patterns.md) when the draft has several interacting patterns or the user asks for an audit. Read [references/examples.md](references/examples.md) when rewriting service, student, course, or report content.

### 5. Rewrite from the reader's path

Prefer this sequence for student and customer materials:

**current question → how support works → concrete deliverable → observable outcome → necessary boundary**

Apply it as a reasoning sequence, not a repeated template. Vary the wording and paragraph form across sections.

Use these techniques:

- Lead with the outcome or decision the reader cares about.
- Name the actor, action, object, and result when the source supports them.
- Attribute judgments to a real point of view. Use “我” only when the user supplied that experience or explicitly owns the judgment; otherwise name the source or use a neutral formulation.
- Move necessary boundaries next to the decision they affect, or consolidate them once near the end.
- Replace negative contrast with a positive claim whenever the contrast adds no real information.
- Use lists only for genuinely parallel items. Use paragraphs for explanation and transitions.
- When a paragraph leaves the main line for a case, analogy, or background fact, add a concise return that explains why it matters here.
- When presenting several cases, tests, or proof points, choose an order that creates understanding or raises the stakes. Do not dump them into a flat list by default.
- State genuine uncertainty, cost, trade-off, or failure point when the source supports it. Credibility comes from accountable limits, not compulsory humility.
- Keep useful repetition of a technical term; avoid synonym cycling for its own sake.
- Prefer concrete nouns and verbs over stacks such as “赋能、打造、构建、全面提升”.
- Vary rhythm by information weight. Use a short standalone line only when it deserves a pause; never add fragments, slang, ellipses, or question marks to simulate spontaneity.
- End on a concrete next step, result, or unresolved decision rather than a generic uplifting sentence.

### 6. Run a four-layer final audit

Run the passes in order. Fix higher-level failures before polishing words.

1. **Integrity and hard signals**: preserve facts, citations, commitments, and boundaries; remove invented scenes, emotions, quotes, personal experience, unsupported authority, intentional mistakes, production residue, and repeated formulaic signals.
2. **Logic and content**: confirm that the opening establishes the real question, every section advances it, claims have support, counterevidence was considered where relevant, and examples return to the main thread.
3. **Voice and surface fit**: compare with the user's samples or accepted edits; check ownership, register, rhythm, transitions, structure, and whether the formatting fits the delivery surface.
4. **Human-presence and reader experience**: ask whether a real observation, accountable judgment, or honest choice shapes the text. Flag passages that are merely correct, smooth, and interchangeable. Confirm what the reader can take away or do next.

For a detailed audit, record only the highest-value failures from each layer. For an embedded gate, repair them silently and return the clean copy.

For Markdown or text files, optionally run:

```bash
python3 scripts/audit_cn_style.py path/to/draft.md --format text --fail-on high
```

The script is a heuristic quality gate. Review its findings in context; do not mechanically obey every flag.

## Pattern priorities

Fix in this order:

1. fabricated or unsupported content;
2. reader-value order and repeated disclaimers;
3. missing editorial judgment, contradictory evidence, and lost main thread;
4. paragraph-level repetition and template skeletons;
5. missing evidence ownership and unearned first-person voice;
6. vague actors, abstract claims, and missing actions;
7. sentence rhythm, transitions, punctuation, and word choice.

Lexical cleanup alone cannot rescue weak logic.

## Output requirements

- Deliver the revised text without an essay about AI writing.
- Summarize changes in no more than five bullets unless the user requested a detailed audit.
- In file or embedded mode, keep audit notes out of the reader-facing artifact.
- When the source contains uncertain or missing facts, retain the uncertainty in natural language instead of filling the gap.

## Quality gate

The final text should pass all nine checks:

1. **Reader fit**: audience, purpose, and action are clear.
2. **Directness**: the value or conclusion appears before defensive explanation.
3. **Progression**: each paragraph moves the idea forward.
4. **Ownership**: first-person experience, emotion, and judgment belong to a real supplied source.
5. **Thread**: stories, analogies, and proof points return to the main question.
6. **Specificity**: supported actors, actions, dates, evidence, and outcomes replace empty abstractions.
7. **Natural variation**: structure and rhythm vary for a reason, not randomly or through forced colloquial markers.
8. **Trust**: the text respects the reader and states uncertainty, cost, and boundaries where they matter.
9. **Fidelity**: facts and source meaning remain intact.

## Research basis

See [references/sources.md](references/sources.md) for the reviewed public skills and the design choices adopted or rejected here.
