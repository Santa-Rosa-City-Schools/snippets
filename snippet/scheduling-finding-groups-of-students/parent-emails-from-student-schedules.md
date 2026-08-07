---
id: "1786058342317"
title: "Parent Emails from Student Schedules"
category: "scheduling - finding groups of students"
tags: ["Contact"]
createdAt: "2026-08-06T23:19:02Z"
---

Exports a list of all education rights holders emails from scheduling master schedule section(s). Add additional `OR SSS.SE = ##` if you want to include additional sections.

Replace ## with the section number.

```text
LIST STU CON SSS STU.ID STU.LN STU.FN CON.EM IF ( SSS.SE = ## OR SSS.SE = ## ) AND CON.ERH = Y
```
