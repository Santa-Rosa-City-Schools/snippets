---
id: "1738287868338"
title: "Students with specific teacher name, period, and room number."
category: "student queries"
tags: ["Scheduling", "Teacher"]
createdAt: "2025-01-31T01:44:28Z"
---

Students with specific teacher name, period, and room number. -

```text
LIST STU SEC MST FTF SSE STF LOC STU.ID STU.LN STU.FN STF.LN STF.FN MST.RM FTF.STI LOC.SNM IF SSE.PR = 1 AND ( SSE.ED > 1/19/2023 OR SSE.ED = NULL ) AND ( ( MST.SC = 21 AND FTF.STI = WIN ) OR ( MST.SC = 23 AND FTF.STI = Advis ) OR ( MST.SC = 34 AND FTF.STI = 2 ) OR ( MST.SC = 31 AND FTF.STI = 2 ) OR ( MST.SC = 32 AND FTF.STI = 3 ) OR ( MST.SC = 33 AND FTF.STI = 7 OR FTF.STI = 8 ) OR ( MST.SC = 53 AND FTF.STI = 4 ) OR ( MST.SC = 54 AND FTF.STI = ADV ) OR ( MST.SC = 50 AND FTF.STI = 4 ) OR ( MST.SC = 51 AND FTF.STI = 3 ) OR ( MST.SC = 52 AND FTF.STI = 3 ) OR ( MST.SC = 60 AND FTF.STI = Advo ) )
```
