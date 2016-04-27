# Import the modules
from googleapiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDB41nojBDn1q85V-HLVOj8oxpo9UQIZ7Y"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    type="video",
    location=options.location,
    locationRadius=options.location_radius,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  search_videos = []

  # Merge video ids
  for search_result in search_response.get("items", []):
    search_videos.append(search_result["id"]["videoId"])
  video_ids = ",".join(search_videos)

  # Call the videos.list method to retrieve location details for each video.
  video_response = youtube.videos().list(
    id=video_ids,
    part='snippet, recordingDetails'
  ).execute()

  videos = []

  # Add each result to the list, and then display the list of matching videos.
  for video_result in video_response.get("items", []):
    videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
                              video_result["recordingDetails"]["location"]["latitude"],
                              video_result["recordingDetails"]["location"]["longitude"]))

  print "Videos:\n", "\n".join(videos), "\n"


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--location", help="Location", default="37.42307,-122.08427")
  argparser.add_argument("--location-radius", help="Location radius", default="5km")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

"""import requests
import json

# Make it a bit prettier..
print ("-" * 30)
print ("This will show the Most Popular Videos on YouTube")
print ("-" * 30)

# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc").json()
r.text

# Convert it to a Python dictionary   
data = json.loads(r)

# Loop through the result. 
for item in data['data']['items']:

    print ("Video Title: %s" % (item['title']))

    print ("Video Category: %s" % (item['category']))

    print ("Video ID: %s" % (item['id']))

    print ("Video Rating: %f" % (item['rating']))

    print ("Embed URL: %s" % (item['player']['default']))

"""
