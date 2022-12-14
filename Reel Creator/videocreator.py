from moviepy.editor import *
import os
import shutil

import sys
sys.path.append("/Users/aryanmehra/Documents/CS Projects/Instagram-bot/scripts/")
from tojpg import convert_to_jpg
sys.path.append("/Users/aryanmehra/Documents/CS Projects/Instagram-bot/")



def create_clips(before, after):
    # Clear Photos folder and recreate it
    try:
        shutil.rmtree('Reel Creator/Photos')
    except Exception:
        pass

    os.mkdir('Reel Creator/Photos')


    # Convert before and after images to jpg and lower size
    convert_to_jpg(infile=before, outfile='Reel Creator/Photos/before.jpg')
    convert_to_jpg(infile=after, outfile="Reel Creator/Photos/after.jpg")





def create_reel():
    # Clear Reel folder and recreate it
    try:
        shutil.rmtree('Reel Creator/Reel')
    except Exception:
        pass

    os.mkdir('Reel Creator/Reel/')


    # Create reel with before and after images
    clips = [ImageClip('Reel Creator/Photos/before.jpg').set_duration(2.4) ,
            ImageClip('Reel Creator/Photos/after.jpg').set_duration(1.6)]


    before_after = concatenate_videoclips(clips, method="compose")
    
    
    black_image = (ImageClip("Reel Creator/assets/1080x1920black.jpg").set_duration(4))

    clip_background = CompositeVideoClip([black_image, before_after.set_position("center")])
    

    # Generate text clips
    txt_clips = [TextClip("Before Lightroom", fontsize = 75, color = 'white'), TextClip("After Lightroom", fontsize = 75, color = 'white')]
        
    # setting position and duration of each clip 
    formatted_txt_clips = [txt_clips[0].set_duration(2.4), 
                           txt_clips[1].set_duration(1.6)]
    
    # coming text clips
    txt_concat_clips = concatenate_videoclips(formatted_txt_clips, method="compose").set_position(("center",1700))
        
    # Overlay the text clip on the first video clip 
    reel = CompositeVideoClip([clip_background, txt_concat_clips]) 
    
    # add audio
    audioclip = AudioFileClip("Reel Creator/assets/soundeffect.mp3")
    reel = reel.set_audio(audioclip)
    reel.fps = 24
    
    # export video 
    # reel.write_videofile("Reel Creator/Reel/reel.mp4")
    reel.write_videofile("Reel Creator/Reel/reel.mp4", 
                     codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True
                     )






create_clips(
    "/Users/aryanmehra/Downloads/4V7A0377 6.21.36 PM.jpg",
    "/Users/aryanmehra/Downloads/4V7A0377-2.jpg"
)
create_reel()



# GET HASHTAGS AND POST TO INSTA

# bot.upload_video(file,caption)