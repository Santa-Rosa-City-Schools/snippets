---
id: "1787259946972"
title: "Student has D or F on Transcript by Term"
category: "student queries"
tags: []
createdAt: "2026-08-20T21:05:46Z"
---

Search for all students that have D or F on transcript by grade, term, year

```text
LIST STU HIS CRS STU.ID STU.LN STU.FN STU.GR? HIS.YR HIS.TE HIS.MK CRS.CO BY HIS.GR IF HIS.YR = "25" AND HIS.GR = 8 AND ( HIS.TE = "3" OR HIS.TE = "4" ) AND ( HIS.MK = "F" OR HIS.MK : "D" )
```
