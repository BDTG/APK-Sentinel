# --- File MỚI: manifest_analyzer.py ---

def analyze_manifest(apk_object):
    """
    Phân tích file AndroidManifest.xml để tìm các thành phần bị "lộ" ra ngoài (exported).
    Một thành phần bị exported có thể được khởi chạy bởi các ứng dụng khác,
    tạo ra nguy cơ bảo mật nếu không được xử lý cẩn thận.
    """
    exported_activities = []
    exported_services = []
    exported_receivers = []

    try:
        # Androguard có sẵn phương thức is_exported() cực kỳ tiện lợi
        for activity in apk_object.get_activities():
            if apk_object.is_exported_activity(activity):
                exported_activities.append(activity)

        for service in apk_object.get_services():
            if apk_object.is_exported_service(service):
                exported_services.append(service)

        for receiver in apk_object.get_receivers():
            if apk_object.is_exported_receiver(receiver):
                exported_receivers.append(receiver)
                
    except Exception as e:
        print(f"[!] Lỗi khi phân tích manifest: {e}")

    return {
        "activities": exported_activities,
        "services": exported_services,
        "receivers": exported_receivers
    }