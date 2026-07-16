---
id: "1784231994784"
title: "List of NPS students by grade and school"
category: "student queries"
tags: ["Special Education"]
createdAt: "2026-07-16T19:59:54Z"
author: "PContreras"
---

Used to pull all NPS students, with their current NPS school and next School. (Used to update the next school if necessary).

```text
LIST STU CID ID NM SC GR NS NG IF ( SC = 81 OR SC = 80 ) AND GR = 6
```
