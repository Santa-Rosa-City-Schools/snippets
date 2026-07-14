---
id: "1743106706544"
title: "List Specific Truancy Letters"
category: "aeries-query"
tags: ["Truancy", "Attendance"]
createdAt: "2025-03-27T20:25:11Z"
---

This query lists the letters your students have received alongside the date they were issued.

Use one of the following options instead of `Truancy` to filter for a specific letter:
- Truancy 1
- Truancy 2
- Truancy 3
- Truancy SART
- Truancy 3
- Truancy SARB
- Meeting SART
- Meeting SARB

```text
LIST STU LTL STU.ID STU.LN STU.FN STU.GR LTL.ID LTL.DT WHERE LTL.DT > '2024-07-01' AND LTL.ID : 'Truancy'
```
