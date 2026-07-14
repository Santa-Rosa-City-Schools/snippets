---
id: "1738287868522"
title: "Test Score Import Confirmation"
category: "test score queries"
tags: ["Testing", "Elpac", "Summative", "Import", "Export"]
createdAt: "2025-01-31T01:44:28Z"
---

Test Score Import Confirmation - If confirmation email is not received from Aeries, run to verify test score imports were successful. Change the name in the quotes to the scores that were uploaded. This does not generate in "real-time".

```text
LIST EML BY DTS ^ IF SUB : "ELPAC Test Results"
```
