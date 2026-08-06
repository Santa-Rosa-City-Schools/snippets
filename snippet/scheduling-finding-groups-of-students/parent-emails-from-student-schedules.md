---
id: "1786058918614"
title: "Parent Emails from Student Schedules"
category: "scheduling - finding groups of students"
tags: ["Contact"]
createdAt: "2026-08-06T23:28:38Z"
---

Exports a list of parent emails from scheduling master schedule section(s). Add additional `OR SSS.SE = ##` if you want to include additional sections. 

Replace ## with the section number.

```text
LIST STU SSS STU.ID STU.LN STU.FN STU.PEM IF SSS.SE = ## OR SSS.SE = ##
```
