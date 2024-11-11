# JustEva: Uncovering Gender Bias in Communication
- This reposotory is for the project **JustEva** which is entered to She Builds AI hackathon by Google's Women Techmakers presents. The Goal is to Develop an AI powered solution to address gender equity challenges around the world, as outlined in UN Sustainable Development Goal 5.JustEva directly supports **UN Sustainable Development Goal 5** (UN SDG 5), which strives to “achieve gender equality and empower all women and girls.” The project aims to contribute to this goal by:
- **Ending Discrimination**: JustEva brings awareness to discriminatory language and behavior in everyday interactions, enabling women and non-binary individuals to identify and address these biases.
- **Providing Emotional Support**: Through personalized podcast guidance, JustEva creates a safe space for users to process their experiences, validate their feelings, and explore actionable solutions.
- **Promoting Economic Empowerment and Leadership**: By highlighting bias in workplace interactions, JustEva empowers users to advocate for fair treatment and build resilience in professional environments.

# #About this project
**JustEva** is an innovative AI-powered platform designed to address gender bias in communication and provide emotional support to the individuals who face daily challenges navigating gendered interactions. Using Google’s **Gemini** model and **gTTS** (Google Text-to-Speech), JustEva leverages natural language processing to identify and analyze gender-based discrimination in various communication contexts. It also offers personalized emotional support through solo podcasts, creating a safe space for users to process and understand these experiences.

# #Inspiration
 
Coming from a society with strong expectations for women’s roles, I thought moving to a progressive country like Canada would mean fewer instances of  gender-based discrimination. To my surprise, these biases only took different forms, in various contexts. Biases can arise from unexpected places and may even challenge progressive intentions.

 It’s not about isolated incidents; it’s about the subtle language and assumptions that can accumulate over time, impacting self-worth and mental well-being. In a conversation about career progression, I was reminded that, as a married woman, financial concerns shouldn't trouble me. Though well-intentioned, the comment underscored how gender-based stereotypes can overshadow professional achievements, even in career-focused settings.

 My own experiences and those of my colleagues and friends have made me deeply aware of the need for tools that identify and address these biases. **JustEva** was born out of a desire to create a tool that can recognize and validate these often-overlooked biases, giving individuals the support they need to navigate these interactions confidently.

## What it does
### 1. **JustEva** is an innovative AI-powered tool designed to address gender bias in communication and provide emotional support to individuals  who face daily challenges navigating gendered interactions. 

### 2. By using AI to identify gender bias in communication—whether through text, email, or images—**JustEva** empowers people to recognize bias, understand its impact, and take actionable steps toward building mental resilience and self-assurance. 

### 3. It also offers personalized emotional support through solo podcasts, creating a safe space for users to process and understand these experiences.

## How we built it
### 1. **Bias Detection and Analysis (Gemini Multimodal Capabilities)**
JustEva uses **Gemini’s multimodal capabilities** to analyze gender bias in both **text** (e.g., written communication, emails) and **images** (e.g., screenshots of conversations, social media posts). Users can upload text snippets or images that represent interactions they suspect may contain gender bias. Gemini’s model, trained on diverse communication patterns, can detect not only overt discrimination but also subtle nuances that often go unnoticed.

### 2. **Personalized Emotional Support through Solo Podcasts (Inspired by NotebookLM)**
JustEva offers a unique **solo podcast feature** that provides personalized support based on each user’s specific situation. This feature is inspired by **NotebookLM** and leverages **gTTS** to create a personalized, empathetic solo podcast that addresses the user’s concerns, helps them process experiences, and offers actionable suggestions for navigating future challenges.

### 3.- **Realistic Storytelling**: Using prompt engineering, the podcast presents Eva as a supportive friend who shares real-life stories and solutions tailored to the user’s experiences.

### 4. **Safe and Responsible AI Implementation (Gemini Safety Settings)**
JustEva prioritizes safe and responsible use of AI, particularly in handling sensitive topics like gender bias. The **safety settings** within Gemini allow the model to filter out harmful, misleading, or inappropriate content, ensuring that users receive guidance that is respectful, accurate, and helpful.


