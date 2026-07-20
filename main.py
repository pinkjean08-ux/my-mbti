import streamlit as st


# ---------------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="🔮",
    layout="centered",
)


# ---------------------------------------------------------
# MBTI별 포켓몬 데이터
# ---------------------------------------------------------
POKEMON_DATA = {
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢",
        "type": "물",
        "title": "신뢰할 수 있는 방어 전문가",
        "description": (
            "ISTJ는 책임감이 강하고 맡은 일을 꾸준히 완수하는 유형입니다. "
            "단단한 등껍질과 강력한 방어력을 가진 거북왕처럼, "
            "쉽게 흔들리지 않고 안정적으로 주변을 지켜줍니다."
        ),
        "keyword": "책임감 · 안정성 · 신뢰",
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "🥚",
        "type": "노말",
        "title": "따뜻한 마음을 가진 치유자",
        "description": (
            "ISFJ는 다른 사람의 필요를 세심하게 살피고 조용히 도움을 줍니다. "
            "다친 포켓몬을 돌보는 해피너스처럼, 따뜻한 배려로 주변 사람에게 "
            "안정감과 위로를 줍니다."
        ),
        "keyword": "배려 · 헌신 · 따뜻함",
    },
    "INFJ": {
        "pokemon": "루기아",
        "emoji": "🌊",
        "type": "에스퍼 · 비행",
        "title": "깊은 통찰력을 가진 수호자",
        "description": (
            "INFJ는 조용하지만 강한 신념과 통찰력을 지닌 유형입니다. "
            "깊은 바다에서 세상의 균형을 지키는 루기아처럼, "
            "겉으로 드러내지 않아도 사람과 세상의 변화를 깊이 생각합니다."
        ),
        "keyword": "통찰 · 이상 · 신념",
    },
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧬",
        "type": "에스퍼",
        "title": "독립적인 전략 설계자",
        "description": (
            "INTJ는 복잡한 문제를 분석하고 장기적인 전략을 세우는 데 능합니다. "
            "강력한 지능과 독립성을 가진 뮤츠처럼, 기존의 방식에 얽매이지 않고 "
            "자신만의 해답을 찾아갑니다."
        ),
        "keyword": "전략 · 독립성 · 분석",
    },
    "ISTP": {
        "pokemon": "루카리오",
        "emoji": "🥋",
        "type": "격투 · 강철",
        "title": "침착하고 민첩한 문제 해결사",
        "description": (
            "ISTP는 상황을 빠르게 파악하고 실용적인 방법으로 문제를 해결합니다. "
            "상대의 움직임과 파동을 감지하는 루카리오처럼, "
            "필요한 순간에 정확하고 효율적으로 행동합니다."
        ),
        "keyword": "실용성 · 민첩함 · 침착함",
    },
    "ISFP": {
        "pokemon": "님피아",
        "emoji": "🎀",
        "type": "페어리",
        "title": "부드러운 감성을 가진 평화주의자",
        "description": (
            "ISFP는 섬세한 감성과 자신만의 미적 취향을 가진 유형입니다. "
            "다정한 모습으로 갈등을 가라앉히는 님피아처럼, "
            "부드럽고 자연스러운 방식으로 주변에 평화를 가져옵니다."
        ),
        "keyword": "감성 · 조화 · 다정함",
    },
    "INFP": {
        "pokemon": "뮤",
        "emoji": "✨",
        "type": "에스퍼",
        "title": "무한한 가능성을 품은 몽상가",
        "description": (
            "INFP는 풍부한 상상력과 내면의 가치관을 중요하게 생각합니다. "
            "모든 포켓몬의 유전자를 지닌 신비로운 뮤처럼, "
            "겉으로 보이는 것보다 훨씬 다양한 가능성과 세계를 품고 있습니다."
        ),
        "keyword": "상상력 · 가치 · 가능성",
    },
    "INTP": {
        "pokemon": "후딘",
        "emoji": "🥄",
        "type": "에스퍼",
        "title": "끝없이 탐구하는 지적 탐험가",
        "description": (
            "INTP는 원리와 구조를 파악하고 새로운 아이디어를 탐구하는 것을 좋아합니다. "
            "뛰어난 두뇌를 가진 후딘처럼, 복잡한 문제도 논리적으로 분석하며 "
            "끊임없이 새로운 가능성을 생각합니다."
        ),
        "keyword": "논리 · 탐구 · 아이디어",
    },
    "ESTP": {
        "pokemon": "초염몽",
        "emoji": "🔥",
        "type": "불꽃 · 격투",
        "title": "도전을 즐기는 행동파",
        "description": (
            "ESTP는 빠른 판단력과 뛰어난 적응력으로 현장에서 능력을 발휘합니다. "
            "민첩하고 열정적으로 싸우는 초염몽처럼, "
            "새로운 도전 앞에서 주저하기보다 직접 부딪치며 해결합니다."
        ),
        "keyword": "도전 · 순발력 · 행동력",
    },
    "ESFP": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "type": "전기",
        "title": "사랑받는 분위기 메이커",
        "description": (
            "ESFP는 밝고 친근하며 현재의 즐거움을 다른 사람과 나누는 유형입니다. "
            "어디에서나 사람들의 사랑을 받는 피카츄처럼, "
            "생기 넘치는 에너지로 주변 분위기를 밝게 만듭니다."
        ),
        "keyword": "활기 · 친화력 · 즐거움",
    },
    "ENFP": {
        "pokemon": "이브이",
        "emoji": "🦊",
        "type": "노말",
        "title": "가능성이 가득한 자유로운 모험가",
        "description": (
            "ENFP는 호기심이 많고 새로운 사람과 가능성을 발견하는 것을 즐깁니다. "
            "다양한 모습으로 진화할 수 있는 이브이처럼, "
            "하나의 길에 갇히지 않고 여러 가능성을 자유롭게 탐색합니다."
        ),
        "keyword": "호기심 · 자유 · 가능성",
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "👻",
        "type": "고스트 · 독",
        "title": "재치 넘치는 아이디어 발명가",
        "description": (
            "ENTP는 새로운 아이디어와 논쟁을 즐기며 기존의 규칙을 뒤집어 봅니다. "
            "예측하기 어렵고 장난기 많은 팬텀처럼, "
            "독창적인 발상과 재치로 사람들에게 새로운 관점을 제시합니다."
        ),
        "keyword": "창의성 · 재치 · 도전",
    },
    "ESTJ": {
        "pokemon": "윈디",
        "emoji": "🦁",
        "type": "불꽃",
        "title": "믿음직한 현장 지휘관",
        "description": (
            "ESTJ는 목표와 기준을 분명히 세우고 조직을 효율적으로 이끕니다. "
            "위엄과 충성심을 갖춘 윈디처럼, 책임감을 바탕으로 앞장서서 "
            "구성원들이 목적지에 도달하도록 이끕니다."
        ),
        "keyword": "리더십 · 책임 · 추진력",
    },
    "ESFJ": {
        "pokemon": "토게키스",
        "emoji": "🕊️",
        "type": "페어리 · 비행",
        "title": "행복을 전하는 관계의 중심",
        "description": (
            "ESFJ는 사람들과의 관계를 소중히 여기고 공동체의 화합을 위해 노력합니다. "
            "평화로운 곳에 나타나 행복을 나누는 토게키스처럼, "
            "세심한 관심으로 모두가 편안한 분위기를 만듭니다."
        ),
        "keyword": "친화력 · 협력 · 화합",
    },
    "ENFJ": {
        "pokemon": "리자몽",
        "emoji": "🐉",
        "type": "불꽃 · 비행",
        "title": "사람들의 성장을 이끄는 리더",
        "description": (
            "ENFJ는 사람의 가능성을 발견하고 공동의 목표를 향해 이끄는 데 능합니다. "
            "강한 존재감과 따뜻한 불꽃을 가진 리자몽처럼, "
            "열정과 격려를 통해 다른 사람의 성장을 돕습니다."
        ),
        "keyword": "영감 · 리더십 · 열정",
    },
    "ENTJ": {
        "pokemon": "망나뇽",
        "emoji": "🐲",
        "type": "드래곤 · 비행",
        "title": "목표를 현실로 만드는 지휘관",
        "description": (
            "ENTJ는 큰 목표를 세우고 필요한 자원과 사람을 조직하여 결과를 만들어냅니다. "
            "강력한 힘과 넓은 활동 영역을 가진 망나뇽처럼, "
            "도전적인 상황에서도 자신감을 가지고 목표를 향해 나아갑니다."
        ),
        "keyword": "목표 · 전략 · 추진력",
    },
}


