import os
from dotenv import load_dotenv
import googleapiclient.discovery


def getPlaylistDetails():
    pass


def main():
    load_dotenv()

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY =os.environ["YOUTUBE_API_KEY"] 

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=10,
        playlistId="PLUl4u3cNGP60_JNv2MmK3wkOt9syvfQWY"
    )
    response = request.execute()

    print(response)
    print(type(response))

if __name__ == "__main__":
    main()