## Challenges we ran into
### 1. **Building a Multi-Modal System**  
   Integrating both text and image analysis posed a unique challenge in prompt engineering, as the model needed to analyze context accurately. Through prompt iterations, I was able to enhance the model’s ability to process different forms of input while maintaining high relevance.
### 2. **Handling Sensitive Topics with Care**  
   Creating an AI tool for detecting gender bias required thoughtful planning to avoid unintended biases within the model itself. By configuring Gemini’s safety settings, I ensured that the tool could provide insightful analysis while remaining respectful and non-judgmental.
### 3. **Balancing Realism with Resource Constraints**  
   Generating  a two  hosts  podcast  like NotebookLM with free features of **gTTS** require significant time to process several requests to simulate generated podcast script into two  hosts  podcast .  Therefore, I designed JustEva to generate Solo podcast in a tone that the host is reading email, letter or messages from the audience. In this way we could utilize gTTS optimally.

## Accomplishments that we're proud of

- **Creating a Platform That Uplifts and Empowers**: With **JustEva**, we’ve built more than just an analytical tool. JustEva actively validates and supports individuals who may feel overlooked or misunderstood. By providing insights into subtle gender biases, it helps users navigate these interactions with confidence and resilience.

- **Contributing to UN Sustainable Development Goal 5**: We are especially proud of JustEva’s alignment with **UN SDG 5** (Gender Equality). Tackling gender bias through education, empowerment, and emotional support, JustEva goes beyond raising awareness. It empowers users to take actionable steps toward overcoming bias, fostering a healthier and more inclusive community.

- **Innovative, Cost-Effective Solo Podcast Feature**: By using a single-host podcast format, JustEva is accessible to users without requiring extensive resources, offering a scalable solution that can reach more individuals. This approach allows for realistic, story-driven support that feels personal and immediate, yet remains affordable.

- **Building a Human-Centered, Responsible AI Solution**: Beyond technical achievements, JustEva represents a thoughtful, human-centered approach to AI. Addressing sensitive topics like gender bias required careful design. This makes JustEva a trustworthy companion for users seeking validation and support in professional and social settings.

- **Setting a New Standard for AI-Driven Gender Equity Solutions**: JustEva has the potential to become a pioneering model for gender-equity-focused AI tools, promoting mental well-being and resilience for women, girls, and non-binary individuals worldwide.

We’re proud that **JustEva** aligns advanced technology responsibly, supporting individuals and contributing to a more equitable future.

## What We Learned

Building JustEva provided valuable insights into the complexities of developing an AI tool that addresses sensitive issues, requiring careful consideration and innovative solutions. Key lessons learned include:

### 1. **The Importance of Contextual Analysis**: 
Detecting subtle forms of bias required fine-tuning Gemini’s model to analyze language and context effectively. Through iterative prompt engineering, we optimized JustEva to pick up on nuanced communication cues that users might otherwise overlook.

### 2. **Balancing Realism with Practicality**: 
Developing the solo podcast feature within resource constraints taught us how to balance ambition with feasibility. We learned to leverage **gTTS** effectively, using prompt engineering to simulate a personalized solo podcast. However, this approach limits the ability to deliver an empathetic and realistic voice, which can affect the emotional depth of a single-hosted podcast.

### 3. **Addressing AI's Inherent Biases**: 
Creating a tool to detect bias involved acknowledging potential biases within the model itself. We took careful steps to ensure JustEva remains objective, respectful, and non-judgmental, understanding that this approach fosters a supportive and inclusive experience for all users. 


## What's next for JustEva
While JustEva currently analyzes uploaded content, future iterations could integrate real-time monitoring for live text inputs (e.g., during virtual meetings or email composition), providing instant feedback on potential biases to promote more equitable communication. Additionally, by incorporating audio effects or voice cloning, the solo podcast could potentially be broadcast on platforms like Spotify, offering a cost-effective way to reach a broader audience.
