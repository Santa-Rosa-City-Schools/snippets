---
id: "1738287868343"
title: "Tracking 504 student under the FOF"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Tracking 504 student under the FOF - Gives a list of students with a 504 plan and includes counseor last name.

```text
LIST STU FOF TCH STU.ID STU.LN STU.FN STU.GR TCH.TE FOF.SD FOF.RD BY TCH.TE IF ( 504_PLAN = YES OR 504_PRG = YES ) AND STU.TG = " "
```
