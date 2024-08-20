import streamlit as st
import json

# JSON 파일 로드
with open('option_translation.json', 'r', encoding='utf-8') as f:
    option_translation = json.load(f)

# 페이지 설정
st.set_page_config(page_title="Midjourney Prompt Generator", layout="wide")

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0

# 프롬프트 생성 함수 (기존 코드 유지)
def generate_customizable_prompt(user_inputs):
    person_count = user_inputs['인물 수']
    age = user_inputs.get('나이', '')

    # 1명일 때 프롬프트 구조
    if person_count == 1:
        gender = option_translation['주인공 특징']['성별'].get(user_inputs.get('주인공 특징', {}).get('성별', ''), '')
        ethnicity = option_translation['주인공 특징']['인종'].get(user_inputs.get('주인공 특징', {}).get('인종', ''), '')
        prompt = f"/imagine prompt: A fashion-style photograph of a {age}-year-old {gender} {ethnicity}"

        main_char_features = [option_translation['주인공 특징'][feature].get(value, value) 
                              for feature, value in user_inputs.get('주인공 특징', {}).items() 
                              if feature not in ['성별', '인종'] and value]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."

        if pose := option_translation['인물 배치 및 포즈']['주인공 포즈'].get(user_inputs.get('인물 배치 및 포즈', {}).get('주인공 포즈', ''), ''):
            prompt += f" The character is {pose}."
    
    # 2명일 때 프롬프트 구조
    elif person_count == 2:
        gender = option_translation['주인공 특징']['성별'].get(user_inputs.get('주인공 특징', {}).get('성별', ''), '')
        ethnicity = option_translation['주인공 특징']['인종'].get(user_inputs.get('주인공 특징', {}).get('인종', ''), '')
        prompt = f"/imagine prompt: A fashion-style photograph of 2 persons, including a {age}-year-old {gender} {ethnicity} main character"
        
        main_char_features = [option_translation['주인공 특징'][feature].get(value, value) 
                              for feature, value in user_inputs.get('주인공 특징', {}).items() 
                              if feature not in ['성별', '인종'] and value]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."
        
        supporting_features = [option_translation['보조 인물 특징'][feature].get(value, value) 
                               for feature, value in user_inputs.get('보조 인물 특징', {}).items() if value]
        if supporting_features:
            prompt += f" The second character is {', '.join(supporting_features)}."

        if interaction := option_translation['인물 관계 및 상호작용'].get(user_inputs.get('인물 관계 및 상호작용', ''), ''):
            prompt += f" The characters are {interaction}."

    # 3명 이상일 때 프롬프트 구조
    else:
        gender = option_translation['주인공 특징']['성별'].get(user_inputs.get('주인공 특징', {}).get('성별', ''), '')
        ethnicity = option_translation['주인공 특징']['인종'].get(user_inputs.get('주인공 특징', {}).get('인종', ''), '')
        prompt = f"/imagine prompt: A fashion-style photograph of {person_count} persons, with a {age}-year-old {gender} {ethnicity} main character"
        
        main_char_features = [option_translation['주인공 특징'][feature].get(value, value) 
                              for feature, value in user_inputs.get('주인공 특징', {}).items() 
                              if feature not in ['성별', '인종'] and value]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."

        supporting_features = [option_translation['보조 인물 특징'][feature].get(value, value) 
                               for feature, value in user_inputs.get('보조 인물 특징', {}).items() if value]
        if supporting_features:
            prompt += f" Supporting characters include {', '.join(supporting_features)}."
        
        if interaction := option_translation['인물 관계 및 상호작용'].get(user_inputs.get('인물 관계 및 상호작용', ''), ''):
            prompt += f" The characters are {interaction}."

    # 전체 구성 및 장면 설정
    if composition := option_translation['인물 배치 및 포즈']['전체 구성'].get(user_inputs.get('인물 배치 및 포즈', {}).get('전체 구성', ''), ''):
        prompt += f" The overall composition is {composition}."

    scene_elements = []
    scene_settings = user_inputs.get('장면 설정', {})
    if background := option_translation['장면 설정']['배경'].get(scene_settings.get('배경', ''), ''):
        scene_elements.append(f"set in {background}")
    if time := option_translation['장면 설정']['시간'].get(scene_settings.get('시간', ''), ''):
        scene_elements.append(f"during {time}")
    if weather := option_translation['장면 설정']['날씨'].get(scene_settings.get('날씨', ''), ''):
        scene_elements.append(f"with {weather} weather")
    if lighting := option_translation['장면 설정']['조명'].get(scene_settings.get('조명', ''), ''):
        scene_elements.append(f"illuminated by {lighting}")
    if scene_elements:
        prompt += ', '.join(scene_elements) + '. '

    # 구도 및 카메라 설정
    camera_settings = user_inputs.get('구도 및 카메라 설정', {})
    camera_elements = []
    if angle := option_translation['구도 및 카메라 설정']['앵글'].get(camera_settings.get('앵글', ''), ''):
        camera_elements.append(f"Shot from a {angle} angle")
    if shot_size := option_translation['구도 및 카메라 설정']['샷 크기'].get(camera_settings.get('샷 크기', ''), ''):
        camera_elements.append(f"as a {shot_size}")
    if focus := option_translation['구도 및 카메라 설정']['초점'].get(camera_settings.get('초점', ''), ''):
        camera_elements.append(f"with {focus}")
    if lens := option_translation['구도 및 카메라 설정']['렌즈'].get(camera_settings.get('렌즈', ''), ''):
        camera_elements.append(f"using a {lens} lens")
    if camera_elements:
        prompt += ', '.join(camera_elements) + '. '

    # 스타일 및 후처리
    style_elements = []
    style_settings = user_inputs.get('스타일 및 후처리', {})
    if style := option_translation['스타일 및 후처리']['스타일'].get(style_settings.get('스타일', ''), ''):
        style_elements.append(f"In {style} style")
    if color := option_translation['스타일 및 후처리']['색감'].get(style_settings.get('색감', ''), ''):
        style_elements.append(f"with {color} colors")
    if effect := option_translation['스타일 및 후처리']['후처리 효과'].get(style_settings.get('후처리 효과', ''), ''):
        style_elements.append(f"and {effect} effect")
    if style_elements:
        prompt += ', '.join(style_elements) + '. '

    # 기술적 설정
    tech_settings = user_inputs.get('기술적 설정', {})
    if aspect_ratio := option_translation['기술적 설정']['이미지 비율'].get(tech_settings.get('이미지 비율', ''), ''):
        prompt += f"--ar {aspect_ratio} "
    if model := option_translation['기술적 설정']['모델'].get(tech_settings.get('모델', ''), ''):
        prompt += f"--v {model}"

    return prompt.strip()

