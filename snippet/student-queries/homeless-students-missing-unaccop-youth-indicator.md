---
id: "1738287868398"
title: "Homeless Students missing Unaccop Youth indicator"
category: "student queries"
tags: ["Student", "Program", "Import", "Export"]
createdAt: "2025-01-31T01:44:28Z"
---

This query will provide a list of current & past homeless students who are missing the Unaccop Youth indicator. This is a required field by CALPADS. Without htis field the student's program will not import to CALPADS

```text
LIST STU PGM STU.CID STU.ID STU.NM STU.GR STU.SC? PGM.CD PGM.ESD PGM.EED PGM.UY IF PGM.CD = 191 AND PGM.UY = " "
```
