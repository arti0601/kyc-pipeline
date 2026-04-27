ALLOWED = {
    "draft": ["submitted"],
    "submitted": ["under_review"],
    "under_review": ["approved", "rejected", "more_info_requested"],
    "more_info_requested": ["submitted"],
}

def change_state(current, new):
    if new not in ALLOWED.get(current, []):
        raise ValueError(f"Invalid transition from {current} to {new}")
    return new