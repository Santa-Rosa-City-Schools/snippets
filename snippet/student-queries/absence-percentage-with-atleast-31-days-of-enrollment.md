---
id: "1738287868469"
title: "Absence Percentage with atleast 31 days of Enrollment "
category: "student queries"
tags: ["Attendance", "Enrollment"]
createdAt: "2025-01-31T01:44:28Z"
---

Absence Percentage with atleast 31 days of Enrollment (Days enrolled, present, days absent)

```text
LIST STU AHS STU.ID STU.SC? STU.GR STU.NM AHS.SP AHS.EN AHS.AB AHS.PR (( 1.0 * AHS.AB/AHS.EN * 100 )) BY AHS.SCL STU.GR IF AHS.EN >= 31 AND AHS.YR = "2023-2024" AND AHS.SCL = STU.SC AND LOC.U = 0
```
