---
id: "1738287868435"
title: "Feeder Schools from outside "
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Feeder Schools from outside [Replace STU.SC (current site) and STU.GR (current grade) as needed]

```text
LIST STU ODE STU.ID STU.LN STU FN ODE.SNM BY ODE.SNM IF STU.SC = 31 AND STU.GR = 7 AND ODE.SNM # NULL AND ODE.SQ = 1    
```
