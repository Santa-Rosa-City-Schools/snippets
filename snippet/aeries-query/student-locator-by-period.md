---
id: "1738287868462"
title: "Student Locator by Period"
category: "aeries-query"
tags: ["Scheduling", "Student", "Course"]
createdAt: "2025-02-01T02:37:20Z"
---

Lists student id, name, grade, period, room number, course. Replace X in FTF.STI = X with the desired period.

```text
LIST STU GRD MST SSE STF CRS FTF STU.ID STU.NM STU.GR FTF.STI MST.RM CRS.CO STF.LN BY MST.RM IF SSE.PR = 1 AND FTF.STI = X
```
