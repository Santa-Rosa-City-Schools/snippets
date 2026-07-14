---
id: "1738287868231"
title: "Grades in the GRD table without credits"
category: "course queries"
tags: ["Course", "Variable", "Credits"]
createdAt: "2025-01-31T01:44:28Z"
---

This query will show you which grades in your GRD table are also missing credits

```text
LIST STU GRD CRS STU.ID STU.NM STU.GR? GRD.PD GRD.CN CRS.CO GRD.TN GRD.MK GRD.M1 GRD.M2 GRD.M3 GRD.CR GRD.TM GRD.SE IF GRD.CR = 0 
```
