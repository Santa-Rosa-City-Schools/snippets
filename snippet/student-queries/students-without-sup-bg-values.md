---
id: "1738287868383"
title: "Students without SUP.BG values"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Students without SUP.BG values - Find Students without SUP.BG values. WORKING QUERY. STILL NEEDS REFINING.This will find students who do not have a value in the Birth Gender supplemental field.

```text
LIST STU SUP STU.SC? STU.ID STU.LN STU.FN STU.GR? STU.SX SUP.BG BY STU.SC STU.GR IF SUP.BG = ""
```
