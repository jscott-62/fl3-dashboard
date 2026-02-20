# fl3-dashboard
FL3 Business Dashboard

**Automatic weekly snapshots:**
- When you run `./update-metrics.sh` (or I run it for you), it checks the date of the latest week entry
- If it's **less than 7 days old**, it updates the email count in place (same week)
- If it's **7+ days old**, it freezes the current week as a snapshot and creates a new week entry with the fresh GHL count
- The "New Emails This Week" card on the dashboard computes the difference between the two most recent weeks
- 
