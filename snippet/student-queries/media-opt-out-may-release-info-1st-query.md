---
id: "1738287868323"
title: "Media Opt Out - May Release Info - 1st Query"
category: "student queries"
tags: ["Student"]
createdAt: "2025-01-31T01:44:28Z"
---

Media Opt Out - May Release Info - 1st Query - You must run the SKIP query first to eliminate the parents have denied permisson. This will capture all parents who have completed their authorizations as well as those who have not (a blank is also considered permission granted.

```text
SKIP STU AUT IF AUT.CD = MRO AND AUT.ST = 2
```
