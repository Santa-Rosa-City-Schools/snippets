---
id: "1738287868620"
title: "Language Table Changes"
category: "SSID Import"
tags: ["SSID", "Import", "Logs"]
createdAt: "2025-01-31T01:44:28Z"
---

To see what students had their language page updated

```text
LIST LOG IF DT > "04/19/2023" AND OB = LAC AND USR = "username@srcs.k12.ca.us"
```
