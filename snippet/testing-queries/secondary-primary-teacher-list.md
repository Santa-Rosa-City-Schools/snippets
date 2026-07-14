---
id: "1738287868551"
title: "Secondary Primary Teacher List"
category: "testing queries"
tags: ["Testing", "Caaspp", "Teacher"]
createdAt: "2025-01-31T01:44:28Z"
---

Secondary Primary Teacher List - Run to provide a list of current teachers by department at each site for the TSC to identify which ones will be Test Administrators

```text
LIST STU SEC MST FTF SSE STF SSE.PR STU.ID STU.LN STU.FN STU.MN STU.CID STU.BD STU.GN STU.SC? STU.GR STF.FN STF.LN FTF.STI CRS.DC? BY STF.LN IF SSE.PR = 1 AND ( ( ( CRS.DC = E OR CRS.DC = M ) AND STU.GR = 11) OR ( ( CRS.DC = P OR CRS.DC = B ) AND ( STU.GR = 11 OR STU.GR = 12 ) )
```
