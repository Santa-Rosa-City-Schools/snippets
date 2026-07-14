---
id: "1738287868334"
title: "Students with 14 or more Absences"
category: "student queries"
tags: ["Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

Students with 14 or more Absences - Gives you absences greater than 14 and also give you the attendance percentage. Change year ( AHS.YR = "202X-202X" ) as needed

```text
LIST STU TCH AHS STU.ID STU.SC STU.NM STU.GR TCH.TE AHS.SP AHS.EN AHS.AB AHS.PR (( 1.0 * AHS.PR/AHS.EN * 100 )) BY AHS.SCL IF AHS.EN # 0 AND AHS.YR = "202X-202X" AND AHS.SCL = STU.SC AND LOC.U = 0 AND AHS.AB > 14
```
