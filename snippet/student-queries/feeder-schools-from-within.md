---
id: "1738287868434"
title: "Feeder Schools from within "
category: "student queries"
tags: ["Student", "Enrollment"]
createdAt: "2025-01-31T01:44:28Z"
---

Feeder Schools from within [Replace ENR.YR (enrollment year), STU.SC(current site), and STU.GR(current grade) as needed]

```text
LIST STU ENR STU.ID STU.LN STU.FN STU.GR ENR.SC ENR.YR IF ENR.YR = 2021 AND STU.SC = 31  AND STU.GR = 7 AND ENR.SC < 100  
```
