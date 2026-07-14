---
id: "1738287868584"
title: "List of students w/Teachers missing PFT scores"
category: "aeries-query"
tags: ["Testing", "Pft", "Scheduling", "Teacher"]
createdAt: "2025-01-31T22:28:20Z"
---

Flex Scheduling list of students - Run to identify students that do not have any PFT scores for the administration year

```text
LIST STU SEC MST FTF SSE STF PFT STU.ID STU.LN STU.FN STU.GR STU.SC? STF.FN STF.LN FTF.STI CRS.DC? PFT.TA BY STU.ID IF ( ( SSE.PR = 1 AND CRS.DC = G ) AND ( STU.GR = 7 OR STU.GR = 9 ) AND PFT.TA = NULL ) OR ( STU.GR = 5 AND STU.SC < 90 AND PFT.TA = NULL AND STF.PSC = STU.SC )    
```
