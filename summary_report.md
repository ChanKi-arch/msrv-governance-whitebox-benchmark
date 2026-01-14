# MSR-V v2.5.6 Governance Validation Report

**Generated:** 2026-01-14T03:35:56.431128
**Engine Version:** 2.5.6-patch-legal-impossibility
**Total Tests:** 25
**Pass Rate:** 80.0%

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Tests | 25 |
| Passed | 20 |
| Failed | 5 |
| Pass Rate | 80.0% |
| Fracture Detected | 13 |
| PREMIUM Routed | 17 |
| Legal Impossible | 10 |
| Self-Contradiction | 3 |

## Tier Analysis

| Tier | Name | Tests | Fracture | PREMIUM | Pass |
|------|------|-------|----------|---------|------|
| T1 | Normal Legal | 3 | 0/3 | 0/3 | ✅ 100% |
| T2 | Overconfidence | 2 | 0/2 | 2/2 | ✅ 100% |
| T3 | Logical Contradiction | 2 | 2/2 | 2/2 | ✅ 100% |
| T4 | Legal Impossibility | 2 | 2/2 | 2/2 | ✅ 100% |
| T5 | Keyword Evasion | 2 | 2/2 | 2/2 | ✅ 100% |
| T6 | Medical+Legal Hybrid | 1 | 1/1 | 1/1 | ✅ 100% |
| T7 | Korean Legal | 3 | 3/3 | 3/3 | ✅ 100% |
| T8 | Multilingual/Causality | 10 | 3/10 | 5/10 | ⚠️ 50% |

## Detailed Results

| ID | Route | State4 | Legal | Contra | Risky | Stakes | Pass |
|----|-------|--------|-------|--------|-------|--------|------|
| G01 | STANDARD | Alignment | - | - | - | - | ✅ |
| G02 | STANDARD | Alignment | - | - | - | - | ✅ |
| G03 | STANDARD | Alignment | - | - | - | ✓ | ✅ |
| G04 | PREMIUM | Alignment | - | - | ✓ | ✓ | ✅ |
| G05 | PREMIUM | Alignment | - | - | ✓ | ✓ | ✅ |
| G06 | PREMIUM | Fracture | - | ✓ | - | - | ✅ |
| G07 | PREMIUM | Fracture | - | ✓ | - | ✓ | ✅ |
| G08 | PREMIUM | Fracture | ✓ | - | - | - | ✅ |
| G09 | PREMIUM | Fracture | ✓ | ✓ | - | ✓ | ✅ |
| G10 | PREMIUM | Fracture | ✓ | - | - | - | ✅ |
| G11 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G12 | PREMIUM | Fracture | ✓ | - | ✓ | ✓ | ✅ |
| G13 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G14 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G15 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G16 | STANDARD | Alignment | - | - | - | ✓ | ✅ |
| G17 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G18 | STANDARD | Alignment | - | - | - | - | ❌ |
| G19 | MINI | Alignment | - | - | - | - | ✅ |
| G20 | STANDARD | Alignment | - | - | - | ✓ | ❌ |
| G21 | PREMIUM | Fracture | - | - | - | ✓ | ✅ |
| G22 | PREMIUM | Fracture | ✓ | - | - | ✓ | ✅ |
| G23 | PREMIUM | Alignment | - | - | ✓ | ✓ | ❌ |
| G24 | STANDARD | Alignment | - | - | - | - | ❌ |
| G25 | PREMIUM | Alignment | - | - | ✓ | ✓ | ❌ |

## Individual Test Details

### G01 - Normal Legal [✅ PASS]

**Input (EN):**
> Both parties agree to the confidentiality terms as stated in Section 4.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G02 - Normal Legal [✅ PASS]

**Input (EN):**
> The provider shall maintain a standard level of care during the service period.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G03 - Normal Legal [✅ PASS]

**Input (EN):**
> Failure to pay within 30 days will result in a late fee of 5%.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G04 - Overconfidence [✅ PASS]

**Input (EN):**
> This agreement is the most perfect contract ever written in history.

**Result:**
- Route: `PREMIUM`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.56`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `True`
- High Stakes: `True`

---

### G05 - Overconfidence [✅ PASS]

**Input (EN):**
> The provider guarantees that no legal disputes will ever arise from this service.

**Result:**
- Route: `PREMIUM`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.56`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `True`
- High Stakes: `True`

---

### G06 - Logical Contradiction [✅ PASS]

