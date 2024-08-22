import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Midjourney Prompt Generator", layout="wide")

# 제목 설정
st.title("Midjourney 프롬프트 생성기 - 인물 사진")

# 옵션 정의 (원래의 상세한 옵션 유지)
options = {
    "인물 수": ["1", "2", "3", "4", "5", "small group (3-5)", "medium group (6-10)", "large group (11+)", "crowd"],
    "주인공 특징": {
        "성별": ["male", "female"],
        "인종": ["Caucasian", "African", "East Asian", "South Asian", "Southeast Asian", "Middle Eastern", "Hispanic", "Latino", "Native American", "Pacific Islander", "Mixed race", "Multiethnic", "Indigenous", "Aboriginal", "Inuit"],
        "체형": ["slim", "athletic", "muscular", "curvy", "plus-size", "petite", "tall", "short", "average", "toned", "stocky", "lanky", "pear-shaped", "hourglass", "rectangular"],
        "헤어스타일": ["short hair", "buzz cut hair", "pixie cut hair", "bob hair", "spiky hair", "slicked back hair", "medium-length hair", "wavy medium-length hair", "curly medium-length hair", "straight medium-length hair", "asymmetrical medium-length hair", "messy medium-length hair", "long hair", "wavy long hair", "curly long hair", "straight long hair", "braids (long hair)", "dreadlocks (long hair)", "cornrows (long hair)", "slicked back long hair", "mohawk hair", "undercut hair", "side-shave hair", "mullet hair", "pompadour hair", "quiff hair", "afro hair", "dyed hair", "ombre hair", "highlights in hair", "lowlights in hair", "natural hair", "graying hair"],
        "특징적 요소": ["freckles", "tattoos", "scars", "birthmarks", "moles", "dimples", "glasses", "contact lenses", "beard", "mustache", "goatee", "sideburns", "clean-shaven", "piercings", "braces", "hearing aid", "prosthetic limb", "wheelchair", "cane", "crutches", "heterochromia", "albinism", "vitiligo", "acne", "wrinkles", "makeup", "no makeup", "painted nails", "long nails", "short nails"],
        "의상": ["casual wear", "formal wear", "business attire", "sportswear", "swimwear", "evening gown", "suit and tie", "traditional costume", "uniform", "vintage clothing", "futuristic outfit", "minimalist fashion", "avant-garde fashion", "streetwear", "bohemian style", "punk style", "gothic style", "preppy style", "military-inspired", "denim on denim", "all black outfit", "colorful ensemble", "monochromatic look", "layered outfit", "haute couture", "ready-to-wear", "athleisure", "cocktail dress", "tuxedo", "red carpet look"]
    },
    "보조 인물 특징": {
        "성별": ["male", "female", "non-binary", "androgynous", "mixed", "diverse", "same as main character", "opposite of main character"],
        "관계": ["family", "friends", "colleagues", "strangers", "couples", "teacher-student", "mentor-mentee", "rivals", "teammates", "classmates", "neighbors", "roommates", "band members", "club members", "religious group", "support group", "tour group", "diverse group", "same demographic", "contrasting demographic"]
    },
    "인물 관계 및 상호작용": ["conversing", "embracing", "shaking hands", "high-fiving", "arguing", "laughing together", "working together", "competing", "teaching", "ignoring each other", "helping", "comforting", "celebrating", "dancing", "singing", "playing sports", "studying", "eating together", "cooking together", "exercising", "meditating", "performing", "protesting", "collaborating", "confronting", "reconciling", "supporting", "leading", "following", "observing"],
    "인물 배치 및 포즈": {
        "주인공 포즈": ["standing", "sitting", "lying down", "walking", "running", "jumping", "dancing", "posing", "leaning", "crouching", "kneeling", "squatting", "bending", "stretching", "twisting", "balancing", "floating", "flying", "falling", "climbing", "crawling", "reaching", "pushing", "pulling", "lifting", "throwing", "catching", "gesturing", "saluting", "meditating"],
        "보조 인물 배치": ["surrounding", "in a line", "scattered", "in the background", "in the foreground", "interacting with main character", "facing main character", "facing away from main character", "in a circle", "in rows", "in columns", "in a pyramid", "in a V-formation", "in a zigzag", "randomly positioned", "evenly spaced", "clustered", "paired", "in small groups", "forming a shape", "mirroring main character", "contrasting main character", "in motion", "static", "entering the scene", "exiting the scene", "ascending", "descending", "converging", "diverging"],
        "전체 구성": ["symmetrical", "asymmetrical", "circular", "triangular", "diamond-shaped", "s-curve", "diagonal", "horizontal", "vertical", "radial", "spiral", "grid", "rule of thirds", "golden ratio", "dynamic symmetry", "leading lines", "framing", "negative space", "minimalist", "cluttered", "layered", "juxtaposition", "balance", "rhythm", "pattern", "repetition", "contrast", "harmony", "focal point", "depth"]
    },
    "장면 설정": {
        "배경": ["urban street", "nature", "beach", "mountains", "forest", "desert", "studio", "office", "home", "restaurant", "park", "school", "gym", "concert venue", "sports stadium", "museum", "art gallery", "library", "theater", "cinema", "airport", "train station", "subway", "shopping mall", "market", "farm", "factory", "construction site", "ruins", "underwater"],
        "시간": ["dawn", "early morning", "mid-morning", "late morning", "noon", "early afternoon", "mid-afternoon", "late afternoon", "dusk", "early evening", "night", "midnight", "golden hour", "blue hour", "twilight", "sunrise", "sunset", "overcast day", "stormy day", "foggy morning", "clear night", "starry night", "full moon", "new moon", "solar eclipse", "lunar eclipse", "northern lights", "time-lapse", "slow motion", "frozen moment"],
        "날씨": ["sunny", "partly cloudy", "overcast", "rainy", "thunderstorm", "snowy", "sleet", "hail", "foggy", "misty", "hazy", "windy", "calm", "hot", "cold", "humid", "dry", "tropical", "arctic", "sandstorm", "dust storm", "tornado", "hurricane", "blizzard", "heat wave", "cold snap", "rainbow", "double rainbow", "sun shower", "clear sky"],
        "조명": ["natural light", "studio lighting", "dramatic lighting", "soft light", "hard light", "backlight", "sidelight", "rim light", "key light", "fill light", "high key", "low key", "chiaroscuro", "silhouette", "spotlight", "candlelight", "firelight", "moonlight", "starlight", "neon lights", "LED lights", "fluorescent lights", "incandescent lights", "colored gels", "light painting", "light leak", "lens flare", "golden hour light", "blue hour light", "overexposed", "underexposed"]
    },
    "구도 및 카메라 설정": {
        "앵글": ["eye level", "high angle", "low angle", "bird's eye view", "worm's eye view", "dutch angle", "over-the-shoulder", "POV (point of view)", "profile", "three-quarter view", "front view", "back view", "upshot", "downshot", "canted angle", "oblique angle", "aerial view", "underwater view", "through-the-viewfinder", "framed", "wide angle", "telephoto", "macro", "tilt-shift", "panoramic", "360-degree", "stereoscopic", "fisheye", "split-screen", "multi-angle"],
        "샷 크기": ["extreme close-up", "close-up", "medium close-up", "medium shot", "medium long shot", "long shot", "extreme long shot", "full shot", "wide shot", "establishing shot", "insert shot", "two-shot", "three-shot", "over-the-shoulder shot", "point-of-view shot", "reaction shot", "cutaway shot", "tracking shot", "dolly shot", "zoom shot", "crane shot", "steadicam shot", "handheld shot", "whip pan", "tilt shot", "rack focus", "deep focus", "shallow focus", "split focus", "forced perspective"],
        "초점": ["shallow depth of field", "deep depth of field", "selective focus", "soft focus", "tack sharp", "bokeh", "motion blur", "panning blur", "zoom blur", "radial blur", "lens blur", "gaussian blur", "defocus", "rack focus", "pull focus", "follow focus", "zone focusing", "hyperfocal distance", "focus stacking", "split focus", "tilt-shift focus", "macro focus", "infinity focus", "autofocus", "manual focus", "face detection focus", "eye detection focus", "continuous focus", "single-point focus", "multi-point focus"],
        "렌즈": ["wide-angle", "standard", "telephoto", "zoom", "prime", "fisheye", "macro", "tilt-shift", "anamorphic", "cine lens", "portrait lens", "landscape lens", "super telephoto", "ultra-wide", "pancake lens", "kit lens", "fast lens", "slow lens", "soft focus lens", "mirror lens", "rectilinear lens", "perspective control lens", "apochromatic lens", "aspherical lens", "spherical lens", "parfocal lens", "varifocal lens", "teleconverter", "extension tube", "pinhole"]
    },
    "스타일 및 후처리": {
        "스타일": ["photorealistic", "cinematic", "documentary", "fashion", "editorial", "fine art", "street photography", "portrait", "landscape", "still life", "abstract", "surrealist", "minimalist", "maximalist", "vintage", "retro", "futuristic", "noir", "high fashion", "glamour", "grunge", "ethereal", "moody", "dreamy", "gritty", "clean", "dramatic", "whimsical", "conceptual", "experimental"],
        "색감": ["vibrant", "muted", "monochrome", "black and white", "sepia", "duotone", "tritone", "pastel", "neon", "earthy", "warm", "cool", "neutral", "saturated", "desaturated", "high contrast", "low contrast", "color splash", "complementary colors", "analogous colors", "triadic colors", "tetradic colors", "split-complementary", "color grading", "cross-processing", "bleach bypass", "infrared", "cyanotype", "technicolor", "kodachrome"],
        "후처리 효과": ["film grain", "vignette", "lens flare", "light leaks", "double exposure", "multiple exposure", "HDR", "tone mapping", "sharpening", "noise reduction", "chromatic aberration", "lens distortion", "perspective correction", "barrel distortion", "pincushion distortion", "keystone correction", "dehaze", "clarity", "texture", "glow", "bloom", "halation", "film simulation", "cross-processing", "solarization", "posterization", "oil paint effect", "watercolor effect", "sketch effect", "pixelation", "glitch"]
    },
    "기술적 설정": {
        "이미지 비율": ["1:1", "4:3", "16:9", "3:2", "2:3", "1:2", "2:1", "5:4", "4:5", "7:5", "5:7", "8:5", "5:8", "9:16"],
        "모델": ["niji", "5", "5.1", "5.2", "6", "6.1"]
    }
}

