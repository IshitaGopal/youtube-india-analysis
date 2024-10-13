import yt_dlp
from googleapiclient.discovery import build
# quotos for API: https://developers.google.com/youtube/v3/getting-started#quota

def get_video_info(channel_url, max_videos=None):
    """Fetches video titles and URLs from a YouTube channel using yt-dlp.
    
    param:channel_id:channel_url (str): The URL of the YouTube channel/playlist to scrape.
    param:max_videos (int, optional): Maximum number of videos to retrieve. If None, fetches all videos
    returns:list of dict with title and video url
    """
    # yt-dlp options
    ydl_opts = {
        'quiet': True,  # Suppresses yt-dlp console output
        'extract_flat': True,  # Extract only metadata, no media download
        'playlistend': max_videos if max_videos else None,  # fetch all if not specified
    }

    # Use yt-dlp to extract video information without downloading
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)  # Extract metadata from the channel
        
        video_info = []  
        for entry in info['entries']:
            video_info.append({
                'title': entry['title'],  # Extract video title
                'url': entry['url']  # Extract video URL
            })

    return video_info  

#Example use 
#channel_url = 'https://www.youtube.com/@IndianNationalCongress/videos'
#video_info_list = get_video_info(channel_url)

# Function to initialize YouTube API
def get_youtube_service(api_key):
    """Initialize the YouTube API service."""
    return build('youtube', 'v3', developerKey=api_key)
    

# Function to fetch video metadata
def get_video_metadata(video_id, youtube):
    """Fetch video metadata such as description, likes, views, and duration using YouTube Data API.
        param:video_id (str): The ID of the YouTube video.
        param:youtube (googleapiclient.discovery.Resource): YouTube API service object.
        returns:dict: A dictionary containing video metadata.
    """
    
    request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=video_id
        )
    response = request.execute()
    
    video = response['items'][0]
        
    metadata = {
            'id': video['id'],
            'publishedAt':video['snippet']['publishedAt'],
            'channelId':video['snippet']['channelId'],
            'description': video['snippet']['description'],
            'likes': video['statistics'].get('likeCount', 'Not available'),
            'dislikes': video['statistics'].get('dislikeCount', 'Not available'),
            'views': video['statistics'].get('viewCount', 'Not available'),
            'favorites':video['statistics'].get('favoriteCount', 'Not available'),
            'comments':video['statistics'].get('commentCount', 'Not available'),
            'duration': video['contentDetails']['duration'],  # Format like PT5M20S
            'thumbnail':video['snippet']['thumbnails'].get('standard', {}).get('url', 'No standard thumbnail available')
            
        }
        
    return metadata
        

# Example use 
# youtube = get_youtube_service('Replace_with_API_key')
# link = 'https://www.youtube.com/watch?v=B6bF6oKJKKQ'
# get_video_metadata('B6bF6oKJKKQ', youtube)





