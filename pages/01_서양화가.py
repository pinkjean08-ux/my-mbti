import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 서양화가 매칭",
    page_icon="🎨",
    layout="centered",
)


# =========================================================
# MBTI별 화가 매칭 데이터
# 재미를 위한 창작형 매칭입니다.
# =========================================================
PAINTER_DATA = {
    "ISTJ": {
        "name_ko": "얀 베르메르",
        "name_en": "Johannes Vermeer",
        "years": "1632–1675",
        "country": "네덜란드",
        "movement": "네덜란드 바로크",
        "emoji": "🪟",
        "title": "정돈된 일상 속에서 깊이를 발견하는 관찰자",
        "description": (
            "ISTJ는 질서와 안정성을 중요하게 여기며 세부적인 부분을 꼼꼼하게 살피는 "
            "경향이 있습니다. 조용한 실내와 일상의 순간을 정교한 빛과 구도로 표현한 "
            "베르메르의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "질서 · 관찰력 · 안정감",
        "artwork": "진주 귀걸이를 한 소녀, 우유를 따르는 여인",
        "message": "평범한 일상도 세심하게 바라보면 하나의 작품이 됩니다.",
    },

    "ISFJ": {
        "name_ko": "피에르 오귀스트 르누아르",
        "name_en": "Pierre-Auguste Renoir",
        "years": "1841–1919",
        "country": "프랑스",
        "movement": "인상주의",
        "emoji": "🌷",
        "title": "사람 사이의 따뜻한 온기를 그리는 화가",
        "description": (
            "ISFJ는 가까운 사람을 세심하게 돌보고 따뜻한 관계를 중요하게 생각합니다. "
            "가족과 친구, 평화로운 일상의 행복을 밝고 부드러운 색채로 표현한 "
            "르누아르의 그림과 잘 어울립니다."
        ),
        "keywords": "배려 · 친밀감 · 따뜻함",
        "artwork": "물랭 드 라 갈레트의 무도회, 뱃놀이 일행의 점심",
        "message": "당신이 건네는 따뜻한 관심이 일상을 아름답게 만듭니다.",
    },

    "INFJ": {
        "name_ko": "구스타프 클림트",
        "name_en": "Gustav Klimt",
        "years": "1862–1918",
        "country": "오스트리아",
        "movement": "빈 분리파·상징주의",
        "emoji": "✨",
        "title": "내면의 감정과 상징을 탐색하는 이상주의자",
        "description": (
            "INFJ는 겉으로 드러난 모습보다 사람의 내면과 관계의 의미를 깊이 바라봅니다. "
            "화려한 장식 안에 사랑, 삶, 죽음과 같은 주제를 상징적으로 담아낸 "
            "클림트의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "통찰 · 상징 · 내면",
        "artwork": "키스, 아델레 블로흐바우어의 초상",
        "message": "보이지 않는 감정과 의미를 발견하는 능력이 당신의 강점입니다.",
    },

    "INTJ": {
        "name_ko": "레오나르도 다 빈치",
        "name_en": "Leonardo da Vinci",
        "years": "1452–1519",
        "country": "이탈리아",
        "movement": "르네상스",
        "emoji": "📐",
        "title": "예술과 지식을 연결하는 전략적 탐구자",
        "description": (
            "INTJ는 복잡한 원리를 분석하고 서로 다른 지식을 하나의 체계로 연결하는 데 "
            "흥미를 느끼는 유형입니다. 회화뿐 아니라 해부학, 공학, 자연 관찰을 함께 "
            "탐구했던 레오나르도 다 빈치와 잘 어울립니다."
        ),
        "keywords": "분석 · 전략 · 지적 호기심",
        "artwork": "모나리자, 최후의 만찬",
        "message": "서로 다른 분야를 연결할 때 새로운 가능성이 나타납니다.",
    },

    "ISTP": {
        "name_ko": "에드가 드가",
        "name_en": "Edgar Degas",
        "years": "1834–1917",
        "country": "프랑스",
        "movement": "인상주의",
        "emoji": "🩰",
        "title": "움직임의 구조를 정확하게 포착하는 관찰자",
        "description": (
            "ISTP는 상황을 냉정하게 관찰하고 실제 움직임과 구조를 파악하는 데 능합니다. "
            "무용수와 경주마의 순간적인 동작을 반복해서 연구하고 독특한 구도로 포착한 "
            "드가의 작업 방식과 잘 어울립니다."
        ),
        "keywords": "관찰 · 기술 · 정확성",
        "artwork": "무용 수업, 스타",
        "message": "직접 관찰하고 실험할 때 가장 정확한 답을 찾을 수 있습니다.",
    },

    "ISFP": {
        "name_ko": "클로드 모네",
        "name_en": "Claude Monet",
        "years": "1840–1926",
        "country": "프랑스",
        "movement": "인상주의",
        "emoji": "🪷",
        "title": "순간의 빛과 감각을 섬세하게 느끼는 예술가",
        "description": (
            "ISFP는 현재의 감각과 아름다움을 섬세하게 받아들이며 자신의 방식으로 "
            "표현하는 유형입니다. 시시각각 달라지는 빛과 자연의 분위기를 포착한 "
            "모네의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "감성 · 자연 · 섬세함",
        "artwork": "인상, 해돋이, 수련 연작",
        "message": "지금 이 순간에만 존재하는 빛과 감정을 놓치지 마세요.",
    },

    "INFP": {
        "name_ko": "빈센트 반 고흐",
        "name_en": "Vincent van Gogh",
        "years": "1853–1890",
        "country": "네덜란드",
        "movement": "후기 인상주의",
        "emoji": "🌌",
        "title": "강렬한 내면을 색채로 표현하는 이상주의자",
        "description": (
            "INFP는 자신만의 가치와 감정 세계를 중요하게 여기며 진실한 표현을 추구합니다. "
            "자연과 사람을 바라보며 느낀 감정을 강렬한 색과 붓질로 드러낸 "
            "반 고흐의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "진정성 · 감수성 · 이상",
        "artwork": "별이 빛나는 밤, 해바라기",
        "message": "당신만의 감정과 시선은 다른 사람이 대신 표현할 수 없습니다.",
    },

    "INTP": {
        "name_ko": "르네 마그리트",
        "name_en": "René Magritte",
        "years": "1898–1967",
        "country": "벨기에",
        "movement": "초현실주의",
        "emoji": "🍏",
        "title": "익숙한 세계에 논리적인 질문을 던지는 사상가",
        "description": (
            "INTP는 당연하게 여겨지는 개념과 언어의 관계를 의심하고 새로운 가능성을 "
            "탐구하는 것을 좋아합니다. 익숙한 사물을 낯선 방식으로 배치해 현실과 "
            "이미지의 관계를 질문한 마그리트와 잘 어울립니다."
        ),
        "keywords": "논리 · 질문 · 개념",
        "artwork": "이미지의 배반, 인간의 아들",
        "message": "당연하다고 생각했던 전제를 의심하는 순간 새로운 생각이 시작됩니다.",
    },

    "ESTP": {
        "name_ko": "카라바조",
        "name_en": "Caravaggio",
        "years": "1571–1610",
        "country": "이탈리아",
        "movement": "바로크",
        "emoji": "⚔️",
        "title": "극적인 순간을 강렬하게 포착하는 행동가",
        "description": (
            "ESTP는 긴장감 있는 상황에서 빠르게 판단하고 강한 존재감을 드러내는 "
            "경향이 있습니다. 명암의 극적인 대비와 현실적인 인물 표현으로 사건의 "
            "결정적 순간을 포착한 카라바조와 잘 어울립니다."
        ),
        "keywords": "대담함 · 현실감 · 순간 판단",
        "artwork": "성 마태오의 소명, 홀로페르네스의 목을 베는 유디트",
        "message": "결정적인 순간에는 과감한 선택이 강한 인상을 남깁니다.",
    },

    "ESFP": {
        "name_ko": "앙리 마티스",
        "name_en": "Henri Matisse",
        "years": "1869–1954",
        "country": "프랑스",
        "movement": "야수파",
        "emoji": "💃",
        "title": "색채와 리듬으로 즐거움을 전하는 표현가",
        "description": (
            "ESFP는 밝은 에너지와 풍부한 표현력으로 주변 사람에게 즐거움을 줍니다. "
            "대담한 색채와 자유로운 형태를 통해 생명력과 기쁨을 표현한 "
            "마티스의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "즐거움 · 표현력 · 생동감",
        "artwork": "춤, 붉은 방",
        "message": "당신의 밝은 에너지는 주변의 분위기까지 변화시킬 수 있습니다.",
    },

    "ENFP": {
        "name_ko": "마르크 샤갈",
        "name_en": "Marc Chagall",
        "years": "1887–1985",
        "country": "벨라루스 출생·프랑스 활동",
        "movement": "모더니즘·상징주의",
        "emoji": "🕊️",
        "title": "사랑과 상상으로 현실의 경계를 넘는 몽상가",
        "description": (
            "ENFP는 새로운 가능성을 상상하고 사람과 세상을 낙관적인 시선으로 "
            "바라보는 유형입니다. 연인과 동물, 고향의 기억을 환상적으로 결합한 "
            "샤갈의 자유로운 작품 세계와 잘 어울립니다."
        ),
        "keywords": "상상력 · 낙관성 · 자유",
        "artwork": "나와 마을, 생일",
        "message": "현실에 상상력을 더하면 전혀 새로운 세계를 만들 수 있습니다.",
    },

    "ENTP": {
        "name_ko": "살바도르 달리",
        "name_en": "Salvador Dalí",
        "years": "1904–1989",
        "country": "스페인",
        "movement": "초현실주의",
        "emoji": "⏳",
        "title": "상식을 뒤집는 기발한 실험가",
        "description": (
            "ENTP는 기존의 규칙을 의심하고 예상하지 못한 방식으로 아이디어를 "
            "발전시키는 것을 즐깁니다. 꿈과 무의식을 정교하면서도 기묘한 이미지로 "
            "표현한 달리의 실험적인 태도와 잘 어울립니다."
        ),
        "keywords": "발상 · 도전 · 실험",
        "artwork": "기억의 지속, 코끼리를 비추는 백조",
        "message": "엉뚱해 보이는 발상이 새로운 관점을 만드는 출발점이 될 수 있습니다.",
    },

    "ESTJ": {
        "name_ko": "자크 루이 다비드",
        "name_en": "Jacques-Louis David",
        "years": "1748–1825",
        "country": "프랑스",
        "movement": "신고전주의",
        "emoji": "🏛️",
        "title": "명확한 질서와 목표를 제시하는 지도자",
        "description": (
            "ESTJ는 분명한 기준과 목표를 세우고 사람들을 조직적으로 이끄는 데 "
            "능합니다. 엄격한 구도와 명확한 메시지를 통해 의무와 결단을 강조한 "
            "자크 루이 다비드의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "질서 · 책임 · 리더십",
        "artwork": "호라티우스 형제의 맹세, 마라의 죽음",
        "message": "분명한 기준과 실행력이 복잡한 상황을 정리하는 힘이 됩니다.",
    },

    "ESFJ": {
        "name_ko": "메리 커샛",
        "name_en": "Mary Cassatt",
        "years": "1844–1926",
        "country": "미국",
        "movement": "인상주의",
        "emoji": "🤱",
        "title": "관계 속의 애정과 돌봄을 섬세하게 그리는 화가",
        "description": (
            "ESFJ는 사람 사이의 관계를 중요하게 생각하고 애정과 관심을 적극적으로 "
            "표현합니다. 가족과 여성의 일상을 따뜻하고 세심한 시선으로 그린 "
            "메리 커샛의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "관계 · 돌봄 · 친화력",
        "artwork": "아이의 목욕, 푸른 안락의자에 앉은 어린 소녀",
        "message": "당신의 관심과 돌봄이 사람들 사이의 관계를 단단하게 만듭니다.",
    },

    "ENFJ": {
        "name_ko": "외젠 들라크루아",
        "name_en": "Eugène Delacroix",
        "years": "1798–1863",
        "country": "프랑스",
        "movement": "낭만주의",
        "emoji": "🚩",
        "title": "열정과 이상으로 사람들을 움직이는 화가",
        "description": (
            "ENFJ는 공동의 가치와 비전을 제시하고 사람들에게 용기를 불어넣는 데 "
            "강점을 보입니다. 강렬한 색채와 역동적인 구성으로 자유와 열정을 표현한 "
            "들라크루아의 작품 세계와 잘 어울립니다."
        ),
        "keywords": "열정 · 이상 · 영향력",
        "artwork": "민중을 이끄는 자유의 여신, 사르다나팔루스의 죽음",
        "message": "당신이 전하는 확신과 열정은 다른 사람을 움직이는 힘이 됩니다.",
    },

    "ENTJ": {
        "name_ko": "파블로 피카소",
        "name_en": "Pablo Picasso",
        "years": "1881–1973",
        "country": "스페인",
        "movement": "입체주의·현대미술",
        "emoji": "🔷",
        "title": "기존의 규칙을 재구성하는 혁신가",
        "description": (
            "ENTJ는 큰 목표를 세우고 기존의 체계를 과감하게 바꾸며 새로운 흐름을 "
            "만드는 데 강점을 보입니다. 전통적인 원근법과 형태를 해체하고 새로운 "
            "미술 언어를 만든 피카소와 잘 어울립니다."
        ),
        "keywords": "혁신 · 추진력 · 영향력",
        "artwork": "아비뇽의 처녀들, 게르니카",
        "message": "기존의 방식을 재구성할 때 새로운 시대를 여는 결과가 만들어집니다.",
    },
}


# =========================================================
# 화면 스타일
# 결과 내용은 Streamlit 기본 구성요소로 표시해
# HTML 태그가 그대로 노출되는 문제를 방지합니다.
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, #f6e4cf 0%, transparent 25%),
            radial-gradient(circle at 92% 12%, #dce8f5 0%, transparent 27%),
            linear-gradient(135deg, #fffaf3 0%, #f3f5f8 100%);
    }

    .block-container {
        max-width: 780px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        text-align: center;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        height: 3.2rem;
        border-radius: 14px;
        font-size: 1.05rem;
        font-weight: 700;
    }

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 제목
# =========================================================
st.title("🎨 MBTI 서양화가 매칭")

st.write(
    "MBTI를 선택하면 성격적 이미지와 어울리는 서양화가를 추천해 드립니다."
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
    "나와 어울리는 화가 찾기",
    type="primary",
)


# =========================================================
# 추천 결과
# =========================================================
if recommend_button:
    if selected_mbti == "MBTI를 선택하세요":
        st.warning("먼저 MBTI 유형을 선택해 주세요.")

    else:
        result = PAINTER_DATA[selected_mbti]

        st.balloons()
        st.divider()

        st.subheader(f"{selected_mbti}에게 어울리는 서양화가")

        # 화가를 상징하는 이모지
        st.markdown(
            f"""
            <div style="
                text-align: center;
                font-size: 100px;
                line-height: 1.2;
                margin: 10px 0;
            ">
                {result["emoji"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.header(result["name_ko"])
        st.subheader(result["name_en"])

        st.caption(
            f"{result['years']} · {result['country']} · {result['movement']}"
        )

        st.info(result["title"])

        st.write(result["description"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="추천 MBTI",
                value=selected_mbti,
            )

        with col2:
            st.metric(
                label="대표 사조",
                value=result["movement"],
            )

        st.success(f"핵심 키워드: {result['keywords']}")

        st.subheader("먼저 감상해 볼 작품")
        st.write(result["artwork"])

        st.subheader("당신에게 전하는 한마디")
        st.write(result["message"])

        with st.expander("이 화가가 추천된 기준"):
            st.write(
                f"{selected_mbti} 유형에 흔히 연결되는 성향과 "
                f"{result['name_ko']}의 작품 세계 및 창작 이미지를 "
                "재미를 위한 방식으로 연결한 결과입니다."
            )


# =========================================================
# 하단 안내
# =========================================================
st.divider()

st.caption(
    "이 결과는 재미를 위한 창작형 추천입니다. "
    "공식 MBTI 검사나 심리학적 진단을 의미하지 않습니다."
)