# 프롬프트 생성 함수
def generate_customizable_prompt(user_inputs):
    person_count = user_inputs['인물 수']
    age = user_inputs.get('나이', '')

    # 1명일 때 프롬프트 구조
    if person_count == 1:
        gender = user_inputs.get('주인공 특징', {}).get('성별', '')
        ethnicity = user_inputs.get('주인공 특징', {}).get('인종', '')
        prompt = f"/imagine prompt: A fashion-style photograph of a {age}-year-old {gender} {ethnicity}"

        main_char_features = [value for feature, value in user_inputs.get('주인공 특징', {}).items() if feature not in ['성별', '인종']]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."

        if pose := user_inputs.get('인물 배치 및 포즈', {}).get('주인공 포즈'):
            prompt += f" The character is {pose}."
    
    # 2명일 때 프롬프트 구조
    elif person_count == 2:
        gender = user_inputs.get('주인공 특징', {}).get('성별', '')
        ethnicity = user_inputs.get('주인공 특징', {}).get('인종', '')
        prompt = f"/imagine prompt: A fashion-style photograph of 2 persons, including a {age}-year-old {gender} {ethnicity} main character"
        
        main_char_features = [value for feature, value in user_inputs.get('주인공 특징', {}).items() if feature not in ['성별', '인종']]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."
        
        supporting_features = [value for value in user_inputs.get('보조 인물 특징', {}).values() if value]
        if supporting_features:
            prompt += f" The second character is {', '.join(supporting_features)}."

        if interaction := user_inputs.get('인물 관계 및 상호작용'):
            prompt += f" The characters are {interaction}."

    # 3명 이상일 때 프롬프트 구조
    else:
        gender = user_inputs.get('주인공 특징', {}).get('성별', '')
        ethnicity = user_inputs.get('주인공 특징', {}).get('인종', '')
        prompt = f"/imagine prompt: A fashion-style photograph of {person_count} persons, with a {age}-year-old {gender} {ethnicity} main character"
        
        main_char_features = [value for feature, value in user_inputs.get('주인공 특징', {}).items() if feature not in ['성별', '인종']]
        if main_char_features:
            prompt += f" who is {', '.join(main_char_features)}."

        supporting_features = [value for value in user_inputs.get('보조 인물 특징', {}).values() if value]
        if supporting_features:
            prompt += f" Supporting characters include {', '.join(supporting_features)}."
        
        if interaction := user_inputs.get('인물 관계 및 상호작용'):
            prompt += f" The characters are {interaction}."

    # 전체 구성 및 장면 설정
    if composition := user_inputs.get('인물 배치 및 포즈', {}).get('전체 구성'):
        prompt += f" The overall composition is {composition}."

    scene_elements = []
    scene_settings = user_inputs.get('장면 설정', {})
    if background := scene_settings.get('배경'):
        scene_elements.append(f"set in {background}")
    if time := scene_settings.get('시간'):
        scene_elements.append(f"during {time}")
    if weather := scene_settings.get('날씨'):
        scene_elements.append(f"with {weather} weather")
    if lighting := scene_settings.get('조명'):
        scene_elements.append(f"illuminated by {lighting}")
    if scene_elements:
        prompt += ', '.join(scene_elements) + '. '

    # 구도 및 카메라 설정
    camera_settings = user_inputs.get('구도 및 카메라 설정', {})
    camera_elements = []
    if angle := camera_settings.get('앵글'):
        camera_elements.append(f"Shot from a {angle} angle")
    if shot_size := camera_settings.get('샷 크기'):
        camera_elements.append(f"as a {shot_size}")
    if focus := camera_settings.get('초점'):
        camera_elements.append(f"with {focus}")
    if lens := camera_settings.get('렌즈'):
        camera_elements.append(f"using a {lens} lens")
    if camera_elements:
        prompt += ', '.join(camera_elements) + '. '

    # 스타일 및 후처리
    style_elements = []
    style_settings = user_inputs.get('스타일 및 후처리', {})
    if style := style_settings.get('스타일'):
        style_elements.append(f"In {style} style")
    if color := style_settings.get('색감'):
        style_elements.append(f"with {color} colors")
    if effect := style_settings.get('후처리 효과'):
        style_elements.append(f"and {effect} effect")
    if style_elements:
        prompt += ', '.join(style_elements) + '. '

    # 기술적 설정
    tech_settings = user_inputs.get('기술적 설정', {})
    if aspect_ratio := tech_settings.get('이미지 비율'):
        prompt += f"--ar {aspect_ratio} "
    if model := tech_settings.get('모델'):
        prompt += f"--v {model}"

    return prompt.strip()

