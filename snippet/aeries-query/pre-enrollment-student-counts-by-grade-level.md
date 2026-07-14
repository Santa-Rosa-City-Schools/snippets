---
id: "1742870719931"
title: "Pre-Enrollment Student Counts by Grade Level"
category: "aeries-query"
tags: ["Enrollment", "Student"]
createdAt: "2025-03-25T02:45:19Z"
---

Reports the total number of students pre-enrolled at a site for next school year. This combines current students promoted to a new grade and pre-enrolled students.

```text
TOTAL STU STU.NG BY NG IF ( STU.TG = ' ' OR STU.TG = * ) AND STU.NG < 13
```
