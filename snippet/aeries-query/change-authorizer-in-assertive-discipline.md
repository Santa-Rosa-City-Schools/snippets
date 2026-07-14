---
id: "1738287868679"
title: "Change Authorizer in Assertive Discipline"
category: "aeries-query"
tags: ["Assertive", "Discipline", "Change", "Student"]
createdAt: "2025-01-31T22:34:12Z"
---

Change assertive discipline authorizer from 10 to 0 if a student wasn't suspended

```text
CHANGE STU ADS DSP DSP.AA TO "10" IF DSP.AA = "" AND DSP.DS : SUS
```
