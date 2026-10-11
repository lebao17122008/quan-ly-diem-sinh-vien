#1. Thư viện và thiết lập trang
from html import escape
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="wide")
HO_TEN_TAC_GIA = "Lê Duy Bảo"
MSSV_TAC_GIA = "052208007506"

#2. Giao diện
st.markdown('''
<style>
.stApp {background:#f5f7fb;color:#0f172a;}
[data-testid="stSidebar"] {background:#eaf0f9;color:#0f172a;}
[data-testid="stMetric"] {background:white;border:1px solid #e2e8f0;border-radius:16px;padding:18px;}
[data-testid="stMetricLabel"] {color:#475569;}
[data-testid="stMetricValue"] {color:#1d4ed8;}
.hero {background:linear-gradient(120deg,#172554,#2563eb);padding:28px;border-radius:20px;margin-bottom:24px;}
.hero h1 {color:white;font-size:32px;margin:0;}
.hero p {color:#dbeafe;margin:10px 0 0;}
.student-card {background:white;border:1px solid #e2e8f0;border-left:5px solid #2563eb;border-radius:14px;padding:18px 22px;margin-bottom:18px;}
.student-card h3 {color:#0f172a;margin:0;}
.student-card p {color:#475569;margin:8px 0 0;}
</style>
''', unsafe_allow_html=True)

#3. Dữ liệu mẫu của 10 sinh viên
DU_LIEU = {
    "Ho_ten": ["Nguyễn Văn An", "Trần Thị Bình", "Lê Minh Châu", "Phạm Quốc Dũng", "Hoàng Thị Hà", "Vũ Minh Hùng", "Đặng Ngọc Lan", "Bùi Tuấn Minh", "Đỗ Thị Ngọc", "Ngô Văn Phúc"],
    "Chuyen_can": [9, 8, 7, 6, 10, 5, 8, 4, 7, 3],
    "Giua_ky": [9, 7, 6, 5, 9, 4, 8, 3, 7, 4],
    "Cuoi_ky": [9, 8, 7, 5, 10, 5, 9, 4, 6, 3]
}
df = pd.DataFrame(DU_LIEU)

#4. Tính tổng kết và xếp loại; không làm tròn trước khi xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Tong_ket"] = 0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

#5. Thống kê, gồm tất cả sinh viên đồng điểm cao nhất/thấp nhất
diem_trung_binh = df["Tong_ket"].mean()
diem_cao_nhat = df["Tong_ket"].max()
diem_thap_nhat = df["Tong_ket"].min()
so_sv_dat = int((df["Tong_ket"] >= 5).sum())
sv_cao_nhat = ", ".join(df.loc[df["Tong_ket"] == diem_cao_nhat, "Ho_ten"])
sv_thap_nhat = ", ".join(df.loc[df["Tong_ket"] == diem_thap_nhat, "Ho_ten"])

#6. Thanh bên và tiêu đề
with st.sidebar:
    st.title("🎓 Student Dashboard")
    st.caption("Bài thực hành Python · Pandas · Streamlit")
    st.divider()
    st.subheader("Cách tính điểm")
    st.write("Chuyên cần: **20%**")
    st.write("Giữa kỳ: **30%**")
    st.write("Cuối kỳ: **50%**")
    st.subheader("Mức xếp loại")
    st.write("🟢 Giỏi: từ 8.5")
    st.write("🔵 Khá: từ 7 đến dưới 8.5")
    st.write("🟠 Trung bình: từ 5 đến dưới 7")
    st.write("🔴 Yếu: dưới 5")
    st.divider()
    st.caption(f"Người thực hiện: {HO_TEN_TAC_GIA}")
    st.caption(f"MSSV: {MSSV_TAC_GIA}")

st.markdown('''<div class="hero"><h1>🎓 QUẢN LÝ ĐIỂM SINH VIÊN</h1><p>Theo dõi kết quả học tập và tra cứu điểm của lớp.</p></div>''', unsafe_allow_html=True)

