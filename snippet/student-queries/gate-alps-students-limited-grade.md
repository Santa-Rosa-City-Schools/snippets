---
id: "1738287868356"
title: "GATE/ALPS Students Limited Grade"
category: "student queries"
tags: ["Student", "Program", "Special Education", "Education"]
createdAt: "2025-01-31T01:44:28Z"
---

GATE/ALPS Students Limited Grade - Will return students with a GATE/ALPS program limited by grade level. GATE/ALPS is not in Student Special Programs.

```text
LIST STU GTE STU.ID STU.LN STU.FN STU.GR? STU.SC? GTE.ESD GTE.PSD IF GTE.ESD # NULL AND ( STU.GR = 3 OR STU.GR = 4 OR STU.GR = 5 OR STU.GR = 6 )
```
