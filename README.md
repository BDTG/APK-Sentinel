# APK Sentinel - Đồ án môn học Cơ sở An toàn Thông tin HUTECH

Công cụ phân tích bảo mật tĩnh cho file APK Android, được phát triển cho đồ án môn học Cơ sở An toàn Thông tin tại HUTECH. Công cụ có khả năng phát hiện quyền nguy hiểm và các lỗ hổng bảo mật phổ biến.

---

## Tính năng chính

*   **Phân tích quyền (Permissions Analysis):** Phát hiện các quyền nguy hiểm, quyền đặc biệt và tính điểm rủi ro.
*   **Phân tích thành phần bị lộ (Exported Components):** Tìm kiếm các Activity, Service có thể bị ứng dụng khác lợi dụng.
*   **Quét lỗ hổng tĩnh (Static Vulnerability Scanning):** Tìm kiếm các dấu hiệu của lỗ hổng như sử dụng HTTP, lưu trữ không an toàn (SharedPreferences), hardcoded secrets, v.v.
*   **Giao diện dòng lệnh (CLI):** Hoạt động hiệu quả trên môi trường Termux của Android.

---

## Yêu cầu

*   Một thiết bị Android (khuyến nghị Android 7.0+).
*   Ứng dụng Termux đã được cài đặt.
*   Python 3.9+

---

## Hướng dẫn Cài đặt Môi trường (trên Termux)

1.  **Cập nhật Termux và cấp quyền truy cập bộ nhớ:**
    ```bash
    pkg update && pkg upgrade -y
    termux-setup-storage
    ```
    *(Một pop-up sẽ hiện lên, hãy chọn "CHO PHÉP")*

2.  **Cài đặt Python và các gói hệ thống cần thiết:**
    ```bash
    pkg install python libxml2 libxslt -y
    ```

3.  **Cài đặt các thư viện Python:**
    ```bash
    pip install androguard==3.4.0a1 --no-deps
    pip install colorama networkx pygments lxml asn1crypto click
    ```

---

## Hướng dẫn Sử dụng

1.  **Clone repository này về máy:**
    ```bash
    git clone https://github.com/BDTG/APK-Sentinel.git
    ```

2.  **Di chuyển vào thư mục dự án:**
    ```bash
    cd APK-Sentinel
    ```

3.  **Chạy phân tích:**
    Sử dụng lệnh `python main.py` theo sau là đường dẫn đến file APK. Thư mục `apks/` đã chứa sẵn 3 file để bạn thử nghiệm.

    *   **Phân tích một ứng dụng an toàn:**
        ```bash
        python main.py apks/clean_app.apk
        ```
    *   **Phân tích một ứng dụng có nhiều rủi ro:**
        ```bash
        python main.py apks/risky_app.apk
        ```
    *   **Phân tích một ứng dụng thực tế:**
        ```bash
        python main.py apks/real_world_app.apk
        ```

---

## Thông tin nhóm

*   **Nhóm:** Cyber Shield
*   **Lớp:** 23DATA1
*   **Thành viên:** Lê Đình Duy, Trần Duy Thái, Phạm Duy Khánh, Võ Nhật Minh
