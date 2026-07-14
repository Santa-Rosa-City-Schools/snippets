---
id: "1738287868587"
title: "PFT: No entries "
category: "testing queries"
tags: ["Testing", "Pft"]
createdAt: "2025-01-31T01:44:28Z"
---

PFT: No entries  - Run to identify students without an entry for the current test administration window

```text
LIST STU PFT STU.CID STU.ID STU.LN STU.FN STU.SC? STU.GR PFT.TA IF PFT.TA = NULL AND ( STU.GR = 5 OR STU.GR = 7 OR STU.GR = 9 )
```
