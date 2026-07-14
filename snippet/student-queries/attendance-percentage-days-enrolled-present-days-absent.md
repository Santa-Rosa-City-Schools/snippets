---
id: "1738287868446"
title: "Attendance Percentage (Days enrolled, present, days absent)"
category: "student queries"
tags: ["Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

Attendance Percentage (Days enrolled, present, days absent)

```text
LIST STU NM GR SC? DE DA DP (( LEFT (1.0 * DP / DE * 100 , 5 ) + "%" )) BY (( DP / DE )) REV IF DE # 0
```
