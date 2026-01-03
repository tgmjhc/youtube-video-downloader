"""
VidExtract Backend Server
A simple Flask server that handles YouTube video downloads using yt-dlp
"""

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import yt_dlp
import requests
from urllib.parse import unquote

app = Flask(__name__)
CORS(app)

YDL_OPTS = {
    'format': 'best',
    'quiet': True,
    'no_warnings': True,
    'extract_flat': False,
}

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'online'}), 200

@app.route('/download', methods=['POST'])
def download_video():
    """Extract video info and formats"""
    try:
        data = request.get_json()
        video_url = data.get('url')
        requested_quality = data.get('quality', '1080')
        
        if not video_url:
            return jsonify({'error': 'No URL provided'}), 400
        
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            video_data = {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'channel': info.get('uploader', 'Unknown'),
                'thumbnail': info.get('thumbnail', ''),
                'formats': [],
                'audio_url': None
            }
            
            video_formats = []
            audio_format = None
            
            for fmt in info.get('formats', []):
                if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none':
                    height = fmt.get('height', 0)
                    if height > 0:
                        video_formats.append({
                            'quality': f"{height}p",
                            'height': height,
                            'url': fmt.get('url'),
                            'ext': fmt.get('ext', 'mp4'),
                            'filesize': fmt.get('filesize', 0),
                            'fps': fmt.get('fps', 0)
                        })
                
                if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':
                    if not audio_format or (fmt.get('abr', 0) > audio_format.get('abr', 0)):
                        audio_format = fmt
            
            video_formats.sort(key=lambda x: x['height'], reverse=True)
            video_data['formats'] = video_formats[:6]
            
            if audio_format:
                video_data['audio_url'] = audio_format.get('url')
            
            return jsonify(video_data), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stream', methods=['GET'])
def stream_video():
    """Stream video for download"""
    try:
        video_url = request.args.get('url')
        title = request.args.get('title', 'video.mp4')
        
        if not video_url:
            return jsonify({'error': 'No URL'}), 400
        
        video_url = unquote(video_url)
        r = requests.get(video_url, stream=True)
        
        def generate():
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk
        
        return Response(
            generate(),
            headers={
                'Content-Disposition': f'attachment; filename="{title}"',
                'Content-Type': r.headers.get('Content-Type', 'video/mp4')
            }
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("VidExtract Backend - Running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
