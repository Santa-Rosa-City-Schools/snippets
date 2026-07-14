---
id: "1738287868346"
title: "Totals for Attendance Codes T and R"
category: "student queries"
tags: ["Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

Totals for Attendance Codes T and R - This query will give you the totals by grade, then period, for those with Attendance Codes T and R. You can adjust the dates as needed.

```text
TOTAL STU CAT SEC MST FTF STU.GR FTF.STI CAT.AC BY STU.GR FTF.STI CAT.AC IF CAT.AC = T OR CAT.AC = R AND CAT.DT > MM/DD/YYYY AND CAT.DT < MM/DD/YYYY
```
