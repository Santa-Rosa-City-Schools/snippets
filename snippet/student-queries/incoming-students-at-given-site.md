---
id: "1738287868370"
title: "Incoming Students at Given Site"
category: "student queries"
tags: ["Enrollment"]
createdAt: "2025-01-31T01:44:28Z"
---

Incoming Students at Given Site - Gives a list of students enrolled at a given site. You must replace XX with your site number.

```text
LIST STU STU.ID STU.LN STU.FN STU.NG? STU.SC? STU.NS? IF STU.NS = XX AND STU.NS # '' AND STU.NG # "13"  OR  STU.TG = "*"
```
