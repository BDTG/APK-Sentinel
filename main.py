# --- File: main.py (PHIÊN BẢN NÂNG CẤP) ---
import sys
from androguard.misc import AnalyzeAPK

from permission_analyzer import analyze_permissions
from vulnerability_scanner import scan_for_vulnerabilities
from report_generator import generate_cli_report
from manifest_analyzer import analyze_manifest # <-- DÒNG MỚI

def main(apk_path):
    print(f"\033[94m[*] Bắt đầu phân tích file: {apk_path}\033[0m")
    try:
        a, d_list, dx = AnalyzeAPK(apk_path)
        
        print("[*] Đã nạp APK. Bắt đầu trích xuất thông tin...")

        permission_results = analyze_permissions(a)
        # d_list[0] là file DEX chính của ứng dụng
        vulnerability_results = scan_for_vulnerabilities(d_list[0])
        manifest_results = analyze_manifest(a) # <-- DÒNG MỚI

        print("[*] Phân tích hoàn tất. Đang tạo báo cáo...")
        # Thêm manifest_results vào lời gọi hàm
        generate_cli_report(apk_path, permission_results, vulnerability_results, manifest_results) # <-- DÒNG ĐƯỢC CẬP NHẬT

    except Exception as e:
        print(f"\033[91m[!] Lỗi: Không thể phân tích file APK. {e}\033[0m")
        print("[!] Hãy chắc chắn rằng đường dẫn file là chính xác và file không bị lỗi.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Sử dụng: python main.py <đường_dẫn_tới_file.apk>")
        sys.exit(1)
        
    apk_file_path = sys.argv[1]
    main(apk_file_path)