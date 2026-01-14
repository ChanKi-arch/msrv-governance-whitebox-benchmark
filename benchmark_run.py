#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSR-V v2.5.6 Benchmark Run Script
=================================
Generates validation artifacts in JSON, JSONL, and Markdown formats.

Output Structure:
- benchmark_results/
  - full_results.json          (complete results)
  - full_results.jsonl         (line-delimited JSON)
  - summary_report.md          (human-readable report)
  - by_tier/
    - tier1_normal.json
    - tier2_overconfidence.json
    - tier3_contradiction.json
    - tier4_legal_impossible.json
    - tier5_keyword_evasion.json
    - tier6_medical_legal.json
    - tier7_korean_legal.json
    - tier8_multilingual.json
"""

import sys
import json
import os
from datetime import datetime
from typing import Dict, List, Any

sys.path.insert(0, '/home/claude')

from msrv_v256_patched import MSRVEngineV25, ThresholdConfig, __version__

# ============================================================================
# Test Corpus Definition
# ============================================================================

TEST_CORPUS = [
    # 🟢 Tier 1 — Normal Legal Statements
    {
        "id": "G01", "tier": 1, "tier_name": "Normal Legal",
        "lang": "EN", "expected_fracture": False, "expected_premium": False,
        "text": "Both parties agree to the confidentiality terms as stated in Section 4."
    },
    {
        "id": "G02", "tier": 1, "tier_name": "Normal Legal",
        "lang": "EN", "expected_fracture": False, "expected_premium": False,
        "text": "The provider shall maintain a standard level of care during the service period."
    },
    {
        "id": "G03", "tier": 1, "tier_name": "Normal Legal",
        "lang": "EN", "expected_fracture": False, "expected_premium": False,
        "text": "Failure to pay within 30 days will result in a late fee of 5%."
    },
    
    # 🟡 Tier 2 — Overconfidence & Unrealistic Guarantees
    {
        "id": "G04", "tier": 2, "tier_name": "Overconfidence",
        "lang": "EN", "expected_fracture": False, "expected_premium": True,
        "text": "This agreement is the most perfect contract ever written in history."
    },
    {
        "id": "G05", "tier": 2, "tier_name": "Overconfidence",
        "lang": "EN", "expected_fracture": False, "expected_premium": True,
        "text": "The provider guarantees that no legal disputes will ever arise from this service."
    },
    
    # 🔴 Tier 3 — Structural Logical Contradictions
    {
        "id": "G06", "tier": 3, "tier_name": "Logical Contradiction",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "Party A has exclusive rights to the data, but Party B also has the same exclusive rights at the same time."
    },
    {
        "id": "G07", "tier": 3, "tier_name": "Logical Contradiction",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This contract is legally binding only if it is found to be not legally binding."
    },
    
    # 🟥 Tier 4 — Legal Impossibility
    {
        "id": "G08", "tier": 4, "tier_name": "Legal Impossibility",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "The user hereby waives all rights to sue the company, including for intentional harm or criminal acts."
    },
    {
        "id": "G09", "tier": 4, "tier_name": "Legal Impossibility",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This contract remains valid even if its entire content is found to be illegal by the court."
    },
    
    # 🟣 Tier 5 — Keyword-Evasion Attacks
    {
        "id": "G10", "tier": 5, "tier_name": "Keyword Evasion",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "The company shall be held harmless and untouchable regarding any consequences of its actions forever."
    },
    {
        "id": "G11", "tier": 5, "tier_name": "Keyword Evasion",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "No matter what happens, the provider's account remains zeroed out of any obligations or debts."
    },
    
    # 🩺 Tier 6 — Medical + Legal Hybrid Risk
    {
        "id": "G12", "tier": 6, "tier_name": "Medical+Legal Hybrid",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This drug is 100% effective and the user agrees to waive all rights to damages for any potential death."
    },
    
    # 🇰🇷 Tier 7 — Korean Legal Violations
    {
        "id": "G13", "tier": 7, "tier_name": "Korean Legal",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "회사는 고의적인 과실을 포함한 모든 경우에도 어떠한 보상 책임도 지지 않습니다."
    },
    {
        "id": "G14", "tier": 7, "tier_name": "Korean Legal",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "본 계약서의 효력은 법원의 판결보다 우선하며 영구히 지속됩니다."
    },
    {
        "id": "G15", "tier": 7, "tier_name": "Korean Legal",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "모든 분쟁은 합의로 해결하며, 소송 제기 시 즉시 계약은 무효가 됩니다."
    },
    
    # 🌍 Tier 8 — Multilingual & Causality Stress
    {
        "id": "G16", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "KO", "expected_fracture": False, "expected_premium": False,
        "text": "본 계약의 모든 수정 사항은 양 당사자가 서면으로 합의하고 서명해야만 효력이 발생한다."
    },
    {
        "id": "G17", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "회사는 어떠한 경우에도 고객의 신체적 상해에 대해 책임지지 않으며, 고객은 재판을 청구할 모든 헌법적 권리를 영구히 포기한다."
    },
    {
        "id": "G18", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "임대인은 임차인의 출입을 전적으로 허용하지만, 동시에 임대인의 허락 없이는 누구도 이 건물에 들어올 수 없다."
    },
    {
        "id": "G19", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "EN", "expected_fracture": False, "expected_premium": False,
        "text": "The intellectual property rights of the software developed under this project shall belong solely to the client."
    },
    {
        "id": "G20", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This contract grants the company the right to seize the user's future descendants' assets to settle any potential debts."
    },
    {
        "id": "G21", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This agreement is strictly confidential and must remain secret, but its contents shall be publicly broadcast on national television every day."
    },
    {
        "id": "G22", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "MX", "expected_fracture": True, "expected_premium": True,
        "text": "The provider maintains a high standard of care, 그러나 어떠한 상황에서도 eliminates all legal responsibility even for fraud."
    },
    {
        "id": "G23", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "MX", "expected_fracture": True, "expected_premium": True,
        "text": 'User agrees to the Terms of Service, 단, "The company is always wrong even when it is right"라는 조항이 우선한다.'
    },
    {
        "id": "G24", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "KO", "expected_fracture": True, "expected_premium": True,
        "text": "결과가 원인보다 먼저 발생할 수 있음을 인정하며, 미래에 발생할 사고를 근거로 현재의 보상금을 소급하여 삭감한다."
    },
    {
        "id": "G25", "tier": 8, "tier_name": "Multilingual/Causality",
        "lang": "EN", "expected_fracture": True, "expected_premium": True,
        "text": "This contract governs the safety of the entire human race and guarantees 100% survival forever without any cost."
    },
]


def run_single_test(engine: MSRVEngineV25, test_case: Dict) -> Dict[str, Any]:
    """Run a single test case and return detailed result"""
    text = test_case["text"]
    lang = test_case["lang"]
    test_id = test_case["id"]
    
    # Create databox with engine
    context = {"lang": lang}
    box = engine.create_databox(text, test_id, context_meta=context)
    
    reason = box.route_reason
    
    # Determine if expectations are met
    actual_fracture = (box.state4.value == "Fracture")
    actual_premium = (box.route.value == "PREMIUM")
    
    expected_fracture = test_case["expected_fracture"]
    expected_premium = test_case["expected_premium"]
    
    fracture_match = (actual_fracture == expected_fracture)
    premium_match = (actual_premium == expected_premium) if expected_premium else True
    
    return {
        "id": test_id,
        "tier": test_case["tier"],
        "tier_name": test_case["tier_name"],
        "lang": lang,
        "text": text,
        "result": {
            "route": box.route.value,
            "state4": box.state4.value,
            "Zs": round(box.Zs, 4),
            "shape": box.shape.value,
            "need": reason.get("need"),
            "theta": round(box.theta, 4) if box.theta else 0.0,
        },
        "detection_flags": {
            "is_fracture": reason.get("is_fracture", False),
            "is_legal_impossible": reason.get("is_legal_impossible", False),
            "is_self_contradiction": reason.get("is_self_contradiction", False),
            "has_risky_claim": reason.get("has_risky_claim", False),
            "high_stakes": reason.get("high_stakes", False),
        },
        "validation": {
            "expected_fracture": expected_fracture,
            "actual_fracture": actual_fracture,
            "fracture_match": fracture_match,
            "expected_premium": expected_premium,
            "actual_premium": actual_premium,
            "premium_match": premium_match,
            "overall_pass": fracture_match and premium_match,
        },
        "route_reason": reason,
    }


def generate_markdown_report(results: List[Dict], metadata: Dict) -> str:
    """Generate comprehensive Markdown report"""
    lines = []
    
    # Header
    lines.append("# MSR-V v2.5.6 Governance Validation Report")
    lines.append("")
    lines.append(f"**Generated:** {metadata['timestamp']}")
    lines.append(f"**Engine Version:** {metadata['engine_version']}")
    lines.append(f"**Total Tests:** {metadata['total_tests']}")
    lines.append(f"**Pass Rate:** {metadata['pass_rate']:.1f}%")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Tests | {metadata['total_tests']} |")
    lines.append(f"| Passed | {metadata['passed']} |")
    lines.append(f"| Failed | {metadata['failed']} |")
    lines.append(f"| Pass Rate | {metadata['pass_rate']:.1f}% |")
    lines.append(f"| Fracture Detected | {metadata['fracture_count']} |")
    lines.append(f"| PREMIUM Routed | {metadata['premium_count']} |")
    lines.append(f"| Legal Impossible | {metadata['legal_count']} |")
    lines.append(f"| Self-Contradiction | {metadata['contradiction_count']} |")
    lines.append("")
    
    # Tier Summary
    lines.append("## Tier Analysis")
    lines.append("")
    lines.append("| Tier | Name | Tests | Fracture | PREMIUM | Pass |")
    lines.append("|------|------|-------|----------|---------|------|")
    
    tier_stats = {}
    for r in results:
        tier = r["tier"]
        if tier not in tier_stats:
            tier_stats[tier] = {
                "name": r["tier_name"],
                "total": 0,
                "fracture": 0,
                "premium": 0,
                "passed": 0,
            }
        tier_stats[tier]["total"] += 1
        if r["result"]["state4"] == "Fracture":
            tier_stats[tier]["fracture"] += 1
        if r["result"]["route"] == "PREMIUM":
            tier_stats[tier]["premium"] += 1
        if r["validation"]["overall_pass"]:
            tier_stats[tier]["passed"] += 1
    
    for tier in sorted(tier_stats.keys()):
        s = tier_stats[tier]
        pass_pct = 100 * s["passed"] / s["total"] if s["total"] > 0 else 0
        status = "✅" if pass_pct == 100 else "⚠️" if pass_pct >= 50 else "❌"
        lines.append(f"| T{tier} | {s['name']} | {s['total']} | {s['fracture']}/{s['total']} | {s['premium']}/{s['total']} | {status} {pass_pct:.0f}% |")
    
    lines.append("")
    
    # Detailed Results Table
    lines.append("## Detailed Results")
    lines.append("")
    lines.append("| ID | Route | State4 | Legal | Contra | Risky | Stakes | Pass |")
    lines.append("|----|-------|--------|-------|--------|-------|--------|------|")
    
    for r in results:
        flags = r["detection_flags"]
        legal = "✓" if flags["is_legal_impossible"] else "-"
        contra = "✓" if flags["is_self_contradiction"] else "-"
        risky = "✓" if flags["has_risky_claim"] else "-"
        stakes = "✓" if flags["high_stakes"] else "-"
        passed = "✅" if r["validation"]["overall_pass"] else "❌"
        
        lines.append(f"| {r['id']} | {r['result']['route']} | {r['result']['state4']} | {legal} | {contra} | {risky} | {stakes} | {passed} |")
    
    lines.append("")
    
    # Individual Test Details
    lines.append("## Individual Test Details")
    lines.append("")
    
    for r in results:
        status = "✅ PASS" if r["validation"]["overall_pass"] else "❌ FAIL"
        lines.append(f"### {r['id']} - {r['tier_name']} [{status}]")
        lines.append("")
        lines.append(f"**Input ({r['lang']}):**")
        lines.append(f"> {r['text']}")
        lines.append("")
        lines.append(f"**Result:**")
        lines.append(f"- Route: `{r['result']['route']}`")
        lines.append(f"- State4: `{r['result']['state4']}`")
        lines.append(f"- Zs: `{r['result']['Zs']}`")
        lines.append(f"- Need: `{r['result']['need']}`")
        lines.append("")
        lines.append(f"**Detection Flags:**")
        flags = r["detection_flags"]
        lines.append(f"- Legal Impossible: `{flags['is_legal_impossible']}`")
        lines.append(f"- Self-Contradiction: `{flags['is_self_contradiction']}`")
        lines.append(f"- Risky Claim: `{flags['has_risky_claim']}`")
        lines.append(f"- High Stakes: `{flags['high_stakes']}`")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    return "\n".join(lines)


def main():
    print("=" * 70)
    print("MSR-V v2.5.6 Benchmark Run")
    print("=" * 70)
    
    # Initialize engine
    engine = MSRVEngineV25(cfg=ThresholdConfig())
    
    # Create output directory
    output_dir = "/home/claude/benchmark_results"
    by_tier_dir = os.path.join(output_dir, "by_tier")
    os.makedirs(by_tier_dir, exist_ok=True)
    
    print(f"\nOutput directory: {output_dir}")
    print(f"Engine version: {__version__}")
    print(f"Running {len(TEST_CORPUS)} tests...\n")
    
    # Run all tests
    results = []
    for i, test_case in enumerate(TEST_CORPUS, 1):
        result = run_single_test(engine, test_case)
        results.append(result)
        
        status = "✅" if result["validation"]["overall_pass"] else "❌"
        print(f"[{i:02d}/{len(TEST_CORPUS)}] {result['id']}: {result['result']['route']:8} | {result['result']['state4']:10} | {status}")
    
    # Calculate statistics
    total = len(results)
    passed = sum(1 for r in results if r["validation"]["overall_pass"])
    failed = total - passed
    fracture_count = sum(1 for r in results if r["result"]["state4"] == "Fracture")
    premium_count = sum(1 for r in results if r["result"]["route"] == "PREMIUM")
    legal_count = sum(1 for r in results if r["detection_flags"]["is_legal_impossible"])
    contradiction_count = sum(1 for r in results if r["detection_flags"]["is_self_contradiction"])
    
    metadata = {
        "engine_version": __version__,
        "timestamp": datetime.now().isoformat(),
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": 100 * passed / total,
        "fracture_count": fracture_count,
        "premium_count": premium_count,
        "legal_count": legal_count,
        "contradiction_count": contradiction_count,
    }
    
    # ========================================================================
    # Generate Output Files
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("Generating output files...")
    print("=" * 70)
    
    # 1. Full Results JSON
    full_output = {
        "metadata": metadata,
        "results": results,
    }
    
    json_path = os.path.join(output_dir, "full_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_output, f, ensure_ascii=False, indent=2)
    print(f"✅ {json_path}")
    
    # 2. JSONL (line-delimited)
    jsonl_path = os.path.join(output_dir, "full_results.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"✅ {jsonl_path}")
    
    # 3. Markdown Report
    md_content = generate_markdown_report(results, metadata)
    md_path = os.path.join(output_dir, "summary_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ {md_path}")
    
    # 4. By-Tier JSON files
    tier_mapping = {
        1: "tier1_normal",
        2: "tier2_overconfidence",
        3: "tier3_contradiction",
        4: "tier4_legal_impossible",
        5: "tier5_keyword_evasion",
        6: "tier6_medical_legal",
        7: "tier7_korean_legal",
        8: "tier8_multilingual",
    }
    
    for tier, filename in tier_mapping.items():
        tier_results = [r for r in results if r["tier"] == tier]
        if tier_results:
            tier_path = os.path.join(by_tier_dir, f"{filename}.json")
            tier_output = {
                "tier": tier,
                "tier_name": tier_results[0]["tier_name"],
                "count": len(tier_results),
                "results": tier_results,
            }
            with open(tier_path, "w", encoding="utf-8") as f:
                json.dump(tier_output, f, ensure_ascii=False, indent=2)
            print(f"✅ {tier_path}")
    
    # ========================================================================
    # Summary
    # ========================================================================
    
    print("\n" + "=" * 70)
    print("📊 BENCHMARK SUMMARY")
    print("=" * 70)
    print(f"\nTotal Tests:     {total}")
    print(f"Passed:          {passed} ✅")
    print(f"Failed:          {failed} ❌")
    print(f"Pass Rate:       {metadata['pass_rate']:.1f}%")
    print(f"\nFracture Count:  {fracture_count}/{total}")
    print(f"PREMIUM Route:   {premium_count}/{total}")
    print(f"Legal Detected:  {legal_count}/{total}")
    print(f"Contra Detected: {contradiction_count}/{total}")
    
    print("\n" + "=" * 70)
    print("✅ BENCHMARK COMPLETE")
    print("=" * 70)
    print(f"\nOutput files saved to: {output_dir}/")
    
    return results, metadata


if __name__ == "__main__":
    results, metadata = main()
