# --- File: permission_analyzer.py ---

# Danh sách được rút gọn từ tài liệu chính thức của Android
DANGEROUS_PERMISSIONS = {
    "android.permission.READ_CALENDAR", "android.permission.WRITE_CALENDAR",
    "android.permission.CAMERA",
    "android.permission.READ_CONTACTS", "android.permission.WRITE_CONTACTS", "android.permission.GET_ACCOUNTS",
    "android.permission.ACCESS_FINE_LOCATION", "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.RECORD_AUDIO",
    "android.permission.READ_PHONE_STATE", "android.permission.CALL_PHONE",
    "android.permission.SEND_SMS", "android.permission.RECEIVE_SMS", "android.permission.READ_SMS",
    "android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"
}

SPECIAL_PERMISSIONS = {
    "android.permission.SYSTEM_ALERT_WINDOW",
    "android.permission.WRITE_SETTINGS",
    "android.permission.REQUEST_INSTALL_PACKAGES"
}

def analyze_permissions(apk_object):
    """Phân tích và tính điểm rủi ro cho các quyền của APK."""
    try:
        permissions = apk_object.get_permissions()
    except Exception:
        permissions = []

    score = 0
    dangerous_found = []
    special_found = []

    for perm in permissions:
        if perm in DANGEROUS_PERMISSIONS:
            score += 1
            dangerous_found.append(perm.split('.')[-1])
        if perm in SPECIAL_PERMISSIONS:
            score += 3
            special_found.append(perm.split('.')[-1])

    if "android.permission.READ_SMS" in permissions and "android.permission.INTERNET" in permissions:
        score += 5

    return {
        "total_permissions": len(permissions),
        "dangerous_found": sorted(list(set(dangerous_found))),
        "special_found": sorted(list(set(special_found))),
        "risk_score": score
    }