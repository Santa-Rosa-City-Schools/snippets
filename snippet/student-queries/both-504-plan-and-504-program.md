---
id: "1738287868392"
title: "Both 504 Plan and 504 Program"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Both 504 Plan and 504 Program - This query will give you all the students who have an entry for a 504 Plan and a 504 Program. Verify they actually have a plan. Some may not. After the Plan is created, the Program needs to be removed.

```text
LIST STU SC? ID LN FN 504_PLAN 504_PRG BY STU.SC IF 504_PLAN = YES AND 504_PRG = YES
```
