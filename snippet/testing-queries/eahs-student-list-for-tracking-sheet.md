---
id: "1738287868560"
title: "EAHS Student List for Tracking Sheet "
category: "testing queries"
tags: ["Testing", "Caaspp", "Student"]
createdAt: "2025-01-31T01:44:28Z"
---

EAHS Student List for Tracking Sheet  - Run at the site level for a full list of eligible students for CAASPP testing in the specific classes the site is testing 
(Testing in English and History Classes)

```text
LIST STU SEC MST FTF SSE STF STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STF.FN STF.LN FTF.STI CRS.DC? BY STF.LN IF SSE.PR = 1 AND ( ( ( CRS.DC = E ) AND STU.GR = 11) OR ( ( CRS.DC = H ) AND ( STU.GR = 11 OR STU.GR = 12 ) )
```
