---
id: "1738287868359"
title: "InterDistrict Students"
category: "aeries-query"
tags: ["Enrollment"]
createdAt: "2025-02-01T02:36:11Z"
---

Provides a list of current students on InterDistrict (Code stars with O), the school they attend, and the district or school they come from.

```text
LIST STU ENR STU.ID STU.LN STU.FN STU.SC? STU.IT? STU.ITD ENR.ED ENR.LD IF STU.IT : O AND ENR.ED >= 08/11/2023 AND ENR.LD = NULL 
```
