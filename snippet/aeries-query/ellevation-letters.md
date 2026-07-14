---
id: "1738287868535"
title: "Ellevation Letters"
category: "aeries-query"
tags: ["Testing", "Elpac", "Summative"]
createdAt: "2025-01-31T22:27:30Z"
---

List students taking the ELPAC test and who become EL after a given date with their correspondence language

```text
LIST STU LAC STU.ID STU.NM STU.SC? STU.LF STU.CL? IF ( LAC.EIT = "ELPAC" AND LAC.EID >= 2/1/2023 ) 
```
