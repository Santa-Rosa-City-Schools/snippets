---
id: "1747154273243"
title: "Students with Ds or Fs on Report Card"
category: "aeries-query"
tags: ["Grades", "Student"]
createdAt: "2025-05-13T16:37:53Z"
---

List of student with D or F on the latest grade report period.

Update M9 to match the latest grade report period.

```text
LIST STU GRD STF CRS STU.ID STU.LN STU.FN STU.GR STF.LN GRD.CN CRS.DE GRD.M8 GRD.M9 WHERE GRD.M9 = 'D' OR GRD.M9 = 'D-' OR GRD.M9 = 'D+' OR GRD.M9 = 'F'
```
