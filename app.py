from flask import Flask, render_template, request, redirect, url_for
from markov_generator import MarkovGenerator
import os

app = Flask(__name__)

script_dir = os.path.dirname(os.path.realpath(__file__))

# Process the song lyrics for each artist when the application starts
generators = {
    'taylor_swift': MarkovGenerator(order=1),
    'drake': MarkovGenerator(order=1),
}
for artist in generators:
    file_path = os.path.join(script_dir, f'data/songs/{artist}')
    generators[artist].process_directory(file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        artist = request.form.get('artist')
        if artist in generators:
            return redirect(url_for(artist))
    return render_template('home.html')

@app.route('/taylor_swift')
def taylor_swift():
    image = "https://c4.wallpaperflare.com/wallpaper/954/946/470/taylor-swift-4k-mtv-video-music-awards-2017-wallpaper-preview.jpg"
    lyrics = generators['taylor_swift'].generate_lyrics(num_lines=6)
    lyrics_html = lyrics.replace('\n', '<br>')
    return render_template('lyrics.html', lyrics=lyrics_html, image=image)

@app.route('/drake')
def drake():
    image = "https://doubletoasted.com/wp-content/uploads/2015/12/drake-hd-desktop-wallpaper-1080p-hdwallwide.com_.jpg"
    lyrics = generators['drake'].generate_lyrics(num_lines=8)
    lyrics_html = lyrics.replace('\n', '<br>')
    return render_template('lyrics.html', lyrics=lyrics_html, image=image)

if __name__ == '__main__':
    app.run(debug=True)
