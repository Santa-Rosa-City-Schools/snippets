---
id: "1738287868251"
title: "Student Requests - SPED and Language included"
category: "scheduling - course request queries"
tags: ["Scheduling", "Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Student Requests - SPED and Language included - Run at the district level. Will give you all students for next year with their requests. You must replace XX with your school number

```text
LIST STU CSE SSS CRS STU.ID STU.LN STU.FN STU.NG STU.SC STU.NS SSS.CN CRS.CO CSE.PL STU.LF? IF STU.NG # "13" AND ( STU.NS = XX OR ( STU.TG = "*" AND STU.NS = XX )  )
```
