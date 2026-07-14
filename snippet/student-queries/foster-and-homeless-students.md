---
id: "1738287868373"
title: "Foster and Homeless Students"
category: "student queries"
tags: ["Student", "Program"]
createdAt: "2025-01-31T01:44:28Z"
---

Updated version of the query above using Eligibility dates and not  participation dates.

```text
LIST STU PGM STU.ID STU.LN STU.FN STU.RAD STU.RCY STU.RST STU.RZC PGM.CD? PGM.ESD PGM.EED IF PGM.EED = NULL AND ( PGM.CD = 190 OR PGM.CD = 191 )
```
