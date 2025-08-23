import streamlit as st
import sqlite3

# DB 연결 함수
def get_connection():
    return sqlite3.connect('customer.db', check_same_thread=False)

# DB 초기화 함수 (옵션)
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists customer(
            id integer primary key,
            name text,
            age integer
        )
    ''')
    conn.commit()
    conn.close()

# 전체 고객 조회
def get_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    conn.close()
    return rows

# 고객 추가
def add_customer(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customer (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

# 고객 수정
def update_customer(customer_id, name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customer SET name=?, age=? WHERE id=?", (name, age, customer_id))
    conn.commit()
    conn.close()

# 고객 삭제
def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customer WHERE id=?", (customer_id,))
    conn.commit()
    conn.close()

# 앱 시작
st.title("고객 관리 시스템 (CRUD)")

# DB 초기화
init_db()

# 메뉴 선택
menu = st.sidebar.selectbox("메뉴", ["전체 고객 보기", "고객 추가", "고객 수정", "고객 삭제"])

# 전체 고객 보기
if menu == "전체 고객 보기":
    st.subheader("📋 고객 리스트")
    customers = get_customers()
    if customers:
        for c in customers:
            st.write(f"🧍 ID: {c[0]} | 이름: {c[1]} | 나이: {c[2]}")
    else:
        st.info("고객이 없습니다.")

# 고객 추가
elif menu == "고객 추가":
    st.subheader("➕ 고객 추가")
    name = st.text_input("이름")
    age = st.number_input("나이", min_value=0, max_value=120, step=1)

    if st.button("고객 등록"):
        if name:
            add_customer(name, age)
            st.success(f"{name}님이 추가되었습니다.")
        else:
            st.warning("이름을 입력해주세요.")

# 고객 수정
elif menu == "고객 수정":
    st.subheader("✏️ 고객 정보 수정")
    customers = get_customers()
    customer_dict = {f"{c[0]} - {c[1]}": c for c in customers}
    selected = st.selectbox("수정할 고객 선택", list(customer_dict.keys()))

    if selected:
        customer = customer_dict[selected]
        new_name = st.text_input("이름", value=customer[1])
        new_age = st.number_input("나이", value=customer[2], min_value=0, max_value=120, step=1)
        if st.button("수정"):
            update_customer(customer[0], new_name, new_age)
            st.success("고객 정보가 수정되었습니다.")

# 고객 삭제
elif menu == "고객 삭제":
    st.subheader("🗑️ 고객 삭제")
    customers = get_customers()
    customer_dict = {f"{c[0]} - {c[1]}": c for c in customers}
    selected = st.selectbox("삭제할 고객 선택", list(customer_dict.keys()))

    if selected:
        customer = customer_dict[selected]
        if st.button("삭제"):
            delete_customer(customer[0])
            st.warning("고객이 삭제되었습니다.")