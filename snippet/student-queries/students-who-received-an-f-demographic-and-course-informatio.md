---
id: "1738287868417"
title: "Students who received an F (Demographic and course information)"
category: "student queries"
tags: ["Student", "Course"]
createdAt: "2025-01-31T01:44:28Z"
---

Students who received a D or F - Demographic and course information -- Replace "GRD.M2" with needed Quarter/IPR and change year as needed (use URL for a guide on "GRD" codes and corresponding grading period). Replace year ("20XX-20XX") with current school year 

https://docs.google.com/document/d/124tVpkMDBnGRy5D37NPWkEEpB2I0LIp4EVSUhb41k4w/preview

```text
LIST GRD STU SEC MST CRS FTF STU.ID STU.NM STU.GR STU.RC1? STU.ETH? STU.LF? STU.PED? STU.U13? FTF.STI CRS.CO GRD.M6 BY STU.NM FTF.STI IF GRD.SE = MST.SE AND SSE.PR = 1 AND STU.GR = 9 AND FTF.YR =  "20XX-20XX" AND GRD.M6 # " " AND  ( GRD.M6 = F  OR GRD.M6 : D )   
```
