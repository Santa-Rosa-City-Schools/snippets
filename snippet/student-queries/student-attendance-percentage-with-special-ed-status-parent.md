---
id: "1738287868475"
title: "Student Attendance Percentage with Special-Ed Status, Parent Contact Info, and Atttendance Summary data"
category: "student queries"
tags: ["Attendance", "Contact", "Student", "Special Education", "Education"]
createdAt: "2025-01-31T01:44:28Z"
---

Student Attendance Percentage with Special-Ed Status, Parent Contact Info, and Atttendance Summary data

```text
LIST STU AHS STU.ID STU.NM STU.GR STU.PG STU.TL STU.PEM STU.CL? STU.U13? AHS.EN AHS.AB AHS.PR (( 1.0 * AHS.PR/AHS.EN * 100 )) IF AHS.EN # 0 AND AHS.YR = "2023-2024" AND AHS.SCL = STU.SC   
```
