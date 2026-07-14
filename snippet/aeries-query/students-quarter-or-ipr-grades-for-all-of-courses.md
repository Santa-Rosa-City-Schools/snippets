---
id: "1738287868415"
title: "Students Quarter or IPR Grades for all of courses"
category: "aeries-query"
tags: ["Student", "Grades", "Course"]
createdAt: "2025-02-01T02:39:11Z"
---

Student's Quarter / IPR Grades for all of their courses -- Replace "GRD.M2" with needed Quarter/IPR and change year as needed (use URL for a guide on "GRD" codes and corresponding grading period). Replace year ("20XX-20XX") with current school year 

https://docs.google.com/document/d/124tVpkMDBnGRy5D37NPWkEEpB2I0LIp4EVSUhb41k4w/preview

```text
LIST GRD STU SEC MST CRS FTF STU.ID STU.NM STU.GR FTF.STI CRS.CO GRD.M2 BY STU.NM FTF.STI IF GRD.SE = MST.SE AND SSE.PR = 1 AND FTF.YR =  "20XX-20XX" AND GRD.M2 # " "  
```
