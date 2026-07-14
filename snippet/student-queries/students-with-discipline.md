---
id: "1738287868349"
title: "Students with Discipline"
category: "student queries"
tags: ["Discipline", "Assertive"]
createdAt: "2025-01-31T01:44:28Z"
---

Students with Discipline - Run this query to find students that have had a discipline record for the current school year. Change XX to the school and change the 07/01/2021 to the first day of school

```text
LIST STU DIS DIS.SN STU.LN STU.FN STU.GR DIS.DT DIS.CD DIS.CD? DIS.SCL DIS.SID DIS.UN IF DIS.SCL = XX AND DIS.DT > 07/01/2021
```