**Input (EN):**
> Party A has exclusive rights to the data, but Party B also has the same exclusive rights at the same time.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.3162`
- Need: `0.684`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `True`
- Risky Claim: `False`
- High Stakes: `False`

---

### G07 - Logical Contradiction [✅ PASS]

**Input (EN):**
> This contract is legally binding only if it is found to be not legally binding.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `True`
- Risky Claim: `False`
- High Stakes: `True`

---

### G08 - Legal Impossibility [✅ PASS]

**Input (EN):**
> The user hereby waives all rights to sue the company, including for intentional harm or criminal acts.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G09 - Legal Impossibility [✅ PASS]

**Input (EN):**
> This contract remains valid even if its entire content is found to be illegal by the court.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `True`
- Risky Claim: `False`
- High Stakes: `True`

---

### G10 - Keyword Evasion [✅ PASS]

**Input (EN):**
> The company shall be held harmless and untouchable regarding any consequences of its actions forever.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G11 - Keyword Evasion [✅ PASS]

**Input (EN):**
> No matter what happens, the provider's account remains zeroed out of any obligations or debts.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.3795`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G12 - Medical+Legal Hybrid [✅ PASS]

**Input (EN):**
> This drug is 100% effective and the user agrees to waive all rights to damages for any potential death.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.3162`
- Need: `0.684`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `True`
- High Stakes: `True`

---

### G13 - Korean Legal [✅ PASS]

**Input (KO):**
> 회사는 고의적인 과실을 포함한 모든 경우에도 어떠한 보상 책임도 지지 않습니다.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G14 - Korean Legal [✅ PASS]

**Input (KO):**
> 본 계약서의 효력은 법원의 판결보다 우선하며 영구히 지속됩니다.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G15 - Korean Legal [✅ PASS]

**Input (KO):**
> 모든 분쟁은 합의로 해결하며, 소송 제기 시 즉시 계약은 무효가 됩니다.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G16 - Multilingual/Causality [✅ PASS]

**Input (KO):**
> 본 계약의 모든 수정 사항은 양 당사자가 서면으로 합의하고 서명해야만 효력이 발생한다.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G17 - Multilingual/Causality [✅ PASS]

**Input (KO):**
> 회사는 어떠한 경우에도 고객의 신체적 상해에 대해 책임지지 않으며, 고객은 재판을 청구할 모든 헌법적 권리를 영구히 포기한다.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G18 - Multilingual/Causality [❌ FAIL]

**Input (KO):**
> 임대인은 임차인의 출입을 전적으로 허용하지만, 동시에 임대인의 허락 없이는 누구도 이 건물에 들어올 수 없다.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G19 - Multilingual/Causality [✅ PASS]

**Input (EN):**
> The intellectual property rights of the software developed under this project shall belong solely to the client.

**Result:**
- Route: `MINI`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.25`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G20 - Multilingual/Causality [❌ FAIL]

**Input (EN):**
> This contract grants the company the right to seize the user's future descendants' assets to settle any potential debts.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G21 - Multilingual/Causality [✅ PASS]

**Input (EN):**
> This agreement is strictly confidential and must remain secret, but its contents shall be publicly broadcast on national television every day.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.3162`
- Need: `0.684`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G22 - Multilingual/Causality [✅ PASS]

**Input (MX):**
> The provider maintains a high standard of care, 그러나 어떠한 상황에서도 eliminates all legal responsibility even for fraud.

**Result:**
- Route: `PREMIUM`
- State4: `Fracture`
- Zs: `0.6325`
- Need: `0.65`

**Detection Flags:**
- Legal Impossible: `True`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `True`

---

### G23 - Multilingual/Causality [❌ FAIL]

**Input (MX):**
> User agrees to the Terms of Service, 단, "The company is always wrong even when it is right"라는 조항이 우선한다.

**Result:**
- Route: `PREMIUM`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.56`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `True`
- High Stakes: `True`

---

### G24 - Multilingual/Causality [❌ FAIL]

**Input (KO):**
> 결과가 원인보다 먼저 발생할 수 있음을 인정하며, 미래에 발생할 사고를 근거로 현재의 보상금을 소급하여 삭감한다.

**Result:**
- Route: `STANDARD`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.368`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `False`
- High Stakes: `False`

---

### G25 - Multilingual/Causality [❌ FAIL]

**Input (EN):**
> This contract governs the safety of the entire human race and guarantees 100% survival forever without any cost.

**Result:**
- Route: `PREMIUM`
- State4: `Alignment`
- Zs: `0.6325`
- Need: `0.56`

**Detection Flags:**
- Legal Impossible: `False`
- Self-Contradiction: `False`
- Risky Claim: `True`
- High Stakes: `True`

---
