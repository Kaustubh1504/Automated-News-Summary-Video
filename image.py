from PIL import Image
import os
from moviepy.editor import *
import datetime

#setup keyword library
import nltk
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake
rake = Rake()

#bind image downloader
from bing_image_downloader import downloader

current_time = datetime.datetime.now()
time_string = current_time.strftime("%Y%m%d%H%M%S")
video_path=time_string+"video-output.mp4"

from youtube_upload.client import YoutubeUploader

def process_articles(summary):
    
    rake.extract_keywords_from_text(summary.strip())
    keywords_with_scores = rake.get_ranked_phrases_with_scores()


    search_query=" hd unsplash"
    for score, keyword in keywords_with_scores[:10]:
        # print(keyword, score)
        search_query+=keyword
        search_query+="_"

    search_query+="_upsplash"
    search_query=search_query.replace(" ","_")
    # print(search_query)
    downloader.download(search_query, limit=1,  output_dir='dataset', 
                        adult_filter_off=False, force_replace=False, timeout=60)


    #1920 1080
    image_path="dataset\\"
    image_path+=search_query
    image_path+="\\Image_1.jpg"


    # Get the current directory
    current_directory = os.getcwd()
    img_combined_path = os.path.join(current_directory, image_path)

    #resize the image
    image = Image.open(img_combined_path)
    resized_image = image.resize((1920, 1080))
    resized_image.save("resized_image.jpg")

    #get list of lines in the summary
    summary_list=summary.split(".")
    # print(summary_list)

    #insert text on each slide
    screensize = (1780,200)
    for i,line in enumerate(summary_list):
        text_clip = TextClip(txt = line,
                            size = screensize,
                            font = "Calibri",
                            color = "white",kerning=-2, interline=-1, method='caption',
                            fontsize=75,
                            )


        text_clip = text_clip.set_position('center')
        tc_width, tc_height = text_clip.size # (800, ?)

        color_clip = ColorClip(size=(tc_width+100, tc_height+50),
                            color=(128, 128, 128))

        color_clip = color_clip.set_opacity(0.6)

        final_clip = CompositeVideoClip([color_clip, text_clip])
        final_clip.save_frame("final.png")

        im_clip = ImageClip("resized_image.jpg")

        final_clip = final_clip.set_position('bottom')

        text_clip.save_frame("text.png")

        final_output = CompositeVideoClip([im_clip, final_clip])
        final_path="slides\\"
        final_path+=str(i)
        final_path+="_final_output.png"
        final_path = os.path.join(current_directory, final_path)
        final_output.save_frame(final_path)

    folder_path=os.path.join(current_directory,"slides")
    audioclip = AudioFileClip("audio.mp3")
    clips=[]

    #make video clips of each slide present in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        clip =  ImageClip(file_path).set_duration(4).set_audio(audioclip).crossfadein(1.5)
        clips.append(clip)
    video_clip = concatenate_videoclips(clips, method='compose')

    video_clip.write_videofile(video_path, fps=24, remove_temp=True, codec="libx264", audio_codec="aac")

uploader = YoutubeUploader("612920003947-ist4or9cgu7g3v3tda89ifsmv5rbrhnu.apps.googleusercontent.com","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")
uploader.authenticate()

# Video options
options = {
    "title" : "This is automatically generated news summary", # The video title
    "description" : "Awesome project", # The video description
    "tags" : ["breakingnews", "sexy", "sexy"],
    "categoryId" : "22",
    "privacyStatus" : "private", # Video privacy. Can either be "public", "private", or "unlisted"
    "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
    # "thumbnailLink" : "slideimg.jpg" # Optional. Specifies video thumbnail.
}

# upload video
uploader.upload("video-output.mp4", options) 
uploader.close()

