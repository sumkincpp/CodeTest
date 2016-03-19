#list devices

$ ffmpeg -f avfoundation -list_devices true -i ''
ffmpeg version 3.0 Copyright (c) 2000-2016 the FFmpeg developers
  built with Apple LLVM version 7.0.2 (clang-700.1.81)
  configuration: --prefix=/usr/local/Cellar/ffmpeg/3.0 --enable-shared --enable-pthreads --enable-gpl --enable-version3 --enable-hardcoded-tables --enable-avresample --cc=clang --host-cflags= --host-ldflags= --enable-opencl --enable-libx264 --enable-libmp3lame --enable-libxvid --enable-vda
  libavutil      55. 17.103 / 55. 17.103
  libavcodec     57. 24.102 / 57. 24.102
  libavformat    57. 25.100 / 57. 25.100
  libavdevice    57.  0.101 / 57.  0.101
  libavfilter     6. 31.100 /  6. 31.100
  libavresample   3.  0.  0 /  3.  0.  0
  libswscale      4.  0.100 /  4.  0.100
  libswresample   2.  0.101 /  2.  0.101
  libpostproc    54.  0.100 / 54.  0.100
[AVFoundation input device @ 0x7f95fa4038e0] AVFoundation video devices:
[AVFoundation input device @ 0x7f95fa4038e0] [0] FaceTime HD Camera (Built-in)
[AVFoundation input device @ 0x7f95fa4038e0] [1] Capture screen 0
[AVFoundation input device @ 0x7f95fa4038e0] AVFoundation audio devices:
[AVFoundation input device @ 0x7f95fa4038e0] [0] Built-in Microphone
[AVFoundation input device @ 0x7f95fa4038e0] [1] BoomDevice
: Input/output error

$ ffmpeg -f qtkit -list_devices true -i ""
ffmpeg version 3.0 Copyright (c) 2000-2016 the FFmpeg developers
  built with Apple LLVM version 7.0.2 (clang-700.1.81)
  configuration: --prefix=/usr/local/Cellar/ffmpeg/3.0 --enable-shared --enable-pthreads --enable-gpl --enable-version3 --enable-hardcoded-tables --enable-avresample --cc=clang --host-cflags= --host-ldflags= --enable-opencl --enable-libx264 --enable-libmp3lame --enable-libxvid --enable-vda
  libavutil      55. 17.103 / 55. 17.103
  libavcodec     57. 24.102 / 57. 24.102
  libavformat    57. 25.100 / 57. 25.100
  libavdevice    57.  0.101 / 57.  0.101
  libavfilter     6. 31.100 /  6. 31.100
  libavresample   3.  0.  0 /  3.  0.  0
  libswscale      4.  0.100 /  4.  0.100
  libswresample   2.  0.101 /  2.  0.101
  libpostproc    54.  0.100 / 54.  0.100
[QTKit input device @ 0x7f8cb2d002a0] QTKit video devices:
[QTKit input device @ 0x7f8cb2d002a0] [0] FaceTime HD Camera (Built-in)
: Input/output error
