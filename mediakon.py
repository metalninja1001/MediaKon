import argparse
import subprocess

def opus_to_mp3(input_file, output_file):
    subprocess.run(['ffmpeg', '-i', input_file, output_file])

def display_supported_formats():
    print("Supported File Extensions:")
    print("1. Video Formats:")
    print("   - .mp4")
    print("   - .avi")
    print("   - .mkv")
    print("   - .wmv")
    print("   - .flv")
    print("   - .mpeg")
    print("   - .mpg")
    print("   - .webm")
    print("   - .3gp")
    print("   - .m4v")
    # Add the rest of the video formats

    print("2. Audio Formats:")
    print("   - .mp3")
    print("   - .wav")
    print("   - .aac")
    print("   - .flac")
    print("   - .ogg")
    print("   - .wma")
    print("   - .m4a")
    print("   - ..opus")
    # Add the rest of the audio formats

    print("3. Image Formats:")
    print("   - .jpg")
    print("   - .png")
    print("   - .gif")
    print("   - .bmp")
    print("   - .tiff")
    print("   - .svg")
    # Add the rest of the image formats

    print("4. Container Formats:")
    print("   - .mov")
    print("   - .mp4")
    print("   - .avi")
    print("   - .mkv")
    print("   - .flv")
    print("   - .webm")
    print("   - .mpeg")
    print("   - .mpg")
    print("   - .ts")
    print("   - .m2ts")
    # Add the rest of the container formats

    print("5. Subtitle Formats:")
    print("   - .srt (SubRip)")
    print("   - .ass (Advanced SubStation Alpha)")
    print("   - .ssa (SubStation Alpha)")
    print("   - .vtt (WebVTT)")
    print("   - .sub (MicroDVD)")
    print("   - .sbv (YouTube)")
    print("   - .smi/.sami (SAMI))")
    print("   - .lrc (Lyrics)")
    # Add the rest of the subtitle formats

def main():
    parser = argparse.ArgumentParser(prog='mediacon.py', description='Media Converter', epilog='This is a program that can convert any of the supported media types. See list for more.', usage='%(prog)s [options]')
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-l', '--list', action='store_true', help='Display the list of supported file extensions')
    args = parser.parse_args()

    if args.list:
        display_supported_formats()
        return

    input_file = args.input
    output_file = args.output

    opus_to_mp3(input_file, output_file)

if __name__ == '__main__':
    main()