# ---------------------------------------------------------
# 화면 디자인
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 15% 15%, #fff1a8 0%, transparent 25%),
                radial-gradient(circle at 85% 20%, #d9ccff 0%, transparent 28%),
                linear-gradient(135deg, #fffaf0 0%, #f5f1ff 100%);
        }

        .main-title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: 800;
            margin-top: 1rem;
            margin-bottom: 0.4rem;
            color: #28243f;
        }

        .sub-title {
            text-align: center;
            font-size: 1.05rem;
            color: #625d75;
            margin-bottom: 2rem;
        }

        .result-card {
            background-color: rgba(255, 255, 255, 0.92);
            border: 2px solid #7867d9;
            border-radius: 24px;
            padding: 28px;
            margin-top: 24px;
            box-shadow: 0 12px 30px rgba(72, 57, 135, 0.15);
            text-align: center;
        }

        .pokemon-emoji {
            font-size: 5rem;
            line-height: 1.2;
        }

        .pokemon-name {
            font-size: 2.2rem;
            font-weight: 800;
            color: #342c68;
            margin-top: 8px;
        }

        .pokemon-type {
            display: inline-block;
            background-color: #eeeaff;
            color: #51459b;
            border-radius: 999px;
            padding: 6px 14px;
            margin-top: 6px;
            font-weight: 700;
        }

        .result-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #413a5c;
            margin-top: 20px;
        }

        .result-description {
            font-size: 1rem;
            line-height: 1.8;
            color: #514d5e;
            margin: 14px auto;
            max-width: 620px;
        }

        .keyword-box {
            background-color: #fff4cc;
            border-radius: 14px;
            padding: 12px;
            margin-top: 18px;
            color: #68551d;
            font-weight: 700;
        }

        .notice {
            text-align: center;
            color: #777184;
            font-size: 0.85rem;
            margin-top: 32px;
        }

        div[data-testid="stButton"] > button {
            width: 100%;
            border-radius: 14px;
            height: 3.2rem;
            font-size: 1.05rem;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# 앱 본문
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🔮 MBTI 포켓몬 연구소</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-title">MBTI를 선택하면 당신과 닮은 포켓몬을 추천해 드립니다.</div>',
    unsafe_allow_html=True,
)

