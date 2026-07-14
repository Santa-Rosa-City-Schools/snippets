---
id: "1738287868563"
title: "Secondary Summative ELPAC: EL Students"
category: "testing queries"
tags: ["Testing", "Elpac", "Summative", "Teacher"]
createdAt: "2025-01-31T01:44:28Z"
---

Summative ELPAC: EL Students - Run for a list of Secondary students who have been classified as an English Learner through their Initial assessment w/ALD or Newcomer Teacher

=IFERROR(query('Raw Data Secondary'!$A$5:$L, "Select K,L where """&A5&""" matches A and L contains 'Ac Lang' "), )

```text
LIST STU SEC MST CRS SSE STF FTF LAC STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STU.LF? STF.LN CRS.CO IF LAC.EAC = "EL" AND ( FTF.STI # "1-6" AND FTF.STI # "1-5" AND FTF.STI # "TK-K" ) AND SSE.PR = 1 AND CRS.CO : "LANG"
```
