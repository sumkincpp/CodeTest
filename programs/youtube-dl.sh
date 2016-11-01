# Subtitles
#--------------------------------------------------------------------
# --write-sub                      Write subtitle file
# --write-auto-sub                 Write automatic subtitle file (YouTube only)
# --all-subs                       Download all the available subtitles of the video
# --list-subs                      List all available subtitles for the video
# --sub-format FORMAT              Subtitle format, accepts formats preference, for example: "srt" or "ass/srt/best"
# --sub-lang LANGS                 Languages of the subtitles to download (optional) separated by commas, use IETF language tags like 'en,pt'
youtube-dl --list-subs URL
youtube-dl --all-subs --skip-download URL
youtube-dl --skip-download --write-srt --sub-lang en URL
#--------------------------------------------------------------------
