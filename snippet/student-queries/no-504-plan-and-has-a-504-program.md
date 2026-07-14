---
id: "1738287868393"
title: "No 504 Plan and has a 504 Program"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

No 504 Plan and has a 504 Program - This query will give you all the students who do NOT have a 504 Plan but do HAVE a 504 Program. They need a Plan and then remove the Program.

```text
LIST STU SC? ID LN FN 504_PLAN 504_PRG BY STU.SC IF 504_PLAN = NO AND 504_PRG = YES
```
