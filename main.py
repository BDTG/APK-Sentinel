# --- File: main.py (Đã chú thích) ---
import sys
# Androguard là thư viện cốt lõi để "mổ xẻ" và phân tích file APK
from androguard.misc import AnalyzeAPK

# Nhập các hàm phân tích chuyên biệt từ các module khác
from permission_analyzer import analyze_permissions
from vulnerability_scanner import scan_for_vulnerabilities
from report_generator import generate_cli_report
from manifest_analyzer import analyze_manifest

def main(apk_path):
    """
    Hàm chính điều phối toàn bộ quá trình phân tích.
    Nhận đường dẫn file APK, gọi các module phân tích, và cuối cùng in báo cáo.
    """
    # Sử dụng mã màu ANSI để làm nổi bật thông báo
    print(f"\033[94m[*] Bắt đầu phân tích file: {apk_path}\033[0m")
    try:
        # Đây là bước quan trọng nhất của Androguard. Nó giải nén và phân tích APK.
        # a: Đối tượng APK, chứa thông tin chung như manifest, permissions.
        # d_list: Danh sách các file Dalvik Executable (.dex), chứa mã nguồn của ứng dụng.
        # dx: Đối tượng Analysis, dùng cho các phân tích sâu hơn về mã.
        a, d_list, dx = AnalyzeAPK(apk_path)
        
        print("[*] Đã nạp APK. Bắt đầu trích xuất thông tin...")

        # 1. Gọi module phân tích quyền, truyền vào đối tượng APK
        permission_results = analyze_permissions(a)
        
        # 2. Gọi module quét lỗ hổng, truyền vào file DEX đầu tiên (thường là file chính)
        vulnerability_results = scan_for_vulnerabilities(d_list[0])

        # 3. Gọi module phân tích manifest để tìm thành phần bị "lộ"
        manifest_results = analyze_manifest(a)

        print("[*] Phân tích hoàn tất. Đang tạo báo cáo...")
        
        # 4. Tập hợp tất cả kết quả và gọi module tạo báo cáo
        generate_cli_report(apk_path, permission_results, vulnerability_results, manifest_results)

    except Exception as e:
        # Bắt tất cả các lỗi có thể xảy ra (ví dụ: file APK lỗi, không đọc được)
        print(f"\033[91m[!] Lỗi: Không thể phân tích file APK. Chi tiết: {e}\033[0m")
        print("[!] Hãy chắc chắn rằng đường dẫn file là chính xác và file không bị lỗi.")

# --- Entry point của chương trình ---
if __name__ == "__main__":
    # Kiểm tra xem người dùng có cung cấp đúng 1 tham số (đường dẫn file APK) không
    if len(sys.argv) != 2:
        print("Sử dụng: python main.py <đường_dẫn_tới_file.apk>")
        # Thoát chương trình nếu dùng sai cú pháp
        sys.exit(1)
        
    apk_file_path = sys.argv[1]
    main(apk_file_path)
