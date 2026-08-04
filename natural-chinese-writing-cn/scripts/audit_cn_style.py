#!/usr/bin/env python3
"""Heuristic audit for templated or AI-like Chinese prose patterns."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


LEVELS = {"low": 0, "medium": 1, "high": 2}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="-", help="UTF-8 text/Markdown file, or - for stdin")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on", choices=("low", "medium", "high"), help="Exit 1 at or above this risk")
    return parser.parse_args()


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def strip_nonprose(text: str) -> tuple[str, list[tuple[int, str]]]:
    lines: list[tuple[int, str]] = []
    in_code = False
    in_frontmatter = False
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if number == 1 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            continue
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or re.match(r"^\s*\|?\s*:?-{3,}", line):
            continue
        lines.append((number, line))
    return "\n".join(line for _, line in lines), lines


def add_finding(findings: list[dict], code: str, severity: str, message: str, matches: list[dict]) -> None:
    if matches:
        findings.append({"code": code, "severity": severity, "count": len(matches), "message": message, "matches": matches[:8]})


def regex_matches(lines: list[tuple[int, str]], pattern: str) -> list[dict]:
    compiled = re.compile(pattern)
    matches: list[dict] = []
    for number, line in lines:
        for hit in compiled.finditer(line):
            matches.append({"line": number, "text": hit.group(0)[:120]})
    return matches


def clean_line(line: str) -> str:
    value = re.sub(r"^\s*(?:#{1,6}|[-*+] |\d+[.)、]\s*)", "", line)
    value = re.sub(r"[*_`>\[\]()|]", "", value)
    return value.strip()


def audit(text: str) -> dict:
    prose, lines = strip_nonprose(text)
    findings: list[dict] = []

    add_finding(
        findings,
        "NEGATIVE_CONTRAST",
        "medium",
        "Repeated negative contrast can delay the positive claim.",
        regex_matches(lines, r"(?:不是|并非|不只是|不仅).{0,45}?(?:而是|而且|还要|更要|更是)"),
    )

    negations = regex_matches(lines, r"不(?:是|会|能|应|要|可|等于|代表|意味着|提供|承诺|保证|替代|编造|虚构)")
    chinese_chars = max(1, len(re.findall(r"[\u4e00-\u9fff]", prose)))
    if len(negations) >= 3 and len(negations) * 500 / chinese_chars >= 2.5:
        add_finding(findings, "DEFENSIVE_STACK", "medium", "Negation density is high; consolidate boundaries and lead with value.", negations)

    add_finding(
        findings,
        "META_ASSISTANT",
        "medium",
        "Meta narration or chatbot service language should stay out of publishable copy.",
        regex_matches(lines, r"下面(?:我们|将)|接下来(?:我们|将|我将)|让我们(?:来)?|本文将|以上就是|希望.{0,12}有所帮助|如有需要.{0,20}(?:告诉|联系)|如果你愿意.{0,20}可以"),
    )

    add_finding(
        findings,
        "PRODUCTION_RESIDUE",
        "high",
        "Production or chat-system residue appears in reader-facing text.",
        regex_matches(lines, r"turn\d+(?:search|view)\d+|contentReference|oaicite|\[attached_file:\d+\]|grok_card|Codex|提示词|模型生成|AI\s*生成"),
    )

    add_finding(
        findings,
        "PLACEHOLDER",
        "high",
        "Visible placeholders are unfinished publishing artifacts.",
        regex_matches(lines, r"\[(?:Your|Insert|Add|Enter|Describe|Specify|Choose|待补|请填写)[^\]]*\]|20\d{2}-XX-XX|<!--\s*(?:TODO|待补|填写)"),
    )

    bold_label = []
    for number, line in lines:
        if re.match(r"^\s*[-*+]\s+\*\*[^*]{1,30}[：:]\*\*", line):
            bold_label.append({"line": number, "text": line.strip()[:120]})
    if len(bold_label) >= 5:
        add_finding(findings, "BOLD_LABEL_LIST", "low", "Many bold-label bullets can make prose read like exported fields.", bold_label)

    opener_lines: dict[str, list[dict]] = defaultdict(list)
    for number, line in lines:
        stripped = clean_line(line)
        if not stripped or line.lstrip().startswith(("#", "|")):
            continue
        opener = re.split(r"[，。；：！？]", stripped, maxsplit=1)[0][:10]
        if len(opener) >= 5:
            opener_lines[opener].append({"line": number, "text": stripped[:120]})
    for opener, matches in sorted(opener_lines.items(), key=lambda item: -len(item[1])):
        if len(matches) >= 3:
            add_finding(findings, "REPEATED_OPENER", "medium", f"The opener “{opener}” repeats across sections or paragraphs.", matches)

    abstract_terms = regex_matches(lines, r"赋能|打造|构建|沉淀|闭环|体系化|全方位|深度(?:赋能|提升|优化|解析)|精准(?:赋能|触达|匹配)|抓手|链路|全面(?:提升|优化|升级)|切实(?:提升|推进)|显著(?:提升|改善)")
    if len(abstract_terms) >= 5:
        add_finding(findings, "ABSTRACT_CLUSTER", "medium", "Abstract promotional terms cluster without enough concrete actors or actions.", abstract_terms)

    connectors = regex_matches(lines, r"(?:^|[。；]\s*)(?:此外|与此同时|值得注意的是|需要指出的是|综上所述|总而言之|从某种意义上说)[，,]")
    if len(connectors) >= 3:
        add_finding(findings, "FORMULA_TRANSITION", "low", "Formulaic transitions repeat; let paragraph logic carry more of the connection.", connectors)

    slogan = regex_matches(lines, r"让每.{0,18}都.{0,35}每.{0,18}都|真正实现.{0,35}(?:跃迁|转变|升级)|共同开启.{0,30}(?:新篇章|新征程)|未来可期|持续赋能")
    add_finding(findings, "GENERIC_SLOGAN", "low", "The ending or summary sounds manufactured rather than concrete.", slogan)

    bullets = sum(1 for _, line in lines if re.match(r"^\s*[-*+]\s+", line))
    headings = sum(1 for _, line in lines if re.match(r"^\s*#{1,6}\s+", line))
    nonempty = sum(1 for _, line in lines if line.strip())
    if bullets >= 10 and bullets / max(1, nonempty) > 0.42:
        findings.append({"code": "LIST_DENSITY", "severity": "low", "count": bullets, "message": "The document relies heavily on bullets; convert explanatory sequences to prose or tables.", "matches": []})
    if headings >= 10 and headings / max(1, nonempty) > 0.22:
        findings.append({"code": "HEADING_DENSITY", "severity": "low", "count": headings, "message": "Heading density is high; reserve headings for navigable sections.", "matches": []})

    weights = {"low": 4, "medium": 10, "high": 24}
    score = min(100, sum(weights[item["severity"]] + min(item["count"], 5) for item in findings))
    risk = "high" if score >= 40 else "medium" if score >= 18 else "low"
    counts = Counter(item["severity"] for item in findings)
    return {
        "risk": risk,
        "score": score,
        "chinese_characters": chinese_chars,
        "finding_count": len(findings),
        "severity_counts": dict(counts),
        "findings": findings,
        "note": "Heuristic signals for editing, not proof of AI authorship.",
    }


def print_text(result: dict) -> None:
    print(f"risk={result['risk']} score={result['score']} findings={result['finding_count']}")
    for item in result["findings"]:
        print(f"[{item['severity']}] {item['code']} x{item['count']}: {item['message']}")
        for match in item.get("matches", [])[:3]:
            print(f"  L{match['line']}: {match['text']}")
    print(result["note"])


def main() -> int:
    args = parse_args()
    try:
        result = audit(read_text(args.path))
    except (OSError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)
    if args.fail_on and LEVELS[result["risk"]] >= LEVELS[args.fail_on]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
