import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 티니핑 추천",
    page_icon="💖",
    layout="centered",
)


# =========================================================
# MBTI별 티니핑 추천 데이터
# 이 추천은 재미를 위한 창작 매칭입니다.
# =========================================================
TEENIEPING_DATA = {
    "ISTJ": {
        "name": "바로핑",
        "emoji": "📘",
        "color": "파란색",
        "title": "원칙을 중요하게 생각하는 모범생",
        "description": (
            "ISTJ는 책임감이 강하고 정해진 원칙과 약속을 중요하게 생각합니다. "
            "해야 할 일을 정확하게 처리하고 주변이 안정적으로 운영되도록 돕는 "
            "바로핑의 이미지와 잘 어울립니다."
        ),
        "keywords": "책임감 · 원칙 · 신뢰",
        "message": "차근차근 해내는 힘이 가장 큰 장점이에요!",
    },

    "ISFJ": {
        "name": "하츄핑",
        "emoji": "💖",
        "color": "분홍색",
        "title": "따뜻한 사랑을 전하는 다정한 친구",
        "description": (
            "ISFJ는 주변 사람의 마음과 필요를 세심하게 살피는 유형입니다. "
            "사랑과 배려를 중요하게 생각하고 가까운 사람을 따뜻하게 보살피는 모습이 "
            "하츄핑과 잘 어울립니다."
        ),
        "keywords": "배려 · 사랑 · 헌신",
        "message": "당신의 따뜻한 마음은 주변 사람에게 큰 힘이 돼요!",
    },

    "INFJ": {
        "name": "해핑",
        "emoji": "🌟",
        "color": "노란색",
        "title": "사람들에게 희망을 전하는 조용한 이상가",
        "description": (
            "INFJ는 사람의 내면을 깊이 이해하고 더 나은 세상을 꿈꾸는 유형입니다. "
            "겉으로는 조용하지만 주변 사람에게 희망과 용기를 전하는 해핑의 이미지와 "
            "잘 어울립니다."
        ),
        "keywords": "통찰 · 희망 · 이상",
        "message": "당신의 조용한 진심은 생각보다 멀리 전해져요!",
    },

    "INTJ": {
        "name": "띠용핑",
        "emoji": "🔮",
        "color": "보라색",
        "title": "남다른 시각을 가진 전략가",
        "description": (
            "INTJ는 상황을 깊이 분석하고 장기적인 계획을 세우는 데 능합니다. "
            "다른 사람이 미처 발견하지 못한 가능성을 찾아내는 독특한 시각이 "
            "띠용핑의 신비로운 이미지와 잘 어울립니다."
        ),
        "keywords": "전략 · 분석 · 독창성",
        "message": "당신만의 시각으로 새로운 길을 발견해 보세요!",
    },

    "ISTP": {
        "name": "아자핑",
        "emoji": "💪",
        "color": "주황색",
        "title": "필요한 순간에 행동하는 해결사",
        "description": (
            "ISTP는 상황을 빠르게 판단하고 현실적인 방법으로 문제를 해결합니다. "
            "말보다 행동을 앞세우며 어려운 상황에서도 침착하게 움직이는 모습이 "
            "용감한 아자핑과 잘 어울립니다."
        ),
        "keywords": "행동력 · 침착함 · 문제 해결",
        "message": "고민이 길어질 때는 직접 해보는 것이 답이에요!",
    },

    "ISFP": {
        "name": "차차핑",
        "emoji": "🌿",
        "color": "초록색",
        "title": "편안함을 전하는 부드러운 감성가",
        "description": (
            "ISFP는 섬세한 감성과 자신만의 취향을 소중하게 생각합니다. "
            "경쟁하기보다는 자연스럽고 평화로운 분위기 속에서 자신을 표현하는 모습이 "
            "차차핑의 편안한 이미지와 잘 어울립니다."
        ),
        "keywords": "감성 · 평화 · 자연스러움",
        "message": "당신만의 속도와 감성을 소중하게 지켜주세요!",
    },

    "INFP": {
        "name": "라라핑",
        "emoji": "🎵",
        "color": "보라색",
        "title": "풍부한 감성을 가진 낭만적인 몽상가",
        "description": (
            "INFP는 풍부한 상상력과 자신만의 가치관을 가진 유형입니다. "
            "음악과 감성으로 마음을 표현하고 아름다운 가능성을 상상하는 모습이 "
            "라라핑과 잘 어울립니다."
        ),
        "keywords": "상상력 · 감성 · 가치",
        "message": "당신의 상상은 세상을 더 아름답게 만들 수 있어요!",
    },

    "INTP": {
        "name": "깜빡핑",
        "emoji": "💡",
        "color": "하늘색",
        "title": "생각의 세계에 빠져드는 탐구자",
        "description": (
            "INTP는 궁금한 것이 생기면 원리와 구조를 끝까지 탐구합니다. "
            "흥미로운 생각에 집중하다 보면 주변 일을 잠시 잊기도 하는 모습이 "
            "깜빡핑과 재미있게 닮아 있습니다."
        ),
        "keywords": "논리 · 탐구 · 호기심",
        "message": "엉뚱해 보이는 질문에서 훌륭한 아이디어가 시작돼요!",
    },

    "ESTP": {
        "name": "키키핑",
        "emoji": "🎉",
        "color": "빨간색",
        "title": "재미있는 일을 놓치지 않는 모험가",
        "description": (
            "ESTP는 새로운 경험과 짜릿한 도전을 좋아합니다. "
            "상황에 빠르게 적응하고 주변 사람에게 웃음과 활력을 주는 모습이 "
            "장난기 넘치는 키키핑과 잘 어울립니다."
        ),
        "keywords": "모험 · 순발력 · 유쾌함",
        "message": "새로운 도전 속에서 당신의 매력이 가장 빛나요!",
    },

    "ESFP": {
        "name": "라라핑",
        "emoji": "🎤",
        "color": "분홍색",
        "title": "무대를 빛내는 분위기 메이커",
        "description": (
            "ESFP는 사람들과 즐거움을 나누고 현재의 순간을 충분히 누리는 유형입니다. "
            "밝은 표현력과 풍부한 에너지로 주변 분위기를 즐겁게 만드는 모습이 "
            "라라핑과 잘 어울립니다."
        ),
        "keywords": "표현력 · 즐거움 · 친화력",
        "message": "당신이 즐거우면 주변 사람도 함께 즐거워져요!",
    },

    "ENFP": {
        "name": "차나핑",
        "emoji": "☁️",
        "color": "하늘색",
        "title": "자유로운 상상력을 가진 낙천적인 탐험가",
        "description": (
            "ENFP는 새로운 사람과 가능성을 발견하는 것을 좋아합니다. "
            "정해진 방식에 얽매이기보다는 자유롭게 움직이며 재미있는 아이디어를 "
            "떠올리는 모습이 차나핑과 잘 어울립니다."
        ),
        "keywords": "자유 · 호기심 · 가능성",
        "message": "마음이 끌리는 새로운 가능성을 따라가 보세요!",
    },

    "ENTP": {
        "name": "따라핑",
        "emoji": "🎭",
        "color": "주황색",
        "title": "새로운 방식을 실험하는 아이디어 발명가",
        "description": (
            "ENTP는 기존의 규칙을 그대로 따르기보다 새로운 방법을 시험해 봅니다. "
            "재치 있는 말과 기발한 행동으로 주변 사람에게 새로운 관점을 보여주는 모습이 "
            "따라핑과 잘 어울립니다."
        ),
        "keywords": "창의성 · 재치 · 도전",
        "message": "당연하다고 생각했던 것에 질문을 던져보세요!",
    },

    "ESTJ": {
        "name": "바로핑",
        "emoji": "✅",
        "color": "파란색",
        "title": "모두를 이끄는 믿음직한 지휘관",
        "description": (
            "ESTJ는 목표와 규칙을 분명하게 정하고 일을 효율적으로 추진합니다. "
            "책임감을 가지고 앞장서며 잘못된 것은 바로잡으려는 모습이 "
            "바로핑과 잘 어울립니다."
        ),
        "keywords": "리더십 · 책임 · 추진력",
        "message": "명확한 목표를 세우면 누구보다 빠르게 도달할 수 있어요!",
    },

    "ESFJ": {
        "name": "하츄핑",
        "emoji": "💕",
        "color": "분홍색",
        "title": "모두의 마음을 이어주는 관계 전문가",
        "description": (
            "ESFJ는 사람들과 함께하는 시간을 중요하게 생각하고 주변의 분위기를 "
            "세심하게 살핍니다. 사랑과 관심을 표현하며 모두가 잘 어울리도록 돕는 모습이 "
            "하츄핑과 잘 어울립니다."
        ),
        "keywords": "친화력 · 배려 · 조화",
        "message": "당신의 관심과 표현이 사람들을 하나로 이어줘요!",
    },

    "ENFJ": {
        "name": "해핑",
        "emoji": "🌞",
        "color": "노란색",
        "title": "사람들에게 용기를 주는 따뜻한 리더",
        "description": (
            "ENFJ는 다른 사람의 가능성을 발견하고 성장을 돕는 유형입니다. "
            "밝고 따뜻한 에너지로 사람들에게 자신감과 희망을 전하는 모습이 "
            "해핑과 잘 어울립니다."
        ),
        "keywords": "격려 · 리더십 · 희망",
        "message": "당신의 응원은 누군가가 앞으로 나아갈 힘이 돼요!",
    },

    "ENTJ": {
        "name": "아자핑",
        "emoji": "🔥",
        "color": "빨간색",
        "title": "목표를 향해 전진하는 당당한 지휘관",
        "description": (
            "ENTJ는 큰 목표를 세우고 사람과 자원을 조직하여 결과를 만들어냅니다. "
            "어려운 상황에서도 쉽게 물러서지 않고 자신 있게 앞으로 나아가는 모습이 "
            "아자핑과 잘 어울립니다."
        ),
        "keywords": "목표 · 자신감 · 추진력",
        "message": "큰 목표일수록 당신의 추진력이 더욱 빛나요!",
    },
}


