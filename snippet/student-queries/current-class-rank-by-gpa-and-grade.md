---
id: "1738287868401"
title: "Current Class Rank - By GPA and Grade"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

This report will provide the class rank sorted roughly by rank. Be sure and change the grade level at the end of the query to match the grade you are looking for.

```text
LIST STU SUP ENR STU.ID STU.LN STU.FN SUP.RNK BY STU.TP ^ IF STU.GR = 12 AND ENR.YR = 2023 AND ENR.PR # C 
```
