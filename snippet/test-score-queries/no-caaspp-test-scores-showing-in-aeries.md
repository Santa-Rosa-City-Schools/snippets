---
id: "1738287868530"
title: "No CAASPP Test Scores Showing in Aeries"
category: "test score queries"
tags: ["Testing", "Caaspp", "Import", "Export", "Student", "AERIES"]
createdAt: "2025-01-31T01:44:28Z"
---

To verify why a student's test scores are not showing in Aeries Test Scores page after import. To see why a students test scores were excluded from import in the Testing Exclusions (TEX) table.

Enter specific testing window

```text
LIST STU TEX STU.ID STU.NM TEX.ID TEX.TD TEX.PT TEX.SPC TEX.TA IF TEX.ID = "SBAC" AND TEX.TA = "SPRGXX"
```
