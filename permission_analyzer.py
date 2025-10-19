# --- File: permission_analyzer.py (Đã chú thích) ---

# Sử dụng set (tập hợp) để tra cứu quyền nhanh hơn list rất nhiều (O(1) so với O(n))
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

# Các quyền đặc biệt, yêu cầu người dùng phải cấp thủ công trong cài đặt
SPECIAL_PERMISSIONS = {
    "android.permission.SYSTEM_ALERT_WINDOW", # Cho phép vẽ đè lên ứng dụng khác (dùng trong tấn công overlay)
    "android.permission.WRITE_SETTINGS", # Cho phép thay đổi cài đặt hệ thống
    "android.permission.REQUEST_INSTALL_PACKAGES" # Cho phép tự cài đặt ứng dụng khác
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
        # Kiểm tra nếu quyền nằm trong danh sách nguy hiểm
        if perm in DANGEROUS_PERMISSIONS:
            score += 1
            # Lấy tên ngắn gọn của quyền để báo cáo (VD: CAMERA)
            dangerous_found.append(perm.split('.')[-1])
        # Kiểm tra nếu quyền nằm trong danh sách đặc biệt
        if perm in SPECIAL_PERMISSIONS:
            score += 3 # Quyền đặc biệt có mức độ rủi ro cao hơn
            special_found.append(perm.split('.')[-1])

    # KIỂM TRA TỔ HỢP QUYỀN NGUY HIỂM CAO
    # Kịch bản: Đọc trộm mã OTP từ SMS rồi gửi về server của kẻ tấn công.
    if "android.permission.READ_SMS" in permissions and "android.permission.INTERNET" in permissions:
        score += 5 # Cộng điểm phạt rất nặng cho tổ hợp này

    # Trả về kết quả dưới dạng dictionary
    return {
        "total_permissions": len(permissions),
        # sorted(list(set(...))) để đảm bảo danh sách không có mục trùng lặp và được sắp xếp
        "dangerous_found": sorted(list(set(dangerous_found))),
        "special_found": sorted(list(set(special_found))),
        "risk_score": score
    }
