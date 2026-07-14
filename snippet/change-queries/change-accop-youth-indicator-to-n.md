---
id: "1738287868681"
title: "Change Accop Youth indicator to N "
category: "change queries"
tags: ["Student", "Program"]
createdAt: "2025-01-31T01:44:28Z"
---

Change Accop Youth indicator to N for all homeless students missing this indicator

```text
CHANGE STU PGM PGM.UY TO "N" IF PGM.CD = 191 AND PGM.UY = " "
```