# =========================================================
# 화면 꾸미기
# 결과 영역에는 HTML을 사용하지 않아 태그 노출을 방지합니다.
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, #ffe4ef 0%, transparent 25%),
            radial-gradient(circle at 90% 15%, #fff1b8 0%, transparent 25%),
            linear-gradient(135deg, #fff9fc 0%, #f6f0ff 100%);
    }

    .block-container {
        max-width: 760px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        text-align: center;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        height: 3.2rem;
        border-radius: 16px;
        font-size: 1.05rem;
        font-weight: 700;
    }

    div[data-testid="stAlert"] {
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 제목
# =========================================================
st.title("💖 MBTI 티니핑 연구소")

st.markdown(
    """
    <div style="text-align:center; font-size:1.05rem; margin-bottom:20px;">
        MBTI를 선택하면 성격과 어울리는 티니핑을 추천해 드려요.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()


# =========================================================
# MBTI 선택
# =========================================================
mbti_options = [
    "MBTI를 선택하세요",
    "ISTJ",
    "ISFJ",
    "INFJ",
    "INTJ",
    "ISTP",
    "ISFP",
    "INFP",
    "INTP",
    "ESTP",
    "ESFP",
    "ENFP",
    "ENTP",
    "ESTJ",
    "ESFJ",
    "ENFJ",
    "ENTJ",
]

selected_mbti = st.selectbox(
    "나의 MBTI",
    options=mbti_options,
)

recommend_button = st.button(
    "나와 어울리는 티니핑 찾기",
    type="primary",
)


# =========================================================
# 추천 결과
# =========================================================
if recommend_button:
    if selected_mbti == "MBTI를 선택하세요":
        st.warning("먼저 MBTI 유형을 선택해 주세요.")

    else:
        result = TEENIEPING_DATA[selected_mbti]

        st.balloons()
        st.divider()

        st.subheader(f"{selected_mbti}에게 어울리는 티니핑")

        # 이모지 그림
        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:110px;
                line-height:1.2;
                margin:15px 0 5px 0;
            ">
                {result["emoji"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<h1 style='text-align:center;'>{result['name']}</h1>",
            unsafe_allow_html=True,
        )

        st.caption(f"대표 색상: {result['color']}")

        st.subheader(result["title"])
        st.write(result["description"])

        st.info(f"핵심 키워드: {result['keywords']}")
        st.success(result["message"])

        with st.expander("왜 이 티니핑이 추천되었나요?"):
            st.write(
                f"{selected_mbti}의 일반적인 성향을 바탕으로 "
                f"{result['name']}의 이미지와 창작 방식으로 연결한 결과입니다."
            )


# =========================================================
# 하단 안내
# =========================================================
st.divider()

st.caption(
    "이 추천은 재미를 위한 창작 콘텐츠이며 공식 MBTI 검사, "
    "심리학적 진단 또는 공식 캐릭터 설정과는 관계가 없습니다."
)
