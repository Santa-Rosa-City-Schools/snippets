---
id: "1738287868430"
title: "Free or Reduced programs with Parent Confirmation and Direct Cert"
category: "student queries"
tags: ["Student", "Program"]
createdAt: "2025-01-31T01:44:28Z"
---

Free or Reduced programs with Parent Confirmation and Direct Cert

```text
LIST STU FRE STU.ID STU.LN STU.FN FRE.CD FRE.ESD FRE.EED FRE.SRC IF FRE.CD # N AND ( FRE.SRC = PDC AND FRE.EED = NULL ) OR ( ( FRE.SRC = T OR FRE.SRC = M OR FRE.SRC = S ) AND FRE.EED > 7/1/2023 )     
```
