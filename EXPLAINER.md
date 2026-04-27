# 1. State Machine
I implemented a centralized state machine in `state_machine.py` using a dictionary of allowed transitions. All status updates go through the `change_state()` function, which raises a ValueError if an invalid transition is attempted. This ensures no illegal state changes can happen at the API level.

# 2. File Upload
File validation checks both file type (PDF, JPG, PNG) and size (max 5MB). If a user tries to upload a file larger than 5MB, the API rejects it with a 400 error before saving.

# 3. Queue
The reviewer dashboard fetches all submissions with status "submitted", ordered by creation time. SLA is calculated dynamically by checking if the submission is older than 24 hours.

# 4. Auth
Authentication is implemented using a simple username header. Merchants can only access their own submissions by verifying `submission.merchant == request.user`. Reviewers can access all submissions.

# 5. AI Audit
Initially, AI suggested directly updating the status field in the view. I identified this as unsafe and replaced it with a centralized state machine to enforce valid transitions and prevent invalid updates.