import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 버튼을 눌러 오늘 먹을 점심 메뉴를 뽑아보세요.")

# 카테고리별 메뉴 데이터
menu_data = {
    "한식": ["김치찌개", "된장찌개", "제육볶음", "비빔밥", "국밥", "불고기", "칼국수", "돈까스"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "볶음밥", "마파두부덮밥"],
    "일식": ["초밥", "라멘", "우동", "규동", "카레라이스", "메밀소바", "가츠동"],
    "양식": ["파스타", "피자", "햄버거", "스테이크", "리조또", "샌드위치"],
    "분식/기타": ["떡볶이", "김밥", "쌀국수", "타코", "샐러드", "포케"]
}

# 사이드바에서 카테고리 선택 기능 제공
st.sidebar.header("메뉴 필터")
selected_categories = st.sidebar.multiselect(
    "원하는 음식 종류를 선택하세요:",
    options=list(menu_data.keys()),
    default=list(menu_data.keys())  # 기본값은 전체 선택
)

# 선택된 카테고리의 메뉴들을 하나의 리스트로 합치기
available_menus = []
for category in selected_categories:
    available_menus.extend(menu_data[category])

st.divider()

# 추천 버튼 및 결과 출력
if st.button("🎲 오늘의 점심 뽑기!", type="primary", use_container_width=True):
    if available_menus:
        chosen_menu = random.choice(available_menus)
        st.balloons()  # 축하 풍선 효과
        st.success(f"오늘의 추천 메뉴는 **{chosen_menu}** 입니다! 맛있게 드세요! 😋")
    else:
        st.warning("왼쪽 사이드바에서 최소 한 개 이상의 음식 종류를 선택해 주세요!")
