---
id: "1738287868573"
title: "SRHS Student List for Tracking Sheet"
category: "testing queries"
tags: ["Testing", "Caaspp", "Student"]
createdAt: "2025-01-31T01:44:28Z"
---

SRHS Student List for Tracking Sheet - Run at the site level for a full list of eligible students for CAASPP testing in each subject area
 (Testing in English, Math and Science Classes)

```text
LIST STU SEC MST FTF SSE STF STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STF.FN STF.LN FTF.STI CRS.DC? BY STF.LN IF SSE.PR = 1 AND  ( ( ( CRS.DC = E OR CRS.DC = M )  OR  ( ( CRS.DC = P OR CRS.DC = B ) AND ( STU.GR = 8 ) )
```
