---
id: "1738287868195"
title: "Enrollment Numbers"
category: "calpas queries"
tags: ["Enrollment"]
createdAt: "2025-01-31T01:44:28Z"
---

Enrollment Numbers - Total number of students enrolled for each grade on a specific day

```text
TOTAL STU ENR STU.GR BY STU.GR IF ( STU.TG = "" OR STU.TG = "I" ) AND ENR.YR = 2020 AND ENR.ED <= 9/30/2020 AND ( ENR.LD >= 9/30/2020 OR ENR.LD = NULL )
```