# 단계별 UI 구성
st.sidebar.header("옵션 선택")

user_inputs = {}

steps = [
    {"name": "주인공 특징", "options": ["인물 수", "나이", "성별", "인종"]},
    {"name": "보조 인물 특징", "options": ["보조 인물 수", "보조 인물 나이", "보조 인물 성별"]},
    {"name": "장면 설정", "options": ["배경", "시간", "날씨", "조명"]},
    {"name": "구도 및 카메라 설정", "options": ["앵글", "샷 크기", "초점", "렌즈"]},
    {"name": "스타일 및 후처리", "options": ["스타일", "색감", "후처리 효과"]},
    {"name": "기술적 설정", "options": ["이미지 비율", "모델"]}
]

st.sidebar.write(f"Step {st.session_state.step + 1}: {steps[st.session_state.step]['name']}")

for option in steps[st.session_state.step]['options']:
    if option in option_translation:
        selected = st.sidebar.selectbox(f"Select {option}", [""] + list(option_translation[option].keys()))
        if selected:
            user_inputs[option] = selected
    else:
        for category, subcategories in option_translation.items():
            if option in subcategories:
                selected = st.sidebar.selectbox(f"Select {option}", [""] + list(subcategories[option].keys()))
                if selected:
                    if category not in user_inputs:
                        user_inputs[category] = {}
                    user_inputs[category][option] = selected
                break

col1, col2, col3 = st.sidebar.columns(3)

with col1:
    if st.button("이전") and st.session_state.step > 0:
        st.session_state.step -= 1
        st.rerun()

with col3:
    if st.button("다음") and st.session_state.step < len(steps) - 1:
        st.session_state.step += 1
        st.rerun()

# 프롬프트 생성 버튼
if st.sidebar.button("프롬프트 생성"):
    prompt = generate_customizable_prompt(user_inputs)
    st.session_state.generated_prompt = prompt
    st.session_state.history = st.session_state.get('history', []) + [prompt]

# 생성된 프롬프트 표시
st.header("생성된 프롬프트")
if 'generated_prompt' in st.session_state:
    st.code(st.session_state.generated_prompt, language="markdown")
    
    # 프롬프트 복사 버튼
    if st.button("프롬프트 복사"):
        st.write("프롬프트가 클립보드에 복사되었습니다!")
        st.markdown(f"<textarea style='position:absolute;left:-9999px'>{st.session_state.generated_prompt}</textarea>", unsafe_allow_html=True)
        st.markdown(f"<script>navigator.clipboard.writeText('{st.session_state.generated_prompt}')</script>", unsafe_allow_html=True)

# 프롬프트 생성 히스토리 표시
st.header("프롬프트 생성 히스토리")
if 'history' in st.session_state:
    for i, hist_prompt in enumerate(reversed(st.session_state.history), 1):
        st.code(hist_prompt, language="markdown")

# 프롬프트 예시 표시
st.header("프롬프트 예시")
example_prompts = [
    "A photograph of 1 female, 25 years old, East Asian. The main character is athletic, with medium-length hair. The main character is posing. Set in urban street during golden hour with sunny weather illuminated by natural light. Shot from eye level as a medium shot with shallow depth of field using a standard lens. In photorealistic style with vibrant colors and film grain effect. --ar 16:9 --v 6.1",
    "A photograph of 2 persons. The main character is male, 40 years old, Caucasian. The main character is muscular, with short hair and beard. The main character is standing. With female young adult supporting characters. The characters are embracing. Supporting characters are in the foreground. The overall composition is triangular. Set in beach during sunset with cloudy weather illuminated by golden hour light. Shot from low angle as a full shot with deep depth of field using a wide-angle lens. In cinematic style with high contrast colors and lens flare effect. --ar 2.35:1 --v 6.1",
    "A photograph of small group (3-5) persons. The main character is non-binary, 17 years old, Mixed race. The main character is slim, with dyed hair and piercings. The main character is sitting. With mixed ages diverse group supporting characters. The characters are laughing together. Supporting characters are scattered. The overall composition is circular. Set in park during daytime with sunny weather illuminated by natural light. Shot from dutch angle as a long shot with selective focus using a telephoto lens. In documentary style with muted colors and vignette effect. --ar 3:2 --v 6.1"
]
for example in example_prompts:
    st.markdown(f"- `{example}`")
