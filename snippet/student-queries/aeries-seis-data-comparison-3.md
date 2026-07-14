---
id: "1738287868342"
title: "Aeries/SEIS Data Comparison 3"
category: "student queries"
tags: ["Special Education", "Education", "Ed", "AERIES"]
createdAt: "2025-01-31T01:44:28Z"
---

Aeries/SEIS Data Comparison 3 - Aeries/SEIS Data Comparison 3 - This allows us to combing STU, CSE & STF tables and combine a first & last name of a staff member. We are using this query to compare data between Aeries and SEIS.

```text
LIST STU CSE STF STU.LN STU.FN STU.CID STU.ID STU.BD STU.GR STU.SC? STU.RS? (( STF.LN + ", " + STF.FN )) CSE.ED CSE.LI CSE.LA CSE.PT CSE.DI CSE.DI2 CSE.XD STU.SP IF CSE.DI > 0 AND CSE.XD = NULL AND STU.SP # C AND ( STU.LD = NULL )
```
