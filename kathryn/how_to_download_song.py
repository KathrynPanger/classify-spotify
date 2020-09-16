#How to download a song

#########################
#enter song urls in a loop
##########################
song_url = 'https://p.scdn.co/mp3-preview/d1223866cfaf80d5644fa53eb84a7d0c8cd3f9ac?cid=577c3414ccf54576a289735f10e3ee13'
  
# URL of the song to be downloaded is defined as song_url) 
r = requests.get(song_url) # create HTTP response object 
  
# send a HTTP request to the server and save 
# the HTTP response in a response object called r 
#NOTE: We will want to label each song with real title as part of our loop
with open("first_song.mp3",'wb') as f:  
  
    # Saving received content as a png file in 
    # binary format 
  
    # write the contents of the response (r.content) 
    # to a new file in binary mode. 
    f.write(r.content) 