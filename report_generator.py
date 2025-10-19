# --- File: report_generator.py (PHIÊN BẢN NÂNG CẤP) ---

def get_risk_level(score):
    if score >= 8:
        return f"\033[91mCAO (Điểm: {score})\033[0m"
    elif 4 <= score < 8:
        return f"\033[93mTRUNG BÌNH (Điểm: {score})\033[0m"
    else:
        return f"\033[92mTHẤP (Điểm: {score})\033[0m"

# Thêm manifest_results vào tham số
def generate_cli_report(apk_path, perm_results, vuln_results, manifest_results):
    file_name = apk_path.split('/')[-1]
    
    print("\n" + "="*60)
    print(f"    BÁO CÁO PHÂN TÍCH BẢO MẬT CHO: {file_name}")
    print("="*60)

    print("\n\033[1m[+] PHÂN TÍCH QUYỀN (PERMISSIONS)\033[0m")
    # ... (phần này giữ nguyên)
    print(f"    - Tổng số quyền yêu cầu: {perm_results['total_permissions']}")
    print(f"    - Mức độ rủi ro: {get_risk_level(perm_results['risk_score'])}")
    if perm_results['dangerous_found']:
        print("\n    \033[93m--> Các quyền Nguy hiểm được tìm thấy:\033[0m")
        for p in perm_results['dangerous_found']:
            print(f"        - {p}")
    if perm_results['special_found']:
        print("\n    \033[91m--> Các quyền Đặc biệt được tìm thấy:\033[0m")
        for p in perm_results['special_found']:
            print(f"        - {p}")

    # --- MỤC MỚI ĐƯỢC THÊM VÀO ---
    print("\n\033[1m[+] PHÂN TÍCH THÀNH PHẦN BỊ LỘ (EXPORTED COMPONENTS)\033[0m")
    total_exported = len(manifest_results["activities"]) + len(manifest_results["services"]) + len(manifest_results["receivers"])
    if total_exported == 0:
        print("    - \033[92mTuyệt vời! Không tìm thấy thành phần nào bị lộ ra ngoài.\033[0m")
    else:
        print("    - \033[91mCẢNH BÁO: Tìm thấy các thành phần có thể bị ứng dụng khác gọi đến!\033[0m")
        if manifest_results["activities"]:
            print("\n    \033[93m--> Activities bị lộ:\033[0m")
            for item in manifest_results["activities"]: print(f"        - {item}")
        if manifest_results["services"]:
            print("\n    \033[91m--> Services bị lộ (Nguy cơ cao):\033[0m")
            for item in manifest_results["services"]: print(f"        - {item}")
        if manifest_results["receivers"]:
            print("\n    \033[91m--> Receivers bị lộ (Nguy cơ cao):\033[0m")
            for item in manifest_results["receivers"]: print(f"        - {item}")
    # --- KẾT THÚC MỤC MỚI ---

    print("\n\033[1m[+] QUÉT DẤU HIỆU LỖ HỔNG (STATIC ANALYSIS)\033[0m")
    if not vuln_results:
        print("    - \033[92mKhông tìm thấy dấu hiệu lỗ hổng cơ bản nào.\033[0m")
    else:
        for key, finding in vuln_results.items():
            print(f"    - \033[93m{key}:\033[0m {finding}")

    print("\n" + "="*60)
    print("                  PHÂN TÍCH HOÀN TẤT")
    print("="*60 + "\n")