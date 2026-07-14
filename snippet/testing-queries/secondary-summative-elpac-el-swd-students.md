---
id: "1738287868547"
title: "Secondary Summative ELPAC: EL SWD Students"
category: "testing queries"
tags: ["Testing", "Elpac", "Summative", "Course"]
createdAt: "2025-01-31T01:44:28Z"
---

SWD Students with ALD courses with IEP or 504 or both.

```text
LIST STU SEC MST CRS SSE STF FTF LAC STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STU.LF? STF.LN STU.U13? CRS.CO IF LAC.EAC = "EL" AND ( FTF.STI # "1-6" AND FTF.STI # "1-5" AND FTF.STI # "TK-K" ) AND SSE.PR = 1 AND ( CRS.CN = NH031 OR CRS.CN = NH032 OR CRS.CN = NHALD OR CRS.CN = NHR30 OR CRS.CN = NM101 OR CRS.CN = NM107 OR CRS.CN = NM108 ) AND ( STU.U13 = 5 OR STU.U13 = I OR STU.U13 = B )
```
