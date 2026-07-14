---
id: "1738287868654"
title: "Update ISP AB130 from Not Applicable to Eligible/Participating 1st Query"
category: "change queries"
tags: ["Student", "Program"]
createdAt: "2025-01-31T01:44:28Z"
---

Update ISP AB130 from Not Applicable to Eligible/Participating 1st Query - Will change PGM.ST for students who are not listed correctly. Run Update ISP AB130 from Not Applicable to Eligible/Participating 1st Query first.

```text
CHANGE PGM PGM.ST TO "2" IF PGM.CD = ISP AND PGM.ST = ""
```
