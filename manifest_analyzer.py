# --- File: manifest_analyzer.py (Đã chú thích) ---

def analyze_manifest(apk_object):
    """
    Phân tích file AndroidManifest.xml để tìm các thành phần bị "lộ" ra ngoài (exported).
    Một thành phần bị exported có thể được khởi chạy bởi các ứng dụng khác,
    tạo ra nguy cơ bảo mật nếu không được xử lý cẩn thận (VD: Lộ dữ liệu, thực thi mã).
    
    Args:
        apk_object: Đối tượng APK đã được phân tích bởi Androguard.

    Returns:
        Một dictionary chứa danh sách các thành phần bị exported.
    """
    # Khởi tạo các danh sách để lưu kết quả
    exported_activities = []
    exported_services = []
    exported_receivers = []

    try:
        # Vòng lặp qua tất cả các Activity được khai báo trong manifest
        for activity in apk_object.get_activities():
            # Androguard cung cấp hàm is_exported_activity() tiện lợi để kiểm tra
            if apk_object.is_exported_activity(activity):
                exported_activities.append(activity)

        # Tương tự với các Service
        for service in apk_object.get_services():
            if apk_object.is_exported_service(service):
                exported_services.append(service)

        # Tương tự với các BroadcastReceiver
        for receiver in apk_object.get_receivers():
            if apk_object.is_exported_receiver(receiver):
                exported_receivers.append(receiver)
                
    except Exception as e:
        print(f"[!] Lỗi khi phân tích manifest: {e}")

    # Trả về kết quả dưới dạng một dictionary có cấu trúc
    return {
        "activities": exported_activities,
        "services": exported_services,
        "receivers": exported_receivers
    }
