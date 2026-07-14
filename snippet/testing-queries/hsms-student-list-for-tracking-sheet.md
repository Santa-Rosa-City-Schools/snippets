---
id: "1738287868577"
title: "HSMS Student List for Tracking Sheet "
category: "testing queries"
tags: ["Testing", "Caaspp", "Student"]
createdAt: "2025-01-31T01:44:28Z"
---

HSMS Student List for Tracking Sheet  - Run at the site level for a full list of eligible students for CAASPP testing in the specific period and classes the site is testing
(Testing in 5 Period and Science Classes)

```text
LIST STU SEC MST FTF SSE STF STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STF.FN STF.LN FTF.STI CRS.DC? BY STF.LN IF STU.GR = 8 AND SSE.PR = 1 AND ( FTF.STI = 5  OR CRS.DC = P OR CRS.DC = B )  
```