#7. Thẻ thống kê
cot1, cot2, cot3, cot4 = st.columns(4)
cot1.metric("👥 Tổng sinh viên", len(df))
cot2.metric("📊 Điểm trung bình", f"{diem_trung_binh:.2f}")
cot3.metric("✅ Sinh viên đạt", f"{so_sv_dat}/{len(df)}")
cot4.metric("🎯 Tỷ lệ đạt", f"{so_sv_dat / len(df) * 100:.0f}%")
cot_trai, cot_phai = st.columns(2)
cot_trai.success(f"🏆 Cao nhất: {sv_cao_nhat} — {diem_cao_nhat:.2f} điểm")
cot_phai.info(f"📌 Thấp nhất: {sv_thap_nhat} — {diem_thap_nhat:.2f} điểm")

#8. Bảng điểm tô màu theo xếp loại
st.subheader("📋 Bảng điểm của lớp")
bang_hien_thi = df.rename(columns={"Ho_ten": "Họ tên", "Chuyen_can": "Chuyên cần", "Giua_ky": "Giữa kỳ", "Cuoi_ky": "Cuối kỳ", "Tong_ket": "Tổng kết", "Xep_loai": "Xếp loại"})

def mau_xep_loai(gia_tri):
    return {
        "Giỏi": "background-color:#dcfce7;color:#166534",
        "Khá": "background-color:#dbeafe;color:#1e40af",
        "Trung bình": "background-color:#fef3c7;color:#92400e",
        "Yếu": "background-color:#fee2e2;color:#991b1b"
    }.get(gia_tri, "")

bang_dinh_dang = bang_hien_thi.style.format({"Chuyên cần": "{:.1f}", "Giữa kỳ": "{:.1f}", "Cuối kỳ": "{:.1f}", "Tổng kết": "{:.2f}"}).map(mau_xep_loai, subset=["Xếp loại"])
st.dataframe(bang_dinh_dang, hide_index=True, height=390)

#9. Chọn sinh viên và xem chi tiết
st.subheader("🔎 Tra cứu sinh viên")
ten_duoc_chon = st.selectbox("Chọn sinh viên để xem chi tiết", df["Ho_ten"].tolist())
sinh_vien = df.loc[df["Ho_ten"] == ten_duoc_chon].iloc[0]
st.markdown(f'<div class="student-card"><h3>{escape(sinh_vien["Ho_ten"])}</h3><p>Xếp loại: <strong>{escape(sinh_vien["Xep_loai"])}</strong></p></div>', unsafe_allow_html=True)
cot1, cot2, cot3, cot4 = st.columns(4)
cot1.metric("Chuyên cần", f"{sinh_vien['Chuyen_can']:.2f}")
cot2.metric("Giữa kỳ", f"{sinh_vien['Giua_ky']:.2f}")
cot3.metric("Cuối kỳ", f"{sinh_vien['Cuoi_ky']:.2f}")
cot4.metric("Tổng kết", f"{sinh_vien['Tong_ket']:.2f}")

#10. Biểu đồ Matplotlib
st.subheader("📈 Điểm tổng kết của 10 sinh viên")
bang_mau = {"Giỏi": "#16a34a", "Khá": "#2563eb", "Trung bình": "#f59e0b", "Yếu": "#ef4444"}
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
cac_cot = ax.bar(df["Ho_ten"], df["Tong_ket"], color=df["Xep_loai"].map(bang_mau).tolist(), width=0.65)
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN", fontsize=15, fontweight="bold", pad=20)
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.axhline(y=5, color="#64748b", linestyle="--", linewidth=1, label="Mốc đạt: 5 điểm")
ax.grid(axis="y", alpha=0.15)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
ax.bar_label(cac_cot, fmt="%.2f", padding=3, fontsize=9)
ax.legend(loc="upper left")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)
st.caption("Màu cột: xanh lá = Giỏi · xanh dương = Khá · cam = Trung bình · đỏ = Yếu")

#11. Xuất CSV tương thích tiếng Việt
st.download_button(label="📥 Tải bảng điểm CSV", data=bang_hien_thi.to_csv(index=False).encode("utf-8-sig"), file_name="bang_diem_sinh_vien.csv", mime="text/csv")

#12. Thông tin cuối trang
st.divider()
st.caption(f"Người thực hiện: {HO_TEN_TAC_GIA} | MSSV: {MSSV_TAC_GIA}")
