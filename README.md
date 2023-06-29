# Real-time News Summary and Video Generation

This project is designed to generate automatic news summaries and convert them into video slides using the latest news articles obtained from the News API. The generated video slides are then combined into a final video using the MoviePy library, and audio is added to enhance the viewing experience.

## Project Workflow

1. **News Retrieval**: The project starts by fetching the latest news articles using the News API. The news articles are selected based on specific criteria or categories.

2. **Text Extraction**: The project utilizes the Newspaper API to extract the main text content from the selected news articles. The extracted text is then processed to generate a concise news summary.

3. **Keyword Extraction**: The extracted news summary is further processed using the RAKE-NLTK library to extract relevant keywords. These keywords are utilized to search for relevant images using the Bing Image Downloader.

4. **Image Processing**: The downloaded images are resized and combined with the news summary text to generate individual video slides. Each slide contains a snippet of the news summary with an overlaid image as the background.

5. **Video Generation**: The individual video slides are combined into a final video using the MoviePy library. The slides are arranged in chronological order, and transitions are added between slides to create a smooth visual flow.

6. **Audio Addition**: An audio clip, such as a background music track or a voice-over narration, is added to the final video to enhance the viewing experience. The audio clip can be customized based on the project requirements.

7. **Video Upload**: The generated video is uploaded to YouTube using the YouTube Data API. The video can be assigned a title, description, tags, category, and privacy settings. This allows for easy sharing and distribution of the news summary video.

## Project Dependencies

The project relies on the following libraries and APIs:

- Python: The primary programming language used for development.
- Newspaper API: Used for extracting the main text content from news articles.
- News API: Provides access to the latest news articles.
- MoviePy: Used for video editing and generation.
- Bing Image Downloader: Enables image retrieval based on relevant keywords.
- RAKE-NLTK: Used for keyword extraction from the news summary.
- YouTube Data API: Allows for uploading the generated video to YouTube.

## Usage Instructions

To use this project, follow these steps:

1. Set up the required dependencies by installing the necessary Python libraries and APIs mentioned above.

2. Obtain API keys for the Newspaper API, News API, and YouTube Data API. Make sure to replace the placeholders in the code with your actual API keys.

3. Configure the project parameters, such as the news source, categories, and video options, according to your preferences.

4. Run the code, which will retrieve the latest news articles, generate a news summary, download relevant images, create video slides, add audio, and generate the final video.

5. Once the video is generated, it will be automatically uploaded to YouTube. You can customize the video title, description, tags, category, and privacy settings in the code.

6. Access the generated video on YouTube and share it with your desired audience.

Note: Ensure that you comply with the terms and conditions of the APIs and platforms used in this project.

## Acknowledgments

This project utilizes various open-source libraries and APIs. We would like to acknowledge the developers and contributors of the following:

- Newspaper API: https://github.com/codelucas/newspaper
- News API: https://newsapi.org/
- MoviePy: https://zulko.github.io/moviepy/
- Bing Image Downloader: https://github.com/gurugaurav/bing_image_downloader
- RAKE-NLTK: https://github.com/csurfer/rake

-nltk
- YouTube Data API: https://developers.google.com/youtube/v3
