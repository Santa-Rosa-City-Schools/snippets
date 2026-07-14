---
id: "1738287868644"
title: "Update STU.LF to EL 2nd Query"
category: "change queries"
tags: ["Testing", "Elpac", "Initial", "Import", "Export", "Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Update STU.LF to EL 2nd Query - This will update the STU.LF to EL based on the Initial ELPAC test results once those are imported. Run Update STU.LF to EL 1st Query first.

```text
CHANGE STU LAC STU.LF TO "L"  IF STU.LF = "T" AND LAC.ITF = "EL"
```
