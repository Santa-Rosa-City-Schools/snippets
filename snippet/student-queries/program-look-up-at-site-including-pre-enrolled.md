---
id: "1738287868450"
title: "Program Look-Up at site including Pre-Enrolled "
category: "student queries"
tags: ["Student", "Program", "Special Education", "Education"]
createdAt: "2025-01-31T01:44:28Z"
---

Special Program Look-Up at site including Pre-Enrolled 
Replace STU.SC = XX with desired school
Replace PGM.CD = XXX with desired program
**Common Programs include: 301 - Dual Immersion 
303 - Newcomers     305 - English Learner LIP
190 - Foster   191- Homeless   135- Migrant   127 - GATE

```text
LIST STU PGM STU STU.ID STU.LS? STU.SC? STU.LN STU.FN STU.NG? PGM.CD? PGM.ESD PGM.EED IF ( STU.TG = "*"  AND STU.SC = XX AND PGM.CD = XXX AND PGM.EED = NULL ) OR PGM.CD = XXX AND PGM.EED = NULL 
```
