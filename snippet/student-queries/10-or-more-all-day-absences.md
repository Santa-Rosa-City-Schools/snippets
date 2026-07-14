---
id: "1738287868353"
title: "10 or more All Day absences"
category: "student queries"
tags: ["Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

10 or more All Day absences - Gives all students with 10 or more All Day absences of any sort.

```text
LIST STU CSE AHS STU.ID STU.LN STU.FN STU.SC? STU.GR 504_PLAN  SPECIALED AHS.AB IF ( 504_PLAN = YES OR SPECIALED = YES ) AND AHS.AB >= 10
```
