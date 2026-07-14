---
id: "1738287868438"
title: "Semester GPA for students in a Program limited by GPA"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Semester GPA for students in a Program limited by GPA (Replace XXX with program code and STU.GT (<, >, = ) desired GPA

```text
LIST STU PGM STU.ID STU.LN STU.FN STU.GT IF PGM.CD = XXX AND PGM.EED = NULL AND STU.GT < 2.5
```
