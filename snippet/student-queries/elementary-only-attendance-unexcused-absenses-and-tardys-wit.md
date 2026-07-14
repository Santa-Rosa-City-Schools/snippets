---
id: "1738287868459"
title: "Elementary Only Attendance - Unexcused Absenses and Tardys with Percentages (for All-Day Codes) "
category: "student queries"
tags: ["Attendance"]
createdAt: "2025-01-31T01:44:28Z"
---

Elementary Only Attendance - Unexcused Absenses and Tardys with Percentages (for All-Day Codes) ** must be run at site level. Replace year ("20XX-20XX") with desired school year

```text
LIST STU AHS ID LN FN GR? EN PR AE AU TD (( 1.0 * AHS.AU/AHS.EN * 100 )) (( 1.0 * AHS.TD/AHS.EN * 100 )) IF YR = 20XX-20XX
```
