---
id: "1738287868636"
title: "Change ISP Subject Class MST.ST 2nd Query"
category: "change queries"
tags: ["Scheduling"]
createdAt: "2025-01-31T01:44:28Z"
---

Change ISP Subject Class MST.ST 2nd Query - Will update any master schedule class Exclude with Flex Period of ISP to X (Do not show on grade/progress). Run Change ISP Subject Class MST.ST 1st Query First

```text
CHANGE MST FTF MST.ST TO "Y"  IF MST.RM = "ISP" AND MST.CN ; "KEI%" AND FTF.STI # "ISP"
```