mbti_list = list(POKEMON_DATA.keys())

selected_mbti = st.selectbox(
    "나의 MBTI를 선택하세요",
    options=mbti_list,
    index=None,
    placeholder="MBTI 유형을 선택해 주세요",
)

recommend_button = st.button(
    "나와 어울리는 포켓몬 찾기",
    type="primary",
)


# ---------------------------------------------------------
# 추천 결과
# ---------------------------------------------------------
if recommend_button:
    if selected_mbti is None:
        st.warning("먼저 MBTI 유형을 선택해 주세요.")
    else:
        result = POKEMON_DATA[selected_mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="result-card">
                <div class="pokemon-emoji">{result["emoji"]}</div>

                <div class="pokemon-name">
                    {selected_mbti}에게 어울리는 포켓몬은<br>
                    {result["pokemon"]}!
                </div>

                <div class="pokemon-type">
                    타입: {result["type"]}
                </div>

                <div class="result-title">
                    {result["title"]}
                </div>

                <div class="result-description">
                    {result["description"]}
                </div>

                <div class="keyword-box">
                    핵심 키워드: {result["keyword"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="notice">
        이 추천 결과는 재미를 위한 것으로, 공식 MBTI 검사나 심리학적 진단이 아닙니다.
    </div>
    """,
    unsafe_allow_html=True,
)
