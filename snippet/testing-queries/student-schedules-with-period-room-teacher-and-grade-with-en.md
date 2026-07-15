---
id: "1784133208337"
title: "Student Schedules with Period, Room, Teacher and Grade (with Enrollment Date Filter)"
category: "testing queries"
tags: ["Schedules"]
createdAt: "2026-07-15T16:33:28Z"
---

Looks up students in a specific class and period by grade level and filtered by enrollment date

```text
LIST STU SEC MST FTF SSE STF LOC STU.ID STU.LN STU.FN STF.LN STF.FN STU.U13 MST.RM FTF.STI LOC.SNM IF SSE.PR = 1 AND ( SSE.ED > 1/19/2026 OR SSE.ED = NULL ) AND ( ( MST.SC = 51 AND FTF.STI = 1 ) AND STU.GR = 11
```
