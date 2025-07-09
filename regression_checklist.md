# Regression Checklist – Segwise.ai Dashboard

This checklist is based on filters, boards, and custom reports as shown in the product demo videos.

| Module         | Test Case                                     | Expected Result                                | Priority |
|----------------|-----------------------------------------------|------------------------------------------------|----------|
| Filters        | Apply campaign/date filter                    | Dashboard updates with correct data            | High     |
| Filters        | Clear filters                                 | Filters reset to default                       | Medium   |
| Filters        | Apply invalid/edge-case filter                | No crash; show empty state or message          | Medium   |
| Boards         | Load saved board                              | Filters and layout load correctly              | High     |
| Boards         | Switch between boards                         | Correct data shown for each board              | High     |
| Boards         | Create new board (no save)                    | Preview works; no UI issues                    | Medium   |
| Custom Reports | Preview custom report                         | Metrics appear as expected                     | High     |
| Custom Reports | Export report                                 | Download completes successfully (CSV, etc.)    | Medium   |
| Custom Reports | Edit report settings                          | UI updates correctly without errors            | Medium   |
