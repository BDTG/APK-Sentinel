# --- File: report_generator.py (Đã chú thích và cải thiện) ---

def get_risk_level(score):
    """Chuyển đổi điểm số thành mức độ rủi ro kèm màu sắc."""
    if score >= 8:
        # Màu đỏ cho mức độ cao
        return f"\033[91mCAO (Điểm: {score})\033[0m"
    elif 4 <= score < 8:
        # Màu vàng cho mức độ trung bình
        return f"\033[93mTRUNG BÌNH (Điểm: {score})\033[0m"
    else:
        # Màu xanh cho mức độ thấp
        return f"\033[92mTHẤP (Điểm: {score})\033[0m"

def generate_cli_report(apk_path, perm_results, vuln_results, manifest_results):
    """Tạo và in báo cáo tổng hợp ra giao diện dòng lệnh (CLI)."""
    file_name = apk_path.split('/')[-1]
    
    print("\n" + "="*60)
    print(f"    BÁO CÁO PHÂN TÍCH BẢO MẬT CHO: {file_name}")
    print("="*60)

    # === Phần 1: Báo cáo về Quyền ===
    print("\n\033[1m[+] PHÂN TÍCH QUYỀN (PERMISSIONS)\033[0m")
    print(f"    - Tổng số quyền yêu cầu: {perm_results['total_permissions']}")
    print(f"    - Mức độ rủi ro: {get_risk_level(perm_results['risk_score'])}")
    if perm_results['dangerous_found']:
        print("\n    \033[93m--> Các quyền Nguy hiểm được tìm thấy (Cần người dùng cho phép lúc chạy):\033[0m")
        for p in perm_results['dangerous_found']:
            print(f"        - {p}")
    if perm_results['special_found']:
        print("\n    \033[91m--> Các quyền Đặc biệt được tìm thấy (Cần cấp phép trong Cài đặt):\033[0m")
        for p in perm_results['special_found']:
            print(f"        - {p}")

    # === Phần 2: Báo cáo về Thành phần bị Lộ ===
    print("\n\033[1m[+] PHÂN TÍCH THÀNH PHẦN BỊ LỘ (EXPORTED COMPONENTS)\033[0m")
    total_exported = len(manifest_results["activities"]) + len(manifest_results["services"]) + len(manifest_results["receivers"])
    if total_exported == 0:
        print("    - \033[92mTuyệt vời! Không tìm thấy thành phần nào bị lộ ra ngoài.\033[0m")
    else:
        # --- CẢI TIẾN: Thêm gợi ý cho người dùng ---
        print("    - \033[91mCẢNH BÁO: Tìm thấy các thành phần có thể bị ứng dụng khác gọi đến!\033[0m")
        print("      \033[3m(Gợi ý: Cần xem xét kỹ lưỡng xem việc 'lộ' các thành phần này có thực sự cần thiết không)\033[0m")
        if manifest_results["activities"]:
            print("\n    \033[93m--> Activities bị lộ:\033[0m")
            for item in manifest_results["activities"]: print(f"        - {item}")
        if manifest_results["services"]:
            print("\n    \033[91m--> Services bị lộ (Nguy cơ cao):\033[0m")
            for item in manifest_results["services"]: print(f"        - {item}")
        if manifest_results["receivers"]:
            print("\n    \033[91m--> Receivers bị lộ (Nguy cơ cao):\033[0m")
            for item in manifest_results["receivers"]: print(f"        - {item}")

    # === Phần 3: Báo cáo về Dấu hiệu Lỗ hổng ===
    print("\n\033[1m[+] QUÉT DẤU HIỆU LỖ HỔNG (STATIC ANALYSIS)\033[0m")
    if not vuln_results:
        print("    - \033[92mKhông tìm thấy dấu hiệu lỗ hổng cơ bản nào.\033[0m")
    else:
        for key, finding in vuln_results.items():
            print(f"    - \033[93m{key}:\033[0m {finding}")

    print("\n" + "="*60)
    print("                  PHÂN TÍCH HOÀN TẤT")
    print("="*60 + "\n")
