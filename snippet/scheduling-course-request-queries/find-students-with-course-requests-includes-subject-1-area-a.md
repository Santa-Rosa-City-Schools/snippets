---
id: "1738287868248"
title: "Find students with course requests includes subject 1 area and department"
category: "scheduling - course request queries"
tags: ["Scheduling", "Course"]
createdAt: "2025-01-31T01:44:28Z"
---

Find students with course requests includes subject 1 area and department - Run at your school. Will show all students who have 1 or more requests, one line per request, course number, and course name. Additionally, this will show subject area 1 and deparment

```text
LIST STU SSS CRS STU.ID STU.LN STU.FN STU.NG STU.SC STU.NS SSS.CN CRS.CO CRS.S1? CRS.DC? IF ( STU.TG = "*" OR STU.TG = "" )
```
