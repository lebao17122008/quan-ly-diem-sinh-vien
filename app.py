#1. Import thư viện và thiết lập trang

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

# Thay bằng thông tin của bạn
HO_TEN_TAC_GIA = "ĐIỀN HỌ TÊN CỦA BẠN"
MSSV_TAC_GIA = "ĐIỀN MSSV CỦA BẠN"

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

#2. Tạo DataFrame

du_lieu = {
    "Ho_ten": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Minh Châu",
        "Phạm Quốc Dũng",
        "Hoàng Thị Hà",
        "Vũ Minh Hùng",
        "Đặng Ngọc Lan",
        "Bùi Tuấn Minh",
        "Đỗ Thị Ngọc",
        "Ngô Văn Phúc"
    ],
    "Chuyen_can": [9, 8, 7, 6, 10, 5, 8, 4, 7, 3],
    "Giua_ky":    [9, 7, 6, 5, 9, 4, 8, 3, 7, 4],
    "Cuoi_ky":    [9, 8, 7, 5, 10, 5, 9, 4, 6, 3]
}

df = pd.DataFrame(du_lieu)

#3. Tính điểm tổng kết và xếp loại

df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

#4. Hiển thị bảng điểm

st.subheader("Bảng điểm của 10 sinh viên")

bang_hien_thi = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(
    bang_hien_thi.style.format({"Tổng kết": "{:.2f}"}),
    hide_index=True
)

#5. Thống kê

diem_trung_binh = df["Tong_ket"].mean()
diem_cao_nhat = df["Tong_ket"].max()
diem_thap_nhat = df["Tong_ket"].min()
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

ten_sv_cao_nhat = ", ".join(
    df.loc[df["Tong_ket"] == diem_cao_nhat, "Ho_ten"].tolist()
)

ten_sv_thap_nhat = ", ".join(
    df.loc[df["Tong_ket"] == diem_thap_nhat, "Ho_ten"].tolist()
)

st.subheader("Thống kê của lớp")

cot1, cot2 = st.columns(2)

cot1.metric("Điểm trung bình lớp", f"{diem_trung_binh:.2f}")
cot2.metric("Số sinh viên đạt", f"{so_sv_dat}/{len(df)}")

st.write(
    f"Sinh viên có điểm cao nhất: "
    f"{ten_sv_cao_nhat} — {diem_cao_nhat:.2f} điểm"
)

st.write(
    f"Sinh viên có điểm thấp nhất: "
    f"{ten_sv_thap_nhat} — {diem_thap_nhat:.2f} điểm"
)

#6. Chọn sinh viên và xem chi tiết

st.subheader("Tra cứu điểm sinh viên")

ten_duoc_chon = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"].tolist()
)

sinh_vien = df.loc[df["Ho_ten"] == ten_duoc_chon].iloc[0]

st.write(f"**Họ tên:** {sinh_vien['Ho_ten']}")

cot1, cot2, cot3 = st.columns(3)

cot1.metric("Chuyên cần", f"{sinh_vien['Chuyen_can']:.2f}")
cot2.metric("Giữa kỳ", f"{sinh_vien['Giua_ky']:.2f}")
cot3.metric("Cuối kỳ", f"{sinh_vien['Cuoi_ky']:.2f}")

st.write(f"**Điểm tổng kết:** {sinh_vien['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sinh_vien['Xep_loai']}")

#7. Vẽ biểu đồ bằng Matplotlib

st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

cac_cot = ax.bar(
    df["Ho_ten"],
    df["Tong_ket"],
    color="steelblue"
)

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
ax.bar_label(cac_cot, fmt="%.2f", padding=3)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

#8. Thông tin người thực hiện

st.divider()

st.caption(
    f("Người thực hiện: Lê Duy Bảo | MSSV: 052208007506")
)
