import os
import sys

# Get video link and id
video_url = sys.argv[1]
video_id = video_url.split('=')[-1]

# Create path to save to
save_path = os.path.join("~/files/site_storage/yt", video_id[0:2], video_id[2:4], video_id[4:6])

os.system('youtube-dl \
        -ciw \
        --youtube-skip-dash-manifest \
        --output "' + save_path + '/%(id)s.%(ext)s" \
        --write-description \
        --write-info-json \
        --write-thumbnail \
        ' + video_url + ' \
        ')

print(video_url)
print(video_id)
print(save_path)