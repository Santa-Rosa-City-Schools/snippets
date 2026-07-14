---
id: "1738287868219"
title: "Finding Newcomers by Course"
category: "course queries"
tags: ["Student", "Newcomers", "Course"]
createdAt: "2025-01-31T01:44:28Z"
---

This query will list all students enrolled in a Newcomers course. Update the code after the IF command to alter focus.

```text
LIST STU SEC MST FTF SSE STF STU.ID STU.LN STU.FN SEC.SC CRS  CRS.CO CRS.CN IF CRS.CO ; "Kitchen NC" AND ( CRS.CO : "NC " OR CRS.CO : " NC" )
```
