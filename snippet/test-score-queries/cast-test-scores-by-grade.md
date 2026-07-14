---
id: "1738287868520"
title: "CAST Test Scores by Grade"
category: "test score queries"
tags: ["Testing", "Caaspp"]
createdAt: "2025-01-31T01:44:28Z"
---

CAST scores for students by grade level. Science in given in 5th, 8th and 11th grades. Replace the X with the grade level the assessment was given (5th graders tested in 2023-24 are now 6th graders, etc.).

```text
LIST STU TST CTL STU.ID STU.LN STU.FN STU.MN STU.SC? STU.GR TST.ID TST.TA TST.TD CTL.NM TST.SS TST.PL IF TST.TA = SPRGXX AND TST.ID = "CAST" AND STU.GR = X
```
