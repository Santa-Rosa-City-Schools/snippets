---
id: "1743107413615"
title: "Update Credits Received Based on Grades - Ridgway"
category: "aeries-query"
tags: ["Grades", "Ridgway"]
createdAt: "2025-03-27T20:30:13Z"
---

These queries update students credits based on their grades, following the 2024-2025 Ridgway MOU.

```text
CHANGE GRD CR TO 3.5 IF M6 = A+ OR M6 = A OR M6 = A- OR M6 = F

CHANGE GRD CR TO 3 IF M6 = B+ OR M6 = B OR M6 = B- OR M6 = C+ OR M6 = C OR M6 = C-

CHANGE GRD CR TO 2.5 IF M6 = D+ OR M6 = D OR M6 = D-

```
