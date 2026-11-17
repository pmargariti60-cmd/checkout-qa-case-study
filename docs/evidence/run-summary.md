# Local QA run evidence

**Executed:** 17 November 2026  
**Environment:** macOS arm64, Python 3.9.6, pytest 8.4.2, Playwright 1.60.0, headless Chromium 148.0.7778.96  
**Inputs:** Fresh browser context per case and the same fixture data on both builds.

| Build | Passed | Failed | Exit code |
| --- | ---: | ---: | ---: |
| Reference | 8 | 0 | 0 |
| Candidate | 5 | 3 | 1 |

Candidate passes were CK01, CK04, CK05, CK06, and CK08. The three failures were requirement assertions.

| Candidate case | Expected | Observed | Defect |
| --- | --- | --- | --- |
| CK02 | `$50.00` displayed total | `$55.00` displayed total | [QA-01](../defects.md#qa-01--total-stays-at-5500-after-applying-save10) |
| CK03 | `SAVE10 applied.` | `Code not recognized.` | [QA-03](../defects.md#qa-03--lowercase-promo-code-is-rejected) |
| CK07 | Order button disabled | Order button enabled | [QA-02](../defects.md#qa-02--shopper-can-submit-again-after-confirmation) |

The screenshots were captured in a targeted replay against the same candidate fixture. See the [exploratory notes](../exploratory-notes.md) for the extra actions and observations, and the [README](../../README.md#run-the-case-study-locally) for commands to regenerate traces, screenshots, and JUnit results.
