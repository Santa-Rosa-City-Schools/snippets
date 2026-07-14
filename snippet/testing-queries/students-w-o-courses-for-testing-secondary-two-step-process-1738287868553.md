---
id: "1738287868553"
title: "Students w/o Courses for Testing - Secondary (Two Step Process) 1st Query"
category: "testing queries"
tags: ["Testing", "Caaspp", "Course"]
createdAt: "2025-01-31T01:44:28Z"
---

Students w/o Courses for Testing - Secondary (Two Step Process) 1st Query - 1st Query: Run a SKIP Statement for students in the specific CAASPP subjects:
Replace "X" with initial for department, E = English; M = Math; B = Bio Science or P = Phy Science. 

For science will need to be in parentheses ( CRS.DC = B or CRS.DC = P )

```text
SKIP STU SEC CRS IF CRS.DC =X
```