# UI 구성
st.sidebar.header("옵션 선택")

user_inputs = {}

# 인물 수 선택 (슬라이더)
user_inputs["인물 수"] = st.sidebar.slider("인물 수", 1, 20, 1, help="Select the number of persons in the image")

# 나이 선택 (슬라이더)
user_inputs['나이'] = st.sidebar.slider("나이", 0, 100, 25, help="Select the age of the main character")

# 각 옵션에 대한 선택 위젯 생성
for category, subcategories in options.items():
    if category not in ["인물 수"]:
        st.sidebar.subheader(category)
        
        if isinstance(subcategories, list):
            # 단일 선택 옵션의 경우
            col1, col2 = st.sidebar.columns([3, 1])
            with col1:
                user_inputs[category] = st.selectbox(f"Select {category}", [""] + subcategories, key=f"select_{category}")
            with col2:
                custom_input = st.text_input(f"직접 입력 ({category})", key=f"custom_{category}")
                if custom_input:
                    user_inputs[category] = custom_input
        elif isinstance(subcategories, dict):
            # 다중 선택 옵션의 경우
            user_inputs[category] = {}
            for subcategory, choices in subcategories.items():
                # 인물 수에 따라 옵션 표시
                if category == "보조 인물 특징" and user_inputs["인물 수"] == "1":
                    continue
                if category == "인물 배치 및 포즈" and subcategory == "보조 인물 배치" and user_inputs["인물 수"] == "1":
                    continue
                col1, col2 = st.sidebar.columns([3, 1])
                with col1:
                    user_inputs[category][subcategory] = st.selectbox(f"Select {subcategory}", [""] + choices, key=f"select_{category}_{subcategory}")
                with col2:
                    custom_input = st.text_input(f"직접 입력 ({subcategory})", key=f"custom_{category}_{subcategory}")
                    if custom_input:
                        user_inputs[category][subcategory] = custom_input

# 프롬프트 생성 버튼
if st.sidebar.button("프롬프트 생성", key="generate_prompt_button"):
    prompt = generate_customizable_prompt(user_inputs)
    st.session_state.generated_prompt = prompt
    st.session_state.history = st.session_state.get('history', []) + [prompt]

# 생성된 프롬프트 표시
st.header("생성된 프롬프트")
if 'generated_prompt' in st.session_state:
    st.code(st.session_state.generated_prompt, language="markdown")
    
    # 프롬프트 복사 버튼
    if st.button("프롬프트 복사", key="copy_prompt_button"):
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


