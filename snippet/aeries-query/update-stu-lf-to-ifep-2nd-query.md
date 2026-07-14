---
id: "1738287868640"
title: "Update STU.LF to IFEP 2nd Query"
category: "aeries-query"
tags: ["Testing", "Elpac", "Initial", "Import", "Export", "Student"]
createdAt: "2025-01-31T22:56:48Z"
---

Update STU.LF to IFEP 2nd Query - This will update the STU.LF to IFEP based on the Initial ELPAC test results once those are imported. Run Update STU.LF to IFEP 1st Query first.

```text
CHANGE STU LAC STU.LF TO "I"   IF STU.LF = "T" AND LAC.ITF = "IFEP"
```
