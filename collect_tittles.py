import argparse
from savetoDb import create_database, save_videos_to_db
from youtube_infoParser import get_video_info


# Main script execution
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch all video titles and links from a YouTube channel and store it in a sql databse.")
    parser.add_argument('--channel_name', type=str, help='The name of the YouTube channel to scrape (e.g., "StevenWilsonHQ").')
    parser.add_argument('--db_name', type=str, default='youtube_videos.db', help='The name of the SQLite database (default: youtube_videos.db).')
    parser.add_argument('--max_videos', type=int, default=None, help='Maximum number of videos to retrieve (default: fetch all videos).')

    args = parser.parse_args()

    # Create the database and the required table
    conn, cursor = create_database(args.db_name)
    
    # Construct the channel URL
    channel_url = f"https://www.youtube.com/c/{args.channel_name}/videos"  # Channel URL construction

    # Get video info
    video_data = get_video_info(channel_url, max_videos=args.max_videos)  # Fetch specified number of videos or all
    
    # Save the collected video info to the database
    save_videos_to_db(video_data, cursor)
    
    # Close the database connection
    cursor.close()
    conn.close()

