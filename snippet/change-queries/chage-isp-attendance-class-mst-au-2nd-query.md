---
id: "1738287868625"
title: "Chage ISP Attendance Class MST.AU 2nd Query"
category: "change queries"
tags: ["Scheduling", "Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

Chage ISP Attendance Class MST.AU 2nd Query - Will update any master schedule class Attendance Ruleset with Flex Period of ISP to ISP. Run Chage ISP Attendance Class MST.AU 1st Query first.

```text
CHANGE MST FTF MST.AU TO "ISP" IF FTF.STI = "ISP"
```
