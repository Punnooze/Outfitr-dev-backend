def individual_serial_user_data_profile(user_profile) -> dict:
    return {
        "user_id": user_profile.get("user_id"),
        "age_group": user_profile.get("age_group"),
        "location": user_profile.get("location"),
        "gender": user_profile.get("gender"),
        "preferred_brands": user_profile.get("preferred_brands", {}),
        "preferred_sizes": user_profile.get("preferred_sizes", {}),
        "preferred_fits": user_profile.get("preferred_fits", {}),
        "preferred_themes": user_profile.get("preferred_themes", {}),
        "preferred_master_categories": user_profile.get("preferred_master_categories", {}),
        "preferred_sub_categories": user_profile.get("preferred_sub_categories", {}),
        "budget_range": user_profile.get("budget_range", {}),
        "style_preferences": user_profile.get("style_preferences"),
        "brand_blacklist": user_profile.get("brand_blacklist", {})
    }