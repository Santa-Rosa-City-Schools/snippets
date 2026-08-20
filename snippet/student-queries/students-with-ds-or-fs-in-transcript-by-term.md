---
id: "1787259944313"
title: "Students with Ds or Fs in Transcript by Term"
category: "student queries"
tags: ["Grades"]
createdAt: "2026-08-20T21:05:44Z"
author: "Aleta"
---

Query for Student's with D's or F's on their transcript (Adjust grade, year and term as needed)

```text
LIST STU HIS CRS STU.ID STU.LN STU.FN STU.GR? HIS.YR HIS.TE HIS.MK CRS.CO BY HIS.GR IF HIS.YR = "25" AND HIS.GR = 8 AND ( HIS.TE = "3" OR HIS.TE = "4" ) AND ( HIS.MK = "F" OR HIS.MK : "D" )
```
