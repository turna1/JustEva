import os
from PIL import Image
import google.generativeai as genai
import gradio as gr
from gtts import gTTS
from pydub import AudioSegment
import tempfile

# Configure Google API Key and model
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_ID = "gemini-1.5-pro-latest"
model = genai.GenerativeModel(MODEL_ID)

# System prompts
analysis_system_prompt = "You are an expert in gender studies. Analyze the following content for any signs of gender-based discrimination and suggest actionable advice."
podcast_prompt = """You are Eva, a solo podcast host focusing on gender equality topics.
- Discuss real-life scenarios involving gender-based discrimination, provide insights, and offer solutions in a conversational, storytelling style.
- Based on the analyzed text, create an engaging solo podcast as if reading stories from different victims who send you their story.
- Introduce yourself as Eva.
- Keep the conversation within 20000 characters in 60s, with a lot of emotion.
- Use short sentences suitable for speech synthesis.
- Maintain an empathetic tone.
- Include filler words like 'äh' for a natural flow.
- Avoid background music or extra words.
"""

# Model generation configuration
generation_config = genai.GenerationConfig(
    temperature=0.9,
    top_p=1.0,
    top_k=32,
    candidate_count=1,
    max_output_tokens=8192,
)

# Safety settings
safety_settings = {
    genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

# Analyze text
def analyze_text(text):
    prompt = f"{analysis_system_prompt}\nContent:\n{text}"
    response = model.generate_content(
        [prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    return response.text if response else "No response generated."

def analyze_image(image: Image.Image) -> str:
    """Analyzes the uploaded image for gender-based discrimination."""
    prompt = "Analyze this image for any instances of gender-based discrimination and provide actionable advice."
    resized_image = preprocess_image(image)  # Resize the image to the required size
    response = model.generate_content(
        [prompt, resized_image],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    return response.text if response else "No response generated."

def preprocess_image(image: Image.Image) -> Image.Image:
    """Resizes the image maintaining aspect ratio."""
    image_height = int(image.height * 512 / image.width)
    return image.resize((512, image_height))

# Generate podcast script
def generate_podcast_script(content):
    prompt = f"{podcast_prompt}\nAnalyzed content:\n{content}"
    response = model.generate_content([prompt], generation_config=generation_config)
    script = response.text if response else "Eva has no commentary at this time."
    return script

# Convert script to audio using gTTS
def text_to_speech(script):
    lines = [line.strip() for line in script.split(".") if line.strip()]  # Split by sentences for manageable TTS segments
    audio_files = []

    for line in lines:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        try:
            tts = gTTS(text=line, lang='en', tld='ca')  # Using 'com' for American accent
            tts.save(temp_file.name)
            sound = AudioSegment.from_mp3(temp_file.name)
            sound += AudioSegment.silent(duration=500)  # Add a 0.5-second pause after each sentence
            sound.export(temp_file.name, format="mp3")
            audio_files.append(temp_file.name)
        except Exception as e:
            print(f"Error generating audio for line '{line}': {e}")

    combined_audio = AudioSegment.empty()
    for file in audio_files:
        sound = AudioSegment.from_mp3(file)
        combined_audio += sound
        os.remove(file)  # Clean up temporary files

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    combined_audio.export(output_file.name, format="mp3")
    return output_file.name

# Generate and play podcast
def generate_and_play_podcast(content, content_type='text'):
    script = generate_podcast_script(content)
    return text_to_speech(script)
  


    # Example scenarios for gender discrimination analysis
example_scenarios = [
    "I once faced a situation during a team meeting where every time I tried to share my opinion, male colleagues would interrupt or talk over me. It was frustrating and made me feel like my contributions were less valued.",
    "A friend of mine shared her experience of constantly receiving feedback focused more on her demeanor rather than her actual achievements. It’s as if her accomplishments weren’t even part of the evaluation.",
    "I've noticed that male colleagues are often considered for promotions and challenging projects more frequently than women, even when female employees have similar or even better qualifications.",
    "One time, during a hiring interview, I was asked about my personal life and family plans, specifically how I would balance work with home responsibilities. It felt like my commitment to the job was being questioned just because I'm a woman.",
    "In my previous role, there was a noticeable wage discrepancy between male and female employees who held the same position and had similar experience. It was demoralizing to see this gap go unaddressed.",
    "A close friend once told me about male colleagues making inappropriate jokes and comments about her appearance and clothing. It made her feel uncomfortable, yet she felt pressured to laugh it off to fit in."
]

example_images = [["ex1.jpg"],["ex2.png"]]

css_style = """

   body, .gradio-container {
        background-color: #1c1c1e; /* Replace with your preferred color */
    }
    
    #logo {
        display: flex;
        justify-content: center;
        font-size: 3em;
        font-weight: bold;
        letter-spacing: 3px;
    }
    .letter {
        opacity: 0;
        animation: fadeIn 0.1s forwards;
    }
.letter.j { animation-delay: 0s; color:#4285F4; }  /* Blue */
.letter.u { animation-delay: 0.1s; color: #3A9CF1; }
.letter.s { animation-delay: 0.2s; color: #32B3EE; }
.letter.t { animation-delay: 0.3s; color: #2BC9EA; }
.letter.e { animation-delay: 0.4s; color: #23E0E7; }
.letter.v { animation-delay: 0.5s; color: #1BF7E4; }
.letter.a { animation-delay: 0.6s; color: #14F0B5; }  /* Greenish */

@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}
 """

# Gradio interface setup
with gr.Blocks(theme="shivi/calm_seafoam", css=css_style) as app:
    gr.HTML("""
        <div id="logo">
            <span class="letter j">J</span>
            <span class="letter u">u</span>
            <span class="letter s">s</span>
            <span class="letter t">t</span>
            <span class="letter e">E</span>
            <span class="letter v">v</span>
            <span class="letter a">a</span>
        </div>
         <h1 style="text-align: center; color:#f0f0f0;">Promotes Gender Equality in Every Conversation</h1>
         <p style="text-align: center; font-size: 16px; color: #f0f0f0;">Powered by Gemini to advocate against gender-based violence</p>
    """)
    #gr.Markdown("<h1 style='text-align: center; color: #1c;'>Promotes Gender Equality in Every Conversation</h1>")
    #gr.Markdown("<p style='text-align: center; font-size: 16px; color: #;'>Powered by Gemini to advocate against gender-based violence</p>")
    with gr.Tab("Text Analysis"):
        text_input = gr.Textbox(label="Enter Text or Select an Example", placeholder="Type here or select an example...", lines=4)
        text_output = gr.Textbox(label="Analysis Output", lines=6)
        analyze_text_btn = gr.Button("Analyze Text")
        analyze_text_btn.click(analyze_text, inputs=text_input, outputs=text_output)
        examples = gr.Examples(
            examples=example_scenarios,
            inputs=text_input,
            outputs=text_output
        )
        listen_podcast_btn = gr.Button("Listen to Eva's Solo Podcast (this may take a few minutes to generate)")
        listen_podcast_btn.click(generate_and_play_podcast, inputs=text_output, outputs=gr.Audio())

    with gr.Tab("Image Analysis"):
        image_input = gr.Image(label="Upload Image(e.g., screenshot, photos, etc.)", type="pil")
        image_output = gr.Textbox(label="Analysis Output", lines=6)
        analyze_image_btn = gr.Button("Analyze Image")
        analyze_image_btn.click(analyze_image, inputs=image_input, outputs=image_output)
        examples = gr.Examples(
            examples=example_images,
            inputs=image_input,
            outputs=image_output
        )
        listen_podcast_image_btn = gr.Button("Listen to Eva's Solo Podcast(this may take a few minutes to generate)")
        listen_podcast_image_btn.click(generate_and_play_podcast, inputs=image_output, outputs=gr.Audio())

app.launch()
